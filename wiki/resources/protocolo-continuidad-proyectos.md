---
type: reference
date: 2026-05-19
tags: [proyectos, agentes, continuidad, recuperacion, protocolo]
---

# Protocolo de continuidad de proyectos

Regla común para Geoffrey y cualquier agente especializado cuando JR pregunta por un proyecto, subproyecto, pendiente, “lo que estábamos haciendo”, “contigo”, “fase”, “roadmap” o continuidad de trabajo.

## Problema que resuelve

Un proyecto puede existir en varias capas del Vault:

- página canónica del proyecto;
- subcarpeta del proyecto;
- decisiones mensuales;
- log mensual;
- conversación diaria del agente;
- checkpoints;
- fuentes externas autorizadas como Drive/iCloud/Docs/Sheets.

Si un agente lee solo la página general o solo usa búsqueda semántica, puede no recuperar una iniciativa específica ya existente.

## Regla raíz

`memory_search` o memoria runtime son señales auxiliares, no autoridad. Si no devuelven resultados, **no significa que el proyecto no exista**.

Para proyectos del Vault, la recuperación mínima es filesystem + índices + historial.

## Protocolo obligatorio

Antes de responder sobre continuidad de un proyecto:

1. **Ubicar el dominio**
   - Leer [[vault-map]] o [[index]].
   - Identificar slug del proyecto/persona/agente.

2. **Leer página canónica**
   - Ejemplo: `wiki/proyectos/activos/understanding-kids.md`.

3. **Revisar subcarpeta del proyecto**
   - Si existe `wiki/proyectos/activos/[slug]/`, listar archivos y buscar términos relevantes.
   - No asumir que la página canónica contiene todas las iniciativas internas.

4. **Revisar historial operativo**
   - `wiki/log/YYYY-MM.md` del mes actual y, si aplica, anterior.
   - `wiki/decisiones/YYYY-MM.md` del mes actual y, si aplica, anterior.

5. **Revisar continuidad del agente**
   - `wiki/agentes/[agent]/conversaciones/YYYY-MM-DD.md` recientes.
   - Checkpoints relevantes en `wiki/agentes/[agent]/checkpoints/`.

6. **Revisar fuentes externas autorizadas**
   - Solo si el proyecto depende de Drive/iCloud/Gmail/Sheets/etc.
   - Modo read-only y minimizado.
   - No abrir secretos ni PII salvo solicitud explícita.

7. **Responder con estado recuperado**
   - Nombrar la iniciativa exacta encontrada.
   - Distinguir hecho confirmado, pendiente y duda.
   - Si hay varias iniciativas posibles, listar opciones y pedir selección.

## Orden de autoridad

1. Instrucción reciente explícita de JR.
2. Página canónica del proyecto + subarchivos específicos.
3. Decisiones mensuales.
4. Log mensual.
5. Conversaciones/checkpoints.
6. Fuentes externas autorizadas.
7. Memoria runtime / `memory_search`.

## Checklist corto para agentes

Antes de decir “no sé” o responder genérico:

- [ ] ¿Leí `vault-map` o `index`?
- [ ] ¿Leí la página canónica?
- [ ] ¿Busqué en la subcarpeta?
- [ ] ¿Busqué en `log/`?
- [ ] ¿Busqué en `decisiones/`?
- [ ] ¿Revisé conversaciones/checkpoints recientes?
- [ ] ¿Hay fuente externa autorizada que deba revisar?

## Caso de referencia

El 2026-05-19 Geoffrey no recuperó inicialmente el proyecto específico de UK [[understanding-kids/plan-nutricion-completa]] y respondió desde el mapa operativo general. Auditoría: [[geoffrey/auditoria-recuperacion-uk-2026-05-19]].

## Relacionado

- [[_AI_BOOTSTRAP]]
- [[arquitectura]]
- [[vault-map]]
- [[geoffrey/auditoria-recuperacion-uk-2026-05-19]]
