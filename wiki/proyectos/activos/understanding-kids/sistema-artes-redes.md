---
type: resource
date: 2026-07-21
last-touched: 2026-10-19
tags:
  - resource
  - tema/marketing
  - tema/branding
  - tema/automatizacion
  - proyecto/understanding-kids
status: operativo
---

# Sistema de artes para redes — UK / IS (operativo)

Sistema automatizado que produce los artes de Instagram y Facebook de [[understanding-kids|Understanding Kids]] (UK) y su submarca [[integracion-sensorial|Integración Sensorial]] (IS): plantillas HTML/CSS renderizadas con Playwright a PNG (1080×1350 posts, 1080×1920 historias). Esta página describe **cómo funciona en octubre de 2026**: quién hace qué, cuándo corre, qué reglas no se rompen y dónde vive cada pieza.

> **Reescrita el 2026-10-19** a partir de las instrucciones vivas de las tareas (`SKILL.md`), los prompts y scripts de `~/Claude/bin/`, los LaunchAgents y las memorias de Claude. Lo que no se pudo comprobar está marcado **(sin verificar)**. Reglas visuales completas: [[guia-maestra-estilo]] · promos: [[guia-promos-talleres]] · plantillas: [[plantillas-artes]] · rutas: [[mapa-de-archivos]].

## Piezas del sistema

| Pieza | Qué hace | Dónde |
|---|---|---|
| Motor | Plantillas `build_*.py`, guiones `armar_*.py` (aquí vive el copy), verificadores, fuentes y logos | `~/Documents/Understanding Kids/Artes/Sistema/` (iCloud, taller) |
| Calendario de Artes | Briefs de Magoo, estados, enlace al arte y a Drive | Notion `collection://175780c0-4762-81ec-a2a0-000bf5fe9eac` |
| Base 🔥 Tendencias | Sugerencias del agente de tendencias | Notion `collection://c8b3310c-b24a-49f9-8a3f-3dd4c60c5359` |
| Cola de revisión | Artes recién hechos | `Artes/Pendientes de Revision/` |
| Histórico local | Artes cerrados | `Artes/Aprobadas/` (descartes en `Artes/_Descartadas/`) |
| Vitrina | Lo aprobado, de donde publica Magoo | Drive `Administración (1)/Artes/2026/<Marca>/<Tipo>/` |
| Automatizaciones | 2 tareas programadas de Claude + 3 LaunchAgents | `~/.claude/scheduled-tasks/`, `~/Claude/bin/`, `~/Library/LaunchAgents/com.jr.uk-*` |

Todo corre en la **Mac Mini `jr`** (migrada el 2026-08-14). `~/Documents/Understanding Kids` es un symlink a `~/Library/Mobile Documents/com~apple~CloudDocs/Documents/Understanding Kids`.

## Horarios

| Qué | Cuándo | Cómo se dispara |
|---|---|---|
| `uk-tendencias-virales` | lunes y jueves 7:00 | Tarea programada de Claude (cron `0 7 * * 1,4`) |
| `uk-artes-semanales` | domingo 18:00 | Tarea programada de Claude (cron `0 18 * * 0`) |
| `uk-cambios` | lunes, miércoles y viernes 20:00 | LaunchAgent `com.jr.uk-cambios` → `uk-cambios-watch.sh` |
| `uk-cierre` | cada 15 min (y al cargar) | LaunchAgent `com.jr.uk-cierre` → `uk-cierre-watch.sh` |
| Resumen a Magoo | todos los días 6:00 | LaunchAgent `com.jr.uk-resumen-magoo` → `uk-resumen-magoo.py` |

Las tareas programadas de Claude **necesitan la app de Claude abierta** en la Mac a la hora del cron. Su horario está en `~/Library/Application Support/Claude/claude-code-sessions/…/scheduled-tasks.json` (lo administra la app, no se edita a mano). Los watchers de `~/Claude/bin` consultan Notion directo por REST (barato) y **solo despiertan a Claude** (`claude -p`) si hay trabajo.

