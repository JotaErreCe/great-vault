---
type: reference
date: 2026-05-07
tags: [agente, arquitectura, reference]
---

# Arquitectura de agentes

El Vault puede tener varios agentes especializados. Cada agente vive en `wiki/agentes/[nombre]/` para conocimiento duradero y comparte las reglas base de [[_AI_BOOTSTRAP]]. El runtime activo de OpenClaw vive fuera del Vault, en workspaces por agente bajo `~/.openclaw/`.

## Separación runtime/Vault

- `~/.openclaw/workspace-[agent-id]/` = entorno runtime del agente: `AGENTS.md`, `IDENTITY.md`, `SOUL.md`, `USER.md`, `HEARTBEAT.md`, `MEMORY.md`, skills locales y artefactos temporales.
- `wiki/agentes/[agent-id]/` = paquete canónico duradero del agente: identidad, instrucciones, memoria, rutinas, integraciones y decisiones auditables.
- Vault root (`AGENTS.md`, `IDENTITY.md`, `USER.md`, `SOUL.md`) no debe definir una persona activa para todos los agentes. Sirve como schema/control o boundary; ningún agente debe inferir su identidad desde el root del Vault.
- `wiki/decisiones/YYYY-MM.md` guarda decisiones destiladas de JR para consulta futura; no es transcript ni log técnico.
- Workspace neutral/fallback: `/Users/jr/.openclaw/workspaces/_default-neutral/`. Si un agente cae allí, debe detenerse y pedir/configurar workspace específico.
- Geoffrey activo: `/Users/jr/.openclaw/workspace-geoffrey/` + `wiki/agentes/geoffrey/`.

## Principio central

Los agentes especializados son expertos por dominio; [[geoffrey/SOUL|Geoffrey]] es el orquestador con visión global de JR. Geoffrey consolida información de agentes, fuentes e integraciones para preparar el brief diario unificado.

## Agentes previstos

| Agente | Carpeta canónica | Rol | Estado |
|---|---|---|---|
| Geoffrey | `wiki/agentes/geoffrey/` | Asistente personal, orquestador y generador del brief consolidado. | Activo |
| Understanding Kids | `wiki/agentes/understanding-kids/` | Operación de UK: staff, finanzas, catálogo, diplomado y seguimiento comercial. | Previsto |
| Finanzas | `wiki/agentes/finanzas/` | IBKR, cripto, propiedades, patrimonio, cobros y suscripciones. | Previsto |
| Legal | `wiki/agentes/legal/` | AMC Legal, casos, clientes, facturación, plazos y Diario de Centro América. | Previsto |
| Meta Ads | `wiki/agentes/meta-ads/` | Campañas publicitarias, pauta, métricas y alertas. | Previsto |
| Marketing / Imágenes | `wiki/agentes/marketing-imagenes/` | Identidad visual, Canva, creativos y activos gráficos. | Previsto |

## Captura de decisiones

Cualquier agente que opere con JR debe distinguir tres registros:

- `wiki/decisiones/YYYY-MM.md`: decisiones de JR y acuerdos destilados, consultables por tema/fecha.
- `wiki/agentes/[agent-id]/conversaciones/YYYY-MM-DD.md`: continuidad operativa diaria del agente.
- `wiki/log/YYYY-MM.md`: auditoría append-only de cambios hechos al Vault.

No guardar conversaciones completas salvo fuente cruda autorizada en `raw/`. Las decisiones deben ser breves, específicas y enlazadas a proyecto/persona/agente cuando aplique.

## Auto-ubicación de agentes

Regla para cualquier agente especializado:

1. Leer [[_AI_BOOTSTRAP]] como schema global.
2. Identificar su nombre/rol operativo actual.
3. Normalizarlo a slug `lowercase-con-guiones`.
4. Buscar su carpeta canónica en `wiki/agentes/[slug]/`.
5. Si la carpeta existe, cargar en orden: `SOUL.md`, `AGENT.md`, `memoria.md`, `skills-permitidas.md`.
6. Si la carpeta no existe, **no inventar identidad ni reglas**: usar esta arquitectura como referencia, revisar `_templates/openclaw-agent/` y pedir aprobación a Master JR o coordinación de Geoffrey antes de crear la instancia.

Las carpetas previstas arriba son compromisos de ubicación; no implican que el agente esté creado todavía.

## Carpeta mínima por agente

Cada agente debe tener, como mínimo:

- `SOUL.md` — identidad, tono, límites y rol.
- `AGENT.md` — instrucciones operativas.
- `memoria.md` — aprendizajes persistentes del agente.
- `skills-permitidas.md` — whitelist de skills que ese agente puede usar.

Todo agente nuevo debe incorporar explícitamente la regla de oro de skills en su `SOUL.md` o `AGENT.md`, además de tener su whitelist propia.

## Regla de oro de skills

Ningún agente puede usar libremente cualquier skill instalada en el sistema.

Un agente solo puede usar una skill si cumple ambas condiciones:

1. La skill está documentada y auditada en [[skills/index|catálogo común de skills]].
2. La skill aparece explícitamente en el `skills-permitidas.md` de ese agente.

Si una tarea requiere una skill no autorizada, el agente debe pedir aprobación a Master JR antes de usarla, instalarla o configurarla.

## Brief diario consolidado

El brief diario sigue la arquitectura descrita en [[briefs|briefs multi-agente]]. No debe ser una suma mecánica de reportes. Geoffrey debe:

1. Recibir o consultar señales de los agentes especializados.
2. Quitar duplicados, ruido y temas fríos sin movimiento.
3. Priorizar por impacto para JR.
4. Presentar un resumen corto en Telegram, estilo newsletter.
5. Incluir acciones recomendadas y cómo ejecutarlas.
6. Guardar el brief en `wiki/agentes/geoffrey/briefs/brief-YYYY-MM-DD.md` cuando corresponda.

## Relacionado

- [[geoffrey/SOUL|Geoffrey]] · [[geoffrey/AGENT|AGENT — Geoffrey]] · [[skills/index|Skills]] · [[_AI_BOOTSTRAP]]
