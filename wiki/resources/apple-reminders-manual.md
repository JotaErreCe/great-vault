---
type: resource
date: 2026-05-13
tags: [resource, agentes, reminders, productividad]
---

# Manual operativo — Apple Reminders de JR

> **BORRADOR NO AUTORIZADO.** Este documento todavía no debe tratarse como manual canónico. Falta que JR defina para qué sirve cada apartado/lista/sección de su sistema real de Recordatorios. Hasta entonces, ningún agente debe usar este archivo para reorganizar, mover o clasificar recordatorios automáticamente.

Este borrador reúne supuestos iniciales sobre cómo podría usarse la app Recordatorios de Apple de JR. Debe validarse con JR antes de convertirse en regla operativa.

## Principio central pendiente de validar

Recordatorios parece ser el sistema vivo de ejecución de JR, pero falta confirmar con JR la función exacta de cada apartado.

Todo agente debe tratar cada recordatorio como una unidad operativa con esta pregunta:

> ¿Qué necesita pasar con esto y cuándo debe volver a aparecer?

## Modelo mental correcto

La estructura puede verse en Apple Reminders como grupos, listas y secciones. Para operar, piense en tres niveles:

1. **Área / proyecto** — dónde vive el asunto.
2. **Sección estándar** — qué tipo de recordatorio es.
3. **Recordatorio** — la acción concreta, con o sin fecha/repetición.

No asumir que las cuatro categorías son siempre listas separadas. En la implementación actual pueden existir como **secciones dentro de una lista**. Por eso los agentes deben buscar tanto listas como secciones antes de concluir que “no existe”.

## Secciones detectadas / objetivo pendiente de definición

Se detectan estas secciones, pero falta que JR confirme para qué sirve exactamente cada una en su sistema real:

- **✅ Tareas** — accionable, depende de JR, sin fecha fija.
- **🔁 Recurrentes** — se repite: pagos, rutinas, hábitos, llamadas periódicas, mantenimiento.
- **📅 Próximos** — fecha/hora específica: citas, deadlines, eventos, vencimientos no recurrentes.
- **💡 Algún día** — idea, deseo, proyecto potencial o cosa que no toca todavía.

## Áreas y proyectos

Áreas base previstas:

- **🏠 Personal** — vida personal no doméstica, administración personal, asuntos propios.
- **💼 Trabajo** — trabajo general y operación profesional que no pertenezca claramente a un proyecto.
- **🎯 Metas y hábitos** — hábitos, rutinas personales, salud, aprendizaje, disciplina.
- **👨‍👩‍👧 Familia y social** — Mónica, Nicolás, familia, amistades, compromisos sociales.
- **🏡 Hogar y mandados** — casa, servicios, mantenimiento, carro, compras, diligencias.
- **🚀 Proyectos** — proyectos activos o incubados.

Proyectos conocidos/esperados en el sistema actual o reciente:

- Propi
- UK / Understanding Kids
- Tesis
- Crisol TCG
- Disegno Casa / Altezza

Si un proyecto existe en la app, úselo. No pregunte “cuáles son sus proyectos” sin antes auditar la app y el Vault.

## Cómo clasificar nuevos recordatorios — pendiente de validación

### Regla rápida

1. Elegir área/proyecto.
2. Elegir sección estándar.
3. Crear recordatorio con verbo claro.
4. Agregar fecha/repetición solo si corresponde.

### Por sección

- Tiene repetición → **🔁 Recurrentes**, aunque tenga fecha.
- Tiene fecha/hora fija y no se repite → **📅 Próximos**.
- No tiene fecha pero se puede hacer cuando haya tiempo → **✅ Tareas**.
- No es para ahora / idea futura → **💡 Algún día**.

### Por área

- Pagos de servicios, mantenimiento de propiedades, carro, mandados → **🏡 Hogar y mandados**.
- Pagos o tareas administrativas personales no domésticas → **🏠 Personal**, salvo que JR haya indicado otra cosa.
- Cliente/proyecto legal concreto → proyecto correspondiente, por ejemplo **Propi** o **Disegno Casa**.
- UK/terapias/web/empresa/cuenta bancaria → **UK / Understanding Kids**.
- Tesis, investigación, escritura académica → **Tesis**.
- Hábitos/rutinas de salud, estudio o disciplina → **🎯 Metas y hábitos**.
- Familia/social → **👨‍👩‍👧 Familia y social**.

## Cómo redactar recordatorios

Usar verbos y objetos claros. Evitar títulos vagos.

Bueno:

- `Responder a Thelma sobre Sur Desarrollos`
- `Pagar mantenimiento Cañada 16`
- `Revisar informe Read.ai Disegno Casa y extraer compromisos`
- `Enviar datos faltantes de Intense Group a Astrid`

Malo:

- `Propi`
- `Revisar`
- `Pendiente`
- `Tema contrato`

## Fechas, horas y repetición

No cambiar fechas, horas ni repetición de recordatorios existentes salvo instrucción explícita.

Al crear nuevos:

- Si JR debe hacerlo hoy: poner fecha de hoy, hora solo si ayuda.
- Si vence mañana o fecha concreta: usar **📅 Próximos** o **🔁 Recurrentes** según corresponda.
- Si es recurrente: usar repetición nativa de Reminders, no duplicar recordatorios manualmente.
- Si no hay fecha real: dejar sin fecha en **✅ Tareas** o **💡 Algún día**.

## Etiquetas

Etiquetas disponibles/objetivo:

- `#urgente` — algo sensible a tiempo o con costo claro de no atender.
- `#rapido` — se puede resolver en pocos minutos.
- `#$$` — implica pago, cobro, gasto, factura o dinero.

No aplicar etiquetas automáticamente por ansiedad. Usarlas solo si agregan valor operativo.

## Consultar Reminders para briefs

En briefs, Reminders debe alimentar la sección **Reminders / qué haceres**.

Formato recomendado:

- **Hacer o confirmar hoy** — vencidos o críticos.
- **Mañana / próximos días** — vencimientos cercanos.
- **Ordenar / reprogramar** — tareas sin fecha que están flotando.
- **Convertir en acción** — crear correo, llamada, evento, reminder nuevo.

No hacer análisis financiero. Si hay pagos, tratarlos como pendientes operativos.

No incluir “Puede ignorar hoy”. Si algo se ignora, se omite.

## Consultar antes de actuar

Antes de responder sobre Reminders, el agente debe auditar o verificar estado actual. No responder desde memoria si el estado puede haber cambiado.

Comando read-only preferido:

```bash
python3 ~/.openclaw/plugin-skills/apple-reminders/scripts/dump_reminders.py --format markdown
```

Importante: el dump debe mostrar **listas y secciones**. Si solo muestra listas, está incompleto para este sistema.

## Escritura y cambios

### Permitido sin confirmación destructiva

- Leer/auditar estructura.
- Resumir recordatorios.
- Proponer clasificación.
- Preparar plan.
- Preparar texto de nuevos recordatorios.

### Requiere confirmación explícita

- Crear recordatorios.
- Mover recordatorios entre lista/sección.
- Cambiar fecha/hora/repetición.
- Marcar como completado.
- Renombrar listas/secciones.
- Crear/eliminar listas, secciones o grupos.
- Eliminar cualquier cosa.

### Antes de cambios grandes

1. Auditar estado actual.
2. Hacer backup de la base de Reminders.
3. Mostrar plan concreto.
4. Esperar aprobación.
5. Ejecutar en lote pequeño y verificable.
6. Auditar después.

## Qué NO hacer

- No preguntar por estructura que ya se puede auditar.
- No asumir que algo no existe porque no aparece como lista; puede ser sección.
- No “limpiar” duplicados si JR pidió solo manual o uso.
- No crear categorías nuevas sin razón.
- No mezclar proyectos con áreas personales.
- No mover recordatorios solo porque “parecen” mal clasificados sin aprobación.
- No borrar completados antiguos salvo instrucción directa.

## Uso por agentes — regla temporal

Hasta que JR valide este manual, cuando un agente reciba una tarea que implique Reminders:

1. Leer este manual o la skill `apple-reminders`.
2. Auditar Reminders actual.
3. Auditar y describir lo que ve, sin asumir significado.
4. Si necesita clasificar/mover/crear, preguntar la intención del apartado si no está explícita.
5. Si implica cambio: pedir aprobación concreta.
6. Después de cambiar: verificar y reportar qué quedó dónde.

## Relación con el Vault

- Este manual define el comportamiento general.
- La skill ejecutable vive en `~/.openclaw/plugin-skills/apple-reminders/SKILL.md`.
- Geoffrey puede mantener notas operativas en `wiki/agentes/geoffrey/reminders.md`.
- Cambios importantes deben registrarse en `wiki/log/YYYY-MM.md`.

## Relacionado

- [[agentes/geoffrey/reminders|Reminders — Geoffrey]] · [[agentes/geoffrey/brief-mananero|Brief mañanero — Geoffrey]] · [[agentes/geoffrey/rutinas|Rutinas — Geoffrey]]