## Estados del Calendario (desde el 16-oct-2026)

```
Por hacer → En revisión (JR) ⇄ Cambios pedidos → Revisión Magoo → Aprobado → Publicado
```

| Estado | Quién lo pone | Qué dispara |
|---|---|---|
| Por hacer | Magoo / corrida semanal (filas 🔥) | La corrida del domingo la toma si cae en los próximos 10 días |
| En revisión | Corrida semanal o corrida de cambios, solo con la pieza completa | JR revisa desde el teléfono |
| Cambios pedidos | JR (o Magoo) con comentarios | La corrida de cambios (L/M/V) arma la v2 |
| Revisión Magoo | JR (su visto bueno) | Entra al resumen de las 6:00 |
| Aprobado | **Magoo** | El vigilante de cierre sube a Drive |
| Publicado | Magoo | — |

Los estados viejos (Backlog, Planning, Draft, Done, Posted) ya no existen, y la casilla «Aprobado» tampoco: aprobar es el estado. El campo `Area` se eliminó el 16-oct-2026.

**Campos que usa el sistema:** `Name`, `Página` (Understanding Kids / Integración Sensorial), `Status`, `Visuals needed`, `Categoría`, `Campaña`, `Text` (brief de Magoo: Tema, Objetivo, Enfoque, Hook, Dirección visual, CTA, Notas), `Date`, `Carpeta del arte` (nombre exacto de la carpeta en disco; es la llave del cierre), `Enlace Drive`, `Fotos`.

## 1. Corrida semanal — `uk-artes-semanales` (domingo 18:00)

Instrucciones: `~/.claude/scheduled-tasks/uk-artes-semanales/SKILL.md`. Desde el 19-oct-2026 (F6 de [[vault-cerebro]]) lee al empezar las páginas del Vault: [[guia-maestra-estilo]], esta página, [[plantillas-artes]], [[artes-decisiones-y-lecciones]] y, si hay promos o campañas, [[guia-promos-talleres]] y [[campana-eda26]]. Los archivos de `Sistema/` con esos nombres son avisos de mudanza. Lo durable que aprende lo deja en «PARA EL VAULT» del reporte (regla en [[agentes/claude/memoria]]).

1. **Candidatos:** `Visuals needed` = sí, `Status` = «Por hacer», las dos marcas, fecha en los próximos 10 días. Ojo: el filtro de `Visuals needed` no es confiable; una semana sin piezas diarias es una anomalía y se reporta como titular (memoria del 11-ago).
2. **Campañas:** si la fila tiene `Campaña`, primero se lee su entrada «PARÁMETROS DE CAMPAÑA» en Notion (prompt maestro: paleta, tipografía, `THEME_*`). Manda Notion sobre la guía local. Sin entrada maestra y gestionada por JR (ej. **AUT26**) → no se genera.
3. **Tendencias aprobadas → Calendario** (regla del 16-oct): cada tendencia en «Aprobada» se convierte en fila(s) «🔥 …» del Calendario (dos si la marca es «Ambas»), con fecha según `EVENTO:` o lo antes posible (al menos 5 extras por semana), y la tendencia pasa a «Hecha». Las vencidas no entran.
4. **Cruce contra Drive:** antes de generar, busca si ya hay arte en `Artes/2026/` (incluye `Campañas/`). Magoo renombra a «subido» al publicar, así que se abre el `caption.txt` para saber qué es.
5. **Arma cada pieza:** portada (keyword de 1-3 palabras) → slides con al menos 1-2 materiales visuales variados → cierre con CTA; **historia obligatoria** (`build_story.py`); caption en `caption.txt`. Reels/video = «atención manual». Lo que falte va a la sección **DATOS FALTANTES**; nunca se inventa.
6. **Verificadores** (los dos en 0) — ver abajo.
7. **Guarda** en `Pendientes de Revision/<AAAA-MM-DD> - <UK|IS> <tema>/` (`01_portada.png`, `02_….png`, `story_*.png`, `caption.txt`).
8. **Deja la pieza visible en Notion:** imágenes en el **cuerpo** de la fila (ver «Fotos en Notion»), `Carpeta del arte` lleno, `Categoría` si es segura, y `Status` → «En revisión» solo si todo está completo y verde. Ningún otro estado; nada a Drive.
9. **Aviso a JR por Telegram** con `avisar-jr.sh` (ver «Avisos»).

