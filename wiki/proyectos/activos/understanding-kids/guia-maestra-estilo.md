---
type: resource
date: 2026-10-19
last-touched: 2026-10-19
tags:
  - resource
  - proyecto/understanding-kids
  - tema/branding
  - tema/marketing
  - tema/autismo
fuente: "~/Documents/Understanding Kids/Artes/Sistema/GUIA_MAESTRA_ESTILO.md"
---

> **Fuente de verdad desde 2026-10-19.** Las tareas y los agentes la leen desde aquí (fase F6 de [[vault-cerebro]]). `Sistema/GUIA_MAESTRA_ESTILO.md` quedó como aviso de mudanza: los cambios se hacen solo en esta página.
>
> Copia fiel de la guía viva de la línea visual de artes UK/IS: marcas, paleta, tipografía, copy, catálogo de plantillas, fotos, pilar de autismo, variaciones, tendencias, campañas y doodles.

> **Ojo, §8 (flujo operativo) describe el flujo de julio** (cierre con «Status Aprobado» y correo a Magoo). El flujo vigente desde el 16-oct-2026 está en [[sistema-artes-redes]].

---

# GUÍA MAESTRA DE ESTILO — Artes UK / IS

**Propósito:** que cualquier arte nuevo — plantilla nueva, variación, formato viral, lo que sea — se pueda crear con libertad **y aún así se vea inconfundiblemente de la casa.** Esta guía define qué es "la línea": qué se puede variar, qué no se toca nunca, y cómo decidir.

Documentos hermanos: `GUIA_PROMOS_TALLERES.md` (sub-sistema de promoción) · `MIGRACION.md` (infraestructura) · `reglas_contenido.py` (largos de copy, ejecutable).

---

## 1. Las dos marcas

| | Understanding Kids (UK) | Integración Sensorial (IS) |
|---|---|---|
| Qué es | Clínica principal | Sub-marca ("by Understanding Kids") |
| **Fondo** | Crema `#FBFAF6` | Celeste claro `#F4F9FA` |
| **Acento de marca** | 🟡 Amarillo `#EEB41E` | 🔵 Turquesa `#3FA8C0` (del logo) |
| Texto sobre el acento | Café oscuro `#3a2c05` | Blanco `#FFFFFF` |
| Acento secundario | Verde `#76B142` | Verde lima `#6FAE1C` |
| Logo | `logo_uk_b64.txt` | `logo_is_b64.txt` |
| Contactos | FB Understanding Kids · IG @kidsunderstanding · WA **de las dos sedes** (Zona 14 +502 5926-9205 · Carretera +502 5214-8161) · kidsunderstanding.com | **Los mismos de UK, siempre** |

> **Los contactos NO se escriben a mano en el script de la corrida.** Se importan:
> `from build_cierre import CONTACT` (o `CONTACT_IS`). Hasta el 10-sep-2026 cada
> `armar_semana_*.py` declaraba su propio dict `CONTACTO`, y por eso el cambio de
> los dos teléfonos no llegaba solo a las corridas: un dict local le gana al de la
> plantilla. Si una pieza necesita contactos distintos, se parte del importado y se
> modifica la clave puntual, nunca se reescribe entero.
>
> Magoo lo pidió el 25-ago-2026: «en los artes colocar el número de teléfono de
> ambas sedes, no únicamente de zona 14». **También aplica a los captions**, donde
> el teléfono se escribe a mano dentro del texto.

Todo lo demás es **compartido**. En código: `"marca": "UK"/"IS"` en cada dict de contenido activa logo + acento automáticamente (`build_contenido.accent_for()`).

## 2. Sistema de diseño (el esqueleto que nunca cambia)

### Lienzo y retícula
- **Post/carrusel:** 1080×1350 (4:5). **Historia:** 1080×1920.
- **Margen lateral:** 100px (posts) / 90px (historias). Contenido crítico dentro de 1000×1270.
- **Columna de texto:** máx. 800px.
- **Historias — zonas seguras:** la interfaz de IG tapa ~250px arriba y ~250px abajo. Todo lo importante entre y=280 y y=1640; la franja inferior queda libre para stickers de Magoo.

