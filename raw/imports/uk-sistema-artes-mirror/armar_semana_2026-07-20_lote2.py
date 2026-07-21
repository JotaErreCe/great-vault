"""
Corrida semanal 2026-07-20 — LOTE 2: las 6 piezas orgánicas restantes (23–30 jul).
AUT26/Diplomado EXCLUIDO (JR las hace por otro lado).
"""
from pathlib import Path
import build_portada, build_contenido, build_contenido_imagen, build_contenido_frase
import build_infografia, build_pasos, build_comparacion, build_cierre
import build_story

# Re-render post-aprobación: escribe directo en Aprobadas (iCloud de JR)
PEND = Path.home() / "Documents/Understanding Kids/Artes/Aprobadas"

# ============================================================
# IS | Mitos y realidades | 23 jul
# ============================================================
OUT = PEND / "2026-07-23 - IS Mitos y realidades"

build_portada.render({
    "marca": "IS",
    "icon": "🔍",
    "headline_main": "No todo lo que escuchas",
    "headline_keyword": "es cierto",
}, str(OUT / "01_portada.png"))

build_contenido.render({
    "icon": "💬",
    "heading": "Hablemos de integración sensorial",
    "body": "Circulan muchas ideas sobre cómo sienten y procesan el mundo los peques. Hoy desarmamos tres de las más comunes, con información clara y aplicable.",
    "bullets": [],
    "closing_pre": "",
    "closing_keyword": "",
}, str(OUT / "02_intro.png"))

build_comparacion.render({
    "icon": "🧩",
    "heading": "«Es muy sensible, ya se le pasará»",
    "left_label": "MITO",
    "left_text": "El tiempo lo resuelve solo.",
    "right_label": "REALIDAD",
    "right_text": "Con apoyo adecuado, aprende a procesar mejor lo que siente.",
}, str(OUT / "03_mito1.png"))

build_comparacion.render({
    "icon": "😤",
    "heading": "«Solo está malcriado»",
    "left_label": "MITO",
    "left_text": "Se porta así para manipular.",
    "right_label": "REALIDAD",
    "right_text": "Muchas veces es sobrecarga sensorial, no mala conducta.",
}, str(OUT / "04_mito2.png"))

build_comparacion.render({
    "icon": "🎈",
    "heading": "«La terapia es solo juego»",
    "left_label": "MITO",
    "left_text": "Ahí solo llegan a jugar.",
    "right_label": "REALIDAD",
    "right_text": "El juego es la vía con la que el cerebro aprende y se organiza.",
}, str(OUT / "05_mito3.png"))

build_cierre.render({
    "marca": "IS",
    "heading": "¡Ponte en Contacto con Nosotros!",
    "body_pre": "Si alguna de estas ideas te sonó conocida, ",
    "body_highlight": "hablemos.",
    "closing": "Escríbenos y resolvamos tus dudas con información clara.",
}, str(OUT / "06_cierre.png"))

build_story.render_story_teaser({
    "icon": "🔍",
    "headline_main": "No todo lo que escuchas",
    "headline_keyword": "es cierto",
}, str(OUT / "story_teaser.png"), marca="IS")

# ============================================================
# UK | Acompañamiento emocional | 23 jul
# ============================================================
OUT = PEND / "2026-07-23 - UK Acompañamiento emocional"

build_portada.render({
    "icon": "🫂",
    "headline_main": "A veces no hay que corregir,",
    "headline_keyword": "sino comprender",
}, str(OUT / "01_portada.png"))

build_contenido_imagen.render({
    "image_path": str(OUT / "foto.jpg"),
    "img_position": "center 18%",
    "heading": "Primero conexión, luego dirección",
    "body": "Cuando la emoción es grande, tu calma es su ancla. Antes que el sermón, tu peque necesita saber que estás ahí.",
    "closing_pre": "",
    "closing_keyword": "",
}, str(OUT / "02_conexion.png"))

