---
type: reference
date: 2026-05-20
tags: [agentes, continuidad, memoria, captura, vault]
---

# Protocolo de captura diaria

Regla general estricta para Geoffrey y cualquier agente existente o futuro: toda interacción importante con JR debe dejar una huella recuperable en el Vault el mismo día, sin depender de memoria runtime, transcripts temporales, embeddings o buena suerte.

## Principio

Si JR razonablemente podría preguntar después “¿qué hablamos?”, “¿qué decidimos?”, “¿qué quedó pendiente?”, “¿qué te mandé?” o “¿qué hiciste con eso?”, entonces el asunto debe quedar registrado en un destino durable del Vault.

No todo va a memoria permanente. Pero todo asunto importante debe quedar recuperable por fecha, proyecto/persona/tema o decisión.

## Clasificación obligatoria

Al cerrar una conversación, audio, documento, análisis o tarea relevante, el agente debe clasificar lo trabajado:

| Tipo | Destino obligatorio | Qué guardar |
|---|---|---|
| Decisión, aprobación, rechazo, permiso, límite, cambio de criterio | `wiki/decisiones/YYYY-MM.md` | Decisión destilada, sin transcript crudo. |
| Continuidad diaria importante | `wiki/agentes/[slug]/conversaciones/YYYY-MM-DD.md` | Resumen operativo: temas, contexto, acuerdos, pendientes, artifacts. |
| Proyecto/persona/finanza/entidad afectada | Página canónica o subpágina en `wiki/` | Estado actualizado, nota estructurada o enlace claro desde decisiones/conversación. |
| Tarea larga o delicada | `wiki/agentes/[slug]/work-logs/` | Qué se intentó, qué cambió, qué falló, decisiones, pendientes, próximo paso y artifacts. |
| Cambio al Vault | `wiki/log/YYYY-MM.md` | Línea append-only con archivo(s) tocado(s) y propósito. |
| Recuerdo duradero candidato | `wiki/agentes/[slug]/memoria-sugerida.md` | Propuesta pendiente; no promover sin JR. |
| Dato sensible | `_sensitive.md` | Solo si JR lo pidió explícitamente; nunca copiar a wiki/log/conversaciones. |

## Regla de cierre

Un asunto importante no se considera cerrado hasta que exista al menos una de estas huellas durables:

1. entrada en conversación diaria;
2. decisión destilada;
3. página wiki/proyecto/persona actualizada;
4. work log;
5. checkpoint si hubo riesgo de pérdida de contexto.

Si el agente generó archivos temporales (`tmp/`, descargas, transcripciones locales, outputs de scripts), debe promover el resumen o artifact relevante al Vault antes de decir que “quedó guardado”. Los temporales no cuentan como Vault.

## Audios, reuniones y documentos enviados por JR

Para audios, reuniones, documentos importantes o análisis solicitados por JR:

1. Conservar solo lo necesario según minimización.
2. No guardar transcript crudo salvo instrucción explícita de JR o necesidad justificada.
3. Crear nota wiki o entrada de conversación diaria con:
   - fuente y fecha;
   - participantes si aplica;
   - resumen ejecutivo;
   - decisiones/acuerdos;
   - acciones y responsables;
   - riesgos/bloqueos;
   - ubicación de artifacts útiles.
4. Si hubo decisiones, agregar también a `wiki/decisiones/YYYY-MM.md`.
5. Registrar cualquier escritura en `wiki/log/YYYY-MM.md`.


## Trabajo largo y compaction

Para trabajos largos, de varias horas, varias herramientas o varias decisiones, el agente no debe esperar al final para guardar continuidad.

Regla estricta:

1. **Al iniciar** un trabajo largo o delicado, crear o actualizar un work log con alcance, estado inicial y próximo paso.
2. **Durante el trabajo**, actualizar el work log al cerrar hitos relevantes: decisión de JR, cambio de dirección, artifact importante, bloqueo, o batch grande de herramientas.
3. **Antes de compaction/reset/cambio de sesión**, si hay oportunidad técnica, crear checkpoint con estado actual, decisiones, archivos tocados, pendientes y siguiente acción.
4. **Si la compaction fue automática y no hubo oportunidad**, al retomar contexto el agente debe reconstruir desde `AGENT.md` → conversación diaria → work log → checkpoint → decisiones → log, y crear una entrada marcada como reconstrucción posterior.
5. **Al final**, cerrar con conversación diaria y, si aplica, decisión/proyecto/log.

Si un trabajo de dos horas se comprime dos veces, el Vault debe conservar una cadena durable:

`work log inicial → checkpoint/pre-compact o reconstrucción → work log actualizado → checkpoint/pre-compact o reconstrucción → cierre en conversación diaria/decisiones/proyecto`

La compaction puede perder matices del chat, pero no debe borrar el estado operativo necesario para continuar.

## Qué NO hacer

- No decir “lo guardé en el Vault” si solo existe en `tmp/`, runtime, cache, transcript interno o respuesta de chat.
- No confiar solo en `memory_search` para recuperar continuidad.
- No guardar transcripts crudos por defecto.
- No duplicar todo en memoria permanente.
- No copiar datos sensibles en conversaciones/log/decisiones.

## Recuperación mínima por fecha

Cuando JR pregunte por algo “de ayer”, “hoy”, “la reunión”, “lo que hablamos” o similar, el agente debe revisar, en este orden:

1. `wiki/agentes/[slug]/conversaciones/YYYY-MM-DD.md` del día indicado y días cercanos;
2. `wiki/decisiones/YYYY-MM.md`;
3. `wiki/log/YYYY-MM.md`;
4. página canónica del proyecto/persona/entidad implicada y subcarpetas;
5. work logs/checkpoints relevantes;
6. artifacts externos autorizados si el asunto dependía de ellos.

## Checklist post-turn para agentes

Antes de cerrar una respuesta sobre un asunto importante:

- [ ] ¿Esto debe ser recuperable mañana?
- [ ] ¿Hay decisión de JR que deba ir a `decisiones`?
- [ ] ¿Afecta proyecto/persona/finanza/entidad?
- [ ] ¿Debe quedar en conversación diaria?
- [ ] ¿Hubo archivo temporal que deba promoverse a wiki?
- [ ] ¿Si edité wiki, agregué log?
- [ ] ¿Separé confirmado, inferido y pendiente?
- [ ] ¿Evité datos sensibles y transcript crudo innecesario?

## Relacionado

- [[protocolo-operativo-agentes]]
- [[protocolo-continuidad-proyectos]]
- [[escribir-memoria]]
- [[agentes/geoffrey/AGENT]]
- [[agentes/geoffrey/memoria]]
- [[decisiones/index]]
