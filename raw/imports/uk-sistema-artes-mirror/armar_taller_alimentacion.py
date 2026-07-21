"""
Carrusel de PROMOCIÓN (v2 — sub-sistema de promos con portada-flyer + paleta propia)
Integración Sensorial — Taller: "Dificultades en la Alimentación"

Cambios vs v1 (feedback JR 2026-07-19):
- La PORTADA ahora es un flyer completo (fecha/horario/modalidad/precio/CTA) — no
  hace falta swipe para enterarse.
- Paleta propia "de apetito" (tomate/miel/verde), no la crema/amarillo diaria.
- Anclas fijas: Cocogoose, layout, logo IS.

5 slides: portada-flyer -> foto/contexto -> qué incluye -> temario -> cierre.
Datos idénticos al Canva/Notion (ejercicio; el taller no se hará pronto).
"""
from pathlib import Path
import build_promo as P

T = P.THEME_ALIMENTACION
OUT = Path("../Pendientes de Revision/IS - Taller Dificultades en la Alimentacion")

CONTACT_IS = {
    "facebook": "Understanding Kids",
    "instagram": "@kidsunderstanding",
    "whatsapp": "+502 5926-9205",
    "web": "www.kidsunderstanding.com",
}

# 1 — PORTADA-FLYER (afiche editorial con foto humana; se sostiene sola)
P.render_cover({
    "image_path": str(OUT / "portada_foto.jpg"),
    "badge": "Taller en vivo",
    "title": "Dificultades en la Alimentación",
    "subtitle": "Herramientas para acompañar a tu peque a la hora de comer.",
    "rows": [
        {"icon": "📅", "value": "6 y 7 de agosto"},
        {"icon": "🕡", "value": "6:30 – 8:30 pm"},
        {"icon": "💻", "value": "Virtual · en vivo"},
        {"icon": "🎟️", "value": "Q499 / USD 65"},
    ],
    "cta": "Regístrate ahora",
}, T, str(OUT / "01_portada.png"))

# 2 — FOTO + CONTEXTO
P.render_foto({
    "image_path": str(OUT / "foto.jpg"),
    "heading": "No siempre es solo maña",
    "body": "Detrás de rechazar ciertos alimentos suele haber una causa sensorial que sí se puede entender y acompañar.",
    "closing_pre": "Y este taller es para",
    "closing_keyword": "aprender cómo",
}, T, str(OUT / "02_contexto.png"))

# 3 — ¿QUÉ INCLUYE?
P.render_incluye({
    "heading": "🎁 ¿Qué incluye tu inscripción?",
    "items": [
        {"icon": "📖", "label": "Recetario e-book"},
        {"icon": "🧩", "label": "Juegos sensoriales"},
        {"icon": "🎓", "label": "Diploma de participación"},
    ],
}, T, str(OUT / "03_incluye.png"))

# 4 — TEMARIO (2 sesiones)
P.render_temario({
    "heading": "📅 ¿Qué veremos en las 2 sesiones?",
    "sessions": [
        {"label": "SESIÓN 1", "text": "Qué es la integración sensorial y cómo se relaciona con la alimentación."},
        {"label": "SESIÓN 2", "text": "Señales de alerta, incluir nuevos alimentos y una relación positiva con la comida."},
    ],
}, T, str(OUT / "04_temario.png"))

# 5 — CIERRE
P.render_cierre({
    "heading": "¡Regístrate ahora!",
    "body_pre": "Si buscas la mejor forma de acompañar a tu peque con la comida, ",
    "body_highlight": "este es tu lugar.",
    "closing": "Escríbenos y aparta tu espacio en el taller.",
}, T, CONTACT_IS, str(OUT / "05_cierre.png"))

# Limpia los PNG de la v1 que ya no aplican (nombres viejos)
for old in ["02_puente.png", "03_flyer.png", "04_incluye.png", "05_temario.png", "06_cierre.png"]:
    (OUT / old).unlink(missing_ok=True)

print("\nCarrusel promo v2 listo en:", OUT)
