---
type: reference
date: 2026-05-19
tags: [agente, geoffrey, ob1, work-log, continuidad]
---

# Work log — Geoffrey

Registro operativo para tareas largas o delicadas. No reemplaza `wiki/log/YYYY-MM.md`; lo complementa con estado de trabajo, decisiones pendientes y bloqueos.

## Cuándo usarlo

- Tareas de más de una sesión.
- Cambios con varias fuentes/herramientas.
- Auditorías, importadores, migraciones, automatizaciones.
- Cualquier trabajo que deba sobrevivir compaction/reset.

## Convención

Crear una sección por tarea con:

- `task_id`: slug corto + fecha.
- `owner`: Geoffrey o subagente.
- `scope`: qué sí/no incluye.
- `status`: proposed / active / blocked / review / done.
- `sources`: archivos/herramientas consultadas.
- `decisions_needed`: decisiones pendientes de JR.
- `next_action`: siguiente acción concreta.

## Tareas activas

### ob1-fase-2-2026-05-19

- owner: Geoffrey
- scope: formalizar jerarquía de confianza, autoridad de herramientas, importadores seguros, work log y auditoría web search.
- status: active
- sources:
  - [[geoffrey/mcp-evaluacion-2026-05-19]]
  - [[geoffrey/checkpoints/checkpoint-2026-05-19-0142-ob1-roadmap-phase1-start-4c4e74ca3e1e]]
  - [[decisiones/2026-05]]
- decisions_needed:
  - Confirmar si se acepta el hook conservador que no lee transcript crudo.
  - Decidir Brave vs Perplexity vs `web_search` nativo actual para research web reforzado.
- next_action: presentar reporte corto de Fase 2 y pedir confirmación solo de decisiones que desbloquean Fase 3.

## Relacionado

- [[geoffrey/ob1-fase-2]]
- [[geoffrey/checkpoints/index]]


## Implementación Fase 2

El formato estándar y los registros individuales viven en [[geoffrey/work-logs/index]]. Para crear nuevos registros usar la skill runtime `geoffrey-work-log` / `/geoffrey-work-log`.
