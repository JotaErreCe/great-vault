"""
Template reutilizable: Slide de DATO / número grande (o gráfico de dona).
Para resaltar UNA cifra real con contexto. HONESTIDAD: el número y la fuente
DEBEN ser reales (del brief o de una fuente citable). Nunca inventar estadísticas
para una clínica infantil. Si no hay dato real, no usar esta plantilla.

Modos:
  - "numero": número/porcentaje grande + etiqueta + fuente
  - "dona": gráfico de dona con un porcentaje (requiere 'valor' 0-100)

Uso: python3 build_dato.py
"""
from playwright.sync_api import sync_playwright
from pathlib import Path

from build_contenido import (
    BASE_DIR, CANVAS_W, CANVAS_H, MARGIN_X,
    COLOR_BG, COLOR_TEXT, COLOR_ACCENT, COCOGOOSE_B64, MONTSERRAT_B64,
)

COLOR_VERDE = "#76B142"
COLOR_DONA_TRACK = "#EDE9DD"

CONTENT = {
    "modo": "dona",                 # "numero" o "dona"
    "numero": "1 de cada 5",        # solo modo "numero": texto de la cifra
    "valor": 20,                    # solo modo "dona": porcentaje 0-100
    "etiqueta": "de los niños presenta alguna dificultad en la alimentación",
    "fuente": "Fuente: (colocar fuente real — no publicar sin esto)",
}


def build_html(content: dict) -> str:
    modo = content.get("modo", "numero")

    if modo == "dona":
        valor = max(0, min(100, content.get("valor", 0)))
        ang = valor / 100 * 360
        figura = f"""
        <div class="dona" style="background:conic-gradient({COLOR_ACCENT} {ang}deg, {COLOR_DONA_TRACK} {ang}deg 360deg);">
          <div class="dona-centro"><span class="dona-num">{valor}%</span></div>
        </div>"""
    else:
        figura = f'<div class="numero">{content.get("numero","")}</div>'

    return f"""<meta charset="utf-8">
<div data-document-role="page" data-label="Dato" style="
    width:{CANVAS_W}px;height:{CANVAS_H}px;position:relative;overflow:hidden;
    background:{COLOR_BG};box-sizing:border-box;">
<style>
@font-face {{ font-family:'CocogoosePro'; src:url(data:font/otf;base64,{COCOGOOSE_B64}) format('opentype'); font-weight:700; }}
@font-face {{ font-family:'Montserrat'; src:url(data:font/ttf;base64,{MONTSERRAT_B64}) format('truetype'); font-weight:100 900; }}
* {{ box-sizing:border-box; margin:0; padding:0; }}
.wrap {{
  position:absolute; left:{MARGIN_X}px; right:{MARGIN_X}px; top:120px; bottom:120px;
  display:flex; flex-direction:column; align-items:center; justify-content:center; gap:44px; text-align:center;
}}
.numero {{
  font-family:'CocogoosePro',sans-serif; font-weight:700; font-size:150px;
  line-height:1; color:{COLOR_TEXT};
}}
.dona {{
  width:420px; height:420px; border-radius:50%;
  display:flex; align-items:center; justify-content:center;
}}
.dona-centro {{
  width:300px; height:300px; border-radius:50%; background:{COLOR_BG};
  display:flex; align-items:center; justify-content:center;
}}
.dona-num {{ font-family:'CocogoosePro',sans-serif; font-weight:700; font-size:96px; color:{COLOR_TEXT}; }}
.etiqueta {{
  font-family:'Montserrat',sans-serif; font-weight:600; font-size:40px;
  line-height:1.35; color:{COLOR_TEXT}; max-width:820px;
}}
.fuente {{
  font-family:'Montserrat',sans-serif; font-weight:400; font-size:24px;
  color:#8A897F; margin-top:4px;
}}
</style>
<div class="wrap">
  {figura}
  <div class="etiqueta">{content.get('etiqueta','')}</div>
  <div class="fuente">{content.get('fuente','')}</div>
</div>
</div>
"""


def render(content: dict, out_path: str):
    fuente = content.get("fuente", "")
    if not fuente or "colocar fuente" in fuente.lower():
        print("[AVISO IMPORTANTE] Falta la fuente real del dato. NO publicar una cifra sin fuente verificable.")
    html = build_html(content)
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
    render(CONTENT, "dato_v1.png")
