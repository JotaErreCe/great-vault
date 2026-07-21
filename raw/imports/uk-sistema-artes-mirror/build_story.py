"""
HISTORIAS (1080×1920) — acompañan SIEMPRE a cada carrusel del feed.

Regla (JR 2026-07-20): cada arte publicado lleva al menos 1 historia relacionada.
Mapeo automático:
  - carrusel informativo  -> render_story_teaser  (anuncia el post, manda al feed)
  - promo de taller/curso -> render_story_promo   (flyer vertical + zona sticker link)
  - post de frase/cita    -> render_story_quote   (frase en grande, compartible)
  - material extra brief  -> render_story_tip     (consejo que NO está en el post)

Los stickers interactivos de IG (link, countdown, encuesta) los agrega Magoo al
publicar — estas plantillas dejan el espacio visual reservado (zona inferior).

ZONAS SEGURAS de IG Stories: la interfaz tapa ~250px arriba (avatar/nombre) y
~250px abajo (responder/compartir). Todo contenido crítico va entre y=280 y y=1640.
"""
from playwright.sync_api import sync_playwright
from pathlib import Path
import base64

from build_contenido import (
    BASE_DIR, COLOR_BG, COLOR_TEXT, COLOR_ACCENT, COCOGOOSE_B64, MONTSERRAT_B64, icon_html,
)
from build_promo import LOGOS, _img_b64

STORY_W, STORY_H = 1080, 1920
SAFE_TOP, SAFE_BOTTOM = 280, 280   # zonas que tapa la interfaz de IG
MARGIN_X = 90

COLOR_VERDE = "#76B142"


def _fonts() -> str:
    return f"""
@font-face {{ font-family:'CocogoosePro'; src:url(data:font/otf;base64,{COCOGOOSE_B64}) format('opentype'); font-weight:700; }}
@font-face {{ font-family:'Montserrat'; src:url(data:font/ttf;base64,{MONTSERRAT_B64}) format('truetype'); font-weight:100 900; }}
* {{ box-sizing:border-box; margin:0; padding:0; }}"""


def _page(inner: str, bg: str, label: str) -> str:
    return f"""<meta charset="utf-8">
<div data-document-role="page" data-label="{label}" style="
    width:{STORY_W}px;height:{STORY_H}px;position:relative;overflow:hidden;
    background:{bg};box-sizing:border-box;">
<style>{_fonts()}</style>
{inner}
</div>"""


def _screenshot(html: str, out_path: str):
    render_file = BASE_DIR / "_render.html"
    render_file.write_text(html, encoding="utf-8")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": STORY_W, "height": STORY_H})
        page.goto("file://" + str(render_file))
        page.wait_for_timeout(160)
        page.screenshot(path=str(BASE_DIR / out_path))
        browser.close()
    print("guardado:", out_path)


# ==================== 1. TEASER "nuevo post" (informativos) ====================
# Anuncia el carrusel y manda al feed. Magoo agrega el sticker de link del post
# en la zona inferior reservada.
def render_story_teaser(content: dict, out_path: str, marca: str = "UK"):
    """content: {icon, headline_main, headline_keyword, kicker?}"""
    from build_contenido import accent_for, accent_text_for
    accent, accent_fg = accent_for(marca), accent_text_for(marca)
    kicker = content.get("kicker", "Nuevo post en el feed")
    inner = f"""
<style>
.wrap {{ position:absolute; left:{MARGIN_X}px; right:{MARGIN_X}px; top:{SAFE_TOP}px; bottom:{SAFE_BOTTOM}px;
  display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; gap:44px; }}
.logo {{ width:150px; height:150px; object-fit:contain; }}
.kicker {{ font-family:'Montserrat'; font-weight:700; font-size:26px; letter-spacing:.1em; text-transform:uppercase;
  background:{accent}; color:{accent_fg}; padding:12px 30px; border-radius:30px; }}
.icon {{ font-size:84px; line-height:1; }}
.headline {{ font-family:'CocogoosePro'; font-weight:700; font-size:74px; line-height:1.1; color:{COLOR_TEXT}; text-wrap:balance; }}
.kw {{ color:{COLOR_TEXT}; box-shadow:inset 0 -18px 0 {accent}; }}
.cta {{ font-family:'Montserrat'; font-weight:600; font-size:32px; color:#6B6A64; margin-top:12px; }}
.arrow {{ font-size:56px; margin-top:-14px; }}
</style>
<div class="wrap">
  <img class="logo" src="data:image/png;base64,{LOGOS.get(marca, LOGOS['UK'])}" />
  <div class="kicker">{kicker}</div>
  <div class="icon">{icon_html(content.get('icon',''))}</div>
  <div class="headline">{content['headline_main']} <span class="kw">{content['headline_keyword']}</span></div>
  <div class="cta">Toca abajo para ver el post completo</div>
  <div class="arrow">👇</div>
</div>"""
    _screenshot(_page(inner, COLOR_BG, "Story-Teaser"), out_path)


