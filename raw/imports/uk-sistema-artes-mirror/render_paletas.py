"""
Tablero de paletas EDA26 — COHERENTES (método workovereasy / Figma).
Principio: base sofisticada (analógica/monocromática) + 1 acento, TODO a una
saturación pareja y tenue → los colores se leen como un sistema, no sueltos.
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = Path(__file__).resolve().parent
COCO = (BASE / "cocogoosepro_bold_b64.txt").read_text().strip()
MONT = (BASE / "montserrat_b64.txt").read_text().strip()

OUT = Path.home() / ("Library/CloudStorage/GoogleDrive-jcastaneda@kidsunderstanding.com/"
                     "My Drive/Administración/Artes/2026/Campañas/"
                     "Especialización Alimentación 2026 - Mockups")

# name, metodo, bg, texto, primario, acento(apagado), apoyo(tenue), on_acc
PALETAS = [
    ("1 · Azul humo & Mostaza", "Complementario apagado", "#F5F3EE", "#2B3640", "#4E6E7E", "#C9A24A", "#E7DECF", "#2B3640"),
    ("2 · Ciruela & Salvia",    "Análogo / split apagado", "#F6F3F4", "#322A33", "#6E5670", "#7E9A6E", "#E1D8DF", "#241E25"),
    ("3 · Pizarra & Rojo suave","Complementario apagado", "#F5F3F0", "#2A3138", "#4A6470", "#BC5A5A", "#DBE0DF", "#FFFFFF"),
]

rows = ""
for name, metodo, bg, texto, prim, acc, apoyo, ona in PALETAS:
    rows += f"""
    <div class="row" style="background:{bg}">
      <div class="left">
        <div class="pname" style="color:{prim}">{name}</div>
        <div class="pmet">{metodo}</div>
        <div class="swatches">
          <div class="sw"><span class="chip" style="background:{bg};border:1px solid #E3E0D8"></span>Fondo<br>{bg}</div>
          <div class="sw"><span class="chip" style="background:{texto}"></span>Texto<br>{texto}</div>
          <div class="sw"><span class="chip" style="background:{prim}"></span>Primario<br>{prim}</div>
          <div class="sw"><span class="chip" style="background:{acc}"></span>Acento<br>{acc}</div>
          <div class="sw"><span class="chip" style="background:{apoyo}"></span>Apoyo<br>{apoyo}</div>
        </div>
      </div>
      <div class="right">
        <div class="kicker" style="background:{apoyo};color:{texto}">ESPECIALIZACIÓN CLÍNICA</div>
        <div class="title" style="color:{prim}">Dificultades de <span style="box-shadow:inset 0 -0.30em 0 {acc};color:{texto}">la Alimentación</span></div>
        <div class="cta" style="background:{acc};color:{ona}">Regístrate</div>
      </div>
    </div>"""

html = f"""<meta charset="utf-8">
<div style="width:1080px;height:1000px;background:#EDEBE6;box-sizing:border-box;position:relative;overflow:hidden;">
<style>
@font-face {{ font-family:'CocogoosePro'; src:url(data:font/otf;base64,{COCO}) format('opentype'); font-weight:700; }}
@font-face {{ font-family:'Montserrat'; src:url(data:font/ttf;base64,{MONT}) format('truetype'); font-weight:100 900; }}
* {{ box-sizing:border-box; margin:0; padding:0; }}
.head {{ height:118px; display:flex; flex-direction:column; align-items:center; justify-content:center; background:#4E6E7E;
  font-family:'CocogoosePro'; color:#fff; font-size:32px; text-align:center; gap:4px; }}
.head small {{ font-family:'Montserrat'; font-weight:600; font-size:15px; opacity:.9; }}
.row {{ height:294px; display:flex; align-items:center; gap:30px; padding:0 46px; }}
.left {{ width:360px; }}
.pname {{ font-family:'CocogoosePro'; font-size:26px; line-height:1.1; }}
.pmet {{ font-family:'Montserrat'; font-weight:600; font-size:13px; color:#8A8A82; margin:4px 0 16px; }}
.swatches {{ display:flex; gap:12px; }}
.sw {{ font-family:'Montserrat'; font-weight:600; font-size:11px; color:#555; text-align:center; line-height:1.3; width:60px; }}
.chip {{ display:block; width:44px; height:44px; border-radius:10px; margin:0 auto 6px; }}
.right {{ flex:1; display:flex; flex-direction:column; align-items:flex-start; gap:16px; padding-left:20px; }}
.kicker {{ font-family:'Montserrat'; font-weight:700; font-size:15px; letter-spacing:.06em; padding:7px 16px; border-radius:20px; }}
.title {{ font-family:'CocogoosePro'; font-size:44px; line-height:1.06; }}
.cta {{ font-family:'CocogoosePro'; font-size:26px; padding:12px 38px; border-radius:34px; }}
</style>
<div class="head">Paletas coherentes<small>base sofisticada + 1 acento · saturación pareja (tenue)</small></div>
{rows}
</div>"""

render_file = BASE / "_paletas.html"
render_file.write_text(html, encoding="utf-8")
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1000})
    pg.goto("file://" + str(render_file))
    pg.wait_for_timeout(200)
    pg.screenshot(path=str(OUT / "paletas_coherentes.png"))
    b.close()
render_file.unlink(missing_ok=True)
print("guardado:", OUT / "paletas_coherentes.png")
