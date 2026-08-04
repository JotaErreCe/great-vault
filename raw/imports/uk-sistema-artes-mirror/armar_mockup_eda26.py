"""
MOCKUPS de identidad visual — Campaña EDA26 (Especialización Dificultades de la
Alimentación). Solo para referencia visual de JR: paleta terracota/miel/salvia +
Cocogoose/Montserrat, con texto Lorem Ipsum. NO es contenido final.
"""
from pathlib import Path
import build_promo as P

# Paleta EDA26 (propuesta de la guía de campaña)
T = P.make_theme(
    title="#35617A",      # azul pizarra (primario/títulos)
    accent="#D44B45",     # rojo (acento: tarjetas, subrayados, temario)
    accent2="#6E8FA0",    # pizarra claro (segundo tono para variedad)
    cover_bg="#F6F4F1",   # fondo claro cálido
    chip_border="#E4DED6",
    bg="#F6F4F1",         # interior
    text="#263039",       # gris pizarra
    muted="#7A8590",
)
T["cta"] = "#D44B45"      # CTA y badge en rojo (color firma)

OUT = Path.home() / ("Library/CloudStorage/GoogleDrive-jcastaneda@kidsunderstanding.com/"
                     "My Drive/Administración/Artes/2026/Campañas/"
                     "Especialización Alimentación 2026 - Mockups")

LOREM = "Lorem ipsum dolor sit amet, consectetur adipiscing elit sed do eiusmod tempor."

# 1 — ANUNCIO (cover-flyer)
P.render_cover({
    "image_path": str(OUT / "cover_foto.jpg"),
    "badge": "Especialización clínica",
    "title": "Dificultades de la Alimentación",
    "subtitle": "Lorem ipsum dolor sit amet consectetur.",
    "rows": [
        {"icon": "📅", "value": "Lorem 5 oct – 14 dic"},
        {"icon": "🕕", "value": "Lorem 6:00 – 8:00 pm"},
        {"icon": "💻", "value": "Lorem virtual en vivo"},
        {"icon": "🎓", "value": "Lorem 11 sesiones"},
    ],
    "cta": "Regístrate",
}, T, str(OUT / "01_anuncio.png"), marca="UK")

# 2 — QUÉ VAS A DOMINAR (tarjetas)
P.render_incluye({
    "heading": "🍽️ Lorem ipsum dolor sit",
    "items": [
        {"icon": "🔎", "label": "Lorem ipsum evaluación"},
        {"icon": "🧩", "label": "Lorem dolor sensorial"},
        {"icon": "🥄", "label": "Lorem sit intervención"},
        {"icon": "🏠", "label": "Lorem amet estrategias"},
    ],
}, T, str(OUT / "02_dominar.png"))

# 3 — TEMARIO (dos columnas, muestra)
P.render_temario({
    "heading": "📚 Lorem ipsum del temario",
    "sessions": [
        {"label": "MÓDULO 1", "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit sed do."},
        {"label": "MÓDULO 2", "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit sed do."},
    ],
}, T, str(OUT / "03_temario.png"))

# 4 — CIERRE / CTA
P.render_cierre({
    "marca": "UK",
    "heading": "Lorem ipsum dolor sit",
    "body_pre": "Lorem ipsum dolor sit amet consectetur adipiscing, ",
    "body_highlight": "regístrate hoy.",
    "closing": "Lorem ipsum dolor sit amet consectetur.",
}, T, {
    "facebook": "Understanding Kids",
    "instagram": "@kidsunderstanding",
    "whatsapp": "+502 5926-9205",
    "web": "www.kidsunderstanding.com",
}, str(OUT / "04_cierre.png"), marca="UK")

print("Mockups EDA26 listos en:", OUT)
