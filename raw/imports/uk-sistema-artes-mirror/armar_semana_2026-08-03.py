"""
Corrida semanal — piezas del ciclo 2026-08-03.

PIEZA 1 — IS | Orgánico | Regulación | 2026-08-06
    Ángulo nuevo (el bucket "Regulación" ya se trabajó en general el 20-jul):
    la explosión al llegar a casa después de la escuela.

PIEZA 2 — IS | Orgánico | Mitos y realidades | 2026-08-07
    Ángulo nuevo (el 23-jul se hicieron mitos generales de IS):
    cruce autismo × integración sensorial. Pilar de autoridad en autismo —
    sello ∞ en todos los slides, lenguaje identidad-primero.
"""
from pathlib import Path
import shutil
import build_portada, build_contenido, build_contenido_imagen
import build_pasos, build_comparacion, build_cierre
import build_story

PEND = Path.home() / "Documents/Understanding Kids/Artes/Pendientes de Revision"

# ============================================================
# PIEZA 1 — IS | Regulación | 2026-08-06
# ============================================================
OUT = PEND / "2026-08-06 - IS Regulación (al salir de la escuela)"
OUT.mkdir(parents=True, exist_ok=True)

build_portada.render({
    "marca": "IS",
    "icon": "🎒",
    "headline_main": "En la escuela, todo bien. En casa,",
    "headline_keyword": "explota",
}, str(OUT / "01_portada.png"))

build_contenido.render({
    "marca": "IS",
    "icon": "🔋",
    "heading": "Aguantó todo el día",
    "body": "Ruido, luces, filas, cambios de clase. Su cuerpo estuvo conteniéndose durante horas para poder funcionar. Al llegar a casa por fin puede soltar.",
    "bullets": [],
    "closing_pre": "",
    "closing_keyword": "",
}, str(OUT / "02_aguanto.png"))

build_comparacion.render({
    "marca": "IS",
    "icon": "💛",
    "heading": "No se porta peor contigo",
    "left_label": "LO QUE PARECE",
    "left_text": "«Conmigo se porta peor que con todos.»",
    "right_label": "LO QUE PASA",
    "right_text": "Contigo se siente seguro para soltar lo que aguantó.",
}, str(OUT / "03_contigo.png"))

build_pasos.render({
    "marca": "IS",
    "icon": "🤲",
    "heading": "Al recogerlo, prueba esto",
    "steps": [
        "Saluda con calma y habla poco",
        "Deja las preguntas del día para después",
        "Agua, algo de comer, ropa cómoda",
        "Movimiento o un rato en silencio",
    ],
}, str(OUT / "04_al_recogerlo.png"))

build_contenido_imagen.render({
    "marca": "IS",
    "image_path": str(OUT / "foto.jpg"),
    "img_position": "center 38%",
    "heading": "El reencuentro también cuenta",
    "body": "Bajar el ritmo al recogerlo le da a su cuerpo un respiro antes de la siguiente exigencia del día.",
    "closing_pre": "",
    "closing_keyword": "",
}, str(OUT / "05_reencuentro.png"))

build_cierre.render({
    "marca": "IS",
    "heading": "Comprender cambia todo",
    "body_pre": "Cuando entendemos qué hay detrás de esa explosión, ",
    "body_highlight": "dejamos de pelear con ella.",
    "closing": "Guárdalo para los días difíciles.",
}, str(OUT / "06_cierre.png"))

build_story.render_story_teaser({
    "icon": "🎒",
    "headline_main": "En la escuela, todo bien. En casa,",
    "headline_keyword": "explota",
}, str(OUT / "story_teaser.png"), marca="IS")

build_story.render_story_tip({
    "icon": "🤲",
    "kicker": "Tip de la semana",
    "tip": "Al recogerlo, habla poco los primeros minutos.",
    "note": "Las preguntas sobre el día pueden esperar a que su cuerpo baje revoluciones.",
}, str(OUT / "story_tip.png"), marca="IS")

# ============================================================
# PIEZA 2 — IS | Mitos y realidades | 2026-08-07  (autismo × sensorial)
# ============================================================
OUT2 = PEND / "2026-08-07 - IS Mitos y realidades (autismo y sensorial)"
OUT2.mkdir(parents=True, exist_ok=True)

FOTO2 = OUT2 / "foto.jpg"
if not FOTO2.exists():
    shutil.copy(
        "/private/tmp/claude-501/-Users-jotaerre-Claude/8c11e058-b04a-4725-afce-9ba0bc7979ad/scratchpad/foto_mitos.jpg",
        FOTO2,
    )

build_portada.render({
    "marca": "IS",
    "autismo": True,
    "icon": "🔍",
    "headline_main": "No todo lo que dicen del autismo",
    "headline_keyword": "es cierto",
}, str(OUT2 / "01_portada.png"))

build_contenido.render({
    "marca": "IS",
    "autismo": True,
    "icon": "🧠",
    "heading": "El punto de partida",
    "body": "El autismo no es una enfermedad: es otra forma de percibir el mundo. Muchas conductas que se malinterpretan son, en realidad, respuestas sensoriales.",
    "bullets": [],
    "closing_pre": "",
    "closing_keyword": "",
}, str(OUT2 / "02_punto_de_partida.png"))

build_comparacion.render({
    "marca": "IS",
    "autismo": True,
    "icon": "👂",
    "heading": "Taparse los oídos",
    "left_label": "MITO",
    "left_text": "«Lo hace para llamar la atención.»",
    "right_label": "REALIDAD",
    "right_text": "El ruido le resulta físicamente incómodo. Se está protegiendo.",
}, str(OUT2 / "03_mito_oidos.png"))

build_comparacion.render({
    "marca": "IS",
    "autismo": True,
    "icon": "🍽️",
    "heading": "Comer siempre lo mismo",
    "left_label": "MITO",
    "left_text": "«Está consentido, come lo que quiere.»",
    "right_label": "REALIDAD",
    "right_text": "Texturas, olores y temperaturas pueden ser demasiado para su sistema.",
}, str(OUT2 / "04_mito_comida.png"))

build_comparacion.render({
    "marca": "IS",
    "autismo": True,
    "icon": "🔄",
    "heading": "Moverse o repetir gestos",
    "left_label": "MITO",
    "left_text": "«Hay que quitarle esa manía.»",
    "right_label": "REALIDAD",
    "right_text": "Ese movimiento lo regula. Quitárselo lo deja sin su herramienta.",
}, str(OUT2 / "05_mito_movimiento.png"))

build_contenido_imagen.render({
    "marca": "IS",
    "autismo": True,
    "image_path": str(FOTO2),
    "img_position": "center 45%",
    "heading": "Lo que sí ayuda",
    "body": "Observar qué le resulta demasiado, ajustar el ambiente y confiar en que su conducta está comunicando algo real.",
    "closing_pre": "",
    "closing_keyword": "",
}, str(OUT2 / "06_lo_que_ayuda.png"))

build_cierre.render({
    "marca": "IS",
    "autismo": True,
    "heading": "Entender antes que corregir",
    "body_pre": "Cuando dejamos de leer la conducta como desobediencia y empezamos a leerla como comunicación, ",
    "body_highlight": "todo se vuelve más fácil.",
    "closing": "Compártelo con quien necesite leerlo.",
}, str(OUT2 / "07_cierre.png"))

build_story.render_story_teaser({
    "icon": "🔍",
    "headline_main": "No todo lo que dicen del autismo",
    "headline_keyword": "es cierto",
}, str(OUT2 / "story_teaser.png"), marca="IS")

print("\nCorrida 2026-08-03 completa.")
