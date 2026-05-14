---
type: reference
date: 2026-05-14
tags: [agente, geoffrey, checkpoint, continuidad, decisiones]
---

# Checkpoint — 2026-05-14 13:43

Resumen operativo creado tras formalizar captura de decisiones destiladas para proteger continuidad ante compaction/reset.

## Motivo

- Tipo: cambio de protocolo de memoria/continuidad.
- Sesión/canal: Telegram directo con JR.
- Riesgo de pérdida de contexto: medio; se acababa de discutir compresión de contexto y recuperación posterior.

## Contexto

JR explicó que el Great Vault debe funcionar como su segundo cerebro y que quiere poder preguntar después decisiones pasadas por tema o mes, sin guardar conversaciones completas.

## Decisiones tomadas

- Crear `wiki/decisiones/` como registro mensual de decisiones destiladas.
- Geoffrey debe capturar automáticamente decisiones explícitas o inequívocas de JR en `wiki/decisiones/YYYY-MM.md`.
- No guardar transcripts completos; guardar decisiones, aprobaciones, rechazos, preferencias, límites y cambios de criterio en versión optimizada.
- En recuperación post-compaction/reset, Geoffrey debe leer decisiones mensuales además de conversación diaria, checkpoint y log.

## Datos confirmados

- Archivos creados: `wiki/decisiones/index.md`, `wiki/decisiones/2026-05.md`.
- Se actualizó el protocolo en `wiki/agentes/geoffrey/AGENT.md` y `wiki/agentes/geoffrey/memoria.md`.
- `_AI_BOOTSTRAP.md` fue actualizado para incluir `wiki/decisiones/` y el tipo `decision`.

## Pendientes

- [ ] En futuras decisiones, actualizar también páginas canónicas de proyecto/persona/agente cuando aplique, no solo el registro mensual.
- [ ] Revisar mensualmente `wiki/decisiones/YYYY-MM.md` para consolidar duplicados y mejorar wikilinks.

## Bloqueos

- Ninguno.

## Archivos consultados

- `_AI_BOOTSTRAP.md`
- `wiki/agentes/geoffrey/AGENT.md`
- `wiki/agentes/geoffrey/memoria.md`
- `wiki/agentes/arquitectura.md`
- `wiki/index.md`
- `_templates/geoffrey-checkpoint.md`

## Archivos creados o modificados

- `wiki/decisiones/index.md`
- `wiki/decisiones/2026-05.md`
- `wiki/agentes/geoffrey/AGENT.md`
- `wiki/agentes/geoffrey/memoria.md`
- `wiki/agentes/geoffrey/conversaciones/2026-05-14.md`
- `wiki/agentes/geoffrey/checkpoints/checkpoint-2026-05-14-decisiones-vault.md`
- `wiki/agentes/arquitectura.md`
- `_AI_BOOTSTRAP.md`
- `wiki/index.md`
- `wiki/log/2026-05.md`

## Fuentes externas consultadas

- Ninguna.

## Próximo paso recomendado

- A partir de ahora, cuando JR exprese una decisión durable, capturarla de inmediato en `wiki/decisiones/2026-05.md` y enlazarla desde la conversación diaria si afecta continuidad operativa.

## Notas de seguridad / privacidad

- No se guardó transcript crudo.
- No se copiaron credenciales, tokens, DPI/NIT/direcciones ni datos sensibles innecesarios.

## Relacionado

- [[geoffrey/AGENT|AGENT — Geoffrey]] · [[geoffrey/memoria|Memoria — Geoffrey]] · [[decisiones/2026-05]] · [[geoffrey/conversaciones/2026-05-14]]
