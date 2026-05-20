---
type: reference
date: 2026-05-19
tags: [agentes, ob1, memoria, continuidad, seguridad, protocolo]
---

# Protocolo operativo común de agentes

Contrato común para Geoffrey y cualquier agente especializado del Great Vault. Integra la estructura OB1 adaptada por JR con la arquitectura de memoria del Vault.

## Principio raíz

Un agente no debe depender de memoria runtime, embeddings o “lo que cree recordar” para operar el Vault. Debe recuperar contexto desde fuentes canónicas, registrar cambios y tratar toda salida de agente como propuesta hasta que sea revisada o destilada.

## Capas que se complementan

| Capa | Fuente | Propósito |
|---|---|---|
| Bootstrap | [[_AI_BOOTSTRAP]] | Entrada única, schema global y reglas de cualquier AI. |
| Arquitectura de agentes | [[arquitectura]] / [[agentes]] | Auto-ubicación, paquetes por agente y reglas comunes. |
| Memoria | [[escribir-memoria]] + memoria del agente | Reglas duraderas y punteros; nunca estados vivos como verdad final. |
| Captura diaria | [[protocolo-captura-diaria]] | Huella durable de asuntos importantes hablados con JR. |
| Continuidad | [[protocolo-continuidad-proyectos]] | Recuperar proyectos/subproyectos antes de responder. |
| Autoridad | [[geoffrey/tool-authority-matrix]] | Qué fuente puede convertirse en qué tipo de conocimiento. |
| Work logs | [[geoffrey/work-log]] | Registro de tareas largas: intentado, cambiado, fallado, decisiones, pendientes, próximo paso y artifacts. |
| Memoria sugerida | [[geoffrey/memoria-sugerida]] | Bandeja de revisión; nada pasa a memoria permanente sin JR. |
| Importadores seguros | [[geoffrey/importadores-seguros]] | Dry-run, fingerprints, dedup, minimización y aprobación antes de escrituras masivas. |
| Checkpoints | [[geoffrey/checkpoints/index]] | Cortes de continuidad ante compaction, reset o handoff. |

## Reglas obligatorias para cualquier agente

### 1. Auto-ubicación

1. Leer [[_AI_BOOTSTRAP]].
2. Identificar agente/rol operativo.
3. Resolver `wiki/agentes/[slug]/`.
4. Cargar `SOUL.md`, `AGENT.md`, `memoria.md` y `skills-permitidas.md` si existen.
5. Si no existe paquete, no inventar identidad ni reglas; pedir aprobación o coordinación de Geoffrey.

### 2. Recuperación antes de responder

Para continuidad de proyectos, aplicar [[protocolo-continuidad-proyectos]]. `memory_search` vacío no prueba inexistencia.

Mínimo: `vault-map/index` → página canónica → subcarpeta → log → decisiones → conversaciones/checkpoints → fuentes externas autorizadas.

### 3. Anti-reinvención antes de proponer

Antes de sugerir crear una norma, workflow, skill, protocolo, estructura, automatización o “solución nueva”, el agente debe verificar si ya existe algo equivalente o parcialmente equivalente en el Vault.

Búsqueda mínima obligatoria:

1. `vault-map` / `index` para navegación.
2. `wiki/agentes/[slug]/AGENT.md`, memoria y recursos del agente.
3. `wiki/resources/`, `wiki/agentes/skills/`, `wiki/agentes/[slug]/work-log*`, `ob1-*`, decisiones y log recientes.
4. Búsqueda exacta por filesystem (`grep`/`rg`) con palabras clave y sinónimos.

Regla: si existe una estructura previa, la respuesta debe partir de ella: “ya tenemos X; falta Y; propongo ajustar Z”, no presentar Y como si fuera idea nueva. `memory_search` vacío no basta para concluir que no existe.

### 4. Escritura segura

- `raw/` es inmutable para agentes.
- `wiki/` puede actualizarse con lectura previa, búsqueda de duplicados y línea en `wiki/log/YYYY-MM.md`.
- `wiki/decisiones/YYYY-MM.md` recibe decisiones explícitas de JR, destiladas.
- `wiki/agentes/[slug]/conversaciones/YYYY-MM-DD.md` recibe continuidad diaria importante: temas, acuerdos, pendientes, artifacts y links, sin transcript crudo.
- Todo asunto importante hablado con JR debe pasar por [[protocolo-captura-diaria]] antes de cerrarse. Un archivo temporal, transcript interno, cache o respuesta de chat no cuenta como guardado en el Vault.
- `_sensitive.md` solo por solicitud explícita y nunca se copia.
- Reorganizaciones amplias, borrados, importaciones masivas y acciones externas requieren aprobación.

### 5. Memoria persistente

Aplicar [[escribir-memoria]] antes de escribir memoria:

- memoria = regla/puntero con fecha, no estado vivo;
- no rutas absolutas universales;
- no transcripts crudos;
- no PII/secrets;
- no promover salida de agente a memoria permanente sin revisión.

### 6. OB1 adaptado

- Tareas largas o delicadas: crear work log.
- Riesgo de pérdida de contexto: crear checkpoint.
- Recuerdo nuevo: proponer en memoria sugerida; JR decide promoción.
- Importación externa: dry-run/fingerprints/dedup/minimización antes de escribir.
- Subagentes: output T4; se revisa antes de hacerlo canónico.

## Checklist pre-respuesta

Antes de contestar sobre algo que puede estar en el Vault:

- [ ] ¿Leí o confirmé el bootstrap/contexto de agente?
- [ ] ¿Busqué en `vault-map`/`index`?
- [ ] ¿Revisé página canónica y subcarpetas?
- [ ] ¿Revisé log/decisiones/conversaciones/checkpoints cuando es continuidad?
- [ ] ¿Separé confirmado vs inferido vs pendiente?
- [ ] ¿Necesito work log, checkpoint o memoria sugerida?
- [ ] ¿Este asunto debe quedar en conversación diaria según [[protocolo-captura-diaria]]?
- [ ] ¿La respuesta evita datos sensibles innecesarios?

## Checklist post-cambio

Después de editar el Vault:

- [ ] Archivo con frontmatter si está en `wiki/`.
- [ ] Wikilinks internos, no markdown links para notas del Vault.
- [ ] `## Relacionado` cuando aplique.
- [ ] Línea en `wiki/log/YYYY-MM.md`.
- [ ] Decisión registrada si JR decidió algo.
- [ ] Conversación diaria actualizada si el asunto debe ser recuperable por fecha.
- [ ] Work log si fue tarea larga/delicada.
- [ ] Memoria sugerida si es una regla duradera pendiente de aprobación.

## Relacionado

- [[_AI_BOOTSTRAP]]
- [[arquitectura]]
- [[agentes]]
- [[escribir-memoria]]
- [[protocolo-captura-diaria]]
- [[protocolo-continuidad-proyectos]]
- [[geoffrey/tool-authority-matrix]]
- [[geoffrey/work-log]]
- [[geoffrey/memoria-sugerida]]
- [[geoffrey/importadores-seguros]]