### Tipografía (JAMÁS otra)
- **Cocogoose Pro Bold** — titulares, keywords, números, CTAs. (`cocogoosepro_bold_b64.txt`)
- **Montserrat** (variable 100–900) — cuerpo, etiquetas, pies. (`montserrat_b64.txt`)

Jerarquía de tamaños en posts: portada 84px (auto-reduce hasta 52 si no cabe) · heading 54–62 · body 36–38 · bullets 36 · closing 40–42 · etiquetas 23–30 · pie de contacto 19.

### Paleta completa y roles
| Color | Hex | Rol |
|---|---|---|
| Crema | `#FBFAF6` | **Fondo de UK** (no es el fondo de todo el sistema — ver abajo) |
| Celeste claro | `#F4F9FA` | **Fondo de IS** |
| Gris oscuro | `#33363B` | Texto |
| Amarillo | `#EEB41E` | Acento UK (énfasis, no "bueno") |
| Turquesa | `#3FA8C0` | Acento IS |
| Verde | `#76B142` | **Semántico: positivo/correcto** + resalte emocional |
| Terracota | `#C0503C` píldora / `#F9E6E1` fondo | **Semántico: negativo** (mito, presión, error). Nunca rojo alarma puro |
| Celeste | `#57BAC6` | Informativo/neutro, resalte emocional alternativo |
| Tintes pastel | `#FBEFCF` `#E6F0DD` `#DDEFF2` `#EEEDE7` | Fondos de tarjetas de infografía |
| Gris pie | `#6B6A64` texto / `#E2DFD5` línea | Barra de contacto |

**FONDO POR MARCA (regla dura, JR 2026-08-03):** UK e IS **NUNCA comparten fondo**. UK va sobre crema `#FBFAF6`; IS sobre celeste claro `#F4F9FA`. La diferencia es deliberadamente sutil: las dos marcas tienen que leerse bajo la misma sombrilla, no como marcas ajenas. Implementado en `build_contenido.py` (`BACKGROUNDS`, `bg_for()`); las 11 plantillas lo leen de `content["marca"]` (las historias, del parámetro `marca=`). **Pasar siempre `"marca":"IS"` en TODOS los dicts de una pieza de IS** — si se olvida en un slide, ese slide sale con el crema de UK y se nota en el carrusel. Antes del 2026-08-03 el crema estaba hardcodeado para ambas marcas: las piezas de IS de julio que ya están en Drive salieron con fondo de UK. **Guardarraíl:** `verificar_marca.py` lee el fondo real de los PNG ya renderizados y avisa si alguno no corresponde a su marca (`python3 verificar_marca.py --todas "<carpeta>"`; deduce la marca del nombre de la carpeta). Correrlo SIEMPRE al terminar de generar.

**LAYOUTS A SANGRE Y EL GUARDARRAÍL (actualizado 2026-09-23):** hay layouts aprobados que **por diseño no llevan fondo de marca**, y el verificador los reconoce por el PATRÓN DE PÍXELES — nunca por el nombre del archivo ni de la carpeta, y sin listas blancas. Son tres pases después del de las esquinas: (1) **foto a sangre + tarjeta flotante** (`render_story_foto`) → el color de marca vive en la tarjeta, se acepta si ocupa ≥6% del área; (2) **foto a sangre + tarjeta hueso** (`build_foto_tarjeta.py`) → se reconoce por el `#FFFDF7` de la tarjeta y se cuenta aparte; (3) **COLLAGE A SANGRE** (aprobado por JR el 2026-09-22, estrenado en el `03_terapias` de «Qué es Understanding Kids») → rejilla de fotos que cubre el lienzo completo, sin un solo píxel de crema/celeste, con el nombre y la bajada en blanco sobre un velo oscuro parejo. Se reconoce por cuatro señales juntas: el color más repetido ocupa <10% del lienzo (una pieza de fondo liso ocupa 57-97%), más de 6.000 colores distintos en la submuestra (huella de fotografía), ≥55% del lienzo bajo el velo, y algo de texto claro pero poco (0,2%-25%). **Un slide así se reporta como `[–] OMITIDO` con el motivo, no como `[✓]`:** en este layout el fondo de marca no existe, así que no hay nada que verificar y decir que está verificado sería mentira. Lo único que sí se revisa es que no haya un bloque del fondo de OTRA marca metido dentro del collage; eso sale en rojo. Un «falso collage» (fondo de color pleno con texto encima) no pasa el filtro de planitud y sigue saliendo en rojo, igual que cualquier pieza normal con el fondo equivocado. **Si aparece un layout a sangre nuevo, se le enseña el formato al verificador — no se le mete una banda crema al arte para contentarlo.**

