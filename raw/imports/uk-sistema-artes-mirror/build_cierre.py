"""
Template reutilizable: Slide de cierre de carrusel UK.
Basado en el patrón real, casi idéntico en los 3 carruseles analizados:
"¡Ponte en Contacto con Nosotros!" + logo + frase de cierre + barra de contacto.

Uso: python3 build_cierre.py
Para reutilizar, cambiar CONTENT abajo.
"""
from playwright.sync_api import sync_playwright
from pathlib import Path
from reglas_contenido import validar_todos

BASE_DIR = Path(__file__).resolve().parent

# ---- Sistema de diseño (compartido con portada y contenido) ----
CANVAS_W, CANVAS_H = 1080, 1350
MARGIN_X = 100
COLUMN_MAX_WIDTH = 800
COLOR_BG = "#FBFAF6"
COLOR_TEXT = "#33363B"
COLOR_ACCENT = "#EEB41E"          # amarillo — acento del sistema
COLOR_VERDE = "#76B142"           # verde de marca
COLOR_CELESTE = "#57BAC6"         # celeste de marca
COLOR_FOOTER_LINE = "#E2DFD5"     # línea fina divisoria de la barra de contacto
COLOR_FOOTER_TEXT = "#6B6A64"     # gris medio para el pie de contacto

# Color para resaltar la frase emocional del CTA (verde o celeste, NO rojo)
HIGHLIGHT_COLOR = COLOR_VERDE

HEADING_SIZE = 62
BODY_SIZE = 38
CLOSING_SIZE = 42
LOGO_SIZE = 340

with open(BASE_DIR / "cocogoosepro_bold_b64.txt") as f:
    COCOGOOSE_B64 = f.read().strip()
with open(BASE_DIR / "montserrat_b64.txt") as f:
    MONTSERRAT_B64 = f.read().strip()
with open(BASE_DIR / "logo_uk_b64.txt") as f:
    LOGO_B64 = f.read().strip()

# Logos por marca — el generador elige según la Página de la pieza
LOGOS = {"UK": LOGO_B64}
_is_logo = BASE_DIR / "logo_is_b64.txt"
if _is_logo.exists():
    LOGOS["IS"] = _is_logo.read_text().strip()

# Barras de contacto por marca. IS: handles pendientes de confirmar con JR;
# por ahora hereda los de UK (IS es "by Understanding Kids").
CONTACT_IS = {
    "facebook": "Understanding Kids",
    "instagram": "@kidsunderstanding",
    "whatsapp": "+502 5926-9205",
    "web": "www.kidsunderstanding.com",
}

# ---- Contenido (esto es lo único que cambia entre piezas) ----
CONTENT = {
    "heading": "¡Ponte en Contacto con Nosotros!",
    "body_pre": "Si estás buscando la mejor forma de guiar a tu peque hacia un desarrollo pleno y feliz, ",
    "body_highlight": "¡este es tu lugar!",   # frase resaltada en color de marca
    "closing": "Escríbenos para conocer cómo las asesorías o terapias pueden transformar la vida de tu peque.",
}

# ---- Barra de contacto (fija — no cambia entre piezas) ----
CONTACT = {
    "facebook": "Understanding Kids",
    "instagram": "@kidsunderstanding",
    "whatsapp": "+502 5926-9205",
    "web": "www.kidsunderstanding.com",
}

# Íconos con currentColor — heredan el color del texto de la barra (gris)
ICONS = {
    "facebook": '<svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.4h-1.2c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.4v7A10 10 0 0 0 22 12Z"/></svg>',
    "instagram": '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1"/></svg>',
    "whatsapp": '<svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15L2 22l5.2-1.4A10 10 0 1 0 12 2Zm5.6 14.2c-.2.7-1.4 1.3-2 1.4-.5.1-1.2.1-1.9-.1-.4-.1-1-.3-1.7-.6-3-1.3-4.9-4.3-5.1-4.5-.1-.2-1.2-1.6-1.2-3s.7-2.1 1-2.4c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5.2.5.7 1.8.8 1.9.1.2.1.3 0 .5-.1.2-.1.3-.3.5-.1.2-.3.4-.4.5-.2.2-.3.4-.1.7.2.3.9 1.4 1.9 2.3 1.3 1.1 2.3 1.5 2.7 1.7.3.1.5.1.6-.1.2-.2.7-.8.9-1.1.2-.3.4-.2.6-.1.2.1 1.5.7 1.8.8.3.1.5.2.5.3.1.2.1.6-.1 1.1Z"/></svg>',
    "web": '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/></svg>',
}


