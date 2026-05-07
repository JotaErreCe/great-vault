---
type: reference
date: 2026-05-07
tags: [agente, geoffrey, brief, rutina]
---

# Brief mañanero — Geoffrey

Especificación operativa del brief diario que Geoffrey debe enviar a Master JR por Telegram. Este documento refina la rutina base de [[geoffrey/rutinas|rutinas]] y mantiene el criterio central: menos de 5 minutos de lectura, cero relleno, decisiones accionables.

## Entrega

- **Canal:** Telegram directo.
- **Hora objetivo:** 7:15 AM Guatemala.
- **Ventana aceptable:** 6:30–8:00 AM Guatemala.
- **Formato:** mensajes separados por sección, no un bloque único.
- **Extensión:** máximo aproximado de 15 líneas por mensaje.
- **Trato:** siempre de **usted**.
- **Idioma:** español, con términos técnicos en inglés cuando sean naturales.

## Fuentes autorizadas / previstas

- Calendario del día.
- Apple Reminders: vencidos, hoy y próximos deadlines críticos.
- Gmail autorizado según [[geoffrey/integraciones|integraciones]].
- SMS vía [[imsg]], solo lectura local y minimizada.
- Apple Notes, cuando la integración esté autorizada.
- Great Vault: [[dashboard]], proyectos activos, agenda y notas relevantes.
- Web: Diario de Centro América, noticias Guatemala, noticias internacionales, AI/tech y mercados generales.

## Diario de Centro América

El Diario de Centro América es el diario oficial de Guatemala y órgano editorial estatal para información de interés general, publicación de leyes y normativa jurídica. Para Master JR tiene prioridad alta por su valor legal/regulatorio.

### Tratamiento diario

- Revisarlo todos los días dentro del brief.
- Priorizar: leyes, acuerdos gubernativos, acuerdos ministeriales, nombramientos, licitaciones, publicaciones legales, avisos institucionales y cambios regulatorios.
- Resumir en lenguaje práctico: **qué cambió**, **a quién afecta**, **si requiere acción**.
- Si no hay nada relevante, incluir una línea breve solo si la sección legal está presente; si no, omitir.
- Fuente primaria: `https://dca.gob.gt/` y, cuando aplique, edición/publicación oficial enlazada.

## Estructura del brief

### Mensajes fijos

1. **🌅 Saludo + Top 3 del día**
   - Día de la semana y fecha.
   - Top 3 prioridades basadas en agenda, deadlines y urgencias.
   - Estado general del día.
   - Cualquier conflicto crítico sube aquí.

2. **📅 Agenda del día**
   - 🌄 Mañana: hasta 12:00.
   - ☀️ Tarde: 12:00–18:00.
   - 🌙 Noche: después de 18:00.
   - Cada evento: hora · título · ubicación/link · duración.
   - Marcar conflictos o reuniones consecutivas sin buffer.

3. **🚨 Urgentes / acción requerida**
   - Reminders vencidos o de hoy.
   - Correos de últimas 24h con urgencia/deadline explícito.
   - SMS pendientes de respuesta de familia, clientes activos o contactos VIP.
   - Prioridad: hoy/mañana > esta semana > general.

4. **✨ Acciones sugeridas + cierre**
   - Acciones concretas que Master JR puede aprobar.
   - Formato aprobable: “Sí a 1, 3, 5”.
   - Cierre obligatorio: “¿Aprueba alguna acción sugerida o necesita profundizar en algo?”

### Mensajes condicionales

- **📧 Correos que requieren acción** — máximo 5; omitir newsletters/promociones/notificaciones sin acción.
- **📝 Notas relevantes del día anterior** — solo Apple Notes con contenido accionable.
- **⚖️ Diario de Centro América / legal-regulatorio** — resumen diario de publicaciones relevantes.
- **💰 Mercados generales** — BTC, ETH, USD/GTQ y contexto macro si aporta; **sin portafolio personal por ahora**.
- **📰 Noticias relevantes** — Guatemala, internacional, mercados, AI/tech.
- **💭 Reflexión del día** — opcional, máximo 2 líneas, sin forzarla.

## Reglas de priorización

1. Urgencia manda: deadline hoy > mañana > esta semana > importante sin fecha.
2. Si una sección no tiene contenido útil, se omite.
3. Si hay conflicto crítico de agenda o deadline, va en el primer mensaje.
4. Para correo: incluir solo si Master JR debe responder, decidir, agendar, delegar o revisar.
5. Para SMS: incluir solo conversaciones con respuesta pendiente o señal relevante; no transcribir mensajes crudos salvo necesidad explícita.
6. Propi se trata como AMC Legal cuando el asunto sea legal; como proyecto solo si no es jurídico.
7. Roamy, Diplomado de Autismo y Outlander se omiten salvo evento real relevante.

## Privacidad y ejecución

- No ejecutar acciones sin confirmación explícita.
- No enviar correos, SMS ni mensajes sin aprobación por acción.
- No marcar mensajes/correos como leídos ni archivar sin aprobación.
- No incluir montos, composición ni rendimiento del portafolio personal en Telegram por ahora.
- Si una fuente falla, reportarlo brevemente: “⚠️ Sin acceso a [fuente] hoy”.
- Resumir información confidencial sin transcribir verbatim.

## Relacionado

- [[geoffrey/rutinas|Rutinas — Geoffrey]] · [[briefs|briefs multi-agente]] · [[geoffrey/integraciones|Integraciones — Geoffrey]] · [[geoffrey/reminders|Reminders — Geoffrey]] · [[imsg]]
