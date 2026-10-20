---
type: index
date: 2026-10-19
last-touched: 2026-10-19
tags:
  - index
  - tema/infraestructura
  - tema/automatizacion
  - proyecto/understanding-kids
---

# Mapa de archivos (lo que vive fuera del Vault)

El Vault guarda el conocimiento; las imágenes, fuentes, artes, scripts y el estado de los agentes viven afuera. Esta página dice **dónde está cada cosa, qué tiene, quién la usa, cada cuánto cambia y si tiene respaldo**. Nació de [[vault-cerebro]] (fase F3).

> Inventario hecho el **2026-10-19** en la Mac Mini `jr`, sin recorrer árboles completos (iCloud se cuelga): los conteos son de primer nivel. «Respaldo» significa copia independiente; iCloud y Drive son **sincronización**, no respaldo. No hay Time Machine configurado (`tmutil`: sin destinos). Secretos: aquí solo la **ruta**, nunca el valor; ver `_sensitive.md`.

## Understanding Kids — `~/Documents/Understanding Kids/`

Symlink a `~/Library/Mobile Documents/com~apple~CloudDocs/Documents/Understanding Kids` (iCloud, «Mantener descargado»). Es el **taller**: carpeta de trabajo de la clínica. Respaldo: solo iCloud (sin copia independiente), salvo lo indicado.

| Carpeta / archivo | Qué contiene | Quién lo usa | Cambia | Últ. mod. |
|---|---|---|---|---|
| `Artes/` | Sistema de artes de redes (detalle abajo) | Tareas de artes, cierre, cambios, JR | A diario | 2026-10-19 |
| `Fonts/` | 11 entradas: familia Cocogoose Classic (7 .otf), carpeta `Cocogoose Pro/`, `Cocogoose.ttf`, `cocogoose.otf`. Fuente original de la Cocogoose que el motor lleva embebida en base64 | Referencia (el motor usa su copia en `Sistema/`) | Casi nunca | 2025-07-29 |
| `$CAMPAIGN/` | `Artes Finales/`, `Borradores/` (carpeta con nombre de variable sin reemplazar) | (sin verificar) | Sin uso aparente | 2026-04-20 |
| `Asambleas/` | Actas notariales, anuales, nombramientos (5) | JR (legal/societario) | Rara vez | 2025-10-17 |
| `Blog/` | `2022/`, `2023/` | Histórico | No | 2026-04-07 |
| `CFO_Model/` | Generador y verificador del modelo financiero (`.mjs`, `node_modules`) | Claude/JR | Ocasional | 2026-08-28 |
| `Campañas/` | `Diplomado Internacional de Autismo 2026/` (AUT26, la maneja JR aparte) | JR | Ocasional | 2026-07-25 |
| `Contratos/` | Contratos de trabajo, servicios profesionales, formatos, generadores `.py` (7) | JR | Ocasional | 2026-08-13 |
| `Documentos S.A./` | Documentos de la sociedad y formularios 2026 | JR | Rara vez | 2026-09-30 |
| `Eventos/` | Evento IS Avanzada 2025, presupuestos | JR | Rara vez | 2026-02-17 |
| `Laboral/` | Cálculo de prestaciones (xlsx) | JR | Rara vez | 2026-04-25 |
| `Metaverse/` | Un KYC (docx) | Histórico | No | 2025-07-29 |
| `Pagos/` | `2024/`, `2025/`, `2026/` | JR / Geoffrey (sin verificar) | Mensual | 2026-10-19 |
| `Página Web/` | Imágenes y misión/visión/valores | Histórico web | Rara vez | 2025-07-29 |
| `Terapeutas/` | Una carpeta por terapeuta (1) | JR | Rara vez | 2025-08-19 |
| `canva-imports/` | Prueba de carrusel «pedir ayuda» (html, pptx, py, png) | Histórico (antes del sistema de artes) | No | 2026-07-06 |
| `docs/`, `.superpowers/` | Notas de brainstorming de un plugin | Claude | No | 2026-08-28 / 2026-07-21 |
| `google-apps-script/` | Script de exportación de hojas de finanzas + README | JR | Rara vez | 2026-04-08 |
| `output/`, `outputs/` | Previews de Canva, imagegen, pdf; salida del modelo CFO | Claude | Ocasional | 2026-07-13 / 2026-08-28 |
| `scripts/`, `vendor/` | Lanzador y paquete de nano-banana MCP (sin cuota, en desuso) | — | No | 2026-04-19 |
| `.secrets/` | **Secreto:** `gemini_api_key` | nano-banana (en desuso) | No | 2026-04-10 |
| Sueltos | 5 xlsx (precios, prestaciones, flujo de caja, compra de carro, proyección 2025), `UNDERSTANDING_KIDS_MAESTRO.md`, un PDF de viaje, un respaldo `.wpress` de la web de 2024 (~4.3 GB) | JR | Rara vez | — |
| `Administración`, `Administración 3` | Symlinks a `/Users/jotaerre/...` (Mac anterior). **Rotos en esta Mac**; nadie del sistema los usa | — | — | 2026-10-19 |

