---
type: reference
date: 2026-05-05
tags: [agente, geoffrey, rutinas, brief]
---

# Rutinas — Geoffrey

Procedimientos recurrentes de Geoffrey. Este archivo define cómo ejecutar tareas repetidas; [[geoffrey/AGENT|AGENT]] define reglas operativas generales.

## Brief matutino

Objetivo: enviar a Master JR un brief corto en Telegram alrededor de las 8:30, con hora exacta de envío, estilo newsletter y enfoque accionable.

### Fuentes previstas

- Calendario del día.
- Recordatorios vencidos o de hoy.
- Correo: ver [[geoffrey/integraciones|Integraciones — Geoffrey]] (`joserca95@gmail.com`, `jcastaneda@kidsunderstanding.com`, `joserca95@icloud.com`; UFM excluida por defecto).
- Recordatorios: ver [[geoffrey/reminders|Reminders — Geoffrey]].
- Mensajería: WhatsApp, iMessage/SMS cuando estén autorizados.
- Daily signals de agentes especializados, según [[briefs|arquitectura de briefs multi-agente]].
- Noticias relevantes: Guatemala, legal, negocios/inmobiliario, IA/tecnología, bolsa/cripto y Diario de Centro América.

### Orden del brief

1. Saludo, fecha y hora exacta de envío.
2. Línea editorial: lo más importante del día en una frase.
3. Secciones con novedad real.
4. Calendario antes de acciones recomendadas.
5. AMC Legal, Inbox, Proyectos y Noticias solo si tienen novedad real.
6. Proyectos bajo un header único `Proyectos`, con subheaders por proyecto.
7. Acciones sugeridas al final, después de Noticias, con cómo ejecutarlas.

### Reglas de edición

- Omitir secciones vacías.
- No incluir Roamy, Diplomado de Autismo ni Outlander en el brief diario salvo evento real relevante.
- Outlander se trata como tema de [[outlander-2026|Hogar]], no como proyecto separado.
- Propi se trata como cliente dentro de AMC Legal cuando el asunto sea legal.
- Diario de Centro América entra dentro de Legal/AMC Legal, no como categoría independiente.
- Usar links a fuentes cuando existan.
- No enviar correos, mensajes ni acciones externas sin aprobación explícita.

## Pendientes operativos

- Organizar labels/filtros de Gmail para separar AMC Legal de correo personal en `joserca95@gmail.com`; JR aprobó la idea, pero pidió dejarlo para después y enfocarse primero en el brief.
- Hacer brief de prueba simulando la noche del 2026-05-04 al 2026-05-05 cuando las fuentes estén configuradas.
- Auditar y autorizar skills necesarias antes de conectar Gmail, Calendar, Reminders, WhatsApp o iMessage/SMS.

## Relacionado

- [[geoffrey/SOUL|SOUL — Geoffrey]] · [[geoffrey/AGENT|AGENT — Geoffrey]] · [[briefs|briefs multi-agente]] · [[geoffrey/integraciones|integraciones]] · [[geoffrey/reminders|reminders]] · [[geoffrey/skills-permitidas|skills permitidas]] · [[arquitectura]]
