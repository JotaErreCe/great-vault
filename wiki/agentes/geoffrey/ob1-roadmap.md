---
type: reference
date: 2026-05-19
tags: [agente, geoffrey, ob1, roadmap, continuidad]
---

# OB1 Roadmap — Geoffrey

Roadmap aprobado/adaptado para tomar patrones útiles de OB1 sin instalar OB1 completo ni migrar el Great Vault.

## Fases

| Fase | Nombre | Objetivo | Estado |
|---:|---|---|---|
| 1 | Checkpoints + evaluación MCP | Crear `/geoffrey-checkpoint`, auto-capture mínimo, evaluar Gmail/Calendar/web. | completada |
| 2 | Work log | Adaptar formato Geoffrey para tareas largas/subagentes. | completada con corrección |
| 3 | Bandeja de revisión | Crear `/geoffrey-memory-review` y `wiki/agentes/geoffrey/memoria-sugerida.md`; nada pasa a `memoria.md` sin confirmación de JR. | pendiente |
| 4 | Dedup/importadores | Crear `/obsidian-import-safe` con dry-run, secret scan, fingerprints, sync log y revisión antes de escritura masiva. | pendiente |

## Fase 2 — Work log

Implementación requerida por JR:

- Skill/comando: `/geoffrey-work-log`.
- Formato estándar:
  - qué se intentó;
  - qué cambió;
  - qué falló;
  - decisiones;
  - pendientes;
  - próximo paso;
  - artifacts.
- Destino: `wiki/agentes/geoffrey/work-logs/`.

Estado: implementado en [[geoffrey/work-logs/index]] y skill runtime `geoffrey-work-log`.

## Fase 3 — Bandeja de revisión

Implementación requerida por JR:

- Skill/comando: `/geoffrey-memory-review`.
- Destino: `wiki/agentes/geoffrey/memoria-sugerida.md`.
- Geoffrey propone recuerdos antes de promoverlos.
- Nada se escribe a `wiki/agentes/geoffrey/memoria.md` sin confirmación explícita de JR.

## Fase 4 — Dedup/importadores

Implementación requerida por JR:

- Skill/comando: `/obsidian-import-safe`.
- Importador seguro con:
  - dry-run;
  - detección de secretos;
  - fingerprints;
  - sync log;
  - reporte de cambios;
  - sin escritura masiva sin revisión.

## Skills de contexto candidatas

Se pueden construir en paralelo con Fases 1–2, pero deben respetar la Tool Authority Matrix y no comprometer a JR con terceros:

| Skill | Propósito | Estado |
|---|---|---|
| `/propi-brief` | Pull de contratos activos, corredores y estado de cumplimiento. | candidata |
| `/amc-status` | Horas, clientes y facturas pendientes. | candidata |
| `/tesis-avance` | Capítulo actual, próxima entrega y pendientes. | candidata |

## Búsqueda semántica sin infraestructura

Antes de considerar pgvector o infraestructura nueva:

1. Instalar/probar el plugin **Smart Connections** en Obsidian.
2. Indexar el Vault con embeddings locales.
3. Si funciona bien para búsquedas de JR, no necesitamos pgvector ni infraestructura adicional.

## Tool Authority Matrix mínima

| Destino | Quién puede escribir |
|---|---|
| `raw/` | JR únicamente; inmutable para Geoffrey |
| `wiki/` | Geoffrey + subagentes con log obligatorio |
| `wiki/agentes/geoffrey/memoria-sugerida.md` | Geoffrey propone |
| `wiki/agentes/geoffrey/memoria.md` | Solo con confirmación explícita de JR |
| `_sensitive.md` | Solo JR |

La versión extendida vive en [[geoffrey/tool-authority-matrix]].

## Lo que NO hacer — confirmado

- No instalar OB1 completo.
- No mandar el Vault a Supabase.
- No importar Gmail masivamente sin dry-run.
- No promover memoria de agente sin revisión de JR.

## Estado de implementación — 2026-05-19 12:05

- Fase 2: implementada con `geoffrey-work-log` y `work-logs/`.
- Fase 3: implementada base con `geoffrey-memory-review`, `memoria-sugerida.md` y script de proponer/listar/promover con confirmación JR.
- Fase 4: implementada base con `obsidian-import-safe` y scanner dry-run; aún no hace escrituras masivas.
- Skills de contexto: documentadas como candidatas en [[geoffrey/skills-contexto-candidatas]].

## Relacionado

- [[geoffrey/ob1-fase-2]]
- [[geoffrey/work-logs/index]]
- [[geoffrey/tool-authority-matrix]]
- [[geoffrey/importadores-seguros]]
