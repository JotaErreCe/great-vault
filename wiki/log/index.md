---
type: reference
date: 2026-05-04
tags: [log, navigation]
---

# Log — historial del vault

> Histórico append-only particionado por mes. Solo cargar bajo demanda — no incluir en bootstrap.

## Meses

- [[log/2026-04|abril 2026]] — init del vault, ingestas masivas, primera estructura
- [[log/2026-05|mayo 2026]] — reestructura, refactor AI-first

## Convención de entradas

```
YYYY-MM-DD | tipo      | descripción
```

Tipos: `init` · `create` · `update` · `correct` · `delete` · `refactor` · `rename` · `archive` · `clean` · `rewrite` · `ingest` · `scan` · `templates`.

## Reglas

- **Append-only** — NO editar entradas pasadas. Si algo cambió, crear nueva entrada.
- **Mensual** — al iniciar nuevo mes, crear `log/YYYY-MM.md`.
