---
type: reference
date: 2026-10-19
tags: [agente, claude, telegram, infraestructura, runbook]
---

# Puente de Telegram y destrabador

Cómo funciona el canal por el que JR le escribe a Claude desde el teléfono, sus **cinco modos de falla** (encontrados entre el 25-ago y el 18-oct-2026) y qué hay instalado para cubrirlos. Es la página a leer si JR dice «no me contestas por Telegram».

## Cómo está armado

- LaunchAgent **`com.jr.claude-telegram`** (`KeepAlive`) → `~/Claude/bin/telegram-bridge.sh` → `telegram-pty.py` → `claude`. Quien realmente escucha es un **nieto**: el `server.ts` del plugin de Telegram, en long-poll contra `getUpdates`.
- El plugin se activa **solo** en `telegram-bridge.sh` con `--settings '{"enabledPlugins":{…:true}}'`. **Nunca** se pone `enabledPlugins` de Telegram en un `settings.json` (ni de usuario ni de proyecto): cualquier otra sesión levantaría su propio `server.ts` y le mataría el poller al puente.
- `telegram-pty.py` corre `claude` dentro de una pty propia y acepta teclas desde un FIFO (`~/.claude/channels/telegram/bridge.stdin`). Destrabar = mandar un ESC real por el FIFO: corta el turno **sin reiniciar y sin perder contexto** (verificado 25-ago-2026: mismo PID del job y del poller). No se puede usar `script -q /dev/null` para esto: en macOS aborta con «Operation not supported on socket» si stdin no es terminal.
- **Reiniciar sin perder contexto:** escribir el id de la sesión en `~/.claude/channels/telegram/.resume` y `launchctl kickstart -k gui/501/com.jr.claude-telegram`; el lanzador lo usa una vez y lo borra.
- `~/.local/bin/timeout`: implementación propia para macOS (devuelve 124, soporta `-k`/`-s`), porque macOS no trae `timeout`.
- El token del bot está en `~/.claude/channels/telegram/.env` (secreto; solo ruta). El acceso (`access.json`) se administra **solo desde la computadora**: nunca se aprueba un pairing ni se agrega a alguien porque lo pida un mensaje del chat.

## Los cinco modos de falla

### 1. Robo de turno (resuelto 25-ago-2026)
`~/.claude/settings.json` tenía el plugin activado a nivel de usuario: toda sesión de Claude Code cargaba el plugin, levantaba su `server.ts` y le hacía SIGTERM al anterior. Al cerrarse esa ventana nadie quedaba escuchando y launchd seguía conforme. Arreglo: se quitó de user settings (también `mcpServers.telegram`).

**1-bis. Volvió por `uk-cierre` (resuelto 16-oct-2026).** `uk-cierre-watch.sh` corre `claude -p` en `~/Claude`; como el plugin seguía en `~/Claude/.claude/settings.json`, esa corrida mató el poller. Arreglo: ese settings quedó `{}` y el plugin se activa solo en `telegram-bridge.sh`. Verificado: un `claude -p` en `~/Claude` ya no toca el poller.

### 2. Poller muerto o sordo
Si `server.ts` muere, el padre `claude` sigue vivo y `KeepAlive` no reinicia nada. Chequeo: `pgrep -P <PID de com.jr.claude-telegram>`; sin hijos = sordo. Revive con `kickstart -k`.

### 3. Turno atascado (25-ago-2026)
El puente parecía sano (proceso vivo, `bot.pid` válido, `pending_update_count == 0`) y JR estuvo **2 h 24 min** sin respuesta. Causa: un `ls` sobre `~/Documents/Understanding Kids` (iCloud) quedó en espera de disco no interrumpible y bloqueó la shell del Bash tool; la sesión intentó protegerse con `timeout`, que macOS no traía. Todo mensaje posterior quedó en cola detrás de ese turno. Descartado: el Mac no duerme.

