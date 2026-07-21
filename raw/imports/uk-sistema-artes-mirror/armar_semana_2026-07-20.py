"""
ENSAYO de la corrida semanal — piezas del 2026-07-20.
Genera: IS Regulación + UK Autonomía (carrusel + historia teaser cada una).
"""
from pathlib import Path
import build_portada, build_contenido, build_contenido_imagen
import build_infografia, build_pasos, build_comparacion, build_cierre
import build_story

# Re-render post-aprobación: escribe directo en Aprobadas (iCloud de JR)
PEND = Path.home() / "Documents/Understanding Kids/Artes/Aprobadas"

# ============================================================
# PIEZA 1 — IS | Orgánico | Regulación | 20 jul
# ============================================================
OUT = PEND / "2026-07-20 - IS Regulación"

build_portada.render({
    "marca": "IS",
    "icon": "🌀",
    "headline_main": "A veces no es desobediencia:",
    "headline_keyword": "es desregulación",
}, str(OUT / "01_portada.png"))

build_contenido.render({
    "icon": "🧠",
    "heading": "¿Qué es la regulación?",
    "body": "Es la capacidad de mantenernos en calma y organizados frente a lo que pasa alrededor. En los peques está en construcción: por eso a veces el cuerpo se desborda.",
    "bullets": [],
    "closing_pre": "",
    "closing_keyword": "",
}, str(OUT / "02_que_es.png"))

build_infografia.render({
    "icon": "👀",
    "heading": "Señales de que hay sobrecarga",
    "items": [
        {"icon": "🙉", "label": "Se tapa los oídos"},
        {"icon": "🌪️", "label": "Se mueve sin parar"},
        {"icon": "🐚", "label": "Se aísla o se esconde"},
        {"icon": "😤", "label": "Explota «de la nada»"},
    ],
}, str(OUT / "03_senales.png"))

build_pasos.render({
    "marca": "IS",
    "icon": "🤲",
    "heading": "Cómo responder en el momento",
    "steps": [
        "Baja el estímulo: luz, ruido, gente",
        "Ponte a su altura y habla poco",
        "Ofrece un apoyo: abrazo, agua, pausa",
        "Cuando pase, nombren lo que sintió",
    ],
}, str(OUT / "04_como_responder.png"))

build_contenido.render({
    "marca": "IS",
    "icon": "🏠",
    "heading": "Apoyos simples en casa",
    "body": "Pequeños ajustes que ayudan a su cuerpo a organizarse:",
    "bullets": [
        "Rutinas predecibles y avisos antes de los cambios",
        "Un espacio tranquilo para recargar",
        "Juego con movimiento todos los días",
    ],
    "closing_pre": "Comprender es la primera forma de",
    "closing_keyword": "ayudar",
}, str(OUT / "05_apoyos.png"))

build_cierre.render({
    "marca": "IS",
    "heading": "¡Ponte en Contacto con Nosotros!",
    "body_pre": "Si sientes que estos momentos se repiten mucho en casa, ",
    "body_highlight": "no estás solo.",
    "closing": "Escríbenos para conocer cómo podemos acompañar a tu peque.",
}, str(OUT / "06_cierre.png"))

build_story.render_story_teaser({
    "icon": "🌀",
    "headline_main": "A veces no es desobediencia:",
    "headline_keyword": "es desregulación",
}, str(OUT / "story_teaser.png"), marca="IS")

# ============================================================
# PIEZA 2 — UK | Orgánico | Autonomía | 20 jul
# ============================================================
OUT = PEND / "2026-07-20 - UK Autonomía"

build_portada.render({
    "icon": "🌱",
    "headline_main": "La autonomía no aparece sola:",
    "headline_keyword": "se construye",
}, str(OUT / "01_portada.png"))

build_contenido_imagen.render({
    "image_path": str(OUT / "foto.jpg"),
    "img_position": "center 62%",
    "heading": "Participar ya es aprender",
    "body": "Cocinar juntos, poner la mesa, regar las plantas: cuando tu peque participa, practica decidir, coordinar y confiar en sí mismo.",
    "closing_pre": "",
    "closing_keyword": "",
}, str(OUT / "02_participar.png"))

build_comparacion.render({
    "icon": "🤝",
    "heading": "No es hacer por, es hacer con",
    "left_label": "SOBREAYUDA",
    "left_text": "Le resuelvo todo para ir más rápido.",
    "right_label": "ACOMPAÑAR",
    "right_text": "Le doy tiempo y pasos pequeños que sí puede lograr.",
}, str(OUT / "03_hacer_con.png"))

build_infografia.render({
    "icon": "⭐",
    "heading": "Responsabilidades a su medida",
    "items": [
        {"icon": "👕", "label": "Elegir su ropa"},
        {"icon": "🍽️", "label": "Poner la mesa"},
        {"icon": "🧸", "label": "Guardar juguetes"},
        {"icon": "🪴", "label": "Regar las plantas"},
    ],
}, str(OUT / "04_responsabilidades.png"))

build_contenido.render({
    "icon": "💬",
    "heading": "Ofrece elecciones simples",
    "body": "Dos opciones reales bastan:",
    "bullets": [
        "«¿Manzana o banano?»",
        "«¿Te bañas antes o después de cenar?»",
        "«¿Qué cuento leemos hoy?»",
    ],
    "closing_pre": "Decidir en pequeño entrena para",
    "closing_keyword": "decidir en grande",
}, str(OUT / "05_elecciones.png"))

build_cierre.render({
    "heading": "¡Ponte en Contacto con Nosotros!",
    "body_pre": "Si quieres acompañar la independencia de tu peque sin presión, ",
    "body_highlight": "¡este es tu lugar!",
    "closing": "Escríbenos para conocer cómo las asesorías pueden ayudarte.",
}, str(OUT / "06_cierre.png"))

build_story.render_story_teaser({
    "icon": "🌱",
    "headline_main": "La autonomía no aparece sola:",
    "headline_keyword": "se construye",
}, str(OUT / "story_teaser.png"), marca="UK")

print("\nEnsayo 2026-07-20 completo.")
