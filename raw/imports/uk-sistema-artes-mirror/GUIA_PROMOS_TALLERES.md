# Guía de artes para talleres (promos / publicidad)

Cómo hacer el arte de un taller/curso/diplomado **en esta línea, sin que dos queden idénticos.**
Aplica a Understanding Kids (UK) y a Integración Sensorial (IS) — lo único que cambia entre marcas es el logo.

Motor: `build_promo.py` (sub-sistema de promos, distinto a los artes diarios). Ejemplo completo: `armar_taller_alimentacion.py`.

---

## 1. Lo que NUNCA cambia (anclas de marca)

Aunque cada taller se vea distinto, estas 5 cosas se mantienen siempre — son las que hacen que "se sienta UK/IS":

1. **Tipografía:** Cocogoose Pro Bold (títulos) + Montserrat (cuerpo). Nunca otra.
2. **Logo:** UK o IS según la marca del taller (sticker en portada + grande en el cierre).
3. **Contactos del cierre:** SIEMPRE los de UK, también para IS →
   FB `Understanding Kids` · IG `@kidsunderstanding` · WhatsApp `+502 5926-9205` · web `www.kidsunderstanding.com`.
4. **Disciplina de layout:** márgenes de 70–100px, texto centrado en la promo, jerarquía clara.
5. **Honestidad de datos:** fechas, precio y "qué incluye" reales (del Canva/Notion del taller). Nunca inventar.

## 2. Lo que SÍ cambia en cada taller (para que no sea idéntico)

- **La paleta** → se elige/inventa según el TEMA (ver §4).
- **La foto** → humana, cercana y relevante al público de ESE taller (ver §5).
- **La estructura** → 5 slides base, pero flexible (ver §3).
- **El copy** → hook y textos propios del tema.

## 3. Estructura del carrusel (5 slides base, adaptable)

| # | Slide | Función | Template |
|---|-------|---------|----------|
| 1 | **Portada-flyer** | Se sostiene sola: título + fecha + horario + modalidad + precio + CTA. La mayoría NO hace swipe, así que la info clave va aquí. | `render_cover` |
| 2 | **Foto / contexto** | Encuadra el problema desde nuestro enfoque, con foto real. | `render_foto` |
| 3 | **¿Qué incluye?** | Beneficios de la inscripción (recetario, materiales, diploma…). | `render_incluye` |
| 4 | **Temario / agenda** | Qué se verá (2 columnas si son 2 sesiones). | `render_temario` |
| 5 | **Cierre** | Logo grande + CTA de registro + barra de contacto. | `render_cierre` |

**Variaciones válidas** (para que no sean todos iguales): agregar un slide de *"¿Para quién es?"*, un *testimonio*, o un *bonus*; quitar el temario si es 1 sola sesión; usar ilustración en vez de foto si el tema no tiene foto buena. Mantener siempre portada (1) y cierre (5).

## 4. La portada: la fórmula que la hace verse como afiche (no aviso de oficina)

Aprobada por JR (2026-07-20). Elementos:

- **Foto humana full-bleed arriba** (~720px), cercana al público del taller.
- **Transición fluida:** degradado + **onda orgánica** que funde el pie de la foto con el fondo — nunca un corte recto ni un recuadro.
- **Fondo cálido/frío SUAVE** (no color pleno intenso). El color fuerte del tema va **solo como acento**: badge, título y botón CTA.
- **Logo sticker** (círculo blanco) arriba a la izquierda, sobre la foto.
- **Jerarquía:** badge kicker ("Taller en vivo") → título en Cocogoose → subtítulo corto → **chips** de datos con íconos (fecha/horario/modalidad/precio) → **CTA pill**.

Regla de oro: **si la portada se pudiera publicar sola como un post único, está bien hecha.**

## 5. La foto

- Buscar con `buscar_foto.py` (Pexels), en **inglés**. Ej.: `"mother feeding happy toddler eating"`.
- Debe ser **humana y cercana**: papás/peques, gesto real, cálida. Evitar fotos frías, de stock corporativo o abstractas.
- Ética: para niños/terapias, foto real o stock profesional; **no** generar niños con IA.

## 6. La paleta (esto es lo que más varía)

Se elige **según el tema**. Regla: 2–3 colores + un neutro, elegidos a propósito (cohesivos, con buen contraste), **distintos al crema/amarillo de los artes diarios**.

Paletas ya listas en `build_promo.py` (usar la que aplique o inventar una nueva):

| Tema | Constante | Vibe |
|------|-----------|------|
| Alimentación | `THEME_ALIMENTACION` | Cálida "de apetito": tomate + miel + verde |
| Lenguaje / comunicación | `THEME_LENGUAJE` | Celeste + turquesa + coral |
| Emociones / autoestima | `THEME_EMOCIONES` | Lila suave + durazno |
| Sensorial / juego | `THEME_SENSORIAL` | Verde + naranja + turquesa (colores del logo IS) |
| Sueño / rutinas | `THEME_SUENO` | Azul noche suave + crema |

**Inventar una nueva** es una línea:

```python
from build_promo import make_theme
T = make_theme(
    title="#RRGGBB",     # color fuerte (título, badge, CTA)
    accent="#RRGGBB",    # acento 1
    accent2="#RRGGBB",   # acento 2
    cover_bg="#RRGGBB",  # fondo SUAVE de la portada (versión clara del título)
    chip_border="#RRGGBB",
)
```

## 7. Cómo producir un taller nuevo (paso a paso)

1. Copiar `armar_taller_alimentacion.py` → `armar_taller_<tema>.py`.
2. Elegir/inventar la paleta (`T = THEME_... ` o `make_theme(...)`).
3. Descargar la foto de portada (y las que hagan falta) con `buscar_foto.py`.
4. Rellenar el contenido de cada slide con los **datos reales** del taller (Canva/Notion).
5. `python3 armar_taller_<tema>.py` → PNGs en `~/Documents/Understanding Kids/Artes/Pendientes de Revision/<Marca> - <Taller>/` (iCloud local de JR).
6. **JR revisa y aprueba.**
7. Cierre: copiar a Drive (`Administración/Artes/2026/<Página>/Promociones/<Taller>/`) + comentario en Notion con link + caption + Status→Done + mover la carpeta a `Artes/Aprobadas/` + correo a Magoo.

---
*Doc viva. Actualizar cuando cambien las reglas de marca o se apruebe una mejora al estilo.*
