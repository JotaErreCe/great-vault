---
type: reference
date: 2026-05-13
tags: [agente, geoffrey, reminders, tareas]
---

# Reminders — Geoffrey

Arquitectura objetivo para Apple Reminders de Master JR. Esta página documenta el formato aprobado y el proceso de seguridad. La skill ejecutable vive en `~/.openclaw/plugin-skills/apple-reminders/SKILL.md`.

## Regla principal

Antes de modificar Reminders, Geoffrey debe:

1. Auditar en modo read-only.
2. Resumir estructura actual.
3. Proponer migración.
4. Preguntar proyectos activos si toca `🚀 Proyectos`.
5. Esperar confirmación explícita antes de cambios destructivos.

## Estructura objetivo

### Grupos principales

- 🏠 Personal
- 💼 Trabajo
- 🎯 Metas y hábitos
- 👨‍👩‍👧 Familia y social
- 🏡 Hogar y mandados
- 🚀 Proyectos

`🚀 Proyectos` debe contener subgrupos, uno por cada proyecto activo. Geoffrey debe preguntar a JR cuáles son los proyectos actuales antes de crearlos.

### Listas estándar dentro de cada grupo/subgrupo

Cada grupo y cada proyecto debe contener exactamente:

- ✅ Tareas
- 🔁 Recurrentes
- 📅 Próximos
- 💡 Algún día

## Colores objetivo

- 🏠 Personal → azul
- 💼 Trabajo → verde
- 🎯 Metas y hábitos → morado
- 👨‍👩‍👧 Familia y social → naranja
- 🏡 Hogar y mandados → amarillo
- 🚀 Proyectos → cada proyecto con color distinto.

Si Apple Reminders no permite aplicar color de forma confiable por API/SQLite, Geoffrey debe crear estructura primero y reportar limitación.

## Etiquetas globales objetivo

Crear sin autoaplicar:

- `#urgente`
- `#rapido`
- `#$$`

## Clasificación

- ✅ Tareas: accionable, depende de JR, sin fecha fija.
- 🔁 Recurrentes: todo lo que se repite — pagos, rutinas, hábitos, llamadas periódicas, mantenimientos.
- 📅 Próximos: fecha/hora específica — citas, deadlines, eventos, vencimientos.
- 💡 Algún día: ideas, deseos, proyectos potenciales sin fecha de inicio.

Heurísticas:

- Tiene recurrencia → 🔁 Recurrentes aunque tenga fecha.
- Tiene fecha/hora sin recurrencia → 📅 Próximos.
- No tiene fecha y es accionable → ✅ Tareas.
- Idea/deseo/later → 💡 Algún día.
- Pagos/casa/carro/mandados → 🏡 Hogar y mandados salvo contexto claro.
- Familia/social → 👨‍👩‍👧 Familia y social.
- Hábitos/metas → 🎯 Metas y hábitos.
- Trabajo general → 💼 Trabajo.
- Proyecto específico → 🚀 Proyectos / proyecto.

## Estado auditado 2026-05-13

Auditoría read-only con `dump_reminders.py --format markdown`:

### Store principal — 25 reminders

Estructura activa visible:

- GROUP: `Proyectos` — 0 total.
- GROUP: `Trabajo` — 0 total.
- LIST: `🏠 Personal` — 8 incompletos.
- LIST: `Proyectos / Crisol TCG` — 0 incompletos.
- LIST: `Trabajo / Disegno Casa` — 0 incompletos.
- LIST: `Trabajo / Propi` — 0 incompletos.
- LIST: `Trabajo / UK` — 6 incompletos, 1 completado.

Stores secundarios:

- `Reminders` — 0.
- `SiriFoundInApps` — 0.

### Recordatorios incompletos detectados

`🏠 Personal`:

- Pagar Luz - Elgin — 2026-05-03 — recurrente.
- Pagar Luz - Z.11 — 2026-05-03 — recurrente.
- Pagar Mantenimiento - Antigua — 2026-05-03 — recurrente.
- Pagar Mantenimiento - Cañada 16 — 2026-05-03 — recurrente.
- Emitir Factura - Airbnb — 2026-05-15 10:00 — recurrente.
- Pagar Tarjeta - Puntos — 2026-06-03 10:00 — recurrente.
- Emitir Factura - Inquilinas — 2026-06-05 10:00 — recurrente.
- Pagar Tarjeta - Millas — 2026-06-09 10:00 — recurrente.

`Trabajo / UK`:

- Pagos a Terapeutas - Quincena — 2026-05-14 — recurrente.
- Pagos a Terapeutas - Fin de Mes — 2026-05-31 — recurrente.
- Crear empresa de ToyLab y Talleres — sin fecha.
- Crear una Nueva Cuenta de banco para ToyLab y Talleres — sin fecha.
- Empezar página web — sin fecha.
- Organizar Calendario — sin fecha.

## Plan preliminar de migración

Sin tocar nada todavía:

### 🏡 Hogar y mandados / 🔁 Recurrentes

- Pagar Luz - Elgin.
- Pagar Luz - Z.11.
- Pagar Mantenimiento - Antigua.
- Pagar Mantenimiento - Cañada 16.

### 🏠 Personal / 🔁 Recurrentes

- Emitir Factura - Airbnb.
- Pagar Tarjeta - Puntos.
- Emitir Factura - Inquilinas.
- Pagar Tarjeta - Millas.

Nota: si JR considera que tarjetas/facturas de inmuebles son “Hogar y mandados”, moverlas ahí en vez de Personal.

### 🚀 Proyectos / UK / 🔁 Recurrentes

- Pagos a Terapeutas - Quincena.
- Pagos a Terapeutas - Fin de Mes.

### 🚀 Proyectos / UK / ✅ Tareas

- Crear empresa de ToyLab y Talleres.
- Crear una Nueva Cuenta de banco para ToyLab y Talleres.
- Empezar página web.
- Organizar Calendario.

## Pendientes antes de ejecutar

- Confirmar proyectos activos para crear subgrupos dentro de `🚀 Proyectos`.
- Confirmar si tarjetas/facturas de inmuebles van en `🏠 Personal` o `🏡 Hogar y mandados`.
- Confirmar autorización para crear estructura y migrar recordatorios.
- Confirmar si se dejan estructuras viejas intactas al principio y se eliminan solo después de verificación.

## Relacionado

- [[geoffrey/rutinas|Rutinas — Geoffrey]] · [[geoffrey/integraciones|Integraciones — Geoffrey]] · [[geoffrey/brief-mananero|Brief mañanero — Geoffrey]] · [[geoffrey/skills-permitidas|Skills permitidas — Geoffrey]]