**Semántica (regla dura):** rojo suave = incorrecto · verde = correcto · amarillo/turquesa = énfasis de marca · celeste = info. Si una comparación no tiene carga (Sesión 1 vs 2), usar neutro gris (`left_kind="neutral"`), no rojo.

**SUBRAYADO DEL REMATE — ARREGLADO EN LA PLANTILLA (2026-10-02):** la barra de acento del `closing_keyword` se mide con JavaScript, y durante meses se midió MAL: el `<script>` inline corría durante el parseo, o sea ANTES de que cargaran la Cocogoose y la Montserrat embebidas en base64 (un `@font-face` se resuelve de forma asíncrona aunque el archivo venga dentro del HTML). Se medía con la tipografía de respaldo, el texto se re-acomodaba al entrar la real y la barra se quedaba con la medida vieja — aparecía corrida a la izquierda, demasiado ancha, o directamente bajo el renglón equivocado. Ahora `build_contenido.py` / `build_contenido_imagen.py` colocan la barra dentro de `document.fonts.ready` y `render()` espera la bandera `window.__subrayadoListo` antes del screenshot (ver `SCRIPT_SUBRAYADO` y `esperar_subrayado()`). Además se mide con `getClientRects()` (un rectángulo por renglón) en vez de `getBoundingClientRect()` (la unión de todos), que era lo que hacía que una keyword partida en dos subrayara la columna entera. **Con la keyword en varias líneas la barra va bajo la ÚLTIMA** — a 40px con `line-height:1.3` no caben 10px de barra entre renglones sin montarse sobre el texto de abajo — y la plantilla **avisa a gritos por consola**: la regla sigue siendo `closing_keyword` de 1–4 palabras en UNA línea, y dos líneas se arregla en el copy del `armar_*.py`, no en la plantilla. **Los artes ya aprobados NO se re-renderizan** (regla dura de corridas pasadas); hay una lista de piezas publicadas con la barra mal puesta pendiente de decisión de JR.

### Composición
- **Una idea por slide.** Si necesita dos párrafos y tres viñetas, son dos slides.
- **Centro óptico, no geométrico:** los bloques centrados suben un poco (la portada usa padding-bottom 100px).
- **El ícono/emoji va en su propia línea**, nunca inline con el titular (indenta la primera línea).
- **Aire:** si un slide se siente lleno, sobra contenido, no falta espacio.
- Alineación: contenido informativo = izquierda; portadas de promo y cierres = centrado.
- **Emojis como íconos:** 1 por slide como marcador de tema + los de tarjetas. Evitar emojis que rendericen con texto/números visibles (📅 muestra "17" — preferir 🗓 u otro).

## 3. Copy

- **Largos:** validados por `reglas_contenido.py` (portada main 4–10 palabras, keyword 1–3 EN UNA LÍNEA, body 15–30, bullets 1–8 c/u, etc. — la tabla completa vive en ese archivo).
- **La keyword de portada es el payoff.** Corta y con golpe. No partir el hook a la mitad: elegir la palabra que duele/ilumina.
- **Tono humano** (regla de JR): nada de "explorar", "descubre", "potencia", "sumérgete" ni lenguaje de AI. Decir "conocer", "aprender", "acompañar". Hablar como Magoo le hablaría a una mamá en la clínica: cálido, claro, sin tecnicismos innecesarios ni tono moralista.
- **Honestidad (regla dura):** cifras, fechas, precios, cupos y estadísticas SOLO si son reales (brief, Canva, Notion o fuente citable). `build_dato.py` avisa fuerte si falta fuente. NUNCA inventar. Si falta un dato → sección DATOS FALTANTES del reporte.
- Captions: gancho primera línea + valor + 1 pregunta o CTA suave + hashtags en español + 💛 ocasional.
- **MÁXIMO 5 hashtags por caption (regla dura, JR 2026-08-05).** Cinco es el techo, no la meta.
- **Nunca un punto pegado antes de un emoji (regla dura, JR 2026-08-05).** ✗ `árbol. 🌳` → ✓ `árbol 🌳`. El punto sobra: el emoji ya cierra la frase. Sí se permiten `?` y `!` antes de emoji (`¿te suena? 👇`), porque ahí el signo carga significado.
- **Guardarraíl:** `verificar_caption.py --todas "<carpeta>"` revisa las dos reglas anteriores en todos los `caption.txt`. Correrlo junto con `verificar_marca.py` antes de reportar.

