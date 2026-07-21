"""
Template reutilizable: Slide de COMPARACIÓN de dos columnas.
Ideal para "mito vs realidad", "esperar vs acompañar", "antes vs después".
Material visual distinto a las tarjetas y a los pasos.

Uso: python3 build_comparacion.py
"""
from playwright.sync_api import sync_playwright
from pathlib import Path

from build_contenido import (
    BASE_DIR, CANVAS_W, CANVAS_H, MARGIN_X,
    COLOR_BG, COLOR_TEXT, COLOR_ACCENT, COCOGOOSE_B64, MONTSERRAT_B64, icon_html, inyectar_sello,
)

COLOR_VERDE = "#76B142"
# Semántica de color (JR 2026-07-20): rojo SUAVE = negativo (mito/presión/error),
# verde = positivo. Para comparaciones sin carga (ej. sesión 1 vs 2) usar left_kind="neutral".
COLOR_NEG_BG = "#F9E6E1"       # tinte terracota suave (no rojo alarma)
COLOR_NEG_PILL = "#C0503C"     # terracota para la píldora, texto blanco
COLOR_NEUTRAL_BG = "#EEEDE7"
COLOR_NEUTRAL_PILL = "#D8D6CC"
HEADING_SIZE = 52
LABEL_SIZE = 30
TEXT_SIZE = 32

CONTENT = {
    "icon": "🍽️",
    "heading": "Mito o realidad",
    "left_label": "MITO",
    "left_text": "Si no come, es puro capricho.",
    "right_label": "REALIDAD",
    "right_text": "Puede haber una dificultad sensorial o motora detrás.",
}


def build_html(content: dict) -> str:
    neutral = content.get("left_kind") == "neutral"
    left_bg = COLOR_NEUTRAL_BG if neutral else COLOR_NEG_BG
    left_pill_bg = COLOR_NEUTRAL_PILL if neutral else COLOR_NEG_PILL
    left_pill_fg = "#5F5E58" if neutral else "#FFFFFF"
    return f"""<meta charset="utf-8">
<div data-document-role="page" data-label="Comparación" style="
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
.cols {{ display:grid; grid-template-columns:1fr 1fr; gap:26px; }}
.col {{ border-radius:22px; padding:34px 28px; display:flex; flex-direction:column; gap:20px; }}
.col.left {{ background:{left_bg}; }}
.col.right {{ background:#E6F0DD; }}
.pill {{
  align-self:flex-start; font-family:'Montserrat',sans-serif; font-weight:700;
  font-size:{LABEL_SIZE}px; letter-spacing:.04em; padding:8px 20px; border-radius:24px;
}}
.pill.left {{ background:{left_pill_bg}; color:{left_pill_fg}; }}
.pill.right {{ background:{COLOR_VERDE}; color:#ffffff; }}
.col-text {{
  font-family:'Montserrat',sans-serif; font-weight:500;
  font-size:{TEXT_SIZE}px; line-height:1.35; color:{COLOR_TEXT};
}}
</style>
<div class="wrap">
  <div class="heading">{icon_html(content['icon'])} {content['heading']}</div>
  <div class="cols">
    <div class="col left">
      <div class="pill left">{content['left_label']}</div>
      <div class="col-text">{content['left_text']}</div>
    </div>
    <div class="col right">
      <div class="pill right">{content['right_label']}</div>
      <div class="col-text">{content['right_text']}</div>
    </div>
  </div>
</div>
</div>
"""


def render(content: dict, out_path: str):
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
    render(CONTENT, "comparacion_v1.png")
