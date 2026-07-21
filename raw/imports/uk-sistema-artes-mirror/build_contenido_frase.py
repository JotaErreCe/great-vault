"""
Template reutilizable: Slide de FRASE / CITA destacada.
Basado en el patrón real "Comprender es aliviar" (cita + atribución).
Pieza de alto impacto: poco texto, mucho aire, la frase como protagonista.

Uso: python3 build_contenido_frase.py
"""
from playwright.sync_api import sync_playwright
from pathlib import Path
from reglas_contenido import validar_todos

# Reutiliza el sistema de diseño de la plantilla de contenido
from build_contenido import (
    BASE_DIR, CANVAS_W, CANVAS_H, MARGIN_X, COLUMN_MAX_WIDTH,
    COLOR_BG, COLOR_TEXT, COLOR_ACCENT, COCOGOOSE_B64, MONTSERRAT_B64, inyectar_sello,
)

QUOTE_SIZE = 78          # tamaño de la cita
ATTR_SIZE = 34           # atribución (autor)
CONTEXT_SIZE = 28        # línea de contexto opcional
QUOTEMARK_SIZE = 200     # comilla decorativa grande

# ---- Contenido (esto es lo único que cambia entre piezas) ----
CONTENT = {
    "quote": "Comprender es aliviar.",
    "author": "Marian Rojas Estapé",
    "context": "Cómo hacer que te pasen cosas buenas",   # opcional; "" para omitir
}


def build_html(content: dict) -> str:
    from build_contenido import accent_for
    accent = accent_for(content.get("marca"))
    context_html = ""
    if content.get("context"):
        context_html = f'<div class="context">{content["context"]}</div>'

    return f"""<meta charset="utf-8">
<div data-document-role="page" data-label="Frase" style="
    width:{CANVAS_W}px;height:{CANVAS_H}px;position:relative;overflow:hidden;
    background:{COLOR_BG};box-sizing:border-box;">
<style>
@font-face {{
  font-family:'CocogoosePro'; src:url(data:font/otf;base64,{COCOGOOSE_B64}) format('opentype'); font-weight:700;
}}
@font-face {{
  font-family:'Montserrat'; src:url(data:font/ttf;base64,{MONTSERRAT_B64}) format('truetype'); font-weight:100 900;
}}
* {{ box-sizing:border-box; margin:0; padding:0; }}
.wrap {{
  position:absolute; left:{MARGIN_X}px; right:{MARGIN_X}px; top:120px; bottom:120px;
  display:flex; flex-direction:column; align-items:center; justify-content:center;
}}
.column {{ width:100%; max-width:{COLUMN_MAX_WIDTH}px; display:flex; flex-direction:column; }}
.quotemark {{
  font-family:'CocogoosePro',sans-serif; font-weight:700;
  font-size:{QUOTEMARK_SIZE}px; line-height:0.7; color:{accent};
  height:{int(QUOTEMARK_SIZE*0.5)}px;
}}
.quote {{
  font-family:'CocogoosePro',sans-serif; font-weight:700;
  font-size:{QUOTE_SIZE}px; line-height:1.12; color:{COLOR_TEXT};
  text-wrap:balance; margin-top:10px;
}}
.attr-row {{ display:flex; align-items:center; gap:16px; margin-top:44px; }}
.dash {{ width:44px; height:6px; border-radius:3px; background:{accent}; flex:none; }}
.author {{
  font-family:'Montserrat',sans-serif; font-weight:700;
  font-size:{ATTR_SIZE}px; color:{COLOR_TEXT};
}}
.context {{
  font-family:'Montserrat',sans-serif; font-weight:400;
  font-size:{CONTEXT_SIZE}px; color:#7A7A73; margin-top:12px; margin-left:60px;
}}
</style>
<div class="wrap">
  <div class="column">
    <div class="quotemark">&ldquo;</div>
    <div class="quote">{content['quote']}</div>
    <div class="attr-row">
      <div class="dash"></div>
      <div class="author">{content['author']}</div>
    </div>
    {context_html}
  </div>
</div>
</div>
"""


def render(content: dict, out_path: str):
    validar_todos("frase", {
        "quote": content.get("quote", ""),
        "author": content.get("author", ""),
        "context": content.get("context", ""),
    })
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
    render(CONTENT, "contenido_frase_v1.png")