## 4. Catálogo de plantillas y cuándo usar cada una

| Plantilla | Para | Material visual |
|---|---|---|
| `build_portada` | Hook de apertura | Keyword subrayada |
| `build_contenido` | Título + párrafo (+viñetas) | — |
| `build_contenido_imagen` | Idea + foto real | Foto (usar `img_position` para encuadrar) |
| `build_contenido_frase` | Cita/frase | Comilla gigante |
| `build_infografia` | 3–6 conceptos paralelos | Tarjetas pastel |
| `build_pasos` | Secuencia/progresión | Números conectados |
| `build_comparacion` | Contraste (mito/realidad…) | 2 columnas rojo/verde |
| `build_dato` | UNA cifra real con fuente | Número grande o dona |
| `build_cierre` | CTA final + contacto | Logo por marca |
| `build_promo` | Talleres/cursos (ver guía hermana) | Portada-flyer + paleta propia |
| `build_story` | Historias 1080×1920 | 8 layouts (ver abajo) |

**Historias — 8 layouts y regla de variedad (JR 2026-08-05):** `teaser` (hook centrado + flecha al feed) · `promo` (flyer vertical de taller) · `quote` (cita) · `tip` (consejo que NO está en el post) · `pregunta` (pregunta grande alineada a la izquierda, deja aire abajo para el sticker de encuesta) · `lista` (3-4 puntos numerados, "lo que vas a encontrar") · `bloque` (frase corta dentro de una tarjeta del color de acento **translúcida** — JR 2026-08-05: el acento pleno a ese tamaño resultaba chocante, así que el bloque va al 22% de opacidad (`BLOQUE_ALPHA` en `build_story.py`) con un borde apenas más saturado; **el texto va sólido**, en gris de marca `#33363B`, no en `accent_text_for` — sobre el tinte claro el blanco de IS no se leería) · `foto` (foto a sangre + tarjeta flotante con el titular). **No repetir el mismo layout dos veces en la misma semana, ni en las dos historias de un mismo carrusel** — el motivo del pedido fue que las historias se veían todas iguales. Ojo: `foto` es el único layout a sangre, y por eso `verificar_marca.py` tiene un segundo pase por área (el fondo de marca vive en la tarjeta, no en las esquinas).

**Regla de variedad:** cada carrusel lleva 1–2 slides de material visual, y el TIPO varía entre slides y entre semanas. Las tarjetas de colores NO son obligatorias ni default. Guía: conceptos paralelos→tarjetas · secuencia→pasos · contraste→comparación · situación real→foto · cifra→dato · reflexión→frase.

## 5. Fotos

- `buscar_foto.py` (Pexels primero, Openverse respaldo). Buscar en **inglés**.
- Criterios: **humana, cercana, cálida** — papás/peques en gesto real. Nada de stock corporativo frío ni imágenes abstractas. La foto debe verse como una familia que podría ser cliente.
- **Revisar cada foto descargada** antes de usar (tema, encuadre, temporada — nada navideño en julio). Ajustar encuadre con `img_position` si corta caras o la acción.
- **Ética:** niños/terapias = foto real o stock profesional. NUNCA generar niños con IA.

## 5-bis. PILAR ESTRATÉGICO: autoridad en autismo (JR 2026-07-21)

**Objetivo declarado:** que UK/IS sean reconocidos como **autoridad en autismo**. Esto afecta qué contenido se prioriza, no solo cómo se ve.

**La estrategia es el CRUCE, no el tema genérico — y la puerta de entrada es SENSORIAL.** Medición real con Apify (2026-07-21, 50 reels):

