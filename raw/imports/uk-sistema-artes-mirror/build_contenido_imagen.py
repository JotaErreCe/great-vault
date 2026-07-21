"""
Template reutilizable: Slide de contenido CON IMAGEN.
Variante del slide de contenido para cuando corresponde acompañar con una imagen
(ilustración o foto real). Misma paleta, márgenes y tipografía que el resto del sistema.

La imagen puede venir de:
  - una foto real (archivo tuyo)
  - una ilustración generada gratis con Pollinations (ver generar_ilustracion.py)

Uso: python3 build_contenido_imagen.py
"""
from playwright.sync_api import sync_playwright
from pathlib import Path
import base64
from reglas_contenido import validar_todos

# Reutiliza el sistema de diseño ya definido en la plantilla de contenido
from build_contenido import (
    BASE_DIR, CANVAS_W, CANVAS_H, MARGIN_X, COLUMN_MAX_WIDTH,
    COLOR_BG, COLOR_TEXT, COLOR_ACCENT, COCOGOOSE_B64, MONTSERRAT_B64, inyectar_sello,
)

HEADING_SIZE = 54
BODY_SIZE = 36
IMG_HEIGHT = 460          # alto de la ventana de imagen
IMG_RADIUS = 28
IMG_WIDTH = 880           # ancho de la imagen (de margen a margen)

# ---- Contenido (esto es lo único que cambia entre piezas) ----
CONTENT = {
    "image_path": "demo_ilustracion_tazon.jpg",   # foto real o ilustración
    "heading": "La alimentación es un proceso complejo",
    "body": "Comer requiere muchas habilidades que podemos desarrollar en terapia de alimentación.",
    "closing_pre": "Y cada una se puede",
    "closing_keyword": "acompañar",
}


def _img_b64(path: str) -> tuple[str, str]:
    p = (BASE_DIR / path) if not Path(path).is_absolute() else Path(path)
    data = base64.b64encode(p.read_bytes()).decode()
    mime = "jpeg" if p.suffix.lower() in (".jpg", ".jpeg") else "png"
    return data, mime


def build_html(content: dict) -> str:
    from build_contenido import accent_for
    accent = accent_for(content.get("marca"))
    img_data, img_mime = _img_b64(content["image_path"])

    closing_html = ""
    if content.get("closing_keyword"):
        pre = content.get("closing_pre", "")
        closing_html = f"""
        <div class="closing-block">
          <span class="closing">{pre} </span><span class="closing kw" id="kw">{content['closing_keyword']}</span>
          <div class="underline" id="bar"></div>
        </div>"""

    return f"""<meta charset="utf-8">
<div data-document-role="page" data-label="Contenido con imagen" style="
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
  position:absolute; left:{MARGIN_X}px; right:{MARGIN_X}px; top:110px; bottom:110px;
  display:flex; flex-direction:column; align-items:center; justify-content:center; gap:44px;
}}
.photo {{
  width:{IMG_WIDTH}px; height:{IMG_HEIGHT}px; object-fit:cover;
  object-position:{content.get("img_position", "center")};
  border-radius:{IMG_RADIUS}px; display:block;
}}
.textcol {{ width:100%; max-width:{COLUMN_MAX_WIDTH}px; display:flex; flex-direction:column; gap:24px; }}
.heading {{
  font-family:'CocogoosePro',sans-serif; font-weight:700;
  font-size:{HEADING_SIZE}px; line-height:1.12; color:{COLOR_TEXT}; text-wrap:balance;
}}
.body {{
  font-family:'Montserrat',sans-serif; font-weight:400;
  font-size:{BODY_SIZE}px; line-height:1.4; color:{COLOR_TEXT};
}}
.closing {{
  font-family:'Montserrat',sans-serif; font-weight:600;
  font-size:38px; line-height:1.3; color:{COLOR_TEXT};
}}
.underline {{ height:9px; border-radius:5px; background:{accent}; margin-top:6px; }}
</style>
<div class="wrap">
  <img class="photo" src="data:image/{img_mime};base64,{img_data}" />
  <div class="textcol">
    <div class="heading">{content['heading']}</div>
    <div class="body">{content['body']}</div>
    {closing_html}
  </div>
</div>
<script>
  const kw=document.getElementById('kw'), bar=document.getElementById('bar');
  if(kw&&bar){{
    const r=kw.getBoundingClientRect(), col=document.querySelector('.textcol').getBoundingClientRect();
    bar.style.width=r.width+'px'; bar.style.marginLeft=(r.left-col.left)+'px';
  }}
</script>
</div>
"""


def render(content: dict, out_path: str):
    validar_todos("contenido_imagen", {
        "heading": content.get("heading", ""),
        "body": content.get("body", ""),
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
    render(CONTENT, "contenido_imagen_v1.png")
