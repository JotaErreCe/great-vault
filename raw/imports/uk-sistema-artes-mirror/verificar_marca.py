"""
GUARDARRAÍL DE FONDO POR MARCA (JR 2026-08-03).

UK va sobre crema `#FBFAF6` e IS sobre celeste claro `#F4F9FA`. El fondo se
activa con `"marca": "IS"` en el dict de contenido de CADA slide; si se olvida
en uno solo, ese slide cae al default de UK y sale con el fondo equivocado en
medio del carrusel. El error es silencioso: nada falla, solo se ve mal.

Este script cierra ese hueco: lee los PNG ya renderizados y verifica que el
fondo real de cada archivo sea el que le toca a la marca. Se corre SIEMPRE al
terminar de generar, antes de reportar.

Uso:
    python3 verificar_marca.py "<carpeta>" [UK|IS]
    python3 verificar_marca.py --todas "<carpeta padre>"

Si no se pasa la marca, se deduce del nombre de la carpeta ("- IS " / "- UK ").
Sale con código 1 si encuentra algún archivo con el fondo equivocado.
"""
import sys
from pathlib import Path

from PIL import Image

from build_contenido import BACKGROUNDS

# Esquinas a muestrear: el fondo se ve en los bordes en todas las plantillas
# (los slides con foto tienen la ventana centrada, nunca a sangre).
SONDAS = [(0.014, 0.014), (0.986, 0.014), (0.014, 0.986), (0.986, 0.986)]


def marca_de_carpeta(nombre: str) -> str | None:
    for m in ("IS", "UK"):
        if f"- {m} " in nombre or nombre.startswith(f"{m} "):
            return m
    return None


def _hex(px) -> str:
    r, g, b = px[:3]
    return f"#{r:02X}{g:02X}{b:02X}"


def verificar(carpeta: Path, marca: str) -> list[tuple[str, str]]:
    """Devuelve la lista de (archivo, fondo_encontrado) que NO coinciden."""
    esperado = BACKGROUNDS[marca].upper()
    malos = []
    for f in sorted(carpeta.glob("*.png")):
        im = Image.open(f).convert("RGB")
        W, H = im.size
        vistos = {_hex(im.getpixel((int(W * x), int(H * y)))) for x, y in SONDAS}
        # basta con que ninguna esquina sea el fondo esperado para considerarlo mal:
        # así los slides con elementos que tocan una esquina no dan falso positivo.
        if esperado not in vistos:
            malos.append((f.name, ", ".join(sorted(vistos))))
    return malos


def revisar_y_reportar(carpeta: Path, marca: str | None = None) -> bool:
    marca = marca or marca_de_carpeta(carpeta.name)
    if marca is None:
        # Carpetas que no son piezas (muestras, pruebas): se omiten, no fallan.
        print(f"[–] {carpeta.name}: omitida (sin marca en el nombre)")
        return True
    malos = verificar(carpeta, marca)
    total = len(list(carpeta.glob("*.png")))
    if malos:
        print(f"[✗] {carpeta.name} ({marca}, esperado {BACKGROUNDS[marca]}):")
        for nombre, visto in malos:
            print(f"      {nombre} -> {visto}")
        print("      Causa casi segura: falta \"marca\" en el dict de ese slide.")
        return False
    print(f"[✓] {carpeta.name}: {total} archivos, todos en {BACKGROUNDS[marca]} ({marca})")
    return True


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        raise SystemExit(2)
    todas = args[0] == "--todas"
    if todas:
        args = args[1:]
    carpetas = [Path(args[0]).expanduser()]
    if todas:
        carpetas = [d for d in sorted(carpetas[0].iterdir()) if d.is_dir()]
    marca = args[1] if len(args) > 1 else None
    ok = all(revisar_y_reportar(c, marca) for c in carpetas)
    raise SystemExit(0 if ok else 1)
