"""
SUB-SISTEMA DE PROMOS / PUBLICIDAD (talleres, cursos, diplomados).

Distinto a los artes "diarios" (informativos): la PORTADA es un flyer completo
que se sostiene solo (título + fecha + horario + modalidad + precio + CTA), porque
la mayoría de la gente NO hace swipe para enterarse. El swipe amplía, no informa.

Además usa una PALETA PROPIA por campaña (no la crema/amarillo diaria). Se elige
un color según el tema del taller. Anclas fijas de marca que NO cambian: la
tipografía (Cocogoose Pro + Montserrat), la disciplina de layout/márgenes y el logo.

Paleta = dict THEME. Se puede intercambiar por campaña sin tocar la estructura.

Uso: pasar THEME + un dict de contenido por slide a las funciones render_*.
"""
from playwright.sync_api import sync_playwright
from pathlib import Path
import base64

from build_contenido import (
    BASE_DIR, CANVAS_W, CANVAS_H, MARGIN_X, COLUMN_MAX_WIDTH,
    COCOGOOSE_B64, MONTSERRAT_B64,
)
from build_cierre import ICONS  # íconos de la barra de contacto

with open(BASE_DIR / "logo_is_b64.txt") as f:
    LOGO_IS_B64 = f.read().strip()
with open(BASE_DIR / "logo_uk_b64.txt") as f:
    LOGO_UK_B64 = f.read().strip()
LOGOS = {"IS": LOGO_IS_B64, "UK": LOGO_UK_B64}

# ---------- PALETAS (una por campaña; elegir/inventar según el TEMA) ----------
# Para crear una paleta nueva basta con 3 colores + el fondo cálido/frío suave de
# la portada. make_theme() rellena el resto. Ver GUIA_PROMOS_TALLERES.md.
def make_theme(title, accent, accent2, cover_bg, chip_border, *,
               bg="#FBF6EF", text="#3E352E", muted="#9A8574", card="#FFFFFF"):
    """title/accent/accent2 = los 3 colores del tema; cover_bg = fondo SUAVE de la
    portada (el color fuerte va solo como acento, nunca de fondo pleno)."""
    return {"title": title, "accent": accent, "accent2": accent2, "cover_bg": cover_bg,
            "chip_border": chip_border, "bg": bg, "text": text, "muted": muted, "card": card}

# Alimentación — cálida "de apetito" (tomate + miel + verde fresco). APROBADA.
THEME_ALIMENTACION = make_theme(
    title="#D4432A", accent="#F2A93B", accent2="#7DA63B",
    cover_bg="#F8E2D3", chip_border="#EFCBB2", bg="#FBF1E8", text="#4A3B33")

# Lenguaje / comunicación — celeste + turquesa + coral.
THEME_LENGUAJE = make_theme(
    title="#2E86A6", accent="#57BAC6", accent2="#F1885B",
    cover_bg="#DDEEF2", chip_border="#BFDDE4", bg="#F0F7F9", text="#26424C")

# Emociones / autoestima — lila/morado suave + durazno.
THEME_EMOCIONES = make_theme(
    title="#7A5AA6", accent="#B491D6", accent2="#F0A24E",
    cover_bg="#EAE2F2", chip_border="#D6C7E6", bg="#F4F0F8", text="#3E3350")

# Sensorial / juego — verde + naranja + turquesa (colores del logo IS).
THEME_SENSORIAL = make_theme(
    title="#5C9E3A", accent="#F2A93B", accent2="#57BAC6",
    cover_bg="#E4F0DA", chip_border="#CBE3BE", bg="#F2F7EC", text="#35462A")

# Sueño / rutinas — azul noche suave + crema.
THEME_SUENO = make_theme(
    title="#3F5C8C", accent="#8CA0C9", accent2="#E8B04B",
    cover_bg="#E1E7F2", chip_border="#C6D2E6", bg="#F0F3F9", text="#2C3652")


def _img_b64(path: str) -> tuple[str, str]:
    p = (BASE_DIR / path) if not Path(path).is_absolute() else Path(path)
    data = base64.b64encode(p.read_bytes()).decode()
    mime = "jpeg" if p.suffix.lower() in (".jpg", ".jpeg") else "png"
    return data, mime