build_contenido.render({
    "icon": "🌊",
    "heading": "La regulación compartida",
    "body": "Los peques aprenden a calmarse prestando de nuestra calma. No es dejarlos solos con lo que sienten, sino sentirlo con ellos hasta que baje la ola.",
    "bullets": [],
    "closing_pre": "",
    "closing_keyword": "",
}, str(OUT / "03_regulacion.png"))

build_contenido.render({
    "icon": "💬",
    "heading": "Frases que validan",
    "body": "Palabras sencillas que abren puerta:",
    "bullets": [
        "«Estoy aquí contigo»",
        "«Es válido sentirse así»",
        "«¿Quieres un abrazo o un momento?»",
    ],
    "closing_pre": "Validar no es ceder: es",
    "closing_keyword": "acompañar",
}, str(OUT / "04_frases.png"))

build_contenido_frase.render({
    "quote": "Las emociones no se corrigen: se acompañan.",
    "author": "Equipo Understanding Kids",
    "context": "",
}, str(OUT / "05_frase.png"))

build_cierre.render({
    "heading": "¡Ponte en Contacto con Nosotros!",
    "body_pre": "Si esos momentos intensos se sienten cuesta arriba, ",
    "body_highlight": "no estás solo.",
    "closing": "Escríbenos para conocer cómo acompañarte en este proceso.",
}, str(OUT / "06_cierre.png"))

build_story.render_story_teaser({
    "icon": "🫂",
    "headline_main": "A veces no hay que corregir,",
    "headline_keyword": "sino comprender",
}, str(OUT / "story_teaser.png"), marca="UK")

# ============================================================
# IS | Estrategias para casa | 27 jul
# ============================================================
OUT = PEND / "2026-07-27 - IS Estrategias para casa"

build_portada.render({
    "marca": "IS",
    "icon": "🏠",
    "headline_main": "Pequeños cambios en casa hacen",
    "headline_keyword": "gran diferencia",
}, str(OUT / "01_portada.png"))

build_contenido_imagen.render({
    "image_path": str(OUT / "foto.jpg"),
    "heading": "Un rincón para recargar",
    "body": "Un espacio pequeño con cojines y poca luz le da a tu peque un lugar seguro donde volver a la calma.",
    "closing_pre": "",
    "closing_keyword": "",
}, str(OUT / "02_rincon.png"))

build_infografia.render({
    "icon": "🎛️",
    "heading": "Ajustes que ayudan",
    "items": [
        {"icon": "💡", "label": "Luz más suave"},
        {"icon": "🔇", "label": "Menos ruido de fondo"},
        {"icon": "🧺", "label": "Orden visual simple"},
        {"icon": "🛋️", "label": "Espacio de calma"},
    ],
}, str(OUT / "03_ajustes.png"))

build_pasos.render({
    "marca": "IS",
    "icon": "⏰",
    "heading": "Anticipa los cambios",
    "steps": [
        "Avisa antes: «en 5 minutos guardamos»",
        "Muestra qué viene después",
        "Dale un rol: «tú apagas la luz»",
    ],
}, str(OUT / "04_anticipar.png"))

build_contenido.render({
    "marca": "IS",
    "icon": "🔄",
    "heading": "Rutinas que sostienen",
    "body": "La previsibilidad calma:",
    "bullets": [
        "Mismos pasos antes de dormir",
        "Juego con movimiento cada día",
        "Pausas tranquilas entre actividades",
    ],
    "closing_pre": "Lo simple, repetido, se vuelve",
    "closing_keyword": "seguridad",
}, str(OUT / "05_rutinas.png"))

build_cierre.render({
    "marca": "IS",
    "heading": "¡Ponte en Contacto con Nosotros!",
    "body_pre": "Si quieres estrategias pensadas justo para tu peque, ",
    "body_highlight": "aquí estamos.",
    "closing": "Escríbenos y armemos juntos un plan para casa.",
}, str(OUT / "06_cierre.png"))

build_story.render_story_teaser({
    "icon": "🏠",
    "headline_main": "Pequeños cambios en casa hacen",
    "headline_keyword": "gran diferencia",
}, str(OUT / "story_teaser.png"), marca="IS")

