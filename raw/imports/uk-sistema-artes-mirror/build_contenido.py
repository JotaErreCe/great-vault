"""
Template reutilizable: Slide de contenido de carrusel UK.
(título + párrafo + viñetas opcionales + cierre con palabra clave)

Basado en el patrón real "autismo_p3" (No siempre se trata de "no hablar")
y reglas del sistema de portada (mismo margen, misma paleta, mismo acento).

Uso: python3 build_contenido.py
Para reutilizar, cambiar CONTENT abajo o importar build_html/render.
"""
from playwright.sync_api import sync_playwright
from pathlib import Path
from reglas_contenido import validar_todos, validar

BASE_DIR = Path(__file__).resolve().parent

# ---- Sistema de diseño (compartido con la portada) ----
CANVAS_W, CANVAS_H = 1080, 1350
MARGIN_X = 100
COLOR_BG = "#FBFAF6"
COLOR_TEXT = "#33363B"
COLOR_ACCENT = "#EEB41E"

# ---- Acento por marca (JR 2026-07-21) ----
# UK = amarillo; IS = turquesa (del logo IS). Estructura y semántica compartidas.
ACCENTS = {"UK": "#EEB41E", "IS": "#3FA8C0"}
ACCENT_TEXT = {"UK": "#3a2c05", "IS": "#FFFFFF"}   # texto legible sobre el acento

def accent_for(marca: str | None) -> str:
    return ACCENTS.get(marca or "UK", ACCENTS["UK"])

def accent_text_for(marca: str | None) -> str:
    return ACCENT_TEXT.get(marca or "UK", ACCENT_TEXT["UK"])

# ---- Símbolo de neurodiversidad (decisión JR 2026-07-21) ----
# En piezas de autismo se usa el INFINITO ∞, NUNCA la pieza de rompecabezas 🧩
# (rechazada por parte de la comunidad autista por su asociación a Autism Speaks).
# El símbolo real es el infinito ARCOÍRIS: un ∞ gris plano no es el símbolo.
INFINITO_NEURODIVERSIDAD = "∞"

# Infinito de neurodiversidad DIBUJADO (no el glifo tipográfico), para que sea
# reconocible como de la casa (JR 2026-07-21):
#  - trazo delgado y parejo con remates REDONDEADOS -> mismo ADN geométrico
#    redondeado de Cocogoose Pro y del anillo del logo de IS.
#  - el arcoíris se arma con LA PALETA DE LA MARCA (terracota, amarillo UK,
#    verde lima IS, turquesa IS, morado) -> sigue leyéndose como el símbolo de
#    neurodiversidad, pero con nuestros colores.
_ND_STOPS = ["#C0503C", "#EEB41E", "#6FAE1C", "#3FA8C0", "#7A5AA6"]
_ND_GROSOR = 7.0          # grosor del trazo en el viewBox (bajarlo = más fino)
# Lóbulos ALARGADOS tipo lima (JR 2026-07-21): elipses horizontales (~1.9:1) con
# las puntas redondeadas, en vez de lóbulos casi circulares. Los puntos de
# control quedan verticales cerca de las puntas para que no se afilen.
_ND_W, _ND_H = 100, 50
_ND_VIEWBOX = f"0 0 {_ND_W} {_ND_H}"
# Lóbulos redondos (la forma que aprobó JR) + EL "BUMP" DE LA LIMA (JR 2026-07-21):
# cada punta se prolonga en una pequeña protuberancia, como el nubcito de una lima.
# Va INTEGRADA al contorno (no como trazo suelto, que se leía como un guion aparte):
# el óvalo se cierra en un vértice en la punta y `stroke-linejoin:round` lo redondea.
_ND_PATH = ("M50,25 C42,9 27,9 20,16.5 C13.5,23 13.5,27 20,33.5 C27,41 42,41 50,25 "
            "C58,9 73,9 80,16.5 C86.5,23 86.5,27 80,33.5 C73,41 58,41 50,25 Z")
# Bump ROMO y CORTO (casi tan ancho como largo), superpuesto al cuerpo para que
# se lea como protuberancia de la fruta y no como un guion suelto.
# El nub es CÓNICO y debe verse SIN escalones. Un trazo SVG tiene grosor constante,
# así que el cono se construye como una sucesión de círculos de radio decreciente
# (como una pincelada que se afina). El primero calza exactamente con el grosor del
# cuerpo en la punta del lóbulo -> la unión es invisible.
_ND_NUB_PASOS = 14        # más pasos = transición más suave
_ND_NUB_X0 = 15.0         # arranque del cono (punta del lóbulo, x del cuerpo)
_ND_NUB_LARGO = 5.0       # cuánto avanza el cono hacia afuera
_ND_NUB_R0 = 3.5          # radio inicial = medio grosor del cuerpo (7.0 / 2)
_ND_NUB_R1 = 1.15         # radio de la puntita
_SELLO_ALTO = 46          # alto del sello de autismo en px (firma discreta)