**Categorías y familias:** constantes (Informativo, Servicios, Frases, Testimonios, Recursos, Producto, Formación) → plantillas diarias; **Publicidad** (pieza suelta) y **Campañas** (hilo de piezas) → `build_promo.py` según [[guia-promos-talleres]].

## 2. Tendencias — `uk-tendencias-virales` (lunes y jueves 7:00)

Instrucciones: `~/.claude/scheduled-tasks/uk-tendencias-virales/SKILL.md`. No hace artes: escribe sugerencias en la base 🔥 Tendencias con `Status` = «Sugerida» (nunca otro).

- **Alcance:** solo Instagram y Facebook, solo estáticos y carruseles. Busca **formatos/ángulos que se replican** entre cuentas, momentos culturales con puente natural (WebSearch) y outliers.
- **Fuentes:** cuentas de [[tendencias-referentes]] + barrido de hashtags con Apify (MCP) + WebSearch. Estado entre corridas en `Sistema/tendencias/` (`ledger.py`, `posts.csv`, `angles.jsonl`, `runlog.md`).
- **Presupuesto Apify:** plan gratis con tope de USD 5/mes; meta ~USD 0.45 por corrida, con escalones según lo que quede del mes (consulta `users/me/limits`).
- **Máximo 4 sugerencias**, al menos 1-2 de autismo **genuino** (piso, no techo: corrección de JR del 14-ago). Marca **UNA sola** (UK o IS); «Ambas» solo si de verdad aplica. Si depende de una fecha: `EVENTO: <nombre> — <fecha>` en la primera línea de la Sugerencia.
- **Filtro de marca:** fuera lo que ridiculice a niños o papás, use miedo, se burle de condiciones del desarrollo, toque política/religión/tragedias, o solo funcione como video. No duplicar.
- JR/Magoo marcan **«Aprobada»** → la corrida del domingo la pasa al Calendario.

## 3. Correcciones

**Automática — `uk-cambios` (L/M/V 20:00).** `uk-cambios-watch.sh` cuenta filas en «Cambios pedidos» con `uk-notion.py cambios`; si hay, corre Claude con `uk-cambios-prompt.md` (con `--permission-mode bypassPermissions`). El agente:
1. Lee los comentarios de la página y de cada lámina (solo la última sección «🎨 Arte generado»).
2. Copia solo el bloque de esa pieza a `Sistema/armar_correccion_<fecha>_<tema>.py` y renderiza en `Pendientes de Revision/<carpeta> (v2)/` (o v3…). **Nunca corre un `armar_*.py` viejo.**
3. Aplica cada pedido literal (lo «aprobado por Mónica», palabra por palabra), mira cada PNG, corre los verificadores.
4. Con todo en verde: `uk-notion.py v2 …` **borra del cuerpo el arte viejo** (en la página queda solo la versión a revisar; JR, 20-oct-2026), sube la v2, actualiza `Carpeta del arte`, vacía `Enlace Drive` y pone «En revisión». Lo borrado se anota en `~/Claude/state/historial-versiones.jsonl`; los PNG viejos siguen en su carpeta. Avisa a JR. Ni Drive, ni correo, ni borrar la v1 de disco.