# ==================== 2. STORY-FLYER promo (talleres/cursos) ====================
# Versión vertical de la portada-flyer: foto + onda + datos + CTA. La zona
# inferior queda para el sticker de link "Regístrate".
def render_story_promo(content: dict, theme: dict, out_path: str, marca: str = "IS"):
    """content: {image_path, badge?, title, rows:[{icon,value}], cta}"""
    PHOTO_H = 860
    img_data, img_mime = _img_b64(content["image_path"])
    bg = theme["cover_bg"]
    chips = "".join(
        f'<div class="chip"><span class="ci">{r["icon"]}</span>{r["value"]}</div>'
        for r in content["rows"]
    )
    badge = f'<div class="badge">{content["badge"]}</div>' if content.get("badge") else ""
    inner = f"""
<style>
.photo {{ position:absolute; top:0; left:0; width:{STORY_W}px; height:{PHOTO_H}px; object-fit:cover; object-position:center 30%; }}
.fade {{ position:absolute; top:{PHOTO_H-260}px; left:0; width:{STORY_W}px; height:280px;
  background:linear-gradient(to bottom, rgba(0,0,0,0) 0%, {bg} 90%); }}
.wave {{ position:absolute; top:{PHOTO_H-100}px; left:0; width:{STORY_W}px; height:160px; }}
.logo-chip {{ position:absolute; top:{SAFE_TOP+10}px; left:44px; width:120px; height:120px; border-radius:50%;
  background:#FFFFFF; box-shadow:0 10px 26px rgba(60,30,20,.20); display:flex; align-items:center; justify-content:center; }}
.logo-chip img {{ width:96px; height:96px; object-fit:contain; }}
.content {{ position:absolute; left:{MARGIN_X}px; right:{MARGIN_X}px; top:{PHOTO_H+30}px; bottom:{SAFE_BOTTOM}px;
  display:flex; flex-direction:column; align-items:center; text-align:center; gap:26px; }}
.badge {{ font-family:'Montserrat'; font-weight:700; font-size:24px; letter-spacing:.08em; text-transform:uppercase;
  background:{theme['title']}; color:#ffffff; padding:10px 28px; border-radius:26px; }}
.title {{ font-family:'CocogoosePro'; font-weight:700; font-size:72px; line-height:1.04; color:{theme['title']}; text-wrap:balance; }}
.chips {{ display:flex; flex-wrap:wrap; justify-content:center; gap:16px; }}
.chip {{ display:flex; align-items:center; gap:10px; background:#FFFFFF; border:1.5px solid {theme['chip_border']};
  border-radius:44px; padding:14px 26px; font-family:'Montserrat'; font-weight:600; font-size:29px; color:{theme['text']}; }}
.chip .ci {{ font-size:28px; }}
.cta {{ font-family:'CocogoosePro'; font-weight:700; font-size:42px; color:#ffffff;
  background:{theme['title']}; padding:22px 62px; border-radius:50px; margin-top:10px;
  box-shadow:0 12px 30px rgba(0,0,0,.18); }}
.hint {{ font-family:'Montserrat'; font-weight:600; font-size:28px; color:{theme['muted']}; }}
</style>
<img class="photo" src="data:image/{img_mime};base64,{img_data}" />
<div class="fade"></div>
<svg class="wave" viewBox="0 0 1080 160" preserveAspectRatio="none">
  <path d="M0,80 C 200,20 420,20 580,62 C 740,104 910,110 1080,56 L1080,160 L0,160 Z" fill="{bg}"/>
</svg>
<div class="logo-chip"><img src="data:image/png;base64,{LOGOS.get(marca, LOGOS['IS'])}" /></div>
<div class="content">
  {badge}
  <div class="title">{content['title']}</div>
  <div class="chips">{chips}</div>
  <div class="cta">{content['cta']}</div>
  <div class="hint">El link está aquí abajo 👇</div>
</div>"""
    _screenshot(_page(inner, bg, "Story-Promo"), out_path)


