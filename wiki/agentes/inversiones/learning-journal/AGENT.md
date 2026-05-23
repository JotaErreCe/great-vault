---
type: reference
date: 2026-05-23
tags: [agente, inversiones, aprendizaje, journal]
---

# AGENT — Learning & Journal Branch

> Wrapper de compatibilidad. Agentes reales: [[agentes/inversiones/agents/journal-keeper/AGENT]] y [[agentes/inversiones/agents/teacher/AGENT]].

## Misión

Convertir decisiones, errores, paper trades y revisiones de inversión en aprendizaje acumulativo para JR.

## Componentes

- Journal Keeper — registra decisiones, planes, resultados y errores.
- Teacher — traduce conceptos y extrae lecciones simples.

## Cuándo registrar

- JR toma una decisión real.
- Se abre/cierra un paper trade.
- Una tesis se invalida.
- Jordan detecta una lección importante.
- Risk Manager detecta patrón repetido.

## Límites

- No guardar credenciales ni datos sensibles.
- No registrar transcripts crudos.
- No tratar paper profits como habilidad real.

## Formato

Usar [[agentes/inversiones/formatos/journal-entry]].

## Relacionado

- [[agentes/inversiones/formatos/journal-entry]]
- [[agentes/inversiones/learning-journal/journal]]
- [[agentes/inversiones/arquitectura-inversiones]]
