"""
Corrida semanal — ciclo 2026-08-03, lote 2.

PIEZA 3 — UK | Tip/recomendación | 2026-08-06
    Brief de Magoo escrito slide por slide en Notion ("luz roja en la rutina
    de sueño"). La fila tiene `Visuals needed` SIN marcar, pero es un brief de
    carrusel completo y UK no tenía ninguna pieza esta semana → se genera y se
    reporta como fuera del filtro estricto, para que JR decida.

    Material visual: comparación (2 col) + infografía (tarjetas) + foto real.
    Sin cifras: el brief no trae ninguna y no se inventa.
"""
from pathlib import Path
import build_portada, build_contenido, build_contenido_imagen
import build_infografia, build_comparacion, build_cierre
import build_story

PEND = Path.home() / "Documents/Understanding Kids/Artes/Pendientes de Revision"
OUT = PEND / "2026-08-06 - UK Rutina de sueño (luz roja)"
OUT.mkdir(parents=True, exist_ok=True)

build_portada.render({
    "marca": "UK",
    "icon": "🌙",
    "headline_main": "Un cambio pequeño para dormir mejor:",
    "headline_keyword": "la luz",
}, str(OUT / "01_portada.png"))

build_contenido.render({
    "marca": "UK",
    "icon": "💡",
    "heading": "La luz sí influye",
    "body": "Las luces blancas, frías o azules mantienen al cerebro en modo despierto. "
            "La luz roja tiene menos impacto sobre la melatonina, la hormona que ayuda a dormir.",
    "bullets": [],
    "closing_pre": "",
    "closing_keyword": "",
}, str(OUT / "02_la_luz_influye.png"))

build_comparacion.render({
    "marca": "UK",
    "icon": "💤",
    "heading": "Qué luz usar de noche",
    "left_label": "LUZ BLANCA",
    "left_text": "Las blancas y azules mantienen el cuerpo en modo despierto.",
    "right_label": "LUZ ROJA TENUE",
    "right_text": "Le ayuda a entender que ya es hora de bajar revoluciones.",
}, str(OUT / "03_que_luz.png"))

build_infografia.render({
    "marca": "UK",
    "icon": "🛏",
    "heading": "Úsala en estos momentos",
    "items": [
        {"icon": "🧷", "label": "Cambio de pañal"},
        {"icon": "📚", "label": "El cuento de la noche"},
        {"icon": "🍼", "label": "La toma de la noche"},
        {"icon": "👀", "label": "Si se despierta"},
    ],
}, str(OUT / "04_momentos.png"))

build_contenido_imagen.render({
    "marca": "UK",
    "image_path": str(OUT / "foto.jpg"),
    "img_position": "center 45%",
    "heading": "Sin prender luces fuertes",
    "body": "Con una lamparita roja tenue puedes acompañarlo de noche sin volver "
            "a activar su cuerpo.",
    "closing_pre": "",
    "closing_keyword": "",
}, str(OUT / "05_acompanar.png"))

build_cierre.render({
    "marca": "UK",
    "heading": "No es magia",
    "body_pre": "Es un apoyo simple dentro de una buena rutina: ",
    "body_highlight": "el ambiente también regula.",
    "closing": "Guárdalo para probarlo hoy.",
}, str(OUT / "06_cierre.png"))

build_story.render_story_teaser({
    "icon": "🌙",
    "headline_main": "Un cambio pequeño para dormir mejor:",
    "headline_keyword": "la luz",
}, str(OUT / "story_teaser.png"), marca="UK")

build_story.render_story_tip({
    "icon": "💡",
    "kicker": "Tip de la semana",
    "tip": "Cambia la luz blanca de la noche por una lamparita roja tenue.",
    "note": "Ayuda a que el cuerpo entienda que ya viene la hora de descansar.",
}, str(OUT / "story_tip.png"), marca="UK")

print("\nLote 2 (2026-08-03) completo.")