### `Artes/` (taller del sistema de artes)

| Carpeta | Qué contiene | Quién la usa | Cambia | Últ. mod. |
|---|---|---|---|---|
| `Sistema/` | Motor: 14 `build_*.py` (plantillas), 65 `armar_*.py` (copy de cada corrida o pieza; incluye `armar_correccion_*`), 10 `correccion*.py`, 2 `verificar_*.py`, utilidades (`buscar_foto`, `hacer_sticker`, `reglas_contenido`, `doodles`, `ilustraciones`, `serie_antes_hoy`…), 4 guías `.md`, fuentes (`.otf`, `.ttf`, base64 `.txt`, `fonts_eda26/`), logos (`.png` + base64 + stickers), renders HTML de caché (`_render*.html`, `_cache_spots/`), PNG de muestra, `tendencias/` (estado del agente de tendencias), `scheduled-tasks-backup/`, `pexels_key.txt`. ~29 MB | Corrida semanal, cambios, cierre (verificadores), correcciones por Telegram | Cada corrida (nuevo `armar_*`) | 2026-10-19 |
| `Pendientes de Revision/` | Cola de revisión: 22 carpetas de pieza (`<fecha> - <UK|IS> <tema>`, 4 con «(v2)») + 1 muestra | Corrida semanal y de cambios escriben; cierre mueve a Aprobadas | Varias veces por semana | 2026-10-19 |
| `Aprobadas/` | Histórico local de piezas cerradas: 68 entradas | El cierre mueve aquí | Cada cierre | 2026-10-19 |
| `_Descartadas/` | 15 piezas que no siguieron (v1 reemplazadas, publicidades descartadas) | Manual | Rara vez | 2026-10-16 |
| `Fotos/` | 120 entradas (102 `.jpg` + carpetas por pieza). Fotos permanentes de los artes (regla del 17-ago) | `armar_*.py` las referencian | Cada corrida | 2026-10-18 |
| `Fotos expositoras/` | 2 retratos (Davinia, Mónica) | Campañas (EDA26) | No | 2026-08-10 |
| `Logos/` | 4 originales: UK, IS, Davinia (original y recortado) | Fuente de los logos del motor | No | 2026-08-10 |

Guías de `Sistema/` con copia en el Vault: [[guia-maestra-estilo]], [[guia-promos-talleres]], [[tendencias-referentes]]. Plantillas: [[plantillas-artes]]. Flujo: [[sistema-artes-redes]].

## Claude — `~/Claude/` (local, sin iCloud)