def build_html(content: dict, contact: dict) -> str:
    from build_contenido import accent_for
    accent = accent_for(content.get("marca"))
    contact_items = "".join(
        f'<div class="contact-item">{ICONS[key]}<span>{value}</span></div>'
        for key, value in contact.items()
    )

    return f"""<meta charset="utf-8">
<div data-document-role="page" data-label="Cierre" style="
    width:{CANVAS_W}px;height:{CANVAS_H}px;position:relative;overflow:hidden;
    background:{COLOR_BG};box-sizing:border-box;">
<style>
@font-face {{
  font-family: 'CocogoosePro';
  src: url(data:font/otf;base64,{COCOGOOSE_B64}) format('opentype');
  font-weight: 700;
}}
@font-face {{
  font-family: 'Montserrat';
  src: url(data:font/ttf;base64,{MONTSERRAT_B64}) format('truetype');
  font-weight: 100 900;
}}
* {{ box-sizing:border-box; margin:0; padding:0; }}
.wrap {{
  position:absolute; left:{MARGIN_X}px; right:{MARGIN_X}px; top:110px; bottom:110px;
  display:flex; flex-direction:column; align-items:center;
}}
.column {{
  width:100%; max-width:{COLUMN_MAX_WIDTH}px;
  display:flex; flex-direction:column; align-items:center; text-align:center; gap:40px;
}}
.heading {{
  font-family:'CocogoosePro',sans-serif; font-weight:700;
  font-size:{HEADING_SIZE}px; line-height:1.1; color:{accent};
  text-wrap:balance;
}}
.body {{
  font-family:'Montserrat',sans-serif; font-weight:500;
  font-size:{BODY_SIZE}px; line-height:1.4; color:{COLOR_TEXT};
}}
.body .hl {{ font-weight:700; color:{HIGHLIGHT_COLOR}; }}
.logo {{ width:{LOGO_SIZE}px; height:{LOGO_SIZE}px; object-fit:contain; }}
.closing {{
  font-family:'Montserrat',sans-serif; font-weight:700;
  font-size:{CLOSING_SIZE}px; line-height:1.35; color:{COLOR_TEXT};
}}
.footer {{
  position:absolute; left:{MARGIN_X}px; right:{MARGIN_X}px; bottom:70px;
  border-top:1.5px solid {COLOR_FOOTER_LINE};
  padding-top:26px; display:flex; justify-content:center; gap:26px; flex-wrap:wrap;
  color:{COLOR_FOOTER_TEXT};
}}
.contact-item {{
  display:flex; align-items:center; gap:8px;
  font-family:'Montserrat',sans-serif; font-weight:500; font-size:19px;
}}
</style>
<div class="wrap">
  <div class="column">
    <div class="heading">{content['heading']}</div>
    <div class="body">{content['body_pre']}<span class="hl">{content['body_highlight']}</span></div>
    <img class="logo" src="data:image/png;base64,{LOGOS.get(content.get('marca','UK'), LOGO_B64)}" />
    <div class="closing">{content['closing']}</div>
  </div>
</div>
<div class="footer">{contact_items}</div>
</div>
"""


def render(content: dict, out_path: str, contact: dict = CONTACT):
    validar_todos("cierre", {
        "heading": content.get("heading", ""),
        "body_pre": content.get("body_pre", ""),
        "body_highlight": content.get("body_highlight", ""),
        "closing": content.get("closing", ""),
    })
    from build_contenido import inyectar_sello
    # En el cierre el sello va al FINAL de la composición: en el hueco entre el
    # último texto y la línea que separa los datos de contacto (esa línea queda
    # a ~168px del borde inferior, así que 200px lo deja justo encima).
    html = inyectar_sello(build_html(content, contact), content.get('autismo'), pos='bottom:200px')
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
    render(CONTENT, "cierre_v1.png")
