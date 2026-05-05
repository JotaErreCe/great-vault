---
type: reference
date: 2026-05-05
tags: [agente, arquitectura, reference]
---

# Arquitectura de agentes

El Vault puede tener varios agentes especializados. Cada agente vive en `wiki/agentes/[nombre]/` y comparte las reglas base de [[_AI_BOOTSTRAP]].

## Principio central

Los agentes especializados son expertos por dominio; [[geoffrey/SOUL|Geoffrey]] es el orquestador con visión global de JR. Geoffrey consolida información de agentes, fuentes e integraciones para preparar el brief diario unificado.

## Agentes previstos

| Agente | Rol |
|---|---|
| Geoffrey | Asistente personal, orquestador y generador del brief consolidado. |
| Understanding Kids | Operación de UK: staff, finanzas, catálogo, diplomado y seguimiento comercial. |
| Finanzas | IBKR, cripto, propiedades, patrimonio, cobros y suscripciones. |
| Legal | AMC Legal, casos, clientes, facturación, plazos y Diario de Centro América. |
| Meta Ads | Campañas publicitarias, pauta, métricas y alertas. |
| Marketing / Imágenes | Identidad visual, Canva, creativos y activos gráficos. |

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