**A demanda — por Telegram.** Reglas en `~/Claude/CLAUDE.md`: Claude actúa como coordinador (prueba hasta ~16-nov-2026), identifica la pieza, confirma en una línea, corrige solo esa pieza, corre los verificadores y manda el PNG por el mismo chat. Una corrección **no** dispara el cierre: no se sube a Drive, no se cambia a Aprobado/Publicado y no se escribe a Magoo. Si la pieza ya está en Drive, se avisa y se espera el OK de JR.

## 4. Cierre — `uk-cierre` (cada 15 min)

`uk-cierre-watch.sh` busca filas con `Status` = «Aprobado» y `Enlace Drive` vacío. Si hay, corre Claude con `uk-cierre-prompt.md`:
1. Valida por pieza: `Carpeta del arte` existe en Pendientes, `Categoría` tiene valor, verificadores en 0. Si algo falla, salta esa pieza y sigue.
2. Copia a Drive por el disco montado (cuenta de la clínica): constantes → `2026/<Página>/<Categoría>/<carpeta>/`; Publicidad → `2026/Publicidad/<carpeta>/`; Campañas → `2026/Campañas/<campaña>/<carpeta>/`. Nunca pisa una carpeta existente.
3. **v2/v3:** el destino es el nombre sin sufijo; si ya estaba en Drive, lo viejo pasa a una subcarpeta «Versión anterior» y la versión nueva queda en la raíz.
4. Verifica cantidad y bytes origen = destino; recién entonces escribe `Enlace Drive`, comenta en Notion (ubicación + caption) y **mueve** la carpeta a `Aprobadas/`.
5. Avisa a JR en una línea. **Sin correo a Magoo** (ella aprobó, ya sabe).

**Resumen a Magoo (6:00):** `uk-resumen-magoo.py` le manda **un** correo al día (de jcastaneda@ a msamayoa@, vía `gws`) con lo que entró a «Revisión Magoo»; si no hay nada nuevo, no manda nada. Estado en `~/Claude/state/resumen-magoo.json`.

**Publicar** no se automatiza: Magoo descarga de Drive y publica en Instagram y Facebook (stickers incluidos). Magoo no sube nada a Drive (JR, 28-ago).

## Guardarraíles (se rompen en silencio)

- **Marca:** pieza de IS lleva `"marca":"IS"` en **todos** los dicts (incluido el cierre) y `marca="IS"` en las historias. Si falta en uno, ese slide sale con fondo de UK y nada falla. **UK = crema `#FBFAF6` + amarillo `#EEB41E`. IS = celeste `#F4F9FA` + turquesa `#3FA8C0`.** Nunca comparten fondo.
- **`build_pasos.steps` = lista de strings**, no de dicts: un dict se imprime literal en el arte y ningún verificador lo caza. Mirar siempre el PNG de un slide de pasos.
- **Portada:** `headline_keyword` de 1-3 palabras en una línea; el resto en `headline_main`.
- **Autismo:** `"autismo": True` en cada slide (sello ∞ discreto). Identidad primero: «niño autista», nunca «niño con autismo». Símbolo ∞; el 🧩 está prohibido. Nunca cura/enfermedad/alarmismo.
- **Contactos:** siempre los de UK, también en IS, importados de `build_cierre` (`CONTACT` / `CONTACT_IS`), con **los dos teléfonos** (Zona 14 +502 5926-9205 · Carretera +502 5214-8161). En captions también se escriben los dos.
- **EDA26:** inscripciones por WhatsApp (+502 5926-9205) desde el 15-sep-2026; ninguna pieza manda a una página web ni promete sticker de enlace.
- **Honestidad:** nunca inventar cifras, fechas, precios ni cupos. Fotos de niños: solo stock real, nunca IA.
- **Copy:** tono humano (nada de «explorar/descubre/potencia»), tuteo, máximo 5 hashtags, nunca punto antes de emoji.
- **Carruseles:** máximo 10 láminas, que se lean como una sola historia; nunca dos layouts iguales seguidos; historias sin logo de la casa (salvo campaña con co-logo); la rejilla 2×2 de infografía solo con 4 o 6 elementos.

## Verificadores

