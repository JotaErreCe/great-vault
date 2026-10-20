---
type: reference
date: 2026-10-19
tags: [agente, claude, automatizacion, tareas-programadas, launchd]
---

# Tareas programadas y LaunchAgents de Claude

Qué corre solo en la Mac Mini `jr`, cuándo, qué hace y dónde están sus instrucciones. **Las instrucciones viven fuera del Vault** (son estado de runtime); aquí solo se documentan. El flujo completo del sistema de artes está en [[sistema-artes-redes]]; rutas, logs y secretos en [[mapa-de-archivos]].

## Tareas programadas de Claude (app de Claude)

Necesitan **la app de Claude abierta** a la hora del cron. El horario lo administra la app en `~/Library/Application Support/Claude/claude-code-sessions/…/scheduled-tasks.json` (no se edita a mano).

| Tarea | Cuándo | Qué hace | Instrucciones |
|---|---|---|---|
| `uk-artes-semanales` | Domingo 18:00 (`0 18 * * 0`) | Lee el Calendario de Artes (Notion), pasa tendencias aprobadas al Calendario, genera los artes de los próximos 10 días, corre verificadores, deja las piezas en «En revisión» con PNG en el cuerpo de Notion y avisa a JR | `~/.claude/scheduled-tasks/uk-artes-semanales/SKILL.md` (lee además las memorias `uk_template_system.md` y `uk_copy_style.md` y `GUIA_MAESTRA_ESTILO.md` de `Sistema/`) |
| `uk-tendencias-virales` | Lunes y jueves 7:00 (`0 7 * * 1,4`) | Busca formatos y tendencias de IG/FB (Apify + WebSearch), escribe máx. 4 sugerencias en la base 🔥 Tendencias con Status «Sugerida» y avisa | `~/.claude/scheduled-tasks/uk-tendencias-virales/SKILL.md` |

Las corridas son **desatendidas**: no se les pueden mandar mensajes, y un prompt de permisos las deja colgadas. Por eso los permisos del proyecto van **por patrón**, nunca con comandos literales (ver [[artes-decisiones-y-lecciones]] § Permisos). Cada tarea guarda además sus permisos aprobados (`approvedPermissions`) en el archivo de tareas de la app de Claude.

**Permisos del llavero quitados a `uk-tendencias-virales` (19-oct-2026, aprobado por JR):** se eliminaron de sus `approvedPermissions` `security find-generic-password *`, `security find-internet-password *` y `security dump-keychain *`. La tarea no necesita leer el llavero de macOS; si alguna corrida lo pidiera, es una señal de alarma, no algo que se vuelve a aprobar sin JR.

## LaunchAgents (`~/Library/LaunchAgents/com.jr.*`)

| Label | Script en `~/Claude/bin/` | Cuándo | Qué hace |
|---|---|---|---|
| `com.jr.claude-telegram` | `telegram-bridge.sh` | Siempre (KeepAlive) | Puente de Telegram ([[agentes/claude/telegram-puente]]) |
| `com.jr.claude-telegram-destrabar` | `telegram-destrabar.sh` | Cada 60 s | Destraba el puente (ESC o reinicio con `.resume`) |
| `com.jr.uk-cierre` | `uk-cierre-watch.sh` → `claude -p` con `uk-cierre-prompt.md` | Cada 15 min y al cargar | Piezas en «Aprobado» con `Enlace Drive` vacío → Drive, Notion, `Aprobadas/`; sin correo |
| `com.jr.uk-cambios` | `uk-cambios-watch.sh` → `claude -p` con `uk-cambios-prompt.md` | Lunes, miércoles y viernes 20:00 | Piezas en «Cambios pedidos» → v2 y «En revisión» |
| `com.jr.uk-resumen-magoo` | `uk-resumen-magoo.py` | Diario 6:00 | Un correo a Magoo con lo nuevo en «Revisión Magoo» (por `gws`) |
| `com.jr.recordatorio-token` | `recordatorio-token.sh` | Diario 10:00 (avisa desde 25-sep-2027) | Renovar el token largo del puente |
| `com.jr.recordatorio-update` | `recordatorio-update.sh` | Día 1 de cada mes, 10:00 | Recordar actualizar Claude Code a mano ([[agentes/claude/actualizaciones]]) |

Los vigilantes consultan Notion directo por REST (barato) y **solo despiertan a Claude** si hay trabajo. `claude -p` corre con cwd `~/Claude`, así que lee `~/Claude/CLAUDE.md`. Logs en `~/Library/Logs/`.

## Apify (lo usa `uk-tendencias-virales`)

- Va como **MCP local con token Bearer** (scope user), no como conector de claude.ai: los conectores de claude.ai dependen del login OAuth por sesión y una corrida programada a veces arrancaba sin la herramienta (10 y 13-ago-2026 sin datos). Diagnóstico del 13-ago-2026.
- Configuración: servidor HTTP `https://mcp.apify.com?tools=apify/instagram-post-scraper,apify/facebook-posts-scraper,apify/instagram-hashtag-scraper,storage`, con el token en la cabecera (el token vive en `~/.claude.json`; nunca en el Vault). `?tools=` fija exactamente los actores que usa la tarea. Verificado «Connected» el 19-oct-2026.
- Permisos en `~/.claude/settings.json`: `mcp__apify` y `mcp__Apify` (nombre viejo). Si se migra, desconectar el Apify de claude.ai para no tener dos servidores iguales.
- Los actores se invocan con **doble guion** (`apify--instagram-post-scraper`…), son asíncronos (guardar `datasetId`, esperar `SUCCEEDED`) y conviene pedir solo los campos útiles en `get-dataset-items`.
- Presupuesto: plan gratis con tope de USD 5/mes; detalle en el SKILL y en [[sistema-artes-redes]] § Tendencias. Runlog: `Sistema/tendencias/runlog.md`.

## Relacionado

- [[agentes/claude/AGENT|Claude]] · [[sistema-artes-redes]] · [[mapa-de-archivos]]
- [[agentes/claude/avisos-tareas-programadas]] · [[agentes/claude/telegram-puente]] · [[agentes/claude/actualizaciones]]
