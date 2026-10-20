---
type: reference
date: 2026-10-19
tags: [agente, claude, infraestructura, runbook]
---

# Actualizaciones de Claude Code (sin auto-update)

Desde el **19-oct-2026** el auto-update de Claude Code está **apagado** y se actualiza a mano una vez al mes, con JR presente.

## Por qué

Causa confirmada por una foto de JR (19-oct-2026): macOS pedía «"2.1.303" wants to access files managed by "Google Drive - jcastaneda@…"». macOS identifica el binario por su versión (`~/.local/share/claude/versions/X.Y.Z`); con cada versión nueva vuelve a pedir permiso, y mientras nadie toque «Permitir» todo acceso a Drive o iCloud se queda colgado → turno trabado → puente sordo ([[agentes/claude/telegram-puente]]).

## Qué quedó configurado

- `DISABLE_AUTOUPDATER=1` en `~/.claude/settings.json` (env) y en `~/Claude/bin/telegram-bridge.sh` (verificado 19-oct-2026).
- Recordatorio: `~/Claude/bin/recordatorio-update.sh` vía `com.jr.recordatorio-update` (día 1 de cada mes, 10:00), avisa con `avisar-jr.sh`.

## Cómo se actualiza

Solo cuando JR diga que está frente a la Mac:
1. `claude update`.
2. Reiniciar el puente: `launchctl kickstart -k gui/501/com.jr.claude-telegram` (con `.resume` si hay que conservar la sesión).
3. Provocar acceso a Drive (las dos cuentas), iCloud, Escritorio y Descargas para que salgan todos los avisos de macOS juntos y JR los apruebe.

**Nunca actualizar sin JR presente.**

## Relacionado

- [[agentes/claude/AGENT|Claude]] · [[agentes/claude/telegram-puente]] · [[agentes/claude/tareas-programadas]] · [[vault-cerebro]]