def _nub_circulos() -> str:
    """Círculos del cono, espejados en ambas puntas."""
    piezas = []
    for i in range(_ND_NUB_PASOS):
        t = i / (_ND_NUB_PASOS - 1)
        r = _ND_NUB_R0 + (_ND_NUB_R1 - _ND_NUB_R0) * t
        dx = _ND_NUB_LARGO * t
        for cx in (_ND_NUB_X0 - dx, _ND_W - _ND_NUB_X0 + dx):
            piezas.append(f'<circle cx="{cx:.2f}" cy="{_ND_H/2:.1f}" r="{r:.2f}"/>')
    return "".join(piezas)


def infinito_nd_svg(alto_em: float = 1.0) -> str:
    """SVG del infinito de neurodiversidad de UK/IS. Escala con el contexto (em);
    1.0em ≈ tamaño de emoji, para que no descuadre la composición."""
    stops = "".join(
        f'<stop offset="{i/(len(_ND_STOPS)-1):.2f}" stop-color="{c}"/>'
        for i, c in enumerate(_ND_STOPS)
    )
    # gradientUnits en userSpaceOnUse: el degradado recorre TODO el símbolo por
    # igual (si no, cada trazo — incluidos los bumps — repetiría el arcoíris).
    return (
        f'<svg viewBox="{_ND_VIEWBOX}" style="height:{alto_em}em;width:auto;'
        'display:inline-block;vertical-align:-.16em;overflow:visible;" '
        'xmlns="http://www.w3.org/2000/svg" aria-label="neurodiversidad">'
        '<defs><linearGradient id="ndg" gradientUnits="userSpaceOnUse" '
        f'x1="0" y1="0" x2="{_ND_W}" y2="0">{stops}</linearGradient></defs>'
        f'<path d="{_ND_PATH}" fill="none" stroke="url(#ndg)" '
        f'stroke-width="{_ND_GROSOR}" stroke-linecap="round" stroke-linejoin="round"/>'
        f'<g fill="url(#ndg)" stroke="none">{_nub_circulos()}</g>'
        '</svg>'
    )


def inyectar_sello(html: str, activo: bool = False, pos: str = "bottom") -> str:
    """SELLO DE AUTISMO (JR 2026-07-21). En las piezas del pilar de autismo el
    infinito NO va como ícono (competía con el titular y desplazaba al emoji del
    tema), sino como firma discreta en el borde de la pieza: pequeño, centrado,
    siempre en el mismo lugar -> se vuelve reconocible sin gritar.

    Se activa con `"autismo": True` en el dict de contenido; el ícono queda libre
    para el emoji del tema."""
    if not activo:
        return html
    # pos: "bottom" | "top" | una posición CSS explícita (ej. "bottom:200px")
    borde = pos if ":" in pos else f"{pos}:56px"
    sello = (f'<div style="position:absolute;{borde};left:0;right:0;'
             f'display:flex;justify-content:center;font-size:{_SELLO_ALTO}px;'
             'line-height:1;">' + infinito_nd_svg() + '</div>')
    i = html.find('<div data-document-role="page"')
    if i == -1:
        return html
    j = html.find(">", i)          # fin de la etiqueta de apertura de la página
    return html[:j + 1] + sello + html[j + 1:]


def icon_html(icon: str) -> str:
    """Ícono listo para insertar en la plantilla. Si es el infinito de
    neurodiversidad, devuelve el SVG propio de la marca en vez del glifo, y lo
    CENTRA en su propia línea: es un símbolo muy simétrico y ancho (JR: "parece
    un antifaz"), así que a la izquierda pelea con la composición; centrado se
    lee como emblema. Los emojis normales siguen inline como siempre."""
    if icon and icon.strip() == INFINITO_NEURODIVERSIDAD:
        return ('<span style="display:block;width:100%;text-align:center;">'
                + infinito_nd_svg() + '</span>')
    return icon

COLUMN_MAX_WIDTH = 800         # ancho de columna de texto, centrado dentro del margen
                                # (evita líneas que se estiran hasta el margen y
                                # dejan la composición "cargada a la izquierda")

