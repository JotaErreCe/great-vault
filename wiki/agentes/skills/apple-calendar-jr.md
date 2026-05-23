---
type: reference
date: 2026-05-14
tags: [skill, agente, calendar, seguridad, reference]
estado: aprobada
---

# apple-calendar-jr

## Resumen

Skill local de Geoffrey para lectura segura del calendario Apple de JR: eventos próximos, alarmas, conflictos y brief mañanero.

## Origen

- Ruta local: `/Users/jr/.openclaw/workspace-geoffrey/skills/apple-calendar-jr/SKILL.md`
- Script: `/Users/jr/.openclaw/workspace-geoffrey/skills/apple-calendar-jr/scripts/dump_calendar.py`
- Fuente: creada localmente para Geoffrey el 2026-05-14.
- Datos: base local Apple Calendar `~/Library/Group Containers/group.com.apple.calendar/Calendar.sqlitedb`.

## Capacidades

- Lee: eventos locales de Apple Calendar, calendario origen, hora inicio/fin, ubicación/link si existen y alarmas.
- Escribe/modifica: no.
- Envía/publica: no.
- Borra: no.
- Usa red: no.
- Usa credenciales: no directamente; lee datos locales disponibles en macOS.

## Riesgos

- Privacidad: expone agenda personal/familiar/laboral.
- Técnico: puede leer datos locales stale si iCloud/Calendar no ha sincronizado; `OccurrenceCache` puede estar atrasado.
- Operativo: no debe confundirse `Scheduled Reminders` con citas reales.

## Condiciones de uso

- Permitido: lectura local para agenda, conflictos, alarmas, brief mañanero y preguntas explícitas de JR.
- Permitido: reportar de forma minimizada en Telegram directo con JR.
- Prohibido sin aprobación explícita por acción: crear, editar, borrar, aceptar/rechazar eventos, invitar personas o cambiar alarmas.
- Prohibido: exponer detalles privados en chats grupales o con terceros.

## Verificación local

- 2026-05-14: `dump_calendar.py --days 2 --alarms` funcionó y listó próximos eventos con alarmas.

## Decisión

Estado: aprobada limitada.
Fecha: 2026-05-14.
Aprobó: Master JR, al pedir habilitar las skills necesarias para Geoffrey.

## Relacionado

- [[agentes/skills/index]] · [[agentes/geoffrey/skills-permitidas|Skills permitidas — Geoffrey]] · [[agentes/geoffrey/integraciones|Integraciones — Geoffrey]]
