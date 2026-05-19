---
type: reference
date: 2026-05-19
tags: [agente, geoffrey, ob1, seguridad, autoridad]
---

# Tool Authority Matrix — Geoffrey

Matriz de autoridad para decidir qué puede leer/escribir Geoffrey y qué requiere aprobación explícita de JR.

## Principio

La confianza se hereda de la fuente y del nivel de revisión, no del entusiasmo del agente. Todo dato generado por agente nace como **propuesta**, no como verdad canónica.

## Niveles de confianza

| Nivel | Fuente | Puede usarse para | Promoción |
|---|---|---|---|
| T0 | Instrucción explícita de JR en conversación directa | Decisiones operativas inmediatas | Se puede registrar como decisión destilada si no contiene sensible innecesario |
| T1 | Archivos canónicos del Vault en `wiki/` | Respuestas, planificación, brief | Ya es conocimiento compilado; editar solo con log |
| T2 | `raw/` del Vault y fuentes originales read-only | Verificación, ingestión, citas internas | Solo se destila a `wiki/` con resumen y log |
| T3 | Herramientas read-only autorizadas (Gmail, Calendar, Drive, imsg, web) | Señales/candidatos | Debe minimizarse; no guardar dumps crudos |
| T4 | Salida de agente/subagente/LLM | Borrador o propuesta | Requiere revisión antes de volverse memoria persistente |
| T5 | Web general no verificada | Contexto preliminar | Verificar con fuentes primarias antes de actuar |


## Matriz mínima aprobada por JR

| Destino | Quién puede escribir |
|---|---|
| `raw/` | JR únicamente (inmutable) |
| `wiki/` | Geoffrey + subagentes con log obligatorio |
| `wiki/agentes/geoffrey/memoria-sugerida.md` | Geoffrey (propone) |
| `wiki/agentes/geoffrey/memoria.md` | Solo con confirmación explícita de JR |
| `_sensitive.md` | Solo JR |

## Autoridad por superficie

| Superficie | Leer | Escribir | Condiciones |
|---|---:|---:|---|
| `raw/` | Sí | No | Solo JR o ingesta aprobada explícitamente. Geoffrey no edita ni borra. |
| `wiki/` | Sí | Sí | Permitido para conocimiento compilado; requiere leer antes, evitar duplicados y append en `wiki/log/YYYY-MM.md`. |
| `wiki/decisiones/` | Sí | Sí | Solo decisiones explícitas/inequívocas de JR, destiladas; no transcript. |
| `wiki/agentes/geoffrey/memoria.md` | Sí | Con confirmación | Memoria duradera de agente; requiere revisión y guía de escritura de memoria. |
| `memoria-sugerida.md` | Sí | Sí | Zona de staging para propuestas de memoria; no es autoridad hasta revisión. |
| `_sensitive.md` | No por defecto | No | Solo leer por solicitud explícita de trámite concreto. Nunca copiar. |
| Gmail | Read-only por defecto | No | Enviar/modificar/archivar/labels requiere aprobación por acción. |
| Calendar | Read-only por defecto | No | Crear/editar/borrar/responder eventos requiere aprobación por acción. |
| Drive/Docs/Sheets | Read-only por defecto | No | Crear/editar/borrar/mover/compartir requiere aprobación por acción. |
| SMS/iMessage | Lectura minimizada | No | No enviar/reaccionar/marcar leído sin aprobación. |
| Web search | Sí | N/A | Preferir fuentes primarias y citar incertidumbre. |

## Regla de conflicto

Si dos fuentes chocan:

1. Gana instrucción explícita reciente de JR, salvo riesgo legal/seguridad.
2. Luego fuente primaria/documento original.
3. Luego `wiki/` actualizado con log.
4. Luego memoria runtime.
5. Luego salida de agente.

Si el conflicto afecta dinero, terceros, legal, salud, permisos o datos sensibles: pausar y preguntar.

## Relacionado

- [[geoffrey/ob1-fase-2]]
- [[geoffrey/importadores-seguros]]
- [[geoffrey/memory-writing-best-practices]]