Desde `Sistema/`, antes de reportar cualquier corrida o corrección:

```bash
python3 verificar_marca.py --todas "<Pendientes de Revision>"
python3 verificar_caption.py --todas "<Pendientes de Revision>"   # o el caption.txt de una carpeta
```

- `verificar_marca.py` lee el fondo real de cada PNG y lo compara con la marca que dice la carpeta (`- UK ` / `- IS `). Reconoce por píxeles los layouts a sangre aprobados y omite las paletas de campaña. **No** detecta un dict impreso en `pasos` ni un color de campaña mal aplicado.
- `verificar_caption.py` revisa máximo 5 hashtags y ningún punto antes de emoji. Con una carpeta como argumento suelto revienta (`IsADirectoryError`): hay que pasarle el archivo o usar `--todas`.
- `reglas_contenido.py` avisa por consola si un texto se sale del largo recomendado (no bloquea).

## Fotos

- **Búsqueda:** `buscar_foto.py` (Pexels primero, Openverse de respaldo), en inglés. La llave de Pexels se lee de `Sistema/pexels_key.txt` (ver `_sensitive.md`).
- **Dónde se guardan:** `~/Documents/Understanding Kids/Artes/Fotos/` (permanente). Nunca referenciar `/private/tmp/...` desde un `armar_*.py`: el scratchpad se borra y la pieza ya no se puede re-renderizar.
- No repetir la misma foto entre piezas ni entre el post y su historia.
- **Ilustraciones:** Pollinations dejó de ser gratis (402) y no se le carga saldo (decisión JR 1-oct-2026); las ilustraciones se dibujan en casa (`ilustraciones.py`, `doodles.py`, `ilustracion_antes_hoy.py`).
- **Fotos en Notion:** el campo `Fotos` **no se puede llenar por API**; los PNG van en el **cuerpo** de la página (`file-upload://…` en bloques de imagen, bajo un encabezado «🎨 Arte generado — <carpeta>»). Si Cloudflare devuelve 403, se re-codifica el PNG y se reintenta.

## Avisos

Todas las corridas desatendidas avisan a JR por Telegram con `~/Claude/bin/avisar-jr.sh "<texto>"` (HTTP `sendMessage`, chat de JR). **Nunca con el plugin MCP de Telegram**: levantarlo en otra sesión le mata el poller al puente. Voz del Tío Iroh, de tú, corto. Se avisa también si la corrida falla.

## Credenciales (solo rutas)

Notion REST: `~/Claude/.secrets/notion.env` · Telegram: `~/.claude/channels/telegram/.env` · token largo de Claude: `~/.claude/secrets/claude-oauth-token` · Pexels: `Sistema/pexels_key.txt` · Apify: configuración MCP en `~/.claude.json`. Valores: nunca en el wiki; referencia en `_sensitive.md`.

## Inconsistencias encontradas el 19-oct-2026 (para F6)

- ~~El `SKILL.md` semanal (paso 6) todavía pide subir los PNG al campo `Fotos`.~~ Corregido en F6 (19-oct-2026): el paso 6 ahora dice cuerpo de la página.
- [[guia-maestra-estilo]] §8 y [[guia-promos-talleres]] §7 (copias fieles de las guías de `Sistema/`) describen el cierre de julio (correo a Magoo, Status «Aprobado» puesto por el agente). Vigente: lo de esta página.
- [[guia-promos-talleres]] §1 lista un solo WhatsApp (desde el 10-sep son dos).
- ~~La memoria `uk_template_system.md` todavía dice que tendencias corre «jueves 18:00» y describe el cierre con correo a Magoo.~~ Resuelto en F6: la memoria quedó como regla corta con enlace.
- La memoria `uk_correcciones_flujo.md` (21-sep) habla de Status «Done» y de responder el correo de Magoo; el flujo del 16/18-oct lo reemplazó (sin correo, estados nuevos). **Resuelto por JR el 19-oct-2026: no se le escribe correo a Magoo; ella pide los cambios por Notion (comentarios + «Cambios pedidos», que procesa `uk-cambios`).** Detalle en [[agentes/claude/subagentes]].
- En `~/Documents/Understanding Kids/` hay dos symlinks («Administración», «Administración 3») que apuntan a `/Users/jotaerre/...` (usuario de la Mac anterior); en esta Mac no resuelven. Nadie del sistema los usa (el cierre usa `~/Library/CloudStorage/...`).
- `Drive/2026/Publicidad/` sigue fuera de la convención de 6 tipos; el cierre ya la usa como destino de la categoría Publicidad.