HEADING_SIZE = 62
BODY_SIZE = 38
BULLET_SIZE = 36
CLOSING_SIZE = 40
LINE_HEIGHT_HEADING = 1.1
LINE_HEIGHT_BODY = 1.4

with open(BASE_DIR / "cocogoosepro_bold_b64.txt") as f:
    COCOGOOSE_B64 = f.read().strip()
with open(BASE_DIR / "montserrat_b64.txt") as f:
    MONTSERRAT_B64 = f.read().strip()

# ---- Contenido (esto es lo único que cambia entre piezas) ----
CONTENT = {
    "icon": "✋",
    "heading": "Motricidad fina y coordinación",
    "body": "Desde agarrar una cuchara, sostener un vaso o llevar la comida a la boca, la coordinación juega un papel clave.",
    "bullets": [],  # lista opcional de strings; vacío = sin viñetas
    "closing_pre": "Cada habilidad se desarrolla a su",
    "closing_keyword": "propio ritmo",
}


def build_html(content: dict) -> str:
    accent = accent_for(content.get("marca"))
    bullets_html = ""
    if content.get("bullets"):
        items = "".join(f"<li>{b}</li>" for b in content["bullets"])
        bullets_html = f'<ul class="bullets">{items}</ul>'

    closing_html = ""
    if content.get("closing_keyword"):
        pre = content.get("closing_pre", "")
        closing_html = f"""
        <div class="closing-block">
          <span class="closing">{pre} </span><span class="closing kw" id="kw">{content['closing_keyword']}</span>
          <div class="underline" id="bar"></div>
        </div>"""

    return f"""<meta charset="utf-8">
<div data-document-role="page" data-label="Contenido" style="
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
  position:absolute; left:{MARGIN_X}px; right:{MARGIN_X}px; top:120px; bottom:120px;
  display:flex; flex-direction:column; justify-content:center; align-items:center;
}}
.column {{
  width:100%; max-width:{COLUMN_MAX_WIDTH}px;
  display:flex; flex-direction:column; gap:36px;
}}
.heading {{
  font-family:'CocogoosePro',sans-serif; font-weight:700;
  font-size:{HEADING_SIZE}px; line-height:{LINE_HEIGHT_HEADING}; color:{COLOR_TEXT};
  text-wrap:balance;
}}
.body {{
  font-family:'Montserrat',sans-serif; font-weight:400;
  font-size:{BODY_SIZE}px; line-height:{LINE_HEIGHT_BODY}; color:{COLOR_TEXT};
}}
.bullets {{
  font-family:'Montserrat',sans-serif; font-weight:400;
  font-size:{BULLET_SIZE}px; line-height:{LINE_HEIGHT_BODY}; color:{COLOR_TEXT};
  padding-left:38px; display:flex; flex-direction:column; gap:14px;
}}
.bullets li {{ padding-left:6px; }}
.closing-block {{ margin-top:8px; }}
.closing {{
  font-family:'Montserrat',sans-serif; font-weight:600;
  font-size:{CLOSING_SIZE}px; line-height:1.3; color:{COLOR_TEXT};
}}
.underline {{
  height:10px; border-radius:5px; background:{accent}; margin-top:6px;
}}
</style>
<div class="wrap">
  <div class="column">
    <div class="heading">{icon_html(content['icon'])} {content['heading']}</div>
    <div class="body">{content['body']}</div>
    {bullets_html}
    {closing_html}
  </div>
</div>
<script>
  const kw = document.getElementById('kw');
  const bar = document.getElementById('bar');
  if (kw && bar) {{
    const r = kw.getBoundingClientRect();
    const col = document.querySelector('.column').getBoundingClientRect();
    bar.style.width = r.width + 'px';
    bar.style.marginLeft = (r.left - col.left) + 'px';
  }}
</script>
</div>
"""


def render(content: dict, out_path: str):
    has_bullets = bool(content.get("bullets"))
    validar_todos("contenido", {
        "heading": content.get("heading", ""),
        "body_con_bullets" if has_bullets else "body_sin_bullets": content.get("body", ""),
        "closing_pre": content.get("closing_pre", ""),
        "closing_keyword": content.get("closing_keyword", ""),
    })
    for item in content.get("bullets", []):
        aviso = validar("contenido", "bullet_item", item)
        if aviso:
            print(aviso, "->", item[:40])

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
    render(CONTENT, "contenido_v1.png")
