---
type: reference
date: 2026-05-19
tags: [agente, geoffrey, ob1, arquitectura, fase-2]
---

# OB1 — Fase 2 — Geoffrey

## Objetivo

Convertir los patrones aprobados de OB1 en reglas operativas seguras para Geoffrey/OpenClaw/Great Vault, sin instalar OB1 completo ni migrar el Vault a una base externa.

Fase 2 trabaja con **diseño, contratos, dry-runs y revisión humana**. No habilita importación masiva ni escritura externa por sí sola.

## Alcance aprobado por continuidad

Patrones OB1 adoptados:

1. Jerarquía de confianza.
2. Fingerprint/deduplicación.
3. Work log para tareas largas.
4. Auto-capture al cierre.
5. Importadores seguros.

Restricciones vigentes:

- No instalar OB1 completo.
- No mandar el Great Vault a Supabase.
- No importar Gmail masivamente sin dry-run.
- No promover memoria generada por agentes sin revisión explícita de JR.
- No guardar transcripts crudos como memoria.

## Entregables de Fase 2

| Entregable | Estado | Archivo |
|---|---:|---|
| Tool Authority Matrix formal | creado | [[geoffrey/tool-authority-matrix]] |
| Especificación de importadores seguros | creado | [[geoffrey/importadores-seguros]] |
| Work log operativo | creado | [[geoffrey/work-log]] |
| Auditoría web search Brave vs Perplexity | preliminar | [[geoffrey/web-search-auditoria-2026-05-19]] |

## Criterio de cierre de Fase 2

Fase 2 queda lista para pasar a Fase 3 cuando:

- La matriz de autoridad esté aceptada por JR o no tenga objeciones.
- Exista formato de dry-run para importadores.
- El work log tenga convención estable y se haya usado al menos una vez.
- Se decida proveedor de web search o se confirme continuar con `web_search` nativo actual.

## Próximo paso recomendado

Aplicar Fase 2 primero al brief mañanero y a Gmail/Calendar read-only:

1. Solo producir candidatos de captura.
2. Deduplicar con fingerprint.
3. Clasificar por confianza.
4. Guardar propuesta en `memoria-sugerida.md` o página temporal revisable.
5. Promover a memoria/wiki solo con revisión cuando corresponda.

## Relacionado

- [[geoffrey/mcp-evaluacion-2026-05-19]]
- [[geoffrey/checkpoints/checkpoint-2026-05-19-0142-ob1-roadmap-phase1-start-4c4e74ca3e1e]]
- [[geoffrey/AGENT]]
