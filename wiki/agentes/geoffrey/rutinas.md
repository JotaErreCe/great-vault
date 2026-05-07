---
type: reference
date: 2026-05-05
tags: [agente, geoffrey, rutinas, brief]
---

# Rutinas — Geoffrey

Procedimientos recurrentes de Geoffrey. Este archivo define cómo ejecutar tareas repetidas; [[geoffrey/AGENT|AGENT]] define reglas operativas generales.

## Brief matutino

Objetivo: enviar a Master JR un brief corto, ejecutivo y accionable por Telegram. La especificación canónica vive en [[geoffrey/brief-mananero|Brief mañanero — Geoffrey]].

### Entrega

- **Hora objetivo:** 7:15 AM Guatemala.
- **Ventana aceptable:** 6:30–8:00 AM Guatemala.
- **Formato:** mensajes separados por sección, máximo aproximado de 15 líneas por mensaje.
- **Trato:** siempre de **usted**.

### Fuentes previstas

- Calendario del día.
- Recordatorios vencidos o de hoy.
- Correo: ver [[geoffrey/integraciones|Integraciones — Geoffrey]] (`joserca95@gmail.com`, `jcastaneda@kidsunderstanding.com`, `joserca95@icloud.com`; UFM excluida por defecto).
- Recordatorios: ver [[geoffrey/reminders|Reminders — Geoffrey]].
- SMS vía [[imsg]] cuando aplique; lectura local minimizada, sin envío ni marcar como leído sin aprobación.
- Daily signals de agentes especializados, según [[briefs|arquitectura de briefs multi-agente]].
- Noticias relevantes: Guatemala, legal/regulatorio, negocios/inmobiliario, IA/tecnología, mercados generales y Diario de Centro América.

### Orden del brief

1. Saludo + Top 3 del día.
2. Agenda del día.
3. Urgentes / acción requerida.
4. Acciones sugeridas + cierre.
5. Mensajes condicionales: correos accionables, notas relevantes, Diario de Centro América/legal, mercados generales, noticias, reflexión.

### Reglas de edición

- Omitir secciones vacías.
- No incluir Roamy, Diplomado de Autismo ni Outlander en el brief diario salvo evento real relevante.
- Outlander se trata como tema de [[outlander-2026|Hogar]], no como proyecto separado.
- Propi se trata como cliente dentro de AMC Legal cuando el asunto sea legal.
- Diario de Centro América debe revisarse todos los días y tratarse como fuente legal/regulatoria de prioridad alta.
- El portafolio personal queda fuera del brief por ahora; mercados generales pueden incluir BTC, ETH y USD/GTQ si aportan contexto.
- Usar links a fuentes cuando existan.
- No enviar correos, mensajes ni acciones externas sin aprobación explícita.

## Pendientes operativos

- Organizar labels/filtros de Gmail para separar AMC Legal de correo personal en `joserca95@gmail.com`; JR aprobó la idea, pero pidió dejarlo para después y enfocarse primero en el brief.
- Hacer brief de prueba cuando las fuentes mínimas estén configuradas.
- Auditar y autorizar skills necesarias antes de conectar Calendar, Reminders, WhatsApp o Apple Notes.
- Verificar permisos macOS de [[imsg]] para lectura SMS; la skill ya está aprobada limitada, pero puede requerir Full Disk Access.

## Relacionado

- [[geoffrey/SOUL|SOUL — Geoffrey]] · [[geoffrey/AGENT|AGENT — Geoffrey]] · [[geoffrey/brief-mananero|Brief mañanero — Geoffrey]] · [[briefs|briefs multi-agente]] · [[geoffrey/integraciones|integraciones]] · [[geoffrey/reminders|reminders]] · [[geoffrey/skills-permitidas|skills permitidas]] · [[arquitectura]]