build_story.render_story_tip({
    "kicker": "Tip extra",
    "icon": "🎒",
    "tip": "Antes de salir de casa, cuéntale a dónde van y qué va a pasar.",
    "note": "La anticipación baja la ansiedad y evita muchas batallas.",
}, str(OUT / "story_tip.png"), marca="IS")

# ============================================================
# UK | Desarrollo | 27 jul
# ============================================================
OUT = PEND / "2026-07-27 - UK Desarrollo"

build_portada.render({
    "icon": "🧭",
    "headline_main": "No todo retraso es alarma:",
    "headline_keyword": "aprende a observar",
}, str(OUT / "01_portada.png"))

build_contenido.render({
    "icon": "📈",
    "heading": "Cada peque, su ritmo",
    "body": "El desarrollo se mueve en rangos, no en fechas exactas. Dos peques sanos pueden lograr lo mismo con meses de diferencia y ambos ir perfectamente bien.",
    "bullets": [],
    "closing_pre": "",
    "closing_keyword": "",
}, str(OUT / "02_ritmo.png"))

build_comparacion.render({
    "icon": "⚖️",
    "heading": "Observar sin comparar",
    "left_label": "COMPARAR",
    "left_text": "«El primo ya habla y él no».",
    "right_label": "OBSERVAR",
    "right_text": "«¿Qué logró este mes que antes no hacía?»",
}, str(OUT / "03_comparar.png"))

build_pasos.render({
    "icon": "📝",
    "heading": "Cómo observar con criterio",
    "steps": [
        "Mira tendencias, no días sueltos",
        "Anota los logros nuevos del mes",
        "Compáralo solo consigo mismo",
        "Si la duda persiste, consulta",
    ],
}, str(OUT / "04_criterio.png"))

build_contenido.render({
    "icon": "🚩",
    "heading": "Cuándo sí consultar",
    "body": "Estas señales merecen una mirada profesional:",
    "bullets": [
        "Pierde habilidades que ya tenía",
        "Conecta poco con miradas y juegos",
        "Tu intuición te dice que algo pasa",
    ],
    "closing_pre": "Consultar a tiempo no es alarmarse:",
    "closing_keyword": "es cuidar",
}, str(OUT / "05_consultar.png"))

build_cierre.render({
    "heading": "¡Ponte en Contacto con Nosotros!",
    "body_pre": "Si tienes dudas sobre el desarrollo de tu peque, ",
    "body_highlight": "estamos para ti.",
    "closing": "Escríbenos y démosle claridad a esas preguntas.",
}, str(OUT / "06_cierre.png"))

build_story.render_story_teaser({
    "icon": "🧭",
    "headline_main": "No todo retraso es alarma:",
    "headline_keyword": "aprende a observar",
}, str(OUT / "story_teaser.png"), marca="UK")

# ============================================================
# IS | Alimentación | 30 jul
# ============================================================
OUT = PEND / "2026-07-30 - IS Alimentación"

build_portada.render({
    "marca": "IS",
    "icon": "🥦",
    "headline_main": "No todo rechazo a la comida",
    "headline_keyword": "es maña",
}, str(OUT / "01_portada.png"))

build_contenido.render({
    "icon": "👅",
    "heading": "Comer es un reto sensorial",
    "body": "Texturas, olores, temperaturas y sabores llegan todos al mismo tiempo. Para algunos peques esa mezcla es demasiado, y rechazar es su forma de protegerse.",
    "bullets": [],
    "closing_pre": "",
    "closing_keyword": "",
}, str(OUT / "02_sensorial.png"))

build_infografia.render({
    "icon": "🔎",
    "heading": "Lo que puede haber detrás",
    "items": [
        {"icon": "👅", "label": "Texturas difíciles"},
        {"icon": "👃", "label": "Olores intensos"},
        {"icon": "🦷", "label": "Masticar aún cuesta"},
        {"icon": "😟", "label": "Experiencias pasadas"},
    ],
}, str(OUT / "03_detras.png"))