| Hashtag | Mediana de vistas | Máximo |
|---|---:|---:|
| `#integracionsensorial` | **89,546** | **2,970,756** |
| `#autismo` | 16,470 | 44,541 |

El hashtag sensorial rinde **5.4× más en mediana y 67× más en el techo**. Además `#autismo` está saturado (~21 posts cada 13 min) y dominado por contenido en portugués de Brasil, así que lo genérico se entierra en minutos. **Conclusión operativa: para construir autoridad en autismo, entrar por la puerta sensorial** — que además es la ventaja real de la casa. Publicar el contenido de autismo bajo el ángulo sensorial y etiquetarlo en ambos mundos. La autoridad se construye en la **intersección entre autismo y los otros servicios de la casa**, que es justo donde la clínica tiene ventaja real y donde casi nadie trabaja en profundidad:

| Cruce | Ángulo de ejemplo |
|---|---|
| **autismo × integración sensorial** ⭐ | El hueco más grande y nuestra mayor ventaja. "Por qué se tapa los oídos", perfiles sensoriales, sobrecarga |
| autismo × alimentación | Selectividad alimentaria, texturas, la mesa sin batalla |
| autismo × lenguaje | Comunicación no verbal, apoyos visuales, prerrequisitos |
| autismo × emociones | Regulación, meltdown vs berrinche, acompañar la crisis |
| autismo × autonomía | Rutinas, anticipación, historias sociales |
| autismo × juego | Juego compartido, intereses específicos como puerta de entrada |

**Meta operativa:** al menos 1-2 piezas de autismo (o cruce) por ciclo semanal, además de lo que pida el calendario.

**Tono en autismo — no negociable (de esto depende la credibilidad):**
- Marco correcto: **el autismo NO es una enfermedad; es otra forma de percibir, sentir e interactuar.**
- ❌ Nunca: lenguaje de cura/arreglar/combatir/vencer, alarmismo, tragedia, burla, "niño normal" como contraste.
- ✅ Sí: respeto, neurodiversidad, foco en apoyos y comprensión, la conducta como comunicación.
**DECISIONES FIJAS (JR, 2026-07-21) — no volver a preguntar:**
- ✅ **Lenguaje identidad-primero: "niño autista" / "persona autista".** NO "niño con autismo", NO "niño que padece/sufre autismo". Es la forma que prefiere la comunidad autista y la que usamos siempre, en artes y en captions.
- ✅ **Símbolo: el infinito ∞ de neurodiversidad.** **PROHIBIDO el 🧩** (pieza de rompecabezas) en cualquier pieza de UK/IS — está asociado a Autism Speaks y a la idea de "pieza faltante", y parte de la comunidad autista lo rechaza.

### El infinito de UK/IS (activo de marca propio)

No usamos el glifo tipográfico ∞ ni un emoji genérico: es un **símbolo dibujado nuestro** (SVG en `build_contenido.py`). Se usa pasando `"icon": "∞"` en cualquier plantilla — se sustituye solo.

Qué lo hace de la casa:
- **Trazo fino y parejo con remates redondeados** — mismo ADN geométrico redondeado de Cocogoose Pro y del anillo del logo de IS. No es un ∞ grueso de fuente.
- **Lóbulos redondos + el "bump" de la lima**: cada punta lleva una pequeña protuberancia cónica, como el nubcito de la fruta. Se dibuja como una **sucesión de círculos de radio decreciente** (una "pincelada" que se afina): el primero calza exactamente con el grosor del cuerpo, así la unión es invisible y el cono sale continuo, sin escalones.
- **Arcoíris hecho con NUESTRA paleta**, no el arcoíris estándar: terracota `#C0503C` → amarillo UK `#EEB41E` → verde lima IS `#6FAE1C` → turquesa IS `#3FA8C0` → morado `#7A5AA6`. Sigue leyéndose como el símbolo de neurodiversidad, pero los colores son los de la marca.
- **Tamaño emoji** (1.0em): pesa igual que los demás íconos y no descuadra la composición.
### Cómo se usa: SELLO, no ícono (regla JR 2026-07-21)

