"""
Template reutilizable: Slide de PASOS / progresión numerada.
Lista vertical de pasos numerados conectados por una línea — para secuencias
o progresiones ("1. contacto visual → 2. atención → 3. imitación...").
Material visual distinto a las tarjetas de infografía. Sin datos inventados.

Uso: python3 build_pasos.py
"""
from playwright.sync_api import sync_playwright
from pathlib import Path
from reglas_contenido import validar

from build_contenido import (
    BASE_DIR, CANVAS_W, CANVAS_H, MARGIN_X,
    COLOR_BG, COLOR_TEXT, COLOR_ACCENT, COCOGOOSE_B64, MONTSERRAT_B64, icon_html, inyectar_sello,
)

HEADING_SIZE = 54
STEP_TEXT_SIZE = 36
NUM_SIZE = 40

CONTENT = {
    "icon": "🗣️",
    "heading": "El camino hacia las primeras palabras",
    "steps": [
        "Contacto visual",
        "Atención compartida",
        "Imitación de gestos y sonidos",
        "Comprensión",
    ],
}


def build_html(content: dict) -> str:
    from build_contenido import accent_for, accent_text_for
    accent = accent_for(content.get("marca"))
    accent_fg = accent_text_for(content.get("marca"))
    rows = ""
    n = len(content["steps"])
    for i, step in enumerate(content["steps"]):
        last = "last" if i == n - 1 else ""
        rows += f"""
        <div class="step {last}">
          <div class="num">{i+1}</div>
          <div class="step-text">{step}</div>
        </div>"""

    return f"""<meta charset="utf-8">
<div data-document-role="page" data-label="Pasos" style="
    width:{CANVAS_W}px;height:{CANVAS_H}px;position:relative;overflow:hidden;
    background:{COLOR_BG};box-sizing:border-box;">
<style>
@font-face {{ font-family:'CocogoosePro'; src:url(data:font/otf;base64,{COCOGOOSE_B64}) format('opentype'); font-weight:700; }}
@font-face {{ font-family:'Montserrat'; src:url(data:font/ttf;base64,{MONTSERRAT_B64}) format('truetype'); font-weight:100 900; }}
* {{ box-sizing:border-box; margin:0; padding:0; }}
.wrap {{
  position:absolute; left:{MARGIN_X}px; right:{MARGIN_X}px; top:110px; bottom:110px;
  display:flex; flex-direction:column; justify-content:center; gap:44px;
}}
.heading {{
  font-family:'CocogoosePro',sans-serif; font-weight:700;
  font-size:{HEADING_SIZE}px; line-height:1.12; color:{COLOR_TEXT}; text-wrap:balance;
}}
.steps {{ display:flex; flex-direction:column; }}
.step {{ display:flex; align-items:center; gap:28px; position:relative; padding-bottom:40px; }}
.step.last {{ padding-bottom:0; }}
/* línea conectora vertical detrás de los números */
.step:not(.last)::before {{
  content:""; position:absolute; left:37px; top:74px; bottom:0; width:4px;
  background:#E2DFD5;
}}
.num {{
  width:74px; height:74px; border-radius:50%; flex:none;
  background:{accent}; color:{accent_fg};
  display:flex; align-items:center; justify-content:center;
  font-family:'CocogoosePro',sans-serif; font-weight:700; font-size:{NUM_SIZE}px;
  position:relative; z-index:1;
}}
.step-text {{
  font-family:'Montserrat',sans-serif; font-weight:600;
  font-size:{STEP_TEXT_SIZE}px; color:{COLOR_TEXT}; line-height:1.25;
}}
</style>
<div class="wrap">
  <div class="heading">{icon_html(content['icon'])} {content['heading']}</div>
  <div class="steps">{rows}</div>
</div>
</div>
"""


def render(content: dict, out_path: str):
    aviso = validar("contenido", "heading", content.get("heading", ""))
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
    render(CONTENT, "pasos_v1.png")