build_comparacion.render({
    "icon": "🍽️",
    "heading": "Presionar no es lo mismo que invitar",
    "left_label": "PRESIONAR",
    "left_text": "«Un bocado más o no te levantas».",
    "right_label": "INVITAR",
    "right_text": "«Está en tu plato, pruébalo si quieres».",
}, str(OUT / "04_presion.png"))

build_contenido.render({
    "marca": "IS",
    "icon": "🤲",
    "heading": "Cómo apoyar sin presión",
    "body": "Pasos pequeños, sin batalla:",
    "bullets": [
        "Deja que toque y explore la comida",
        "Invítalo a cocinar contigo",
        "Respeta cuando dice basta",
    ],
    "closing_pre": "La confianza con la comida se",
    "closing_keyword": "construye",
}, str(OUT / "05_apoyar.png"))

build_cierre.render({
    "marca": "IS",
    "heading": "¡Ponte en Contacto con Nosotros!",
    "body_pre": "Si la hora de comer se volvió batalla, ",
    "body_highlight": "podemos ayudarte.",
    "closing": "Escríbenos para conocer cómo acompañamos la alimentación.",
}, str(OUT / "06_cierre.png"))

build_story.render_story_teaser({
    "icon": "🥦",
    "headline_main": "No todo rechazo a la comida",
    "headline_keyword": "es maña",
}, str(OUT / "story_teaser.png"), marca="IS")

# ============================================================
# UK | Lenguaje | 30 jul
# ============================================================
OUT = PEND / "2026-07-30 - UK Lenguaje"

build_portada.render({
    "icon": "🗣️",
    "headline_main": "Antes de hablar pasan muchas",
    "headline_keyword": "cosas importantes",
}, str(OUT / "01_portada.png"))

build_contenido.render({
    "icon": "👶",
    "heading": "El lenguaje empieza sin palabras",
    "body": "Mucho antes de la primera palabra, tu peque ya se comunica: con miradas, gestos, sonidos y turnos de juego. Esa base lo es todo.",
    "bullets": [],
    "closing_pre": "",
    "closing_keyword": "",
}, str(OUT / "02_base.png"))

build_infografia.render({
    "icon": "🧱",
    "heading": "Los cimientos del lenguaje",
    "items": [
        {"icon": "👀", "label": "Contacto visual"},
        {"icon": "👉", "label": "Señalar lo que quiere"},
        {"icon": "🔁", "label": "Imitación de sonidos"},
        {"icon": "🎯", "label": "Atención compartida"},
    ],
}, str(OUT / "03_cimientos.png"))

build_comparacion.render({
    "icon": "💬",
    "heading": "Apoyar sin presionar",
    "left_label": "PRESIÓN",
    "left_text": "«Di agua. A ver, di a-gua».",
    "right_label": "MODELAR",
    "right_text": "«¿Quieres agua? Agua fresquita»… y esperar.",
}, str(OUT / "04_modelar.png"))

build_contenido.render({
    "icon": "🏡",
    "heading": "En casa, todos los días",
    "body": "El mejor estímulo es la vida diaria:",
    "bullets": [
        "Narra lo que van haciendo",
        "Dale tiempo para responder",
        "Canten y lean juntos",
    ],
    "closing_pre": "Hablarle hoy es regalarle",
    "closing_keyword": "palabras mañana",
}, str(OUT / "05_en_casa.png"))

build_cierre.render({
    "heading": "¡Ponte en Contacto con Nosotros!",
    "body_pre": "Si el lenguaje de tu peque te genera dudas, ",
    "body_highlight": "¡este es tu lugar!",
    "closing": "Escríbenos para conocer cómo la terapia de lenguaje ayuda.",
}, str(OUT / "06_cierre.png"))

build_story.render_story_teaser({
    "icon": "🗣️",
    "headline_main": "Antes de hablar pasan muchas",
    "headline_keyword": "cosas importantes",
}, str(OUT / "story_teaser.png"), marca="UK")

print("\nLote 2 completo: 6 piezas orgánicas (23–30 jul).")
