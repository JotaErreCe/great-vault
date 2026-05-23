---
type: reference
date: 2026-05-05
tags: [skill, agente, seguridad, imessage, sms]
estado: aprobada
---

# imsg

## Resumen

CLI macOS para leer historial local de iMessage/SMS y, si se autoriza, enviar mensajes por Messages.app.

## Origen

- Nombre: `imsg`
- Skill OpenClaw: `/opt/homebrew/lib/node_modules/openclaw/skills/imsg/SKILL.md`
- Fórmula Homebrew: `steipete/tap/imsg`
- GitHub: https://github.com/openclaw/imsg
- Homepage: https://imsg.to
- Versión instalada: `0.6.0`
- Licencia reportada por fórmula: MIT
- ClawHub: no identificado / no aplica por ahora

## Capacidades

- Lee: base local de Messages.app (`~/Library/Messages/chat.db`) con Full Disk Access.
- Escribe/modifica: puede marcar mensajes como leídos; puede enviar mensajes si se usa comando de envío.
- Envía/publica: sí, vía Messages.app, pero queda prohibido salvo aprobación explícita por mensaje.
- Borra: no observado como capacidad principal en `SKILL.md`/help revisado.
- Usa red: indirectamente al enviar iMessage/SMS por Messages.app; lectura histórica es local.
- Usa credenciales: usa sesión local de Messages.app; requiere permisos macOS.

## Riesgos

- Riesgos técnicos: requiere Full Disk Access; puede fallar por permisos de macOS.
- Riesgos de privacidad: expone historial local de SMS/iMessage, incluyendo mensajes sensibles.
- Riesgos externos: puede enviar SMS/iMessage si se invocan comandos de envío; riesgo de contactar terceros.

## Condiciones de uso

- Permitido: lectura local de SMS/iMessage para tareas explícitamente solicitadas por JR, como análisis de gastos Banco GTC.
- Permitido: extracción agregada y minimizada; evitar guardar mensajes crudos en el Vault.
- Prohibido sin aprobación explícita: enviar mensajes, reaccionar, marcar como leído, automatizar respuestas, o compartir mensajes crudos con servicios externos.
- Para análisis financiero: trabajar localmente; a Canva/Nanobanana solo deben ir datos agregados y aprobados.

## Auditoría

- 2026-05-05: Revisado `SKILL.md` bundled de OpenClaw.
- 2026-05-05: Revisada fórmula Homebrew `steipete/tap/imsg`: descarga release `v0.6.0` con `sha256`, instala binario y bundles; caveat oficial pide Full Disk Access.
- 2026-05-05: Instalado con Homebrew y verificado `imsg --version` = `0.6.0`.
- 2026-05-05: Prueba `imsg chats --limit 5 --json` bloqueada por macOS: falta Full Disk Access.

## Decisión

- Estado: aprobada para Geoffrey bajo condiciones limitadas.
- Fecha: 2026-05-05
- Auditó: Geoffrey
- Aprobó: JR, para probar análisis de SMS Banco GTC.

## Relacionado

- [[agentes/skills/index|Catálogo común de skills]] · [[agentes/geoffrey/skills-permitidas|Skills permitidas — Geoffrey]] · [[agentes/geoffrey/integraciones|Integraciones — Geoffrey]]
