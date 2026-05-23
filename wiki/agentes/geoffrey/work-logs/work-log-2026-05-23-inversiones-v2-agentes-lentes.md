---
type: reference
date: 2026-05-23
tags: [agente, geoffrey, inversiones, jordan-belfort, work-log]
---

# Work log — Inversiones v2 agentes + lentes — 2026-05-23

## Qué se intentó

Refinar la arquitectura de inversiones v2 para crear agentes reales explícitos y checklists/lentes explícitos, evitando convertir cada unidad analítica en agente.

## Qué cambió

- Creados 6 agentes reales en `wiki/agentes/inversiones/agents/`:
  - Charlie Munger.
  - Paul Tudor Jones.
  - Mark Douglas.
  - Risk Manager.
  - Journal Keeper.
  - Teacher.
- Creados 26 lentes/checklists en `wiki/agentes/inversiones/lentes/`.
- Actualizados README, arquitectura y protocolo para apuntar a agentes reales y lentes.
- Desk AGENTs anteriores quedan como wrappers de compatibilidad hacia los agentes reales.

## Qué falló / ajustes

- No hubo errores de escritura. La auditoría mantiene los 2 links rotos antiguos de `raw/` y 2 ambigüedades antiguas en `_sensitive.md`/`raw`, deliberadamente no tocadas.

## Decisiones

- Mantener como agentes solo roles con juicio/responsabilidad.
- Mantener como lentes/checklists las unidades de soporte analítico.
- No crear automatizaciones ni conexiones externas.

## Pendientes

- Si JR quiere, siguiente fase puede agregar scoring por lente y reglas de promoción de lente → agente.
- Si Jordan runtime necesita instrucciones, sincronizar su prompt/config con estos archivos.

## Próximo paso

Reportar a JR el inventario creado y evidencia de verificación.

## Artifacts

- `wiki/agentes/inversiones/agents/README.md`
- `wiki/agentes/inversiones/lentes/README.md`
- Reporte temporal: `/Users/jr/.openclaw/workspace-geoffrey/tmp/vault_audit_report.json`

## Relacionado

- [[agentes/inversiones/agents/README]]
- [[agentes/inversiones/lentes/README]]
- [[agentes/inversiones/arquitectura-inversiones]]
