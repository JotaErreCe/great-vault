---
type: reference
date: 2026-05-07
tags: [agente, index, arquitectura]
---

# Agentes

Índice operativo de agentes del Great Vault. Cada agente especializado debe vivir en su propia carpeta canónica bajo `wiki/agentes/[slug]/` y cargar sus reglas desde ahí.

## Regla de auto-ubicación

Si eres un agente:

1. Lee [[_AI_BOOTSTRAP]].
2. Identifica tu nombre/rol operativo.
3. Convierte tu nombre a slug `lowercase-con-guiones`.
4. Busca tu carpeta en `wiki/agentes/[slug]/`.
5. Si existe, carga `SOUL.md`, `AGENT.md`, `memoria.md` y `skills-permitidas.md`.
6. Si no existe, no inventes identidad ni reglas; revisa [[arquitectura|Arquitectura de agentes]] y pide aprobación antes de crear una instancia desde `_templates/openclaw-agent/`.

## Agentes previstos

| Agente | Carpeta canónica | Estado |
|---|---|---|
| Geoffrey | `wiki/agentes/geoffrey/` | Activo |
| Understanding Kids | `wiki/agentes/understanding-kids/` | Previsto |
| Finanzas | `wiki/agentes/finanzas/` | Previsto |
| Legal | `wiki/agentes/legal/` | Previsto |
| Meta Ads | `wiki/agentes/meta-ads/` | Previsto |
| Marketing / Imágenes | `wiki/agentes/marketing-imagenes/` | Previsto |

## Recursos comunes

- [[arquitectura|Arquitectura de agentes]] — reglas de paquetes, agentes previstos y auto-ubicación.
- [[protocolo-operativo-agentes]] — contrato común OB1 + memoria + continuidad + autoridad para todos los agentes.
- [[protocolo-continuidad-proyectos]] — recuperación obligatoria de proyectos/subproyectos antes de responder continuidad.
- [[briefs|Briefs multi-agente]] — señales especializadas y consolidación.
- [[agentes/skills/index|Catálogo común de skills]] — skills auditadas y whitelist por agente.

## Relacionado

- [[_AI_BOOTSTRAP]] · [[arquitectura|Arquitectura de agentes]] · [[briefs|Briefs multi-agente]] · [[agentes/skills/index|Skills]]
