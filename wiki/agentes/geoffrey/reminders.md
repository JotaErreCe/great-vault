---
type: reference
date: 2026-05-05
tags: [agente, geoffrey, reminders, tareas]
---

# Reminders — Geoffrey

Arquitectura propuesta para Apple Reminders cuando la integración esté autorizada.

## Listas / secciones

- **Follow-ups** — esperando respuesta de terceros.
- **AMC Legal**
  - Legal general — Diario de Centro América, normativa general, plazos sin cliente específico.
  - Rafa Gálvez
  - Héctor Rodas
  - Sebastián Martínez
  - Jacky Chang
  - Disegno Casa / Brera
  - Propi
  - General / firma
- **Understanding Kids**
- **Crisol TCG**
- **Tesis**
- **Hogar** — Mónica, Nicolás, Niko, Outlander, casa.
- **Geoffrey** — cosas delegadas al agente.
- **Someday** — Roamy, Diplomado Autismo y temas pausados hasta reactivación.

## Decisiones confirmadas

- `Legal general` queda dentro de `AMC Legal`, no como lista separada.
- Disegno Casa y Brera se tratan unidos como `Disegno Casa / Brera` para Reminders.
- Altezza no es cliente directo de AMC Legal; el caso Altezza se registra bajo `Disegno Casa / Brera` porque Altezza es contraparte.
- Brera Arredamenti, S.A. es la persona jurídica; Disegno Casa es la empresa/nombre comercial operativo.
- Javier Hegel fue cliente de Propi primero; después pidió una renovación de arrendamiento de forma independiente.
- Julio Cruz y Julio Cruz Ramazzini son la misma persona; es accionista de Brera junto con Pablo Cruz Ramazzini.
- Andrés Wer es amigo cercano de JR y pide temas legales ocasionales, pero por ahora no tiene trabajos activos; no se agrega como sección.
- Propi puede vivir en AMC Legal cuando el asunto sea legal; fuera de eso, se trata como proyecto/cliente según contexto.
- JR está al día con actualizaciones de iOS/macOS, así que se pueden usar secciones nativas de Reminders cuando la integración esté autorizada.

## Decisiones pendientes

- Organizar Apple Reminders real cuando la skill esté auditada y autorizada.

## Regla de seguridad

Geoffrey no debe crear, borrar ni reorganizar recordatorios reales sin aprobación explícita de JR hasta que la skill esté auditada y autorizada.

## Relacionado

- [[geoffrey/rutinas|Rutinas — Geoffrey]] · [[geoffrey/integraciones|Integraciones — Geoffrey]] · [[geoffrey/skills-permitidas|Skills permitidas — Geoffrey]]