| Ruta | Qué contiene | Quién la usa | Cambia | Respaldo |
|---|---|---|---|---|
| `~/Claude/CLAUDE.md` | Instrucciones para correcciones por Telegram y rol de coordinador | Sesiones de Claude con cwd `~/Claude` (puente de Telegram, `claude -p` del cierre y cambios) | Ocasional | F0 (`respaldos/2026-10-vault-cerebro/`) |
| `~/Claude/bin/` | 22 entradas: `avisar-jr.sh`, puente de Telegram (`telegram-bridge.sh`, `telegram-pty.py`, `telegram-destrabar.sh`, `telegram_estado.py`), artes (`uk-cierre-watch.sh`, `uk-cierre-prompt.md`, `uk-cambios-watch.sh`, `uk-cambios-prompt.md`, `uk-notion.py`, `uk-resumen-magoo.py`), voz (`nota-de-voz.sh`, `transcribir-vn.sh`), recordatorios (token, update), `.bak` | LaunchAgents y tareas | Semanal | F0 |
| `~/Claude/state/` | `resumen-magoo.json` (qué ya se le avisó a Magoo), `tras-reinicio.md` (pasos tras reiniciar) | `uk-resumen-magoo.py`, puente | A diario | No |
| `~/Claude/notion-backups/` | 10 archivos (~6 MB): JSON del Calendario y Tendencias antes de la migración de estados del 16-oct, `.bak` de cierre | Respaldo manual | Puntual | Es respaldo |
| `~/Claude/pendiente-vault/` | Casa nueva (`casa-nueva-canada-de-elgin.md`), guía de electrodomésticos v1–v8 + validación, interiores/sala (planos PNG + prompt), 7 fotos de la casa (~2 MB). **Integrado al Vault el 2026-10-19 (F5)**: ver «Casa nueva» abajo y `LEEME.md` en la carpeta. No se borró nada | Agentes compras/interiores (siguen escribiendo aquí) | Ocasional | No |
| `~/Claude/respaldos/` | `2026-10-vault-cerebro/` (700): 6 tar.gz de F0 + copia previa de `_sensitive.md` | Rollback de [[vault-cerebro]] | Puntual | Es respaldo |
| `~/Claude/.claude/` | `settings.json`, `settings.local.json` (permisos del proyecto), `agents/` (definiciones de los subagentes `compras`, `interiores`, `pendientes-magoo`: [[agentes/claude/subagentes]]) | Claude Code en `~/Claude` | Ocasional | No |
| `~/.config/gws`, `~/.config/gws-joserca` | Configuración y tokens OAuth de `gws` (Gmail): jcastaneda@ por defecto, joserca95@ con `GOOGLE_WORKSPACE_CLI_CONFIG_DIR` ([[agentes/claude/correo]]). **Contienen tokens** | Claude, `uk-resumen-magoo.py`, `pendientes-magoo` | Rara vez | No |
| `~/.local/bin/timeout` | `timeout` propio para macOS (devuelve 124; `-k`/`-s`) | Toda lectura de iCloud o Drive | No | No |
| `~/Claude/.secrets/` | **Secreto:** `notion.env` (token de la integración de Notion) | `uk-cierre-watch.sh`, `uk-notion.py`, `uk-resumen-magoo.py` | Rara vez | No |
| `~/Claude/_eliminado-20260826/` | Tarea de prueba retirada | — | No | — |

## Casa nueva — `~/Claude/pendiente-vault/` (local, sin iCloud)

Conocimiento en el Vault: [[casa-canada-de-elgin]], [[casa-canada-de-elgin/electrodomesticos]], [[casa-canada-de-elgin/sala-propuesta-v1]]. Aquí quedan los binarios y el historial (añadido 2026-10-19, F5).

| Ruta | Qué es | Quién lo usa |
|---|---|---|
| `fotos-casa-nueva/sala-01.jpg` … `sala-04.jpg` | 4 fotos de la sala vacía (sala-01 desde los arcos hacia la chimenea; es la que usa el prompt de la sala) | Agente interiores, JR |
| `fotos-casa-nueva/comedor-01.jpg` … `comedor-03.jpg` | 3 fotos del comedor vacío | Agente interiores, JR |
| `interiores/sala/plano-sala-v1.png` | Plano a escala de la sala (interpretación A, confirmada por JR el 18-oct) | Agente interiores |
| `interiores/sala/plano-sala-v1-alt.png` | Variante del plano (por el nombre, la otra interpretación de las medidas; sin verificar) | Histórico |
| `interiores/sala/plano-sala-amueblado-v1.png` | Distribución de muebles sobre el plano (base del prompt) | Agente interiores |
| `interiores/sala/prompt-chatgpt-sala-v1.md` | Prompt original (copiado al Vault) | — |
| `compras/electrodomesticos/guia-electrodomesticos-v1.md` … `v7.md` | Versiones anteriores de la guía; la v7 tiene el detalle de investigación y fuentes | Historial |
| `compras/electrodomesticos/guia-electrodomesticos-v8.md` | Versión vigente (copiada al Vault) | — |
| `compras/electrodomesticos/validacion-resenas-v1.md` | Validación de modelos contra reseñas (acompaña a la v1) | Historial |
| `casa-nueva-canada-de-elgin.md` | Nota original de la casa (copiada al Vault, con la dirección exacta) | Agentes compras/interiores |

