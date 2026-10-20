---
type: resource
date: 2026-10-19
last-touched: 2026-10-19
tags:
  - resource
  - proyecto/understanding-kids
  - tema/branding
  - tema/automatizacion
---

# Plantillas de artes (`build_*.py`)

Una sección por plantilla del motor de artes de UK/IS: qué produce, qué recibe y qué guardarraíles trae. Las plantillas **se quedan en** `~/Documents/Understanding Kids/Artes/Sistema/` (decisión D1 de [[vault-cerebro]]): cargan fuentes y logos de su carpeta y escriben ahí sus renders. Aquí solo se describen.

> Fuente: docstring y firma de cada archivo, leídos el 2026-10-19. Las claves listadas son las que el código lee del dict `content`; no todas son obligatorias. Para las reglas visuales, [[guia-maestra-estilo]]; para el flujo, [[sistema-artes-redes]].

## Cómo se usan

- Cada plantilla expone `render(content, out_path)` (algunas con parámetros extra) y se llama desde un guion `armar_*.py`, que es **donde vive el copy**. Se cambia el dict, no el HTML.
- **Línea diaria:** todas leen `content["marca"]` (`"UK"` por defecto, `"IS"`) para fondo, acento y logo; las historias lo reciben como `marca=`. `"autismo": True` agrega el sello ∞.
- Las que llevan texto validan largos con `reglas_contenido.py` (avisa, no bloquea): portada, contenido, contenido_imagen, contenido_frase, infografía, pasos, cierre.
- Base común: `build_contenido.py` define `BACKGROUNDS`, `ACCENTS`, `bg_for()`, `accent_for()`, `accent_text_for()`, el SVG del infinito y `esperar_subrayado()`. Una plantilla nueva hereda de ahí; nunca hardcodea colores ni fuentes.
- Regla dura: **nunca correr un `armar_*.py` de una corrida pasada** (sobrescribe artes aprobados).

## Línea diaria (posts 1080×1350)

### build_portada.py
- **Produce:** portada / hook de apertura con palabra clave subrayada.
- **Recibe:** `headline_main`, `headline_keyword`, `icon`, `bajada`, `ilustracion`, `ilustracion_alto`, `marca`, `autismo`.
- **Guardarraíles:** `headline_keyword` de 1-3 palabras en una línea. Tamaño base 84 px; solo lo reduce (mide con Playwright) si no cabe en la zona segura. Ícono en su propia línea; centro óptico.

### build_contenido.py
- **Produce:** título + párrafo + viñetas opcionales + remate con palabra clave subrayada. Es además la **base** de todo el sistema.
- **Recibe:** `heading`, `body`, `bullets`, `closing_pre`, `closing_keyword`, `icon`, `marca`, `autismo`.
- **Guardarraíles:** `closing_keyword` de 1-4 palabras en una línea (si se parte, avisa fuerte por consola). La barra del subrayado se mide después de cargar las fuentes (`document.fonts.ready`, arreglo del 2-oct-2026).

### build_contenido_imagen.py
- **Produce:** slide de contenido con ventana de imagen (foto real o ilustración).
- **Recibe:** `heading`, `body`, `closing_pre`, `closing_keyword`, `image_path`, `img_position`, `img_height`, `marca`, `autismo`.
- **Guardarraíles:** foto real para niños (nunca IA); `img_position` para no cortar caras. Fotos desde `Artes/Fotos/`, nunca desde `/private/tmp`.

### build_contenido_frase.py
- **Produce:** frase o cita protagonista con atribución.
- **Recibe:** `quote`, `author`, `context`, `marca`, `autismo`.
- **Guardarraíles:** `quote` de 4-14 palabras; si es más larga, usar `build_contenido`. Sin comilla decorativa si no es cita (preferencia de JR, 21-sep).

### build_infografia.py
- **Produce:** conceptos paralelos en tarjetas.
- **Recibe:** `heading`, `icon`, `items` (cada uno con `icon` o `image_path` + texto), `layout` (`auto`, `grid`, `rows`, `centro`), `marca`, `autismo`.
- **Guardarraíles:** `grid` (2×2) solo con 4 o 6 elementos; con 3 o 5 usa `rows` (avisa si se fuerza). `centro` = exactamente 4 fotos con el titular al medio. Las etiquetas tienen que decir algo, no ser una lista suelta.

### build_pasos.py
- **Produce:** pasos numerados conectados por una línea.
- **Recibe:** `heading`, `icon`, `steps`, `marca`, `autismo`.
- **Guardarraíles:** **`steps` es una lista de strings.** Un dict se imprime literal en el arte y ningún verificador lo caza: abrir siempre el PNG. El número lo pone la plantilla.

