---
type: reference
date: 2026-05-05
tags: [agente, skills, seguridad, auditoria]
---

# README — catálogo común de skills

Este directorio documenta skills que pueden ser consideradas por agentes del Vault. Es un catálogo auditado, no una carpeta de ejecución.

Las skills ejecutables siguen viviendo donde OpenClaw las descubre. Este catálogo solo responde: qué skill es, de dónde viene, qué permisos/riesgos tiene, quién la auditó y qué agentes pueden pedir usarla.

## Regla central

Una skill solo puede ser usada por un agente si cumple ambas condiciones:

1. Tiene página propia en `wiki/agentes/skills/` con estado `auditada` o `aprobada`.
2. Está listada en el archivo `skills-permitidas.md` del agente.

Si falta cualquiera de las dos, la skill queda fuera aunque esté instalada en el sistema.

## Rutas ejecutables de OpenClaw

El runtime de OpenClaw carga skills desde sus rutas nativas, entre otras:

- `<workspace>/skills`
- `<workspace>/.agents/skills`
- `~/.agents/skills`
- `~/.openclaw/skills`
- skills bundled con OpenClaw

El Vault no reemplaza esas rutas; las audita y documenta.

## Schema de página por skill

Cada skill documentada debe tener una página propia, por ejemplo `gmail.md`, con:

```markdown
---
type: reference
date: YYYY-MM-DD
tags: [skill, agente, seguridad]
estado: pendiente
---

# Nombre de la skill

## Resumen

Qué hace en una línea.

## Origen

- Nombre:
- Ruta / paquete:
- GitHub:
- ClawHub:
- Versión observada:

## Capacidades

- Lee:
- Escribe/modifica:
- Envía/publica:
- Borra:
- Usa red:
- Usa credenciales:

## Riesgos

- Riesgos técnicos:
- Riesgos de privacidad:
- Riesgos externos:

## Condiciones de uso

- Permitido:
- Prohibido sin aprobación explícita:

## Decisión

- Estado: pendiente/auditada/aprobada/rechazada
- Fecha:
- Auditó:
- Aprobó:

## Relacionado

- [[skills/index]]
```

## Estados

- `pendiente` — identificada, no auditada.
- `auditada` — revisada técnicamente; todavía puede requerir whitelist por agente.
- `aprobada` — JR aprobó uso bajo condiciones específicas.
- `rechazada` — no usar.

## Relacionado

- [[skills/index|Catálogo común de skills]] · [[geoffrey/skills-permitidas|Skills permitidas — Geoffrey]] · [[arquitectura]]
