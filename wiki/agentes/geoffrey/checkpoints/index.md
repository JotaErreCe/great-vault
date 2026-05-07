---
type: reference
date: 2026-05-07
tags: [agente, geoffrey, checkpoints, continuidad]
---

# Checkpoints — Geoffrey

Índice de cortes formales de continuidad de Geoffrey. Un checkpoint se crea cuando existe riesgo de perder contexto operativo: compaction, reset, cambio de sesión importante, cierre de una tarea compleja o antes de que Master JR pida “borrar”/reiniciar memoria de trabajo.

## Propósito

Los checkpoints preservan continuidad sin guardar transcripts crudos. Deben capturar solo lo necesario para que Geoffrey u otro agente pueda continuar con criterio: contexto, decisiones, datos confirmados, pendientes, bloqueos, archivos tocados y próximo paso recomendado.

## Cuándo crear uno

- Antes de `/compact`, compaction automática o resumen de contexto si Geoffrey tiene oportunidad de actuar.
- Antes de `/reset`, `/new`, “borrado” de memoria de trabajo o cambio de sesión importante.
- Al terminar una tarea larga con varias decisiones o fuentes consultadas.
- Antes de pausar trabajo que tiene bloqueos o próximos pasos delicados.

## Convención de nombres

Usar nombres sin espacios, en minúsculas y sin empezar por número:

```text
checkpoint-YYYY-MM-DD-HHMM-motivo.md
```

Ejemplos:

```text
checkpoint-2026-05-07-1145-fase-1-continuidad.md
checkpoint-2026-05-07-1800-pre-compact.md
checkpoint-2026-05-08-0715-brief-mananero.md
```

## Plantilla

Usar [[geoffrey-checkpoint]] como molde base.

## Apoyo automático de OpenClaw

Existe un hook runtime llamado `geoffrey-checkpoint` en `~/.openclaw/workspace/hooks/geoffrey-checkpoint/`.

Eventos cubiertos:

- `command:new`
- `command:reset`
- `session:compact:before`

Este hook es un **guardrail mínimo**, no reemplaza el checkpoint manual de Geoffrey. Por privacidad no guarda transcript crudo ni intenta resumir con LLM; solo crea un checkpoint automático con metadata del evento, puntero local al session file y próximos pasos de recuperación.

Estado al 2026-05-07: hook habilitado en config (`hooks.internal.entries.geoffrey-checkpoint.enabled = true`). La carga efectiva en el Gateway puede requerir restart/reload de hooks; no reiniciar Gateway si Master JR no está en casa o no lo aprueba explícitamente.

## Regla de privacidad

No guardar transcripts crudos ni contenido sensible literal. Si un dato sensible fue operacionalmente importante, resumirlo al mínimo necesario y apuntar al archivo canónico correspondiente, nunca copiar credenciales o identificadores sensibles.

## Relacionado

- [[geoffrey/AGENT|AGENT — Geoffrey]] · [[geoffrey/memoria|Memoria — Geoffrey]] · [[geoffrey/conversaciones/2026-05-07|Conversación — 2026-05-07]] · [[geoffrey-checkpoint]]
