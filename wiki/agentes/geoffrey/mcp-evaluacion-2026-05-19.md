---
type: reference
date: 2026-05-19
tags: [agente, geoffrey, mcp, integraciones, ob1]
---

# Evaluación MCP — Geoffrey — 2026-05-19

## Contexto

JR aprobó iniciar Fase 1 del roadmap Geoffrey/OB1: `/geoffrey-checkpoint`, hook de cierre y evaluación de Gmail MCP + Apple Calendar MCP antes de Fase 2.

## Gmail MCP / Google Workspace MCP

Estado: **instalado y conectado en Claude Code** como `google-workspace`.

- Paquete observado: `@presto-ai/google-workspace-mcp` v1.0.12.
- Config previo: existía en `mcporter` global (`/Users/jr/.mcporter/mcporter.json`).
- Acción: agregado a Claude Code local project config para `/Users/jr/.openclaw/workspace-geoffrey`.
- Health check: `claude mcp list` reportó `google-workspace ... ✓ Connected`.
- Herramientas relevantes disponibles vía schema MCP:
  - `gmail.search`, `gmail.get`, `gmail.downloadAttachment`, `gmail.modify`, `gmail.send`, drafts/labels.
  - `calendar.list`, `calendar.listEvents`, `calendar.getEvent`, create/update/respond/delete.
- Prueba read-only: `gmail.search` con `newer_than:1d maxResults:1` respondió con 1 message id y estimate de resultados.

### Guardrails

- Geoffrey debe usar Gmail read-only por defecto.
- Auto-captura hacia `raw/inbox/` requiere diseño específico: dry-run, fingerprints, filtros de señal, secret/PII scan y evitar mensajes crudos salvo autorización granular.
- No usar `gmail.modify`, `gmail.send`, drafts, labels o attachments sin aprobación explícita por acción.

## Calendar

### Google Calendar MCP

Estado: **cubierto por Google Workspace MCP**.

- `calendar.list` respondió con calendarios Google: festivos GT, Todoist, `joserca95@gmail.com`, Familia.
- Herramientas de escritura existen; Geoffrey debe tratarlas como prohibidas sin aprobación.

### Apple Calendar local

Estado: **funcional sin MCP adicional**.

- AppleScript directo: 17 calendarios; 7 eventos próximos en 14 días.
- Skill local `apple-calendar-jr` lista eventos vía SQLite/dump local: 7 eventos y sin error.
- Esto resuelve la necesidad operativa del brief mañanero sin instalar un MCP amplio.

### Apple Calendar MCP adicional

Estado: **no instalado por ahora**.

Motivo:

- No apareció candidato claro, estrecho y seguro para Apple Calendar MCP.
- Candidatos tipo `local-mcp` son demasiado amplios (Mail/Calendar/Contacts/Teams/OneDrive) para instalarlos sin auditoría separada.
- El requisito del brief queda cubierto por la skill read-only local; si vuelve el error `-600`, investigar causa puntual antes de añadir superficie de ataque.

## Búsqueda web MCP

Pendiente Fase 1/2: comparar Brave Search vs Perplexity.

Hallazgos preliminares:

- ClawHub tiene múltiples skills/plugins Brave Search y Perplexity.
- OpenClaw ya tiene `web_search` habilitado con provider actual `ollama`, pero para research legal/proyectos conviene proveedor web real con citas.
- Recomendación preliminar: Brave para búsqueda factual simple y Perplexity para síntesis con citas; decidir tras auditoría de llaves/costos/privacidad.

## Bloqueantes antes de Fase 2

- Hook de cierre Claude Code ya existe, pero como comando no debe leer ni guardar transcript crudo; por tanto crea checkpoint mínimo y deja destilación semántica manual cuando la sesión fue sustantiva.
- Falta decidir si aceptamos ese límite o si JR quiere un hook más agresivo que lea transcript local para resumir decisiones con LLM.
- Falta auditar búsqueda web MCP/skill antes de instalar Brave o Perplexity.

## Relacionado

- [[geoffrey/checkpoints/index|Checkpoints — Geoffrey]]
- [[geoffrey/skills-permitidas|Skills permitidas — Geoffrey]]
- [[agentes/skills/index|Catálogo común de skills]]
