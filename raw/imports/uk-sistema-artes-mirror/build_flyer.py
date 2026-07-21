"""
Template reutilizable: FLYER de detalles (promoción/publicidad de talleres/cursos/diplomados).
Badge de urgencia (opcional) + nombre del evento + filas de datos (Fecha, Modalidad,
Horario, Cupos, Inversión...) + CTA. On-brand, filas grandes y legibles, un solo acento.

Uso: python3 build_flyer.py
"""
from playwright.sync_api import sync_playwright
from pathlib import Path

from build_contenido import (
    BASE_DIR, CANVAS_W, CANVAS_H, MARGIN_X, COLUMN_MAX_WIDTH,
    COLOR_BG, COLOR_TEXT, COLOR_ACCENT, COCOGOOSE_B64, MONTSERRAT_B64,
)

TITLE_SIZE = 60
ROW_LABEL_SIZE = 26
ROW_VALUE_SIZE = 34
CTA_SIZE = 38

CONTENT = {
    "badge": "Inscripciones abiertas",          # "" para omitir
    "title": "Diplomado Internacional de Autismo 2026",
    "rows": [
        {"label": "INICIO", "value": "Agosto 2026"},
        {"label": "MODALIDAD", "value": "En vivo + grabado"},
        {"label": "SESIONES", "value": "1 por semana (lun y mar)"},
        {"label": "HORARIO", "value": "6:00 – 8:00 pm (Guatemala)"},
    ],
    "cta": "Inscríbete",                          # "" para omitir
}


def build_html(content: dict) -> str:
    badge_html = f'<div class="badge">{content["badge"]}</div>' if content.get("badge") else ""
    subtitle_html = f'<div class="subtitle">{content["subtitle"]}</div>' if content.get("subtitle") else ""
    cta_html = f'<div class="cta">{content["cta"]}</div>' if content.get("cta") else ""
    rows_html = ""
    for r in content["rows"]:
        rows_html += f"""
        <div class="row">
          <div class="dot"></div>
          <div class="row-text"><span class="row-label">{r['label']}</span><span class="row-value">{r['value']}</span></div>
        </div>"""

    return f"""<meta charset="utf-8">
<div data-document-role="page" data-label="Flyer" style="
    width:{CANVAS_W}px;height:{CANVAS_H}px;position:relative;overflow:hidden;
    background:{COLOR_BG};box-sizing:border-box;">
<style>
@font-face {{ font-family:'CocogoosePro'; src:url(data:font/otf;base64,{COCOGOOSE_B64}) format('opentype'); font-weight:700; }}
@font-face {{ font-family:'Montserrat'; src:url(data:font/ttf;base64,{MONTSERRAT_B64}) format('truetype'); font-weight:100 900; }}
* {{ box-sizing:border-box; margin:0; padding:0; }}
.wrap {{
  position:absolute; left:{MARGIN_X}px; right:{MARGIN_X}px; top:110px; bottom:110px;
  display:flex; flex-direction:column; align-items:center; justify-content:center; gap:36px;
}}
.card {{
  width:100%; max-width:{COLUMN_MAX_WIDTH+40}px; background:#FFFFFF;
  border:1.5px solid #ECE9DF; border-radius:28px; padding:48px 44px;
  display:flex; flex-direction:column; gap:30px;
}}
.badge {{
  align-self:flex-start; font-family:'Montserrat',sans-serif; font-weight:700;
  font-size:22px; letter-spacing:.03em; text-transform:uppercase;
  background:{COLOR_ACCENT}; color:#3a2c05; padding:9px 22px; border-radius:24px;
}}
.title {{
  font-family:'CocogoosePro',sans-serif; font-weight:700;
  font-size:{TITLE_SIZE}px; line-height:1.08; color:{COLOR_TEXT}; text-wrap:balance;
}}
.subtitle {{
  font-family:'Montserrat',sans-serif; font-weight:500;
  font-size:30px; color:#6B6A64; line-height:1.25; margin-top:-14px;
}}
.rows {{ display:flex; flex-direction:column; gap:22px; margin-top:4px; }}
.row {{ display:flex; align-items:flex-start; gap:18px; }}
.dot {{ width:16px; height:16px; border-radius:50%; background:{COLOR_ACCENT}; margin-top:9px; flex:none; }}
.row-text {{ display:flex; flex-direction:column; gap:2px; }}
.row-label {{
  font-family:'Montserrat',sans-serif; font-weight:700; font-size:{ROW_LABEL_SIZE}px;
  letter-spacing:.05em; color:#9A8A5C;
}}
.row-value {{
  font-family:'Montserrat',sans-serif; font-weight:500; font-size:{ROW_VALUE_SIZE}px;
  color:{COLOR_TEXT}; line-height:1.25;
}}
.cta {{
  font-family:'CocogoosePro',sans-serif; font-weight:700; font-size:{CTA_SIZE}px;
  color:#3a2c05; background:{COLOR_ACCENT}; padding:18px 46px; border-radius:40px;
}}
</style>
<div class="wrap">
  <div class="card">
    {badge_html}
    <div class="title">{content['title']}</div>
    {subtitle_html}
    <div class="rows">{rows_html}</div>
  </div>
  {cta_html}
</div>
</div>
"""


def render(content: dict, out_path: str):
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
    render(CONTENT, "flyer_v1.png")