def _fonts() -> str:
    return f"""
@font-face {{ font-family:'CocogoosePro'; src:url(data:font/otf;base64,{COCOGOOSE_B64}) format('opentype'); font-weight:700; }}
@font-face {{ font-family:'Montserrat'; src:url(data:font/ttf;base64,{MONTSERRAT_B64}) format('truetype'); font-weight:100 900; }}
* {{ box-sizing:border-box; margin:0; padding:0; }}"""


def _page(inner: str, bg: str, label: str) -> str:
    return f"""<meta charset="utf-8">
<div data-document-role="page" data-label="{label}" style="
    width:{CANVAS_W}px;height:{CANVAS_H}px;position:relative;overflow:hidden;
    background:{bg};box-sizing:border-box;">
<style>{_fonts()}</style>
{inner}
</div>"""


def _screenshot(html: str, out_path: str):
    render_file = BASE_DIR / "_render.html"
    render_file.write_text(html, encoding="utf-8")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": CANVAS_W, "height": CANVAS_H})
        page.goto("file://" + str(render_file))
        page.wait_for_timeout(160)
        page.screenshot(path=str(BASE_DIR / out_path))
        browser.close()
    print("guardado:", out_path)


# ============================ 1. PORTADA-FLYER ============================
# Afiche editorial: foto humana full-bleed arriba, transición ondulada al fondo
# cálido suave (sin recuadro blanco), y abajo título + chips de datos + CTA
# integrados. El tomate se usa solo como acento (título/CTA), no como fondo pleno.
def render_cover(content: dict, theme: dict, out_path: str, marca: str = "IS"):
    PHOTO_H = 720
    img_data, img_mime = _img_b64(content["image_path"])
    bg = theme["cover_bg"]

    chips = ""
    for r in content["rows"]:
        chips += f'<div class="chip"><span class="ci">{r["icon"]}</span>{r["value"]}</div>'
    badge = f'<div class="badge">{content["badge"]}</div>' if content.get("badge") else ""
    subtitle = f'<div class="subtitle">{content["subtitle"]}</div>' if content.get("subtitle") else ""
    cta = f'<div class="cta">{content["cta"]}</div>' if content.get("cta") else ""

    inner = f"""
<style>
.photo {{ position:absolute; top:0; left:0; width:{CANVAS_W}px; height:{PHOTO_H}px; object-fit:cover; object-position:center 32%; }}
/* degradado que funde el pie de la foto con el fondo cálido */
.fade {{ position:absolute; top:{PHOTO_H-240}px; left:0; width:{CANVAS_W}px; height:260px;
  background:linear-gradient(to bottom, rgba(248,226,211,0) 0%, {bg} 88%); }}
/* onda orgánica que sube sobre la foto */
.wave {{ position:absolute; top:{PHOTO_H-96}px; left:0; width:{CANVAS_W}px; height:150px; display:block; }}
/* sticker del logo sobre la foto */
.logo-chip {{ position:absolute; top:44px; left:44px; width:118px; height:118px; border-radius:50%;
  background:#FFFFFF; box-shadow:0 10px 26px rgba(60,30,20,.20); display:flex; align-items:center; justify-content:center; }}
.logo-chip img {{ width:96px; height:96px; object-fit:contain; }}
.content {{ position:absolute; left:70px; right:70px; top:{PHOTO_H+2}px; bottom:60px;
  display:flex; flex-direction:column; align-items:center; text-align:center; gap:20px; }}
.badge {{ font-family:'Montserrat'; font-weight:700; font-size:20px; letter-spacing:.08em; text-transform:uppercase;
  background:{theme['title']}; color:#ffffff; padding:9px 24px; border-radius:22px; }}
.title {{ font-family:'CocogoosePro'; font-weight:700; font-size:62px; line-height:1.04; color:{theme['title']};
  text-align:center; text-wrap:balance; }}
.subtitle {{ font-family:'Montserrat'; font-weight:500; font-size:27px; line-height:1.3; color:{theme['text']}; max-width:760px; }}
.chips {{ display:flex; flex-wrap:wrap; justify-content:center; gap:14px 16px; margin-top:4px; }}
.chip {{ display:flex; align-items:center; gap:10px; background:#FFFFFF; border:1.5px solid {theme['chip_border']};
  border-radius:40px; padding:12px 22px; font-family:'Montserrat'; font-weight:600; font-size:25px; color:{theme['text']}; }}
.chip .ci {{ font-size:24px; }}
.cta {{ font-family:'CocogoosePro'; font-weight:700; font-size:36px; color:#ffffff;
  background:{theme['title']}; padding:18px 54px; border-radius:44px; margin-top:6px;
  box-shadow:0 12px 30px rgba(212,67,42,.30); }}
</style>
<img class="photo" src="data:image/{img_mime};base64,{img_data}" />
<div class="fade"></div>
<svg class="wave" viewBox="0 0 1080 150" preserveAspectRatio="none">
  <path d="M0,74 C 210,18 400,18 560,58 C 720,98 900,104 1080,52 L1080,150 L0,150 Z" fill="{bg}"/>
</svg>
<div class="logo-chip"><img src="data:image/png;base64,{LOGOS.get(marca, LOGO_IS_B64)}" /></div>
<div class="content">
  {badge}
  <div class="title">{content['title']}</div>
  {subtitle}
  <div class="chips">{chips}</div>
  {cta}
</div>"""
    _screenshot(_page(inner, bg, "Portada-Flyer"), out_path)