**En las piezas del pilar de autismo el infinito va como FIRMA discreta en el borde, NO como ícono del slide.** Razón: en el lugar del ícono competía con el titular y además desplazaba al emoji que sí comunica el tema. Como sello dice "esto es contenido nuestro de autismo" sin gritar, y al repetirse siempre en el mismo lugar se vuelve reconocible en el feed — que es justo el objetivo de autoridad.

- Se activa con **`"autismo": True`** en el dict de contenido. El campo `icon` queda libre para el emoji del tema.
- Va **pequeño (46px), centrado, abajo**. En `build_cierre` va **al final de la composición**: en el hueco entre el último texto y la línea que separa los datos de contacto (`pos="bottom:200px"` — al ras de abajo chocaría con esa barra).
- `pos` acepta `"bottom"`, `"top"` o una posición CSS explícita (ej. `"bottom:200px"`) por si alguna plantilla necesita otro punto.
- Ponerlo en **todos los slides** del carrusel de autismo (incluido el cierre): la consistencia es lo que construye el reconocimiento.
- Tamaño ajustable con `_SELLO_ALTO` en `build_contenido.py`.

*(Si alguna vez se quiere el símbolo protagonista en vez de sello, pasar `"icon": "∞"`: se renderiza grande y centrado en su propia línea — es simétrico y ancho, "parece un antifaz", así que a la izquierda pelea con la composición.)*

Para ajustarlo, en `build_contenido.py`: `_ND_GROSOR` (grosor del trazo, **7.0**), `_ND_STOPS` (colores), `_ND_PATH` (forma de los lóbulos) y los del bump — `_ND_NUB_LARGO` (cuánto sobresale, **5.0**), `_ND_NUB_R1` (qué tan fina queda la punta, **1.15**) y `_ND_NUB_PASOS` (suavidad, **14**). `infinito_nd_svg(alto_em=…)` permite pedirlo más grande en piezas especiales.

**Intentos fallidos (para no repetirlos):** integrar el bump al contorno del path ✗ convierte los lóbulos en puntas de hoja · un solo trazo recto ✗ deja escalón · dos trazos superpuestos ✗ suaviza pero aún se nota el salto · alargar los lóbulos tipo elipse ✗ no era lo pedido (JR se refería al bump, no a la silueta). Lo que funciona ✓: **el cono por círculos de radio decreciente** — es la única forma de lograr un ancho variable, porque un trazo SVG tiene grosor constante.

Nota: la campaña del **Diplomado de Autismo (AUT26)** la maneja JR aparte — este pilar es contenido orgánico de posicionamiento, no la campaña.

## 6. Cómo crear una VARIACIÓN o PLANTILLA NUEVA (checklist)

Objetivo del sistema: crecer sin fragmentarse. Antes de codear una plantilla nueva:

1. **¿Ya existe algo que lo resuelve?** Revisar el catálogo (§4). Variar contenido ≠ nueva plantilla.
2. **Hereda el esqueleto:** importar de `build_contenido` (`CANVAS_*`, `MARGIN_X`, `COLOR_*`, fuentes, `accent_for`). Nunca hardcodear colores/fuentes propios.
3. **Respeta las 7 anclas** (lo que NUNCA se toca):
   1. Tipografía Cocogoose Pro + Montserrat
   2. Fondo crema (diario) — solo los promos tienen paleta propia
   3. Acento por marca (amarillo UK / turquesa IS) vía `accent_for()`
   4. Semántica rojo/verde
   5. Márgenes y columna (§2)
   6. Logos y contactos oficiales
   7. Honestidad de datos y ética de fotos
4. **Lo que SÍ se puede variar libremente:** disposición interna, tipo de material visual, uso de tintes pastel, tamaño relativo de elementos, con/sin foto, orientación de tarjetas, cantidad de slides, íconos.
5. **Firma estándar:** `render(content: dict, out_path: str)` con `content["marca"]`, validación con `reglas_contenido` si tiene texto, renderizado Playwright 1080×1350 (o 1920).
6. **Probar con contenido real** de un brief, mirar el PNG con ojo crítico (¿centro óptico? ¿borde izquierdo limpio? ¿se siente de la casa?), y recién entonces usarla.
7. **Documentarla:** una línea en el catálogo (§4) y en la memoria del sistema.

