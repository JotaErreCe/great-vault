"""
Buscador de fotos reales para los templates de UK.
Reemplaza la librería de Canva (que no es accesible por API).

Fuentes, en orden de preferencia:
  1. Pexels    — stock profesional (requiere API key gratuita en pexels_key.txt)
  2. Openverse — fotos con licencia libre, sin registro (respaldo)

Uso CLI:
    python3 buscar_foto.py "niño comiendo" salida.jpg
    python3 buscar_foto.py "manos jugando plastilina" foto.jpg --horizontal

Uso como módulo:
    from buscar_foto import descargar_foto
    info = descargar_foto("terapia de lenguaje", "foto.jpg", vertical=True)
"""
import json
import subprocess
import sys
import urllib.parse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PEXELS_KEY_FILE = BASE_DIR / "pexels_key.txt"
UA = "UnderstandingKids-social/1.0"


def _get_pexels_key() -> str | None:
    if PEXELS_KEY_FILE.exists():
        k = PEXELS_KEY_FILE.read_text().strip()
        return k or None
    return None


def _curl(url: str, headers: dict | None = None) -> bytes:
    cmd = ["curl", "-sSL", "--max-time", "60", "-A", UA]
    for k, v in (headers or {}).items():
        cmd += ["-H", f"{k}: {v}"]
    cmd.append(url)
    res = subprocess.run(cmd, capture_output=True)
    if res.returncode != 0:
        raise RuntimeError(f"curl error: {res.stderr.decode()[:200]}")
    return res.stdout


def _http_json(url: str, headers: dict | None = None) -> dict:
    return json.loads(_curl(url, headers).decode())


def _buscar_pexels(query: str, vertical: bool, key: str) -> list[dict]:
    orient = "portrait" if vertical else "landscape"
    url = (
        "https://api.pexels.com/v1/search?query="
        + urllib.parse.quote(query)
        + f"&orientation={orient}&per_page=15"
    )
    data = _http_json(url, headers={"Authorization": key})
    out = []
    for p in data.get("photos", []):
        out.append({
            "url": p["src"].get("large2x") or p["src"].get("large"),
            "credito": f'Foto de {p.get("photographer","?")} en Pexels',
            "fuente": "pexels",
        })
    return out


def _openverse_url(query: str, aspect: str | None) -> str:
    base = ("https://api.openverse.org/v1/images/?q="
            + urllib.parse.quote(query) + "&license_type=commercial&page_size=15")
    return base + (f"&aspect_ratio={aspect}" if aspect else "")


def _buscar_openverse(query: str, vertical: bool) -> list[dict]:
    aspect = "tall" if vertical else "wide"
    # 1º intento con orientación; si viene vacío, reintento sin ese filtro
    data = _http_json(_openverse_url(query, aspect))
    results = data.get("results", [])
    if not results:
        data = _http_json(_openverse_url(query, None))
        results = data.get("results", [])
    out = []
    for r in results:
        out.append({
            "url": r.get("url"),
            "credito": f'{r.get("creator","?")} / {r.get("source","openverse")} ({r.get("license","")})',
            "fuente": "openverse",
        })
    return out


def buscar(query: str, vertical: bool = True) -> list[dict]:
    """Devuelve lista de candidatos {url, credito, fuente}, Pexels primero."""
    key = _get_pexels_key()
    resultados = []
    if key:
        try:
            resultados = _buscar_pexels(query, vertical, key)
        except Exception as e:
            print(f"[aviso] Pexels falló ({e}); usando Openverse", file=sys.stderr)
    if not resultados:
        resultados = _buscar_openverse(query, vertical)
    return resultados


def descargar_foto(query: str, out_path: str, vertical: bool = True, indice: int = 0) -> dict:
    """Descarga el candidato `indice` de la búsqueda a out_path. Devuelve su metadata."""
    candidatos = buscar(query, vertical)
    if not candidatos:
        raise RuntimeError(f"Sin resultados para: {query!r}")
    elegido = candidatos[indice]
    dest = (BASE_DIR / out_path) if not Path(out_path).is_absolute() else Path(out_path)
    dest.write_bytes(_curl(elegido["url"]))
    elegido["archivo"] = str(dest)
    return elegido


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    vertical = "--horizontal" not in sys.argv
    if len(args) < 2:
        print("uso: python3 buscar_foto.py \"consulta\" salida.jpg [--horizontal]")
        sys.exit(1)
    info = descargar_foto(args[0], args[1], vertical=vertical)
    print("descargada:", info["archivo"])
    print("fuente:", info["fuente"], "|", info["credito"])
