---
type: reference
date: 2026-05-19
tags: [agente, geoffrey, web-search, mcp, ob1, auditoria]
---

# Auditoría web search — Brave vs Perplexity — 2026-05-19

## Contexto

Fase 1 dejó pendiente comparar Brave Search vs Perplexity para investigación web. OpenClaw ya tiene `web_search` habilitado y probado, pero conviene decidir si se necesita proveedor externo adicional para research legal/proyectos.

## Hallazgos preliminares

| Opción | Fortalezas | Riesgos/costos | Recomendación |
|---|---|---|---|
| OpenClaw `web_search` actual | Ya disponible; no requiere instalar MCP nuevo; suficiente para búsquedas simples. | Provider observado como `ollama`; calidad/citas dependen del backend configurado. | Mantener como default mientras no haya necesidad específica. |
| Brave Search MCP oficial | Búsqueda factual directa; proveedor de búsqueda, no motor de síntesis; menor superficie conceptual. Paquete oficial `@brave/brave-search-mcp-server` observado en resultados web/NPM. | Requiere API key/costo; instalar MCP nuevo; revisar permisos y límites. | Mejor candidato si se quiere búsqueda simple con control y menos “opinión”. |
| Perplexity MCP oficial | Buen candidato para síntesis con citas y research; paquete oficial `@perplexity-ai/mcp-server` observado. | Requiere API key/costo; envía prompts a Perplexity; puede mezclar síntesis con fuentes y requiere verificación. | Útil para research profundo, no como fuente canónica automática. |

## Decisión recomendada

Para Geoffrey:

1. **No instalar nada todavía** hasta tener una necesidad concreta o API key/costo aprobado.
2. Si se necesita mejorar búsqueda factual diaria: preferir Brave Search primero.
3. Si se necesita research profundo con síntesis/citas: evaluar Perplexity por tarea, con presupuesto y privacidad explícitos.
4. Nunca promover resultados web a memoria canónica sin fuente primaria o revisión.

## Fuentes consultadas

- Web search: `brave/brave-search-mcp-server`, NPM `@brave/brave-search-mcp-server`, NPM `@modelcontextprotocol/server-brave-search`.
- Web search: GitHub `perplexityai/modelcontextprotocol`, NPM `@perplexity-ai/mcp-server`.
- `npm view @modelcontextprotocol/server-brave-search` devolvió versión `0.6.2` y descripción de MCP para Brave Search API.
- `npm search perplexity mcp` mostró varios paquetes, incluyendo opción oficial `@perplexity-ai/mcp-server`.

## Estado

Auditoría preliminar completa. Falta decisión de JR si quiere pagar/configurar API key para un proveedor externo.

## Relacionado

- [[geoffrey/mcp-evaluacion-2026-05-19]]
- [[geoffrey/ob1-fase-2]]