## 7. Contenido viral / tendencias (trabaja con el agente de tendencias)

El agente de tendencias (`uk-tendencias-virales`, corre **lunes y jueves 7am**) deja sugerencias en la base **"🔥 Tendencias"** de Notion. **Alcance (JR 2026-07-21): SOLO Instagram + Facebook, SOLO posts estáticos y carruseles** (nada de reels/TikTok/YouTube). Su misión es detectar **formatos/ángulos que se están replicando entre cuentas — LO ANTES POSIBLE** — para subirse antes de que se saturen (el dolor: llegar tarde a trends como "Haaland de niño hacía X" o el "semáforo de alimentación"). Vigila una lista de **cuentas referentes** (`tendencias_referentes.md`) + barrido de hashtags en IG + momentos culturales por WebSearch. Al generar contenido desde una tendencia **Aprobada**:

- **La tendencia aporta el QUÉ o el FORMATO** (el tema del momento, la estructura del meme, el estilo de video/carrusel que está funcionando). **La línea aporta el CÓMO:** SIEMPRE renderizado con nuestras anclas (§6.3). Un meme viral hecho con Cocogoose, crema y nuestro acento se ve nuestro; un meme copiado tal cual, no.
- **Adaptar, no copiar:** tomar la estructura viral (ej. "expectativa vs realidad", "POV:", "cosas que nadie te dice de…") y llenarla con nuestro contenido de valor (desarrollo infantil, sensorial, crianza).
- **Filtro de marca (brand safety) — descartar tendencias que:** ridiculicen a niños o papás; usen miedo/alarma como gancho; toquen política, religión o polémicas; requieran audio/material con derechos de terceros; envejezcan mal (la clínica es seria: mejor llegar 2 días tarde que quedar mal); o simplemente no tengan traducción natural a nuestro nicho (no forzar).
- Si la tendencia pide un formato que el sistema no cubre (ej. video), reportar "atención manual" — no improvisar fuera del sistema.

## 7-bis. Campañas (identidad propia — NO se mezclan con el contenido diario)

Las campañas (talleres grandes, diplomados, especializaciones) tienen **su propia identidad visual** y no usan la línea diaria (crema/amarillo UK, turquesa IS, sello ∞). Convención fija (JR 2026-07-21):

