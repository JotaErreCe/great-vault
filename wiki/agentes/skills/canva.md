---
type: reference
date: 2026-05-07
tags: [skill, agente, canva, auditoria]
estado: auditada
---

# canva

## Resumen

Auditoría de skills ClawHub para conectar Canva al flujo de Geoffrey, especialmente para crear o subir presentaciones derivadas de análisis de gastos por SMS.

## Candidatos revisados

| Skill | Estado ClawHub | Riesgo | Observación |
|---|---:|---|---|
| `canva` | CLEAN | medio | Usa Canva Connect API directo con `CANVA_CLIENT_ID`, `CANVA_CLIENT_SECRET` y tokens locales en `~/.canva/tokens.json`. Puede listar/exportar diseños, subir assets y autofill de brand templates. No parece crear slides libres con contenido arbitrario salvo mediante templates. |
| `canva-designs` | CLEAN | medio/alto | Usa ClawLink como broker externo de credenciales e integraciones. Evita pedir API keys locales y promete herramientas dinámicas de Canva, incluyendo importar assets/archivos como diseños. Depende de plugin ClawLink y servicio externo `claw-link.dev`. |
| `canva-automation` | CLEAN | medio/alto | Usa Rube MCP / Composio. Requiere conexión activa de Canva en Rube. Buen catálogo de operaciones, pero agrega otro broker externo. |
| `canva-connect` | SUSPICIOUS | alto | Marcada suspicious por ClawHub; descartar por ahora. |
| `canva-2` | SUSPICIOUS | alto | MCP con muchas herramientas y archivo `app.py` grande; aunque parece potente para leer/editar diseños, está marcada suspicious. Descartar por ahora. |
| `canva-integration` | SUSPICIOUS | alto | Usa Membrane y está marcada suspicious. Descartar por ahora. |
| `canva-skill` | SUSPICIOUS | alto | Similar a `canva`, pero marcada suspicious. Descartar por ahora. |

## Capacidades relevantes

### `canva`

- Lee: diseños, detalles, brand templates, assets permitidos por OAuth.
- Escribe/modifica: crea diseños por autofill de brand templates, sube assets, exporta diseños.
- Envía/publica: no publica por sí misma, pero crea/modifica contenido en Canva.
- Credenciales: requiere Canva developer integration y tokens locales.
- Red: Canva Connect API.

### `canva-designs`

- Lee/escribe según herramientas dinámicas de ClawLink.
- Puede importar assets/archivos externos como diseños, dependiendo del catálogo real de ClawLink.
- Credenciales: gestionadas por ClawLink, no por Geoffrey.
- Riesgo principal: tercero externo con acceso OAuth a Canva.

## Riesgos

- Privacidad: los análisis de gastos podrían terminar en Canva/ClawLink si se suben presentaciones con datos financieros.
- Externo: cualquier creación/importación en Canva modifica una cuenta externa.
- Credenciales: `canva` guarda tokens locales; `canva-designs` delega credenciales a ClawLink.
- Operativo: Canva Connect API puede no permitir crear una presentación completa desde cero sin templates o sin importar un archivo ya armado.

## Hallazgo adicional: Canva oficial ya instalado

2026-05-07: se verificó que existe Canva CLI oficial instalado:

- Binario: `/opt/homebrew/bin/canva`
- Versión: `2.0.1`
- Gemini extension instalada: `~/.gemini/extensions/canva`
- MCP oficial configurado: `https://mcp.canva.com/mcp` con OAuth habilitado.

Al probar Gemini CLI, pidió autenticar el MCP `Canva`, lo que sugiere que la extensión existe pero falta completar/confirmar OAuth para usarla.

## Recomendación

Para el caso de uso de Master JR — analizar SMS bancarios y crear una PPT en Canva — la ruta más segura y controlable es:

1. Geoffrey lee SMS localmente con [[imsg]].
2. Geoffrey genera análisis agregado local, sin guardar mensajes crudos.
3. Geoffrey crea una presentación `.pptx` local con `pptxgenjs` o similar.
4. Usar primero Canva oficial CLI/MCP para importar o transformar la presentación en Canva, previa autenticación OAuth y aprobación.
5. Si el MCP oficial no cubre la operación necesaria, segunda opción: `canva-designs` vía ClawLink, solo si Master JR acepta ese broker externo.

Entre las dos candidatas ClawHub previamente comparadas, `canva-designs` encaja mejor que `canva` para mover/importar presentaciones o assets; `canva` directo es más auditable, pero más limitado y requiere app propia de Canva Developers.

No recomiendo empezar con `canva-2`, `canva-connect`, `canva-integration` ni `canva-skill` por flags suspicious.

## Decisión

Estado: auditada.
Fecha: 2026-05-07.
Auditó: Geoffrey.
Recomendación: priorizar Canva oficial CLI/MCP ya instalado; entre skills ClawHub, preferir `canva-designs` solo si el MCP oficial no basta y Master JR acepta ClawLink.

## Relacionado

- [[agentes/skills/index]] · [[agentes/geoffrey/skills-permitidas|Skills permitidas — Geoffrey]] · [[imsg]]
