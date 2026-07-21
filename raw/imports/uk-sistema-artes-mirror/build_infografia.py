"""
Template reutilizable: Slide de INFOGRAFÍA / diagrama de conceptos.
Una grilla de tarjetas (ícono + etiqueta corta) para mostrar visualmente
un conjunto de conceptos relacionados: "las 4 habilidades", "señales", etc.
Dibujado por código — on-brand, sin datos inventados (no afirma estadísticas).

Uso: python3 build_infografia.py
"""
from playwright.sync_api import sync_playwright
from pathlib import Path
from reglas_contenido import validar

from build_contenido import (
    BASE_DIR, CANVAS_W, CANVAS_H, MARGIN_X,
    COLOR_BG, COLOR_TEXT, COCOGOOSE_B64, MONTSERRAT_B64, inyectar_sello,
)

HEADING_SIZE = 54
CARD_ICON_SIZE = 66
CARD_LABEL_SIZE = 30

# Tintes suaves de marca (categóricos — un color por tarjeta, rota en orden)
CARD_TINTS = ["#FBEFCF", "#E6F0DD", "#DDEFF2", "#EEEDE7"]

CONTENT = {
    "icon": "🍽️",
    "heading": "La alimentación necesita muchas habilidades",
    "items": [
        {"icon": "✋", "label": "Motricidad fina"},
        {"icon": "👅", "label": "Motoras orales"},
        {"icon": "🦷", "label": "Masticación"},
        {"icon": "🧠", "label": "Coordinación"},
    ],
}


def build_html(content: dict) -> str:
    cards = ""
    for i, item in enumerate(content["items"]):
        tint = CARD_TINTS[i % len(CARD_TINTS)]
        cards += f"""
        <div class="card" style="background:{tint}">
          <div class="card-icon">{item['icon']}</div>
          <div class="card-label">{item['label']}</div>
        </div>"""

    # 1 columna si hay <=2 items o si algún label es largo; 2 columnas si hay 3-4 cortos
    two_col = len(content["items"]) >= 3 and all(len(i["label"]) <= 22 for i in content["items"])
    cols = 2 if two_col else 1

    return f"""<meta charset="utf-8">
<div data-document-role="page" data-label="Infografía" style="
    width:{CANVAS_W}px;height:{CANVAS_H}px;position:relative;overflow:hidden;
    background:{COLOR_BG};box-sizing:border-box;">
<style>
@font-face {{ font-family:'CocogoosePro'; src:url(data:font/otf;base64,{COCOGOOSE_B64}) format('opentype'); font-weight:700; }}
@font-face {{ font-family:'Montserrat'; src:url(data:font/ttf;base64,{MONTSERRAT_B64}) format('truetype'); font-weight:100 900; }}
* {{ box-sizing:border-box; margin:0; padding:0; }}
.wrap {{
  position:absolute; left:{MARGIN_X}px; right:{MARGIN_X}px; top:110px; bottom:110px;
  display:flex; flex-direction:column; justify-content:center; gap:48px;
}}
.heading {{
  font-family:'CocogoosePro',sans-serif; font-weight:700;
  font-size:{HEADING_SIZE}px; line-height:1.12; color:{COLOR_TEXT}; text-wrap:balance;
}}
.grid {{ display:grid; grid-template-columns:repeat({cols}, 1fr); gap:26px; }}
.card {{
  border-radius:22px; padding:36px 30px;
  display:flex; flex-direction:column; align-items:center; text-align:center; gap:16px;
}}
.card-icon {{ font-size:{CARD_ICON_SIZE}px; line-height:1; }}
.card-label {{
  font-family:'Montserrat',sans-serif; font-weight:600;
  font-size:{CARD_LABEL_SIZE}px; color:{COLOR_TEXT}; line-height:1.2;
}}
</style>
<div class="wrap">
  <div class="heading">{icon_html(content['icon'])} {content['heading']}</div>
  <div class="grid">{cards}</div>
</div>
</div>
"""


def render(content: dict, out_path: str):
    aviso = validar("contenido", "heading", content.get("heading", ""))  # mismo rango que heading
    if aviso:
        print(aviso)
    html = inyectar_sello(build_html(content), content.get('autismo'))
    render_file = BASE_DIR / "_render.html"
    render_file.write_text(html, encoding="utf-8")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": CANVAS_W, "height": CANVAS_H})
        page.goto("file://" + str(render_file))
        page.wait_for_timeout(150)
        page.screenshot(path=str(BASE_DIR / out_path))
        browser.close()
    print("guardado:", out_path)


if __name__ == "__main__":
    render(CONTENT, "infografia_v1.png")