## Historia

- **2026-07-07:** intento con Canva MCP ([[sistema-templates-canva]]): la API no crea elementos ni cambia fondos.
- **2026-07-16 →:** pivote a HTML/CSS + Playwright; ciclo completo probado el 20-jul.
- **2026-07-21:** motor a iCloud; agente de tendencias; pilar de autismo y símbolo ∞.
- **2026-08-03 / 08-05:** fondo por marca y `verificar_marca.py`; reglas de caption y `verificar_caption.py`; 8 layouts de historia.
- **2026-08-14:** migración a la Mac Mini `jr` ([[migracion-sistema-artes]], hoy obsoleto).
- **2026-08-17:** reglas de la revisión de JR (historias sin logo, rejilla 2×2, fotos permanentes, talleres como producto).
- **2026-08-26:** avisos por Telegram con `avisar-jr.sh`.
- **2026-09-10:** dos teléfonos en todos los cierres.
- **2026-09-15:** EDA26 inscribe por WhatsApp.
- **2026-10-16:** nuevo flujo de estados en Notion, cierre automático cada 15 min, resumen diario a Magoo, tendencias aprobadas pasan al Calendario.
- **2026-10-18:** corrida de cambios L/M/V con v2 y «Versión anterior»; «En revisión» al terminar la corrida semanal.
- **2026-10-19:** el conocimiento del sistema pasa al Vault ([[vault-cerebro]]); se borró la copia vieja del motor de `raw/imports/`.

## Relacionado

- [[understanding-kids]] · [[integracion-sensorial]] · [[monica]] · [[visual-identity]] · [[uk-catalogo]]
- [[guia-maestra-estilo]] · [[guia-promos-talleres]] · [[tendencias-referentes]] · [[plantillas-artes]] · [[artes-decisiones-y-lecciones]]
- [[agentes/claude/AGENT|Claude]] · [[agentes/claude/tareas-programadas]] · [[agentes/claude/subagentes]]
- [[mapa-de-archivos]] · [[vault-cerebro]] · [[campana-eda26]] · [[diplomado-autismo-2026]]
- [[migracion-sistema-artes]] (obsoleto) · [[sistema-templates-canva]] (descartado)
- **2026-10-20:** (JR) Notion es el hub central de publicaciones: todo lo que Magoo pida por correo u otra vía entra al Calendario como fila completa (fecha, contenido, todo). En cada página queda solo la versión a revisar; nada de «Versión anterior» en Notion (el historial va aparte). Pieza terminada = «En revisión», si no JR no la ve.
- **2026-10-20:** (JR) **Matriz del arte en Drive:** cada publicación tiene su carpeta con su TÍTULO (sin fecha ni «subido») dentro de `Artes/2026/<Página>/<Categoría>/` (Publicidad y Campañas en su ruta), y adentro una subcarpeta por versión `v1`, `v2`, `v3`… Cada versión sube apenas se genera (semanal → v1, cambios → v2…) con `~/Claude/bin/uk-drive-version.py`; el cierre solo confirma que la aprobada esté y es el único que llena `Enlace Drive` (enlace a la carpeta del título), al pasar a «Aprobado». Magoo ya no renombra carpetas: «Publicado» se marca en Notion. Lo viejo («subido (N)», «pendiente:», «Versión anterior») no se tocó.
