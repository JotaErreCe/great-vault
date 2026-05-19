---
type: reference
date: 2026-05-19
tags: [agente, geoffrey, auditoria, memoria, understanding-kids, recuperacion]
---

# Auditoría — fallo de recuperación del proyecto UK — 2026-05-19

## Incidente

JR preguntó por “el proyecto de UK contigo”. Geoffrey respondió inicialmente desde el mapa operativo general de Understanding Kids y no recuperó de inmediato el proyecto específico: [[understanding-kids/plan-nutricion-completa]].

## Verificación de existencia

El proyecto sí existía y estaba correctamente documentado en el Vault:

- [[understanding-kids/plan-nutricion-completa]] — plan maestro multi-día para nutrir UK antes de crear `README-AI.md` o agente especializado.
- [[understanding-kids]] — enlaza el plan en “Próximos pasos”.
- [[decisiones/2026-05]] — registra la decisión de nutrir UK antes de crear `README-AI.md`/agente.
- [[geoffrey/conversaciones/2026-05-16]] — registra la continuidad del plan.
- `wiki/log/2026-05.md` — contiene entradas del 2026-05-16 sobre creación/enlace del plan.

También existen fuentes complementarias:

- iCloud local `Documents/Understanding Kids/UNDERSTANDING_KIDS_MAESTRO.md`.
- Drive UK, incluyendo `_Codex/UNDERSTANDING_KIDS_MAESTRO.md`.
- Carpeta local iCloud `Documents/Understanding Kids/`, con documentos operativos, pagos, campañas y contratos.

## Qué falló

### 1. Se usó `memory_search` como primera señal, pero no encontró nada

`memory_search` devolvió cero resultados para consultas sobre UK/plan/proyecto. Esto sugiere que el índice semántico disponible para Geoffrey no cubre adecuadamente el Great Vault completo o no indexa esas páginas de UK de forma útil.

Conclusión: `memory_search` no puede ser la única recuperación para proyectos del Vault.

### 2. Geoffrey leyó páginas correctas, pero demasiado generales

Se consultaron páginas de UK como:

- [[understanding-kids]]
- [[understanding-kids/mapa-operativo]]
- [[understanding-kids/pendientes-operativos-2026-05-15]]

Pero no se priorizó buscar el término “proyecto contigo” en:

- `wiki/log/2026-05.md`
- `wiki/decisiones/2026-05.md`
- `wiki/agentes/geoffrey/conversaciones/`
- subcarpeta `wiki/proyectos/activos/understanding-kids/`

Ahí estaba la pista directa del plan de nutrición completa.

### 3. El índice maestro no exponía el plan como subproyecto visible

[[vault-map]] lista `understanding-kids`, `uk-catalogo`, `diplomado-autismo-2026` e `integracion-sensorial`, pero no listaba explícitamente `understanding-kids/plan-nutricion-completa` como iniciativa activa.

### 4. Se confundió “proyecto UK” con “estado operativo de UK”

El plan específico no era resolver checkout/finanzas/comercial inmediatamente, sino preparar la base de conocimiento de UK para un futuro `README-AI.md`/agente.

## Métodos existentes dentro del Vault que debían evitar el fallo

Ya existían métodos suficientes, pero no se aplicaron en el orden correcto:

1. [[_AI_BOOTSTRAP]]: indica cargar `index`, `dashboard`, páginas específicas, decisiones y log.
2. [[geoffrey/AGENT]]: instruye usar grep/rg como búsqueda primaria y recuperar desde conversaciones/checkpoints/decisiones/log si falta contexto.
3. [[vault-map]]: índice rápido de navegación.
4. [[geoffrey/memoria]]: regla duradera de no preguntar ni responder sin auditar fuentes disponibles.
5. [[escribir-memoria]] y [[geoffrey/memory-writing-best-practices]]: memoria debe apuntar a fuentes canónicas, no copiar estados vivos.
6. [[decisiones/2026-05]]: contiene decisiones destiladas de UK.
7. `wiki/log/2026-05.md`: contiene historial operativo exacto de UK.
8. `wiki/agentes/geoffrey/conversaciones/YYYY-MM-DD.md`: contiene continuidad diaria.

## Causa raíz

La causa raíz fue una **ruta de recuperación incompleta**:

- Se trató `memory_search` como suficiente.
- Al fallar, se saltó a páginas canónicas generales.
- No se ejecutó inmediatamente el barrido obligatorio de proyecto: `log + decisiones + conversaciones + subcarpeta del proyecto + fuentes locales/Drive`.

## Corrección operativa recomendada

Agregar protocolo duradero para consultas de proyectos:

> Cuando JR pregunte por “un proyecto que estábamos haciendo”, Geoffrey debe buscar primero en: `vault-map`, página canónica del proyecto, subcarpeta del proyecto, `wiki/log/YYYY-MM.md`, `wiki/decisiones/YYYY-MM.md`, conversaciones recientes y fuentes externas autorizadas asociadas. No responder desde memoria ni desde la página general si hay subproyectos activos.

## Correcciones aplicadas

- Actualizar [[geoffrey/AGENT]] con protocolo de recuperación de proyectos.
- Registrar candidato de memoria en [[geoffrey/memoria-sugerida]] para que JR pueda promoverlo a memoria permanente.
- Actualizar [[vault-map]] para exponer el plan de nutrición completa de UK como subiniciativa navegable.
- Registrar esta auditoría y los cambios en `wiki/log/2026-05.md`.

## Relacionado

- [[understanding-kids/plan-nutricion-completa]]
- [[understanding-kids]]
- [[geoffrey/AGENT]]
- [[geoffrey/memoria]]
- [[escribir-memoria]]
- [[vault-map]]