## Claude Code — `~/.claude/`

| Ruta | Qué contiene | Quién la usa | Cambia | Respaldo |
|---|---|---|---|---|
| `~/.claude/scheduled-tasks/` | `uk-artes-semanales/SKILL.md` (+ `.bak-20261018`), `uk-tendencias-virales/SKILL.md`. Instrucciones de las tareas programadas | App de Claude (horario en `~/Library/Application Support/Claude/claude-code-sessions/…/scheduled-tasks.json`) | Cuando cambia una regla | F0; copia vieja en `Sistema/scheduled-tasks-backup/` |
| `~/.claude/projects/-Users-jr-Claude/memory/` | 24 memorias `.md` (índice `MEMORY.md`): sistema de artes, copy, Telegram, correo, Drive, finanzas, Propi, rol de coordinador, Vault | Claude en cada sesión | Semanal | F0 |
| `~/.claude/skills/` | `binance-view`, `ibkr-view`, `gws-sheets` | Claude | Rara vez | No |
| `~/.claude/channels/telegram/` | `.env` (**secreto:** token del bot), `access.json`, bandeja, FIFO del puente | Puente de Telegram, `avisar-jr.sh` | Constante | No |
| `~/.claude/secrets/` | **Secretos:** `claude-oauth-token` (token largo, vence ~16-oct-2027), `binance.env`, cachés de Binance | Puente, `uk-cambios-watch.sh`, skill binance | Rara vez | No |
| `~/.claude.json` | Configuración MCP, incluido el **token de Apify** (en la cabecera del servidor) | Agente de tendencias | Rara vez | No |

## LaunchAgents — `~/Library/LaunchAgents/com.jr.*`

| Label | Script | Horario | Para qué |
|---|---|---|---|
| `com.jr.claude-telegram` | `~/Claude/bin/telegram-bridge.sh` | Siempre (KeepAlive) | Puente de Telegram |
| `com.jr.claude-telegram-destrabar` | `telegram-destrabar.sh` | Cada 60 s | Destraba el puente (ESC o reinicio con `.resume`) |
| `com.jr.uk-cierre` | `uk-cierre-watch.sh` | Cada 15 min + al cargar | Cierre de piezas «Aprobado» → Drive |
| `com.jr.uk-cambios` | `uk-cambios-watch.sh` | Lun, mié, vie 20:00 | v2 de piezas en «Cambios pedidos» |
| `com.jr.uk-resumen-magoo` | `uk-resumen-magoo.py` | Diario 6:00 | Correo único a Magoo |
| `com.jr.recordatorio-token` | `recordatorio-token.sh` | Diario 10:00 (avisa desde 25-sep-2027) | Renovar token del puente |
| `com.jr.recordatorio-update` | `recordatorio-update.sh` | Día 1 de cada mes 10:00 | Actualizar Claude Code a mano |

Logs en `~/Library/Logs/` (`uk-cierre.log`, `uk-cambios.log`, `uk-resumen-magoo.log`, `claude-telegram*.log`, `*.err.log`). Respaldo de los `.plist`: no (uno en `~/Claude/bin/*.plist.bak-20261018`). Otros agentes en la carpeta (no son de JR/Claude): Syncthing (`homebrew.mxcl.syncthing`), OpenClaw (`ai.openclaw.gateway`), Google.

## Google Drive — vitrina de artes

