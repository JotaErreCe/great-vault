---
name: apify-mcp-setup
description: "Apify debe ir como MCP local con token Bearer, no como conector de claude.ai (se cae en corridas programadas)"
metadata: 
  node_type: memory
  type: project
  originSessionId: 58edb4fd-be78-44f4-a6a7-1b9069b75d4c
  modified: 2026-08-14T17:41:33.079Z
---

Apify se caía intermitentemente en las corridas programadas del agente `uk-tendencias-virales` (10-ago y 13-ago de 2026 sin datos). Diagnóstico del 2026-08-13: **Apify no estaba en ninguna config local** — no aparecía en `claude mcp list`, ni en `~/.claude.json` (`mcpServers`), ni en `.mcp.json`. Llegaba por la capa de conectores de la cuenta claude.ai, que se resuelve por sesión y depende de que el login/OAuth esté vigente. Una corrida programada no puede hacer el flujo de OAuth, así que a veces arranca sin la herramienta.

Evidencia del patrón: los servidores locales con token o stdio (`nanobanana`, `opennutrition`) reportan Connected; los HTTP con OAuth (`supabase`, `canva`) reportan "Needs authentication". Los docs lo confirman: los conectores de claude.ai requieren el login de claude.ai, mientras que "MCP servers you configure locally still work".

**Configuración correcta** (scope user, sobrevive a corridas programadas, sin browser):

```
claude mcp add --scope user --transport http apify \
  "https://mcp.apify.com?tools=apify/instagram-post-scraper,apify/facebook-posts-scraper,apify/instagram-hashtag-scraper,storage" \
  --header "Authorization: Bearer <APIFY_TOKEN>"
```

El token sale de console.apify.com/settings/integrations. El parámetro `?tools=` fija exactamente los actores que usa el skill (más la categoría `storage` para `get-dataset-items`), así el set de herramientas es determinista y no arrastra el catálogo entero.

Permisos en `~/.claude/settings.json` para que no pregunte en cada corrida: `permissions.allow` incluye `mcp__apify` y `mcp__Apify` (la segunda cubre el nombre viejo del conector). Sintaxis verificada en los docs: `mcp__<servidor>` autoriza todas las herramientas de ese servidor. **Corrección 2026-08-14:** esta nota daba los permisos por puestos, pero en la Mac Mini `permissions.allow` estaba **vacío** — la migración no los trajo. Ya quedaron agregados. Si se vuelve a migrar, verificar en vez de asumir.

Al migrar, **desconectar el Apify de claude.ai** para no tener dos servidores con el mismo set de tools.

## Estado verificado 2026-08-14

Instalado y funcionando en la Mac Mini `jr` (scope user, en `~/.claude.json`). `claude mcp list` → `apify: ... ✓ Connected`. Handshake MCP real contra `https://mcp.apify.com`: **AUTH OK**, servidor `apify-mcp-server 0.14.3`, **13 herramientas** expuestas. El `?tools=` funcionó: están las tres que usa el skill (`apify--instagram-post-scraper`, `apify--facebook-posts-scraper`, `apify--instagram-hashtag-scraper`) más la familia `storage` con `get-dataset-items`. Ojo al **nombrado**: los actores llegan con doble guión (`apify--instagram-post-scraper`), no con slash.

**Dos intentos fallaron antes de este** y conviene recordarlo: (1) se corrió el comando con el placeholder literal `PEGA_TU_TOKEN_AQUI` → 401; (2) el token se pegó truncado, 23 caracteres en vez de 46 → 401. **Un token válido mide 46 caracteres**: `apify_api_` + 36. Si `claude mcp list` dice `Failed to connect`, medir la longitud del token antes que cualquier otra cosa — es lo que falló las dos veces. Diagnóstico rápido sin MCP: `curl https://api.apify.com/v2/users/me -H "Authorization: Bearer <token>"`.

**Presupuesto (decisión de JR, 2026-08-14):** la cuenta `JotaErreCeA` está en plan **FREE con tope duro de $5 USD/mes**. JR fijó el objetivo en **~$4/mes** dejando $1 de colchón — es fase de prueba: *"una vez yo vea que sí me sirve para crear buenos artes según tendencia planea pagar más"*. Con ~9 corridas al mes eso da **~$0.45 por corrida**. El SKILL.md ya lleva la regla escalonada: >$1.50 disponible → corrida normal; $0.50–$1.50 → solo referentes, sin hashtags; <$0.50 → no raspar y reportar en el runlog. Referencia medida: barrido completo (9 cuentas + 5 hashtags, 140 resultados) = **$0.36**, así que cabe holgado. Consultar con `GET https://api.apify.com/v2/users/me/limits`.

**Permisos / corridas desatendidas (JR, 2026-08-14):** esta Mac Mini se usa **solo para tareas automáticas** y JR no está presente para aprobar nada. Las dos tareas afectadas son `uk-tendencias-virales` (lun/jue 7am) y `uk-artes-semanales` (dom 6pm).

Costó tres intentos entender el mecanismo. **Lo que hay que saber (Claude Code 2.1.148):**

1. **`permissions.defaultMode: "bypassPermissions"` NO alcanza por sí solo.** El modo está cerrado tras un diálogo de aceptación, y sin haberlo aceptado no se activa. El flag que lo destraba es **`skipDangerousModePermissionPrompt: true`** (descripción oficial en el esquema: *"Whether the user has accepted the bypass permissions mode dialog"*). Van juntos, en `~/.claude/settings.json`, al nivel raíz — `skipDangerousModePermissionPrompt` NO va dentro de `permissions`.
2. **Los cambios de settings se leen al INICIO de sesión.** Una sesión ya abierta sigue pidiendo permisos aunque el archivo ya esté bien. Esto confundió el diagnóstico dos veces: parecía que la config no servía, y en realidad solo hacía falta una sesión nueva. **Nunca evaluar un cambio de permisos dentro de la sesión donde se hizo.**
3. **Las aprobaciones se guardan POR TAREA.** Los permisos que se aprueban durante una corrida quedan almacenados en esa tarea programada y se reaplican en las siguientes. Consecuencia práctica: **una tarea nueva conviene correrla una vez con "Run now" estando presente**, para pre-aprobar sus herramientas; después ya corre sola. Esto es independiente del modo de permisos.
4. **Un hook `PreToolUse` que devuelva `permissionDecision: "allow"` NO sirve para esto** — hay un bug conocido ([claude-code#52822](https://github.com/anthropics/claude-code/issues/52822)) por el que no suprime el prompt nativo. No perder tiempo por ahí.
5. Como respaldo hay reglas generales por herramienta (`Bash`, `Read`, `Write`, `Edit`, `WebSearch`, `mcp__apify`, …) en `permissions.allow` de ambos archivos de settings. Si el modo bypass fallara, la lista cubre lo que usan las tareas.

**Ojo con el CLI:** `claude -p` en esta máquina falla con *"OAuth access token has expired"*. No afecta a las tareas programadas (corren por otra vía), pero **no se puede usar `claude -p` para probar permisos** — hay que probar con una tarea programada de verdad.

Ver también [[uk_template_system]] y el runlog en `~/Documents/Understanding Kids/Artes/Sistema/tendencias/runlog.md`.
