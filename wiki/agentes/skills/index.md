---
type: reference
date: 2026-05-05
tags: [agente, skills, seguridad, reference]
---

# Catálogo común de skills

Este folder documenta las skills que pueden ser consideradas por los agentes del Vault. Es un catálogo auditado, no una carpeta de ejecución.

Las skills ejecutables siguen viviendo donde OpenClaw las descubre en el sistema. Este catálogo registra qué hace cada skill, qué riesgos tiene, dónde revisar su fuente y si JR aprobó su uso.

## Decisión de arquitectura

- **Runtime:** las skills viven donde OpenClaw ya las carga (`<workspace>/skills`, `<workspace>/.agents/skills`, `~/.agents/skills`, `~/.openclaw/skills`, bundled).
- **Vault:** este directorio mantiene solo el catálogo/auditoría y links de origen.
- **Canonicalidad:** una skill no se considera “aprendida” por un agente solo por estar instalada; debe estar auditada aquí y permitida en la whitelist del agente.
- **Fuentes preferidas:** GitHub del proyecto/autor y ClawHub cuando exista ficha pública.

## Regla de uso

Una skill solo puede ser usada por un agente si:

1. Tiene página propia en este catálogo con estado `auditada` o `aprobada`.
2. Está listada en el `skills-permitidas.md` del agente que quiere usarla.

Si falta cualquiera de las dos, la skill se considera no autorizada.

## Estado de auditoría

Usar estos estados:

- `pendiente` — identificada, no auditada.
- `auditada` — revisada técnicamente, sin aprobación de uso general.
- `aprobada` — Master JR aprobó su uso bajo condiciones específicas.
- `rechazada` — no usar.

## Plantilla para una skill

```markdown
---
type: reference
date: YYYY-MM-DD
tags: [skill, agente, reference]
estado: pendiente
---

# skill-name

## Resumen

Qué hace en una línea.

## Origen

- Ruta / paquete:
- Fuente:
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

Estado: pendiente/auditada/aprobada/rechazada.
Fecha:
Aprobó:

## Relacionado

- [[skills/index]] · [[arquitectura]]
```

## Skills auditadas / aprobadas

> Lista operativa para que los agentes sepan qué skills pueden estudiar o solicitar cuando una tarea lo amerite.

| Skill | Estado | GitHub | ClawHub | Notas |
|---|---|---|---|---|
| [[imsg]] | aprobada | https://github.com/openclaw/imsg | no identificado | Aprobada para Geoffrey con lectura local de SMS/iMessage; enviar mensajes prohibido sin aprobación explícita. |
| [[gmail]] | auditada | https://github.com/openclaw/gmail | no identificado | Auditada para lectura específica de correos (ej.: buscar correos de Thelma sobre contrato Altezza); envío, modificación o acceso a contactos requieren aprobación explícita de JR. |
| [[canva]] | auditada | varios candidatos | `canva`, `canva-designs`, etc. | Recomendación: `canva-designs` si JR acepta ClawLink; alternativa conservadora: `canva` directo con Canva Developers. |
| [[nano-banana-pro]] | auditada | varios candidatos | `nano-banana-pro`, `gemini-nano-banana`, etc. | Recomendación: diferir; si se aprueba, preferir `nano-banana-pro` sobre `nanobanana`. |
| [[google-workspace-mcp]] | aprobada limitada | `@presto-ai/google-workspace-mcp` | `google-workspace-mcp` | Aprobada para Geoffrey: Drive/Docs/Sheets read-only por defecto; escrituras, envíos, permisos y cambios externos solo con aprobación explícita por acción. |

## Candidatas prioritarias por auditar

| Skill / necesidad | Estado | GitHub | ClawHub | Motivo |
|---|---|---|---|---|
| Gmail / correo Google multi-cuenta | pendiente | pendiente | pendiente | Alto valor, alto riesgo externo/privacidad. |
| Apple Reminders | pendiente | pendiente | pendiente | Captura y seguimiento de tareas. |
| Calendar | pendiente | pendiente | pendiente | Agenda y coordinación vía Apple/Google; Google Workspace MCP ya cubre lectura con política limitada. |
| WhatsApp | pendiente | pendiente | pendiente | Mensajería externa; requiere controles fuertes. |
| iMessage / SMS | aprobada limitada | https://github.com/openclaw/imsg | no identificado | Cubierta por [[imsg]] para lectura local; envío bloqueado salvo aprobación explícita. |
| Canva para PPT de gastos | auditada pendiente de aprobación | varios | `canva-designs` recomendado si se acepta ClawLink | Crear PPT local y subir/importar a Canva solo con aprobación. |
| Nano Banana para visuales | auditada pendiente de aprobación | varios | `nano-banana-pro` recomendado si se necesita | No indispensable para el prototipo inicial. |

## Relacionado

- [[arquitectura]] · [[geoffrey/skills-permitidas|skills permitidas — Geoffrey]] · [[_AI_BOOTSTRAP]]
