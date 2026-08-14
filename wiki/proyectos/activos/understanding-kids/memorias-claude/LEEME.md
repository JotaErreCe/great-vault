---
tipo: handoff
proyecto: understanding-kids
creado: 2026-08-14
---

# Memorias de Claude para las automatizaciones de artes

Copia de las memorias que necesitan las dos tareas programadas de UK/IS, puesta
en el Vault para que llegue por Syncthing a la otra Mac sin adjuntos ni copias
manuales.

**Origen:** `~/.claude/projects/-Users-jotaerre-Claude/memory/` en la Mac Pro
(usuario `jotaerre`), al 14 de agosto de 2026.

## Qué hay aquí

| archivo | para qué | ¿bloqueante? |
|---|---|---|
| `uk_template_system.md` | El grueso: plantillas, paletas por marca, reglas de campaña, guardarraíles, historial de decisiones de JR | **Sí** |
| `uk_copy_style.md` | Reglas de copy: tono humano, máx. 5 hashtags, tuteo | **Sí** |
| `apple_mail_access.md` | Envío por osascript + la excepción del correo a Magoo, que va sin preguntar | **Sí** |
| `project_understanding_kids.md` | Qué es UK, dónde vive todo | **Sí** |
| `feedback_style.md` | Cómo le gusta a JR que se trabaje | No, pero ayuda |
| `apify_mcp_setup.md` | Lo necesita el agente de tendencias (lunes y jueves) | Solo para tendencias |

## Cómo instalarlas en la otra máquina

Van a `~/.claude/projects/-Users-<usuario>-Claude/memory/`, donde `<usuario>` es
el de ESA máquina. El nombre de la carpeta sale del directorio de trabajo, así
que **no se copia tal cual desde la Mac Pro**: ahí es `-Users-jotaerre-Claude`.

**No sobrescribas el `MEMORY.md` que ya exista.** Es el índice que se carga en
cada sesión, y si esa máquina ya tiene memorias propias, reemplazarlo las deja
huérfanas. Hay que AGREGARLE estas seis líneas, no cambiarlo:

```
- [UK Template System](uk_template_system.md) — Sistema de artes IG/FB: plantillas, paletas, campañas, guardarraíles
- [UK Copy Style](uk_copy_style.md) — Reglas de copy de UK: tono humano, hashtags, tuteo
- [Apple Mail Access](apple_mail_access.md) — osascript para leer/enviar; el correo a Magoo va sin preguntar
- [Understanding Kids](project_understanding_kids.md) — Qué es UK, dónde vive todo
- [Feedback Preferences](feedback_style.md) — Cómo le gusta a JR que se trabaje
- [Apify MCP Setup](apify_mcp_setup.md) — Token Bearer local; lo usa el agente de tendencias
```

## Aviso

`uk_template_system.md` creció mucho en la semana del 10 al 14 de agosto:
troquel de logos, paleta v2 de EDA26, regla de variedad de formatos, el filtro
`Visuals needed` que resultó no ser confiable y un bug del guardarraíl de marca.
Si alguna máquina arranca con una copia anterior, repite errores ya resueltos.
Esta carpeta es la referencia; ante duda, volver a copiar desde la Mac Pro.
