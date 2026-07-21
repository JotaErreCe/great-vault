"""
Template reutilizable: Portada de carrusel UK.
Basado en el análisis de 3 portadas reales 2026 (autismo, testimonio niñeras, servicio).
Corrige: color de énfasis inconsistente (unificado a amarillo de marca),
espacio vacío excesivo arriba, márgenes sin regla fija.

Tamaño de letra: usa un tamaño BASE grande (HEADLINE_SIZE_MAX, el mismo que ya
aprobamos) y solo lo reduce automáticamente si el texto no cabe en la zona
segura del cuadro — nunca al revés. Mide de verdad con Playwright, no adivina.

Uso: python3 build_portada.py

Para reutilizar con otro contenido, cambiar CONTENT abajo.
"""
from playwright.sync_api import sync_playwright
from pathlib import Path
from reglas_contenido import validar_todos

BASE_DIR = Path(__file__).resolve().parent

# ---- Sistema de diseño (constantes, no "a ojo") ----
CANVAS_W, CANVAS_H = 1080, 1350
MARGIN_X = 100                 # 9.3% del ancho — margen lateral fijo
COLOR_BG = "#FBFAF6"           # crema de marca
COLOR_TEXT = "#33363B"         # gris oscuro funcional (texto de lectura)
COLOR_ACCENT = "#EEB41E"       # amarillo de marca — ÚNICO color de énfasis
LINE_HEIGHT = 1.08

# Tamaño de letra: base grande (el ya aprobado), reducible solo si hace falta.
HEADLINE_SIZE_MAX = 84         # tamaño ideal — se usa siempre que el texto quepa
HEADLINE_SIZE_MIN = 52         # piso — nunca baja de esto (deja de verse "portada")
HEADLINE_SIZE_STEP = 4         # px que baja en cada intento
MAX_BLOCK_HEIGHT = 820         # alto máximo del bloque título+palabra clave (de 1350px totales)

with open(BASE_DIR / "cocogoosepro_bold_b64.txt") as f:
    COCOGOOSE_B64 = f.read().strip()

# ---- Contenido (esto es lo único que cambia entre piezas) ----
CONTENT = {
    "icon": "🥣",
    "headline_main": "La alimentación es un proceso",
    "headline_keyword": "complejo",
}


def build_html(content: dict) -> str:
    from build_contenido import accent_for, icon_html
    accent = accent_for(content.get("marca"))
    return f"""<meta charset="utf-8">
<div data-document-role="page" data-label="Portada" style="
    width:{CANVAS_W}px;height:{CANVAS_H}px;position:relative;overflow:hidden;
    background:{COLOR_BG};box-sizing:border-box;">
<style>
@font-face {{
  font-family: 'CocogoosePro';
  src: url(data:font/otf;base64,{COCOGOOSE_B64}) format('opentype');
  font-weight: 700;
}}
:root {{ --headline-size: {HEADLINE_SIZE_MAX}px; }}
* {{ box-sizing:border-box; margin:0; padding:0; font-family:'CocogoosePro',sans-serif; }}
.wrap {{
  position:absolute; left:{MARGIN_X}px; right:{MARGIN_X}px; top:0; bottom:0;
  display:flex; flex-direction:column; justify-content:center;
  /* centro óptico: el subrayado pesa abajo, así que el bloque sube un poco */
  padding-bottom:100px;
}}
.textblock {{ display:flex; flex-direction:column; }}
/* ícono en su propia línea: evita que la primera línea del titular quede indentada */
.icon {{ font-size:76px; line-height:1; margin-bottom:34px; }}
.headline {{
  font-weight:700; font-size:var(--headline-size); line-height:{LINE_HEIGHT};
  color:{COLOR_TEXT}; text-wrap:balance;
}}
.keyword-row {{ display:inline-block; margin-top:14px; }}
.keyword {{
  font-weight:700; font-size:var(--headline-size); line-height:{LINE_HEIGHT};
  color:{COLOR_TEXT}; display:inline-block;
}}
.underline {{
  height:16px; border-radius:6px; background:{accent}; margin-top:8px;
}}
</style>
<div class="wrap">
  <div class="textblock" id="block">
    <div class="icon">{icon_html(content['icon'])}</div>
    <div class="headline">{content['headline_main']}</div>
    <div class="keyword-row">
      <div class="keyword" id="kw">{content['headline_keyword']}</div>
      <div class="underline" id="bar"></div>
    </div>
  </div>
</div>
</div>
"""


def _fit_and_measure(page, max_height: int, size_max: int, size_min: int, step: int) -> int:
    """Reduce --headline-size hasta que el bloque quepa en max_height. Devuelve el tamaño final usado."""
    size = size_max
    while True:
        page.evaluate(f"document.documentElement.style.setProperty('--headline-size', '{size}px')")
        height = page.evaluate("document.getElementById('block').getBoundingClientRect().height")
        if height <= max_height or size <= size_min:
            break
        size -= step
    # ancho del subrayado = ancho real de la palabra clave, medido en su tamaño final
    page.evaluate("""
        const kw = document.getElementById('kw');
        const bar = document.getElementById('bar');
        bar.style.width = kw.getBoundingClientRect().width + 'px';
    """)
    return size


def render(content: dict, out_path: str):
    validar_todos("portada", {
        "headline_main": content.get("headline_main", ""),
        "headline_keyword": content.get("headline_keyword", ""),
    })
    from build_contenido import inyectar_sello
    html = inyectar_sello(build_html(content), content.get('autismo'))
    render_file = BASE_DIR / "_render.html"
    render_file.write_text(html, encoding="utf-8")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": CANVAS_W, "height": CANVAS_H})
        page.goto("file://" + str(render_file))
        page.wait_for_timeout(80)
        final_size = _fit_and_measure(
            page, MAX_BLOCK_HEIGHT, HEADLINE_SIZE_MAX, HEADLINE_SIZE_MIN, HEADLINE_SIZE_STEP
        )
        page.wait_for_timeout(80)
        page.screenshot(path=str(BASE_DIR / out_path))
        browser.close()
    if final_size < HEADLINE_SIZE_MAX:
        print(f"guardado: {out_path}  (letra reducida a {final_size}px — el hook era largo)")
    else:
        print(f"guardado: {out_path}  (tamaño completo {HEADLINE_SIZE_MAX}px)")


if __name__ == "__main__":
    render(CONTENT, "portada_v1.png")