# ============================ 2. FOTO + CONTEXTO ============================
def render_foto(content: dict, theme: dict, out_path: str):
    img_data, img_mime = _img_b64(content["image_path"])
    closing = ""
    if content.get("closing_pre") or content.get("closing_keyword"):
        closing = (f'<div class="closing">{content.get("closing_pre","")} '
                   f'<span class="ck">{content.get("closing_keyword","")}</span></div>')
    inner = f"""
<style>
.wrap {{ position:absolute; left:{MARGIN_X}px; right:{MARGIN_X}px; top:110px; bottom:110px;
  display:flex; flex-direction:column; justify-content:center; gap:34px; }}
.photo {{ width:100%; height:470px; object-fit:cover; border-radius:28px; display:block; }}
.heading {{ font-family:'CocogoosePro'; font-weight:700; font-size:54px; line-height:1.1; color:{theme['title']}; text-wrap:balance; }}
.body {{ font-family:'Montserrat'; font-weight:500; font-size:36px; line-height:1.4; color:{theme['text']}; }}
.closing {{ font-family:'Montserrat'; font-weight:700; font-size:38px; line-height:1.3; color:{theme['text']}; }}
.ck {{ color:{theme['title']}; border-bottom:5px solid {theme['accent']}; padding-bottom:2px; }}
</style>
<div class="wrap">
  <img class="photo" src="data:image/{img_mime};base64,{img_data}" />
  <div class="heading">{content['heading']}</div>
  <div class="body">{content['body']}</div>
  {closing}
</div>"""
    _screenshot(_page(inner, theme["bg"], "Foto"), out_path)


# ============================ 3. ¿QUÉ INCLUYE? ============================
def render_incluye(content: dict, theme: dict, out_path: str):
    tints = [theme["accent"], theme["accent2"], theme["title"]]
    cards = ""
    for i, it in enumerate(content["items"]):
        c = tints[i % len(tints)]
        cards += f"""
        <div class="card" style="border-color:{c}">
          <div class="ci" style="background:{c}">{it['icon']}</div>
          <div class="cl">{it['label']}</div>
        </div>"""
    inner = f"""
<style>
.wrap {{ position:absolute; left:{MARGIN_X}px; right:{MARGIN_X}px; top:110px; bottom:110px;
  display:flex; flex-direction:column; justify-content:center; gap:44px; }}
.heading {{ font-family:'CocogoosePro'; font-weight:700; font-size:56px; line-height:1.1; color:{theme['title']}; text-wrap:balance; }}
.list {{ display:flex; flex-direction:column; gap:22px; }}
.card {{ background:{theme['card']}; border:2px solid; border-radius:24px; padding:28px 30px;
  display:flex; align-items:center; gap:26px; }}
.ci {{ width:82px; height:82px; border-radius:20px; flex:none; display:flex; align-items:center; justify-content:center; font-size:42px; }}
.cl {{ font-family:'Montserrat'; font-weight:700; font-size:38px; color:{theme['text']}; line-height:1.15; }}
</style>
<div class="wrap">
  <div class="heading">{content['heading']}</div>
  <div class="list">{cards}</div>
</div>"""
    _screenshot(_page(inner, theme["bg"], "Incluye"), out_path)


