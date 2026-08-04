"""
Refinamiento de la paleta elegida (#3 Pizarra & Rojo) — más viva + resaltado
tipo highlighter (marcador translúcido). Muestra 2 intensidades de highlight.
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = Path(__file__).resolve().parent
COCO = (BASE / "cocogoosepro_bold_b64.txt").read_text().strip()
MONT = (BASE / "montserrat_b64.txt").read_text().strip()
OUT = Path.home() / ("Library/CloudStorage/GoogleDrive-jcastaneda@kidsunderstanding.com/"
                     "My Drive/Administración/Artes/2026/Campañas/"
                     "Especialización Alimentación 2026 - Mockups")

BG = "#F6F4F1"; TEXTO = "#263039"; PRIM = "#35617A"; ACC = "#D44B45"; APOYO = "#F0DAD3"
HL_SOFT = "rgba(212,75,69,0.16)"    # highlighter muy tenue
HL_MED = "rgba(212,75,69,0.28)"     # highlighter un punto más marcado

def hero(hl, etiqueta):
    return f"""
    <div class="card" style="background:{BG}">
      <div class="tag">{etiqueta}</div>
      <div class="kicker" style="background:{APOYO};color:{TEXTO}">ESPECIALIZACIÓN CLÍNICA</div>
      <div class="title" style="color:{PRIM}">Dificultades de <span class="hl" style="--hl:{hl}">la Alimentación</span></div>
      <div class="sub">Un método clínico para los casos que nadie te enseñó a resolver.</div>
      <div class="cta" style="background:{ACC}">Regístrate</div>
    </div>"""

html = f"""<meta charset="utf-8">
<div style="width:1080px;height:1200px;background:#E9E7E2;box-sizing:border-box;position:relative;overflow:hidden;">
<style>
@font-face {{ font-family:'CocogoosePro'; src:url(data:font/otf;base64,{COCO}) format('opentype'); font-weight:700; }}
@font-face {{ font-family:'Montserrat'; src:url(data:font/ttf;base64,{MONT}) format('truetype'); font-weight:100 900; }}
* {{ box-sizing:border-box; margin:0; padding:0; }}
.head {{ height:110px; display:flex; flex-direction:column; align-items:center; justify-content:center; background:{PRIM}; color:#fff; }}
.head b {{ font-family:'CocogoosePro'; font-size:32px; }}
.head small {{ font-family:'Montserrat'; font-weight:600; font-size:14px; opacity:.9; }}
.card {{ height:400px; padding:56px 64px; display:flex; flex-direction:column; align-items:flex-start; gap:20px; position:relative; }}
.tag {{ position:absolute; top:20px; right:28px; font-family:'Montserrat'; font-weight:700; font-size:14px; color:{PRIM}; opacity:.6; }}
.kicker {{ font-family:'Montserrat'; font-weight:700; font-size:16px; letter-spacing:.06em; padding:8px 18px; border-radius:22px; }}
.title {{ font-family:'CocogoosePro'; font-size:58px; line-height:1.05; }}
.hl {{ background: linear-gradient(120deg, var(--hl) 0%, var(--hl) 100%); background-repeat:no-repeat;
  background-size:100% 42%; background-position:0 82%; padding:0 4px; }}
.sub {{ font-family:'Montserrat'; font-weight:500; font-size:26px; color:{TEXTO}; opacity:.85; }}
.cta {{ font-family:'CocogoosePro'; font-size:28px; color:#fff; padding:14px 44px; border-radius:38px; }}
.swatches {{ display:flex; gap:16px; padding:24px 64px; align-items:center; }}
.sw {{ font-family:'Montserrat'; font-weight:600; font-size:12px; color:#555; text-align:center; }}
.chip {{ display:block; width:56px; height:56px; border-radius:12px; margin-bottom:6px; }}
</style>
<div class="head"><b>Pizarra & Rojo — refinada</b><small>colores con más vida · resaltado tipo highlighter</small></div>
{hero(HL_SOFT, "Highlight muy tenue (16%)")}
{hero(HL_MED, "Highlight un punto más (28%)")}
<div class="swatches">
  <div class="sw"><span class="chip" style="background:{BG};border:1px solid #ddd"></span>Fondo<br>{BG}</div>
  <div class="sw"><span class="chip" style="background:{TEXTO}"></span>Texto<br>{TEXTO}</div>
  <div class="sw"><span class="chip" style="background:{PRIM}"></span>Primario<br>{PRIM}</div>
  <div class="sw"><span class="chip" style="background:{ACC}"></span>Acento<br>{ACC}</div>
  <div class="sw"><span class="chip" style="background:{APOYO}"></span>Apoyo<br>{APOYO}</div>
  <div class="sw"><span class="chip" style="background:linear-gradient(180deg,#fff 58%, {ACC} 58%);border:1px solid #ddd"></span>Highlight<br>translúcido</div>
</div>
</div>"""

f = BASE / "_final3.html"; f.write_text(html, encoding="utf-8")
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width":1080,"height":1200})
    pg.goto("file://"+str(f)); pg.wait_for_timeout(200)
    pg.screenshot(path=str(OUT/"paleta_final_pizarra_rojo.png")); b.close()
f.unlink(missing_ok=True)
print("guardado:", OUT/"paleta_final_pizarra_rojo.png")