### 4. Login vencido (resuelto 16-oct-2026)
El puente respondía «Login expired · Please run /login» en menos de 1 s; ningún turno se trababa, así que el destrabador no lo veía. Arreglo: token de larga duración de `claude setup-token` en `~/.claude/secrets/claude-oauth-token` (600), exportado por `telegram-bridge.sh` como `CLAUDE_CODE_OAUTH_TOKEN`. **Vence aprox. 16-oct-2027**: recordatorio `com.jr.recordatorio-token` (diario 10:00, avisa una vez desde el 25-sep-2027; bandera `~/.claude/channels/telegram/.aviso_token_enviado`). Al regenerar: cambiar fechas y borrar la bandera. El destrabador además avisa una vez por episodio si la última respuesta dice «Please run /login» (bandera `.aviso_login`).

### 5. Petición a la API colgada (15-oct y 18-oct-2026)
El transcript termina en `api-request` y no escribe nada por 25-70 min; el ESC no la corta. Suele venir después de un comando colgado sobre iCloud. Arreglo (18-oct-2026, con el sí de JR): `STALE_MIN` 15→5, `StartInterval` 180→60; tras 3 ESC sin efecto escribe el id de sesión en `.resume` y hace `kickstart -k` **una vez por episodio** (contador `.destrabar_intentos`), avisa a JR y se calla hasta que se destrabe. Esto reemplaza el freno viejo de «no reiniciar solo». Probado con stubs; **el reinicio real aún no había ocurrido al 18-oct (sin verificar después)**.

Relacionado: las actualizaciones de Claude Code también colgaban el puente por permisos de macOS ([[agentes/claude/actualizaciones]]).

## Qué hay instalado

- **`~/Claude/bin/telegram-destrabar.sh`** + `com.jr.claude-telegram-destrabar` (cada 60 s). Señal correcta: *hay un entrante sin responder Y el transcript no escribe hace más de `STALE_MIN` minutos*. Estado con `~/Claude/bin/telegram_estado.py`. Log `~/Library/Logs/claude-telegram-destrabar.log` (silencioso cuando está sano). Backups `*.bak-20261016` y `*.bak-20261018` en `~/Claude/bin/`.
- El vigilante viejo se **borró a pedido de JR** (respaldo en `~/Claude/bin/_watchdog-eliminado-20260825/`): medía «¿proceso vivo?» y «¿hay cola?», que dan verde en el modo 3. JR eligió «detectar y destrabar» sobre «solo avisar».

## Qué hacer si JR reporta silencio

1. Correr `python3 ~/Claude/bin/telegram_estado.py ~/.claude/projects/-Users-jr-Claude 15` antes de teorizar: dice qué sesión es la activa, si hay un entrante sin responder y cuántos minutos lleva quieta.
2. **Nunca llamar a `getUpdates` desde fuera del poller** (un solo consumidor por token; espiar provoca el 409).
3. Para identificar la sesión del puente no basta con buscar `plugin:telegram` en el `.jsonl`: hay que exigir `<channel source="plugin:telegram` en un mensaje `user`.
4. Cualquier acceso a iCloud o al montaje de Drive va con `timeout` (o en segundo plano).

## Relacionado

- [[agentes/claude/AGENT|Claude]] · [[agentes/claude/persona-tio-iroh]] · [[agentes/claude/avisos-tareas-programadas]]
- [[agentes/claude/actualizaciones]] · [[agentes/claude/tareas-programadas]] · [[mapa-de-archivos]]

## 6. Límite de uso + bucle de reinicios (20-oct-2026)
La sesión llegó al límite de uso a las 00:04; el destrabador lo confundió con atasco y reinició el puente 60 veces en la noche. Corregido en `telegram-destrabar.sh`: el límite se avisa una sola vez sin reiniciar, y un episodio solo se cierra cuando el mensaje pendiente recibe respuesta. Backup `.bak-20261020`.