- **Montaje:** `~/Library/CloudStorage/GoogleDrive-jcastaneda@kidsunderstanding.com/My Drive/Administración (1)/Artes/2026/` (cuenta de la clínica; la carpeta compartida se llama « Administración zona 14 »). Raíz «My Drive», nunca «Mi unidad». No listar la raíz del montaje.
- **Estructura:** `<Marca>/<Tipo>/<carpeta de pieza>/`. Marcas: `Understanding Kids`, `Integración Sensorial`, `Campañas`, `Publicidad`. Tipos: Informativo, Servicios, Promociones, Recursos, Frases, Testimonios (y las que cree el cierre según `Categoría`). Magoo renombra a «subido» al publicar.
- **IDs:** Administración `1ZJ0IzlXr-_NAR4Cj34va9mB9WZBLEI79` · Artes `19OTddA7oieII4MJWxy50nL-WPrdkv4pd` · 2026 `1LT2idGH0gfX6399nHqrBJ8cbzhs7P6cQ` · Campañas `1mc3fbHku7fsJ3T07wmdVX9yHdxYspnae` · Campañas/Especialización Alimentación 2026 `1V2sxc07Tpr4Z6Aq8ZqH8sGhx9NwmF8oF` · UK/Informativo `1-PQcQOU5lJ6pjSGmiZO4Lc-iMdfF-3Yf` · UK/Servicios `1x1Mr3VTimGArQ84xw-utQkgvQO3XmAaW` · IS/Informativo `15ZwOdml94a8M4b24rOVL46wsC-NCQtRW` · IS/Servicios `1OZ4nnuySbXL6drh18GFE5WZ9ecKap94d`.
- **Quién:** el cierre escribe (por el montaje); el MCP de Drive (cuenta personal) sirve para leer y sacar enlaces, no para reemplazar. Magoo descarga y publica.
- **Respaldo:** Drive (historial de versiones de Google). No se hace copia aparte (D2).
- **No verificado hoy** (regla: no tocar Drive en esta fase).

## Notion

| Base | ID | Quién escribe | Quién lee |
|---|---|---|---|
| 🗓️ Calendario de Artes | `collection://175780c0-4762-81ec-a2a0-000bf5fe9eac` (base `175780c0476280a4ae7bd46fec8ef50b`) | Magoo (briefs), corrida semanal, cambios, cierre, JR | Todos los procesos de artes |
| 🔥 Tendencias | `collection://c8b3310c-b24a-49f9-8a3f-3dd4c60c5359` | Agente de tendencias («Sugerida»), JR/Magoo («Aprobada»), corrida semanal («Hecha») | Corrida semanal |

Respaldo: los JSON puntuales de `~/Claude/notion-backups/` (16-oct-2026); no hay copia periódica.

## Secretos (solo ubicación)

| Secreto | Dónde |
|---|---|
| Llave de Pexels | `~/Documents/Understanding Kids/Artes/Sistema/pexels_key.txt` + `_sensitive.md` (no se rota, decisión de JR 19-oct-2026) |
| Token de Notion | `~/Claude/.secrets/notion.env` |
| Token del bot de Telegram | `~/.claude/channels/telegram/.env` |
| Token largo de Claude | `~/.claude/secrets/claude-oauth-token` |
| Binance (solo lectura) | `~/.claude/secrets/binance.env` |
| IBKR (solo lectura) | la memoria `skills_finanzas_solo_lectura` dice `~/.claude/secrets/ibkr.env`, pero **hoy no existe** ese archivo (la skill `ibkr-view` no tendría credenciales; sin verificar si se guardaron en otro lado) |
| Apify | `~/.claude.json` (configuración MCP) |
| Gemini (nano-banana, en desuso) | `~/Documents/Understanding Kids/.secrets/gemini_api_key` (en iCloud) |

## Relacionado

- [[vault-cerebro]] · [[sistema-artes-redes]] · [[plantillas-artes]] · [[guia-maestra-estilo]]
- [[vault-map|Vault Map]] · [[understanding-kids]] · [[_AI_BOOTSTRAP]]
- [[agentes/claude/AGENT|Claude]] · [[casa-canada-de-elgin]] · [[great-vault]]