# ==================== 3. QUOTE (posts de frase) ====================
def render_story_quote(content: dict, out_path: str, marca: str = "UK"):
    """content: {quote, author?}"""
    from build_contenido import accent_for
    accent = accent_for(marca)
    author = f'<div class="author">— {content["author"]}</div>' if content.get("author") else ""
    inner = f"""
<style>
.wrap {{ position:absolute; left:{MARGIN_X}px; right:{MARGIN_X}px; top:{SAFE_TOP}px; bottom:{SAFE_BOTTOM}px;
  display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; gap:40px; }}
.mark {{ font-family:'CocogoosePro'; font-size:170px; line-height:.6; color:{accent}; }}
.quote {{ font-family:'CocogoosePro'; font-weight:700; font-size:66px; line-height:1.22; color:{COLOR_TEXT}; text-wrap:balance; }}
.author {{ font-family:'Montserrat'; font-weight:600; font-size:32px; color:#6B6A64; }}
.author::first-letter {{ color:{accent}; }}
.logo {{ width:130px; height:130px; object-fit:contain; margin-top:16px; }}
</style>
<div class="wrap">
  <div class="mark">“</div>
  <div class="quote">{content['quote']}</div>
  {author}
  <img class="logo" src="data:image/png;base64,{LOGOS.get(marca, LOGOS['UK'])}" />
</div>"""
    _screenshot(_page(inner, COLOR_BG, "Story-Quote"), out_path)


# ==================== 4. TIP complemento (valor extra) ====================
# Un consejo que NO está en el post — da razón propia de existir a la historia.
def render_story_tip(content: dict, out_path: str, marca: str = "UK"):
    """content: {kicker?, icon, tip, note?}"""
    kicker = content.get("kicker", "Tip extra")
    note = f'<div class="note">{content["note"]}</div>' if content.get("note") else ""
    inner = f"""
<style>
.wrap {{ position:absolute; left:{MARGIN_X}px; right:{MARGIN_X}px; top:{SAFE_TOP}px; bottom:{SAFE_BOTTOM}px;
  display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; gap:42px; }}
.kicker {{ font-family:'Montserrat'; font-weight:700; font-size:26px; letter-spacing:.1em; text-transform:uppercase;
  background:{COLOR_VERDE}; color:#ffffff; padding:12px 30px; border-radius:30px; }}
.icon {{ font-size:96px; line-height:1; }}
.tip {{ font-family:'CocogoosePro'; font-weight:700; font-size:62px; line-height:1.18; color:{COLOR_TEXT}; text-wrap:balance; }}
.note {{ font-family:'Montserrat'; font-weight:500; font-size:34px; line-height:1.4; color:#5B5A54; max-width:820px; }}
.save {{ font-family:'Montserrat'; font-weight:600; font-size:30px; color:#6B6A64; margin-top:10px; }}
.logo {{ width:120px; height:120px; object-fit:contain; }}
</style>
<div class="wrap">
  <div class="kicker">{kicker}</div>
  <div class="icon">{icon_html(content.get('icon','💡'))}</div>
  <div class="tip">{content['tip']}</div>
  {note}
  <div class="save">Guarda esta historia para tenerla a mano 📌</div>
  <img class="logo" src="data:image/png;base64,{LOGOS.get(marca, LOGOS['UK'])}" />
</div>"""
    _screenshot(_page(inner, COLOR_BG, "Story-Tip"), out_path)