1. **Cada campaña tiene una entrada "PARÁMETROS DE CAMPAÑA" como primer registro en el Calendario de Artes de Notion** — `Visuals needed`=NO, campo `Campaña` = código (ej. "EDA26 · Especialización Alimentación"). Su **cuerpo es el prompt maestro**: paleta + roles/60-30-10, tipografía, `THEME_*` del motor, highlighter, marca/contactos, y mapeo pieza→plantilla. Es lo PRIMERO que se lee antes de producir cualquier pieza de esa campaña.
2. **Las piezas** de la campaña llevan el campo `Campaña` seteado. El agente las detecta, lee el maestro y aplica ESA identidad — nunca la paleta diaria ni el ∞.
3. **El theme se codifica** en `build_promo.py` como `THEME_<CÓDIGO>`. Activo: **`THEME_EDA26`**.
   **Los valores NO se copian en esta guía.** La paleta, la tipografía, el 60-30-10, el highlighter y las reglas de logos viven en la entrada de PARÁMETROS de esa campaña en Notion, que es la **única fuente**. Acá solo se apunta.
   *Por qué:* esta guía se desincronizó una vez — describía la paleta v1 "Pizarra & Rojo" (#F6F4F1 / #35617A / rojo #D44B45), que **JR rechazó el 10-ago-2026** y reemplazó por **"Azul & Ámbar"** (#F8F8F5 / azul #2E7FA6 / ámbar #F0B024, Fraunces + Hanken Grotesk). El motor y los artes aprobados ya usaban la v2; solo este papel había quedado viejo, y un agente que lo leyera habría pintado la campaña del color equivocado.
   **Si el `THEME_*` del motor y el maestro de Notion no coinciden, manda Notion** y hay que corregir `build_promo.py`.
4. Campañas que JR maneja aparte y sin entrada de parámetros (ej. **AUT26**) → no se generan.

Para crear una campaña nueva: (a) crear su entrada de PARÁMETROS en el calendario; (b) codificar su `THEME_*`; (c) cargar sus piezas con el campo `Campaña`. Guía de la campaña activa en Notion → "Especialización Clínica en Dificultades de la Alimentación 2026 — Campaña".

## 8. Flujo operativo (resumen)

```
Magoo nutre Calendario de Artes (Notion)          Agente de tendencias (jueves)
              │                                    escribe en 🔥 Tendencias
              ▼                                              │ JR/Magoo aprueban
   Corrida semanal (domingo 18:00) ◄─────── lee Aprobadas ───┘
              │  genera carruseles + historias (+caption)
              ▼
   iCloud: ~/Documents/Understanding Kids/Artes/Pendientes de Revision/
              │  JR revisa y dice "aprobadas"
              ▼
   CIERRE: Drive (Administración/Artes/2026/<Marca>/<Tipo>/) → comentario Notion
   + Status Aprobado → mover a Artes/Aprobadas/ → correo a Magoo (msamayoa@)
              │
              ▼
   Magoo publica desde Meta Business Suite (manual, con stickers en historias)
```

Exclusiones fijas: campañas del Diplomado (AUT26) las maneja JR aparte. Reels/video = atención manual.

---

## Doodles — ilustraciones hechas a mano (`doodles.py`) — JR 2026-08-24

Para cuando un arte debe sentirse **más humano y cálido** ("como hecho con crayones de madera", pedido de JR 2026-08-24). Son ilustraciones SVG con un filtro de trazo tembloroso, sobre la paleta de la clínica. Alternativa cálida a los íconos emoji; NO reemplazan la línea diaria, se suman cuando el tema lo pide.

**Módulo:** `doodles.py`. **Tablero de prueba:** `python3 doodles_board.py` (muestra cada doodle en acento UK e IS).

**Catálogo:** `figuras` (dos personitas de la mano, una enredada y una en calma → conexión / pedir apoyo) · `grupo` (tres de la mano → red de apoyo) · `nube` (nube de lluvia sobre una carita → agobio) · `nieve` (bola de nieve cuesta abajo → algo que crece si no se atiende) · `corazon` · `brote` (crecimiento / progreso) · `dialogo` (globo de diálogo → hablar / poner en palabras) · `estrella` (logro).

**Uso:**
- Como SVG dentro de HTML propio (slides custom): `doodles.doodle("figuras", accent=doodles.YEL)` para UK, `accent=doodles.TURQ` para IS.
- Rasterizado a PNG para usarlo como imagen en las plantillas del motor (el `image_path` de `build_contenido_imagen`, los items con imagen de `build_infografia`, etc.): `doodles.to_png("grupo", "out.png", accent=...)` (fondo transparente por defecto).
- **El acento cambia por marca** (amarillo UK / turquesa IS). El trazo es café cálido `#4A3B2F`; rellenos neutros durazno `#F4C89A` y celeste `#DCEBF2`; hojas del brote en verde `#9AC77E`.

**Cómo agregar uno:** escribe una función que arme el `<g>` con paths simples y trazo grueso (~7 sobre viewBox 360×300), regístrala en `DOODLES`, y revísala en `doodles_board.py` (el filtro exagera los detalles finos, así que mantén las formas simples). Cada llamada genera un id de filtro único, así que puedes poner varios doodles en la misma página.

**Referencia de uso completo:** el carrusel "Pedir ayuda no es molestar" (`armar_psico_ado_doodle.py`, 2026-08-24) integra los doodles al look de la clínica (crema + amarillo, Cocogoose + Montserrat, barra de contactos, contenido centrado verticalmente).

---
*Documento vivo. Cada regla nueva que JR apruebe se agrega aquí y a la memoria. Últ. actualización: 2026-08-24.*

## Relacionado

- [[sistema-artes-redes]] — flujo vigente, verificadores y avisos
- [[plantillas-artes]] — una sección por plantilla `build_*.py`
- [[guia-promos-talleres]] — sub-sistema de promos
- [[tendencias-referentes]] — cuentas que vigila el agente de tendencias
- [[understanding-kids]]
- [[integracion-sensorial]]
- [[visual-identity]]
- [[vault-cerebro]]
