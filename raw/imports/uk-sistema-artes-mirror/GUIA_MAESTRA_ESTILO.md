# GUÍA MAESTRA DE ESTILO — Artes UK / IS

**Propósito:** que cualquier arte nuevo — plantilla nueva, variación, formato viral, lo que sea — se pueda crear con libertad **y aún así se vea inconfundiblemente de la casa.** Esta guía define qué es "la línea": qué se puede variar, qué no se toca nunca, y cómo decidir.

Documentos hermanos: `GUIA_PROMOS_TALLERES.md` (sub-sistema de promoción) · `MIGRACION.md` (infraestructura) · `reglas_contenido.py` (largos de copy, ejecutable).

---

## 1. Las dos marcas

| | Understanding Kids (UK) | Integración Sensorial (IS) |
|---|---|---|
| Qué es | Clínica principal | Sub-marca ("by Understanding Kids") |
| **Acento de marca** | 🟡 Amarillo `#EEB41E` | 🔵 Turquesa `#3FA8C0` (del logo) |
| Texto sobre el acento | Café oscuro `#3a2c05` | Blanco `#FFFFFF` |
| Acento secundario | Verde `#76B142` | Verde lima `#6FAE1C` |
| Logo | `logo_uk_b64.txt` | `logo_is_b64.txt` |
| Contactos | FB Understanding Kids · IG @kidsunderstanding · WA +502 5926-9205 · kidsunderstanding.com | **Los mismos de UK, siempre** |

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
| Crema | `#FBFAF6` | Fondo base de todo el sistema diario |
| Gris oscuro | `#33363B` | Texto |
| Amarillo | `#EEB41E` | Acento UK (énfasis, no "bueno") |
| Turquesa | `#3FA8C0` | Acento IS |
| Verde | `#76B142` | **Semántico: positivo/correcto** + resalte emocional |
| Terracota | `#C0503C` píldora / `#F9E6E1` fondo | **Semántico: negativo** (mito, presión, error). Nunca rojo alarma puro |
| Celeste | `#57BAC6` | Informativo/neutro, resalte emocional alternativo |
| Tintes pastel | `#FBEFCF` `#E6F0DD` `#DDEFF2` `#EEEDE7` | Fondos de tarjetas de infografía |
| Gris pie | `#6B6A64` texto / `#E2DFD5` línea | Barra de contacto |

**Semántica (regla dura):** rojo suave = incorrecto · verde = correcto · amarillo/turquesa = énfasis de marca · celeste = info. Si una comparación no tiene carga (Sesión 1 vs 2), usar neutro gris (`left_kind="neutral"`), no rojo.

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
- Captions: gancho primera línea + valor + 1 pregunta o CTA suave + 5 hashtags moderados en español + 💛 ocasional.

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
| `build_story` | Historias 1080×1920 | teaser / promo / quote / tip |

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

El agente de tendencias (`uk-tendencias-virales`, corre jueves) deja sugerencias en la base **"🔥 Tendencias"** de Notion. Al generar contenido desde una tendencia **Aprobada**:

- **La tendencia aporta el QUÉ o el FORMATO** (el tema del momento, la estructura del meme, el estilo de video/carrusel que está funcionando). **La línea aporta el CÓMO:** SIEMPRE renderizado con nuestras anclas (§6.3). Un meme viral hecho con Cocogoose, crema y nuestro acento se ve nuestro; un meme copiado tal cual, no.
- **Adaptar, no copiar:** tomar la estructura viral (ej. "expectativa vs realidad", "POV:", "cosas que nadie te dice de…") y llenarla con nuestro contenido de valor (desarrollo infantil, sensorial, crianza).
- **Filtro de marca (brand safety) — descartar tendencias que:** ridiculicen a niños o papás; usen miedo/alarma como gancho; toquen política, religión o polémicas; requieran audio/material con derechos de terceros; envejezcan mal (la clínica es seria: mejor llegar 2 días tarde que quedar mal); o simplemente no tengan traducción natural a nuestro nicho (no forzar).
- Si la tendencia pide un formato que el sistema no cubre (ej. video), reportar "atención manual" — no improvisar fuera del sistema.

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
   + Status Done → mover a Artes/Aprobadas/ → correo a Magoo (msamayoa@)
              │
              ▼
   Magoo publica desde Meta Business Suite (manual, con stickers en historias)
```

Exclusiones fijas: campañas del Diplomado (AUT26) las maneja JR aparte. Reels/video = atención manual.

---
*Documento vivo. Cada regla nueva que JR apruebe se agrega aquí y a la memoria. Últ. actualización: 2026-07-21.*
