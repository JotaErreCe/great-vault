---
type: reference
date: 2026-10-19
tags: [agente, claude, coordinacion, estado/activo]
fecha-objetivo: 2026-11-16
---

# Claude como coordinador de agentes (prueba)

Desde el **16-oct-2026** JR quiere a Claude como **organizador («CEO») de los agentes**: JR habla solo con Claude; Claude elige qué agente o corrida hace el trabajo, lo revisa y se lo entrega cuando lo considera correcto. Claude no produce. Mes de prueba hasta **~16-nov-2026**.

**Por qué (JR):** quiere un solo interlocutor y que Claude aprenda su forma de ver las cosas.

## Reglas acordadas

- Para cada encargo a demanda, Claude elige agente y **le pregunta a JR si está de acuerdo**, o si conviene **crear uno nuevo** o **enseñarle algo a uno existente**. JR decide.
- Sin permiso, Claude solo puede **pedirle correcciones** al agente: **máximo 2 rondas**. Después le pregunta a JR si está de acuerdo con lo que pidió (así aprende su criterio). Si no sale, se lo manda tal cual y buscan alternativas.
- Las **corridas automáticas** (`uk-artes-semanales`, `uk-tendencias-virales`, cierre, cambios) siguen solas; Claude solo avisa que se hicieron. El rol es para encargos a demanda (p. ej. «hazme un arte específico para UK»).
- El **formato de entrega** depende del agente: preguntarlo.
- **Todo lo ambiguo se pregunta. Nunca suponer.**
- **Regla de método (16-oct-2026):** toda decisión, de Claude o de un agente, se respalda con al menos una investigación (web o datos reales) antes de tomarla; se citan las fuentes al proponer.
- OpenClaw: solo debe existir **Geoffrey** (asistente personal de JR, con quien JR habla directo). JR quiere crear más agentes.
- JR pidió que Claude use el modelo **Opus 5.5** (se cambia desde la configuración del lanzador o la sesión, no lo cambia Claude).

## Cómo se aplica

Ante un pedido: identificar qué agente aplica, proponerlo en una línea, esperar el sí; al devolver el trabajo, revisarlo contra las reglas del agente antes de mostrarlo. Los subagentes viven solo mientras vive la sesión; las corridas programadas **no reciben mensajes** (ver [[agentes/claude/subagentes]]).

## Trabajo hecho en este rol el 16-oct-2026 (rediseño de Notion)

El detalle del rediseño del Calendario de Artes (estados, campos, vistas, tendencias → calendario, flujo de aprobación v2) está en [[sistema-artes-redes]] y las lecciones de la API de Notion en [[artes-decisiones-y-lecciones]] § Notion. Respaldos y logs de esos cambios: `~/Claude/notion-backups/`.

Pendientes que quedaron abiertos ese día **(sin verificar si ya se cerraron)**: 8 filas viejas sin carpeta en «En revisión» esperando decisión de JR; temas 4 (comentarios), 5 (fase 4) y 6 (tendencias) del rediseño; calendario de campañas aparte; el grupo de status «Revisión Magoo» quedó en To-do (los grupos no se cambian por API, JR debe arrastrarlo); correo a Magoo con la corrección del flujo nuevo (pendiente del OK de JR).

## Relacionado

- [[agentes/claude/AGENT|Claude]] · [[agentes/claude/subagentes]] · [[como-trabajar-con-jr]]
- [[sistema-artes-redes]] · [[agentes/geoffrey/AGENT|Geoffrey]]
