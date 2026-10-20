---
type: reference
date: 2026-10-19
tags: [agente, claude, telegram, automatizacion]
---

# Avisos de las tareas desatendidas

JR pidió el **2026-08-26**: «Me gustaría que me avises cuándo las tareas semanales se realicen.» El reporte de una corrida vive en el transcript y JR no lo ve: está en el teléfono.

## La herramienta: `~/Claude/bin/avisar-jr.sh`

- Acepta el texto como argumento o por stdin, lee el token de `~/.claude/channels/telegram/.env`, manda al chat de JR por HTTP (`sendMessage`), recorta a 3900 caracteres y **falla ruidosamente** si Telegram no devuelve `"ok":true`. Probado de punta a punta el 26-ago-2026.
- **Por qué curl y no el plugin MCP de Telegram:** cargar el plugin en otra sesión levanta un segundo `server.ts` que le hace SIGTERM al poller del puente y deja a JR sin canal (modo de falla 1 de [[agentes/claude/telegram-puente]]). `sendMessage` por HTTP no toca `getUpdates`: no hay conflicto. **Nunca reemplazar el script por el plugin en una corrida desatendida.**

## Dónde está cableado

`uk-artes-semanales` (paso 8 del SKILL), `uk-tendencias-virales` (sección propia), los prompts de `uk-cierre` y `uk-cambios`, `uk-resumen-magoo.py` y los recordatorios de token y de actualización (verificado por búsqueda el 19-oct-2026; el destrabador avisa por su cuenta, sin este script). Todos exigen: voz del Tío Iroh ([[agentes/claude/persona-tio-iroh]]), de tú, corto y escaneable, y **avisar igual si la corrida falla** (el silencio no informa nada).

## Si JR dice que no le llegó un aviso

Revisar primero el log de la corrida y después que el `.env` siga teniendo el token. No asumir que el puente está caído: este camino no depende del puente.

Cualquier tarea desatendida nueva que deba avisarle a JR usa este script.

## Relacionado

- [[agentes/claude/AGENT|Claude]] · [[agentes/claude/tareas-programadas]] · [[sistema-artes-redes]]
