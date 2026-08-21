---
type: resource
date: 2026-08-20
tags: [resource, agentes, reminders, productividad]
---

# Manual operativo — Apple Reminders de JR

Cómo deben usar Geoffrey y otros agentes la app Recordatorios de JR.

> **Reescrito 2026-08-20.** La versión anterior describía cuatro secciones estándar dentro de cada lista. Ese modelo se abandonó: las secciones **no son escribibles por ninguna API**, y tres de las cuatro duplicaban campos que ya existen. Copia del manual anterior en `raw/imports/reminders-backup/`.

## Principio central

Recordatorios es el sistema vivo de ejecución de JR. No es lista decorativa ni archivo histórico.

> ¿Qué necesita pasar con esto y cuándo debe volver a aparecer?

## Regla de diseño

**Organizar por el eje que NO cambia.**

- El **proyecto** de un pendiente nunca cambia → va en la **lista**.
- El **estado** cambia todo el tiempo (tarea → con fecha → hecho) → va en los **campos**, y el sistema lo deriva solo.

Invertir esto obliga a arrastrar recordatorios a mano cada vez que cambian de estado. Con TDAH, ese peaje mata el sistema.

## Estructura real (verificada 2026-08-20)

```
📁 Trabajo (grupo)          📁 Proyectos (grupo)      (raíz)
├── Propi                   ├── Crisol TCG            ├── 🏠 Personal
├── UK                      └── Tesis                 ├── Groceries
├── Disegno Casa                                      └── 💡 Algún día
└── AMC Legal
```

`💡 Algún día` es el único eje que no se deriva de un campo, por eso merece lista propia.

## Campos estándar (reemplazan a las secciones)

| Situación | Cómo se registra |
|---|---|
| Tiene deadline real | `dueDateComponents` + alarma. Aparece en Hoy y Programados |
| Cuesta caro no atenderlo | `priority = 1`. Reemplaza la etiqueta `#urgente` |
| Es periódico | **Regla de repetición nativa** (`recurrenceRules`). Nunca duplicar recordatorios a mano |
| "No me molestes hasta X" | `startDateComponents` a futuro: desaparece de la vista y vuelve solo |
| Pendiente grande | Subtareas anidadas vía `parentID` |
| Siempre | Notas con quién, cuándo y los datos duros (montos, fincas, registros) |

**No hace falta una vista de recurrentes.** Un recurrente bien puesto aparece solo el día que toca; si hay que ir a verlos, no están trabajando. El inventario de recurrentes vive mejor en el vault que en la app.

## Cómo redactar

Verbo y objeto claros. El título debe ser accionable sin abrir las notas.

Bueno: `Responder a Thelma sobre Sur Desarrollos` · `Pagar mantenimiento Cañada 16` · `Redactar contrato de arrendamiento bodega Avante`

Malo: `Propi` · `Revisar` · `Pendiente` · `Tema contrato`

## Cómo clasificar

1. Elegir la lista por **proyecto o área**.
2. Llenar los campos según la tabla de arriba.
3. Nunca inventar listas nuevas sin aprobación de JR.

Ruteo por área: pagos de casa, carro y mandados → `🏠 Personal`. Cliente o caso legal concreto → su lista (`Propi`, `Disegno Casa`). Trabajo legal sin cliente específico → `AMC Legal`. Terapias, web, planillas, contabilidad de la empresa → `UK`. Investigación y escritura académica → `Tesis`.

## Acceso técnico

**AppleScript NO sirve.** No enumera listas dentro de grupos ni ve secciones. `list "Propi"` falla con *Can't get list*.

**La vía correcta es EventKit compilado con Swift** (`/usr/bin/swiftc`; permiso ya concedido). Detalles, gotchas y scripts de respaldo/auditoría en la memoria `apple_reminders_access`.

| Escribible por API | No escribible |
|---|---|
| Crear, renombrar y borrar listas | **Secciones** dentro de listas |
| Mover recordatorios entre listas | **Grupos** (Trabajo / Proyectos) |
| Fecha de vencimiento, fecha de inicio, alarmas | **Etiquetas** (`#`) — quedan como texto literal en el título |
| Recurrencia nativa, prioridad, notas, URL, ubicación | |
| Subtareas, completar/descompletar | |

Todo lo de la columna derecha solo se hace a mano en la interfaz.

## Vistas: Smart Lists