### build_comparacion.py
- **Produce:** dos columnas (mito/realidad, antes/después).
- **Recibe:** `heading`, `icon`, `left_label`, `left_text`, `left_kind`, `right_label`, `right_text`, `right_kind`, `marca`, `autismo`.
- **Guardarraíles:** izquierda en terracota (negativo) por defecto; para contrastes sin carga, `left_kind="neutral"`.

### build_dato.py
- **Produce:** una cifra grande o un gráfico de dona.
- **Recibe:** `modo` (`numero` / `dona`), `numero`, `valor` (0-100 para dona), `etiqueta`, `fuente`, `marca`.
- **Guardarraíles:** solo con cifra **real** y fuente citable; avisa fuerte si falta la fuente. Si no hay dato real, no se usa.

### build_cierre.py
- **Produce:** cierre con CTA, logo de la marca y barra de contactos.
- **Recibe:** `heading`, `body_pre`, `body_highlight`, `closing`, `marca`, `autismo`; `render(content, out_path, contact)`.
- **Constantes:** `CONTACT` y `CONTACT_IS` (los mismos datos de UK, con **dos WhatsApp**: Zona 14 y Carretera), `LOGOS`, helper `icono()` (acepta claves repetidas tipo `whatsapp2`).
- **Guardarraíles:** los guiones **importan** `CONTACT`, no declaran uno propio. El sello ∞ va arriba de la barra de contacto.

### build_flyer.py
- **Produce:** flyer de detalles para promoción (taller, curso, diplomado) en línea diaria.
- **Recibe:** `title`, `subtitle`, `badge`, `rows` (Fecha, Modalidad, Horario, Cupos, Inversión…), `cta`, `marca`.
- **Guardarraíles:** datos reales; un solo acento.

### build_foto_tarjeta.py
- **Produce:** formato «foto a sangre + tarjeta» (copia medida del diseño de Canva `DAHUK9UZ8xg`, JR 7-sep-2026), en post o en historia (`alto`).
- **Recibe:** `image_path`, `img_position`, `title`, `items`, `closing`, `layout` (`portada`, `arriba_derecha`, `arriba_izquierda`, `abajo`, `abajo_cierre_fuera`), `redes`, `autismo`.
- **Guardarraíles:** valores medidos, no se cambian sin JR; la tarjeta cambia de posición entre slides y no debe tapar lo importante de la foto. `verificar_marca.py` la reconoce por el `#FFFDF7` de la tarjeta.

## Promos y campañas

### build_promo.py
- **Produce:** sub-sistema de promos y campañas con paleta propia: `render_cover` (portada-flyer), `render_foto`, `render_incluye` (`cols: 2` para rejilla), `render_temario`, `render_sesiones`, `render_expositoras`, `render_precios`, `render_cierre`.
- **Recibe:** `(content, theme, out_path)`; `render_cover` además `marca`, `co_logo`, `logos`; `render_cierre` además `contact`, `marca`, `co_logo`.
- **Themes:** `THEME_ALIMENTACION`, `THEME_LENGUAJE`, `THEME_EMOCIONES`, `THEME_SENSORIAL`, `THEME_SUENO`, `THEME_EDA26`, `THEME_UK_SERVICIOS`, `THEME_IS_SERVICIOS`, o uno nuevo con `make_theme(...)`. Helpers: `font_title/font_body` (tipografía por theme), `texto_sobre()` (contraste por luminancia), `lockup_logos()`, `marcas_html()`; constantes `LOGOS` y `STICKERS`.
- **Guardarraíles:** la identidad de una campaña se lee de su entrada «PARÁMETROS DE CAMPAÑA» en Notion; si el `THEME_*` no coincide, manda Notion. Con co-formador (`co_logo` en el theme), nunca aparece el logo de la casa solo. En EDA26 la portada va sin logo (`logos=False`) y la autoría en `content["firma"]`. Datos reales siempre.

### build_anuncio_taller.py
- **Produce:** anuncio de taller o curso que se sostiene solo (registro del flyer de Canva `DAHUiWjcdas`, JR 7-sep-2026): título, foto en banda, píldora de urgencia, gancho, 4 datos en 2×2, nota y barra de contactos.
- **Recibe:** `render(content, theme, out_path, marca, contacto, alto)`; `content`: `title`, `badge`, `image_path`, `img_position`, `foto_h`, `hook`, `datos`, `nota`, `cta`.
- **Guardarraíles:** es formato de ANUNCIO, distinto de `build_foto_tarjeta` (carrusel). Usa paleta propia, así que `verificar_marca.py` lo omite como campaña.

## Historias (1080×1920)