# ============================ 4. TEMARIO (2 sesiones) ============================
def render_temario(content: dict, theme: dict, out_path: str):
    cols = ""
    for i, s in enumerate(content["sessions"]):
        c = theme["accent"] if i == 0 else theme["accent2"]
        cols += f"""
        <div class="col">
          <div class="pill" style="background:{c}">{s['label']}</div>
          <div class="ctext">{s['text']}</div>
        </div>"""
    inner = f"""
<style>
.wrap {{ position:absolute; left:{MARGIN_X}px; right:{MARGIN_X}px; top:110px; bottom:110px;
  display:flex; flex-direction:column; justify-content:center; gap:44px; }}
.heading {{ font-family:'CocogoosePro'; font-weight:700; font-size:52px; line-height:1.12; color:{theme['title']}; text-wrap:balance; }}
.cols {{ display:grid; grid-template-columns:1fr 1fr; gap:24px; }}
.col {{ background:{theme['card']}; border-radius:24px; padding:32px 28px; display:flex; flex-direction:column; gap:20px; }}
.pill {{ align-self:flex-start; font-family:'Montserrat'; font-weight:700; font-size:28px;
  letter-spacing:.04em; color:#ffffff; padding:8px 22px; border-radius:22px; }}
.ctext {{ font-family:'Montserrat'; font-weight:500; font-size:32px; line-height:1.35; color:{theme['text']}; }}
</style>
<div class="wrap">
  <div class="heading">{content['heading']}</div>
  <div class="cols">{cols}</div>
</div>"""
    _screenshot(_page(inner, theme["bg"], "Temario"), out_path)


# ============================ 5. CIERRE ============================
def render_cierre(content: dict, theme: dict, contact: dict, out_path: str, marca: str = "IS"):
    items = "".join(
        f'<div class="ci">{ICONS[k]}<span>{v}</span></div>' for k, v in contact.items()
    )
    inner = f"""
<style>
.wrap {{ position:absolute; left:{MARGIN_X}px; right:{MARGIN_X}px; top:110px; bottom:150px;
  display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; gap:38px; }}
.heading {{ font-family:'CocogoosePro'; font-weight:700; font-size:60px; line-height:1.1; color:{theme['title']}; text-wrap:balance; }}
.body {{ font-family:'Montserrat'; font-weight:500; font-size:38px; line-height:1.4; color:{theme['text']}; max-width:820px; }}
.body .hl {{ font-weight:700; color:{theme['accent2']}; }}
.logo {{ width:320px; height:320px; object-fit:contain; }}
.closing {{ font-family:'Montserrat'; font-weight:700; font-size:42px; line-height:1.3; color:{theme['text']}; }}
.footer {{ position:absolute; left:{MARGIN_X}px; right:{MARGIN_X}px; bottom:70px;
  border-top:1.5px solid #EAD9C9; padding-top:26px; display:flex; justify-content:center; gap:26px; flex-wrap:wrap; color:{theme['muted']}; }}
.ci {{ display:flex; align-items:center; gap:8px; font-family:'Montserrat'; font-weight:500; font-size:19px; }}
</style>
<div class="wrap">
  <div class="heading">{content['heading']}</div>
  <div class="body">{content['body_pre']}<span class="hl">{content['body_highlight']}</span></div>
  <img class="logo" src="data:image/png;base64,{LOGOS.get(marca, LOGO_IS_B64)}" />
  <div class="closing">{content['closing']}</div>
</div>
<div class="footer">{items}</div>"""
    _screenshot(_page(inner, theme["bg"], "Cierre"), out_path)