Las Smart Lists reemplazan a las secciones. **Solo se crean a mano** (Archivo → Nueva lista → List Type: Smart List); EventKit no las expone y tampoco puede escribir dentro de ellas.

Filtros que ofrece el constructor: **Tags, Date, Time, Priority, Flag, Location, Lists**. No hay filtro por repetición, y **solo se admite un filtro de Lists por Smart List**.

Opciones de Date: Any · Today · On Date · Before a Date · After a Date · Specified Range · **Relative Range** · **No Date**.

Vistas construidas (2026-08-20):

| Vista | Receta | Ordenada por |
|---|---|---|
| 🎯 **Hoy** — la maestra diaria | Date → **Today** + ✅ Include Past Due | Fecha |
| 🔥 **Prioridad** | Priority → **Any** (= con prioridad asignada) | **Priority** |
| 📅 Próximos | Date → Relative Range → In the Next 30 Day + ✅ Include Past Due | Fecha |
| ✅ Tareas | Date → **No Date** + Lists → Exclude Selected List → Groceries | Fecha |

Opciones de Priority: Any · Low · Medium · High · No Priority. **`Any` significa "tiene prioridad asignada"**, no "sin restricción" — por eso 🔥 Prioridad excluye sola a Groceries y al backlog, que nunca llevan prioridad.

El orden **no es un filtro**: se fija por lista en **View → Sort By** (Manual, Due Date, Creation Date, **Priority**, Title). Los submenús requieren *hover*, no clic.

**Convención de prioridad que debe respetar el agente:**

| Nivel | Cuándo | Se ve como |
|---|---|---|
| Alta (1) | Costo real de no atenderlo: deadline duro, exposición legal, dinero parado | `!!!` |
| Media (5) | Compromiso adquirido con alguien, sin fecha crítica | `!!` |
| Baja (9) | Deseable, sin consecuencia | `!` |
| Ninguna (0) | Backlog, súper, cosas sin compromiso | — |

Sin prioridad, un recordatorio **no aparece en 🔥 Prioridad**. Es la decisión más importante al crear uno.

## 💡 Algún día — qué es y qué no

**Es un backlog, no un aplazamiento.** Guarda cosas que *podrían* hacerse en algún momento pero que **no son una realidad hoy** — ideas, proyectos potenciales, deseos sin fecha de inicio. (JR lo precisó el 2026-08-20.)

No confundir con posponer algo que sí va a pasar: para eso va `startDateComponents` a futuro, que lo oculta y lo devuelve solo el día indicado. Un recordatorio en Algún día **no lleva prioridad ni fecha**, y por eso no contamina 🎯 Hoy ni 🔥 Prioridad.

> ⚠️ **Nunca usar "Convert to Smart List" sobre una lista de proyecto.** Etiqueta todos sus recordatorios con el nombre de la lista, destruye la lista real y **EventKit deja de verla** — se pierde el acceso de escritura. Verificado por error el 2026-08-20 sobre AMC Legal; hubo que borrar la Smart List y recrear la lista.

## Escritura y cambios

**Sin confirmación:** leer, auditar, resumir, proponer clasificación, preparar texto.

**Requiere confirmación explícita de JR:** crear recordatorios, moverlos de lista, cambiar fecha/hora/repetición, marcar completado, crear o borrar listas, borrar cualquier cosa.

**Antes de cualquier cambio estructural:**
1. Auditar el estado actual.
2. **Respaldar a JSON** con el script de backup (captura recurrencias como RRULE, notas, alarmas, subtareas). Guardar en `raw/imports/reminders-backup/`.
3. Mostrar el plan concreto y esperar aprobación.
4. Ejecutar en lote pequeño.
5. **Auditar contra el respaldo** y reportar faltantes y recurrencias perdidas.
6. Registrar en `wiki/log/YYYY-MM.md`.

## Qué NO hacer

- No preguntar por estructura que se puede auditar.
- No crear listas ni categorías nuevas sin razón y sin aprobación.
- No mezclar proyectos con áreas personales.
- No duplicar recordatorios para simular repetición: usar la regla nativa.
- No borrar completados antiguos salvo instrucción directa.

## Relacionado

- [[agentes/geoffrey/reminders|Reminders — Geoffrey]] · [[agentes/geoffrey/brief-mananero|Brief mañanero — Geoffrey]] · [[wiki/index]]