### build_story.py
- **Produce:** 8 layouts: `render_story_teaser`, `render_story_promo`, `render_story_quote`, `render_story_tip`, `render_story_pregunta`, `render_story_lista`, `render_story_bloque`, `render_story_foto`.
- **Recibe:** `(content, out_path, marca)`; `pregunta`, `lista` y `bloque` aceptan `theme` (campaña); `promo` recibe `theme`, `co_logo`, `logos`. `paleta_story(marca, theme)` traduce un theme de campaña a colores de historia (incluido `title`, arreglo del 28-ago).
- **Guardarraíles:** cada carrusel lleva al menos una historia; no repetir layout en la misma semana ni en las dos historias de un carrusel; la historia no cuenta todo el post. Sin logo de la casa (`LOGO_EN_HISTORIAS = False`), salvo campaña con `co_logo`. Zona inferior libre para los stickers de Magoo; contenido importante entre y=280 y y=1640.

## Utilidades que no son plantillas

| Archivo | Para qué |
|---|---|
| `verificar_marca.py` | Fondo real de cada PNG contra la marca de la carpeta (obligatorio) |
| `verificar_caption.py` | Máx. 5 hashtags y ningún punto antes de emoji (obligatorio) |
| `reglas_contenido.py` | Largos de copy por campo (avisa) |
| `buscar_foto.py` | Fotos de Pexels/Openverse; llave en `pexels_key.txt` |
| `hacer_sticker.py` | Troquel blanco para logos sobre foto (círculo / rectángulo) |
| `doodles.py`, `doodles_board.py` | Ilustraciones SVG tipo crayón |
| `ilustraciones.py`, `ilustracion_antes_hoy.py`, `serie_antes_hoy.py` | Ilustraciones dibujadas en casa y motor de la serie «Antes se hacía así» |
| `tendencias/ledger.py` | Estado y consultas del agente de tendencias |
| `setup_mac_nueva.sh` | Instala Claude Code (instalador oficial; el de npm daba binario corrupto en arm64), Playwright + Chromium y hace un render de prueba |

## Detalles técnicos que venían de la memoria de Claude

Pasados aquí en la fase F6 de [[vault-cerebro]] (19-oct-2026), cuando la memoria `uk_template_system` se acortó. Lo demás de esa memoria ya estaba en [[guia-maestra-estilo]], [[sistema-artes-redes]], [[artes-decisiones-y-lecciones]] y [[campana-eda26]].

- **Portada, tamaño de letra (piloto 16-jul-2026):** nunca se reduce de antemano. Base fija 84px (la aprobada); `_fit_and_measure` mide de verdad en Playwright y solo achica si el bloque no cabe en la zona segura. Lo que en el piloto se veía «chico» no era la letra, era una `headline_keyword` de 3-4 líneas que diluía el golpe. No partir el hook de Magoo «a la mitad» sin criterio: elegir la palabra corta que es el verdadero remate.
- **`buscar_foto.py` usa `curl` por dentro** (no `requests`) porque el Python de python.org falla SSL; `curl` viene con macOS.
- **`render_story_promo`** acepta `content["hint"]` para no prometer un link que todavía no existe, y toma el color de badge/CTA de `theme["cta"]`.
- **Troquel (`hacer_sticker.py`), cómo funciona:** morfología sobre el canal alfa (dilatar → erosionar → redondear re-binarizando en 128). Paso imprescindible: `_rellenar_huecos()` (inunda desde una esquina; lo que no toca el borde se rellena), aplicado después de dilatar y de erosionar; sin él el logo de IS quedaba como anillo hueco. El lienzo se agranda **antes** de dibujar la figura (bug del 10-ago: el margen se salía del borde). El margen se mide en píxeles del archivo y cada logo se reduce distinto al imprimirse (el de Davinia ~2× menos que el de IS): calibrar mirando el grosor final. En formas de silueta el `redondeo` se limita al `margen`. Salida cacheada como `<logo>_sticker.png` + `_b64.txt`, expuesta en `STICKERS` de `build_promo.py`. Logo de Davinia en el motor: `logo_davinia.png` + `logo_davinia_b64.txt` (`LOGOS["DAVINIA"]`); originales en `Artes/Logos/`. Decisión de uso: [[artes-decisiones-y-lecciones]] § Logos.
- **Barra de contacto del cierre:** tiene `flex-wrap`, así que los cinco ítems (con los dos WhatsApp) caen en dos filas; verificado en cierre UK, cierre IS, anuncio feed y anuncio historia. Los artes ya aprobados con un solo número no se re-renderizan salvo pieza por pieza con visto bueno de JR.
- **Carrusel de ejemplo** aprobado por JR el 16-jul-2026: 6 slides de alimentación, orquestado entonces por `armar_carrusel_alimentacion.py`, que ya no está en `Sistema/` (verificado 19-oct-2026). Para promos, el ejemplo vigente es `armar_taller_alimentacion.py` (solo de referencia; no se corre).

## Relacionado

- [[sistema-artes-redes]] · [[guia-maestra-estilo]] · [[guia-promos-talleres]]
- [[mapa-de-archivos]] · [[vault-cerebro]] · [[understanding-kids]] · [[campana-eda26]]
