---
type: reference
date: 2026-05-13
tags: [agente, geoffrey, reminders, tareas]
---

# Reminders — Geoffrey

Esta página resume cómo Geoffrey debe usar Apple Reminders de JR. El manual canónico para cualquier agente está en [[resources/apple-reminders-manual|Manual operativo — Apple Reminders de JR]]. La skill ejecutable vive en `~/.openclaw/plugin-skills/apple-reminders/SKILL.md`.

## Corrección importante

La estructura de JR **ya existe dentro de la app** y puede estar representada como **secciones dentro de listas**, no necesariamente como listas separadas.

Error que no debe repetirse: auditar solo listas/grupos y concluir que falta estructura. Hay que revisar también secciones.

Comando read-only actualizado:

```bash
python3 ~/.openclaw/plugin-skills/apple-reminders/scripts/dump_reminders.py --format markdown
```

Debe mostrar:

- Structure — grupos/listas.
- Sections inside lists — secciones internas.
- Incomplete reminders — recordatorios incompletos.

## Uso esperado

Recordatorios es el sistema operativo de qué haceres de JR.

Geoffrey debe usarlo para:

- Detectar qué hay vencido, de hoy o próximo.
- Convertir comunicaciones en tareas concretas.
- Crear recordatorios con aprobación.
- Reprogramar o mover recordatorios solo con aprobación.
- Alimentar el brief mañanero con acciones reales.

No debe usarlo para:

- Rediseñar la app sin petición explícita.
- Preguntar por estructura que se puede auditar.
- Limpiar duplicados si JR pidió solo uso/manual.
- Borrar o completar cosas sin permiso.

## Secciones estándar confirmadas por JR

JR definió las secciones así:

- ✅ Tareas — cualquier cosa accionable que dependa de JR, sin fecha fija. Si puede hacerlo cuando tenga tiempo, va aquí.
- 🔁 Recurrentes — todo lo que se repite: diario, semanal, mensual, anual. Pagos, rutinas, hábitos, llamadas periódicas, mantenimientos.
- 📅 Próximos — todo lo que tiene fecha y/u hora específica. Citas, deadlines, eventos, vencimientos.
- 💡 Algún día — lo que JR quiere hacer pero no ahora. Ideas, deseos, proyectos potenciales sin fecha de inicio.

## Áreas/proyectos conocidos

Áreas base:

- 🏠 Personal
- 💼 Trabajo
- 🎯 Metas y hábitos
- 👨‍👩‍👧 Familia y social
- 🏡 Hogar y mandados

Proyectos conocidos/recientes:

- Propi
- UK / Understanding Kids
- Tesis
- Crisol TCG
- Disegno Casa / Altezza

Auditar antes de asumir que falta alguno.

## Brief mañanero

La sección de Reminders debe enfocarse en qué necesita pasar:

- **Hacer o confirmar hoy**
- **Mañana / próximos días**
- **Ordenar / reprogramar**
- **Convertir en acción**

No incluir “Puede ignorar hoy”. Si algo se ignora, se omite.

## Estado auditado 2026-05-13

Se detectó que el dump anterior estaba incompleto porque no mostraba secciones. Se actualizó el script para mostrar `ZREMCDBASESECTION`.

Estructura/secciones visibles en auditoría:

- `🏠 Personal`: contiene secciones estándar y también secciones relacionadas con Hogar/Familia; revisar con cautela antes de concluir duplicados.
- `💼 Trabajo`: ✅ Tareas, 🔁 Recurrentes, 📅 Próximos, 💡 Algún día.
- `🎯 Metas y hábitos`: ✅ Tareas, 🔁 Recurrentes, 📅 Próximos, 💡 Algún día.
- Proyectos/listas detectadas con secciones estándar o parciales: Propi, UK, Tesis, Crisol TCG, Disegno Casa.

Recordatorios incompletos visibles al corte:

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

## Relacionado

- [[resources/apple-reminders-manual|Manual operativo — Apple Reminders de JR]] · [[geoffrey/rutinas|Rutinas — Geoffrey]] · [[geoffrey/integraciones|Integraciones — Geoffrey]] · [[geoffrey/brief-mananero|Brief mañanero — Geoffrey]]
