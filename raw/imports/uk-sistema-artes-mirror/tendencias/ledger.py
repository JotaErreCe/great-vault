#!/usr/bin/env python3
"""
Ledger del agente de tendencias (UK / IS).

Guarda estado entre corridas para poder medir COSAS QUE CAMBIAN, no fotos sueltas:

  posts.csv   historial de posts vistos (cuenta, shortcode, fecha, tipo, likes, comentarios)
  angles.jsonl  log de angulos/formatos detectados y en que cuentas van apareciendo

Uso:
  python3 ledger.py stats          baseline por cuenta + salud de la cuenta
  python3 ledger.py outliers [N]   posts de los ultimos N dias por encima de su propia mediana
  python3 ledger.py angles         estado de convergencia de cada angulo
  python3 ledger.py nuevos <archivo.csv>   que shortcodes del archivo no estaban en el ledger

Notas de diseno:
- likes = -1 significa que la cuenta oculta los likes. Se ignora para la mediana de likes
  y se usa comentarios como metrica de respaldo.
- El outlier es SIEMPRE relativo a la propia cuenta. Comparar likes crudos entre cuentas
  no significa nada: 1,200 likes es flojo para paupautista y enorme para alimento.red.
"""

import csv
import json
import os
import statistics
import sys
from datetime import date, datetime, timedelta

BASE = os.path.dirname(os.path.abspath(__file__))
POSTS = os.path.join(BASE, "posts.csv")
ANGLES = os.path.join(BASE, "angles.jsonl")

TIPO = {"V": "reel", "S": "carrusel", "I": "estatico"}


def cargar():
    with open(POSTS, newline="", encoding="utf-8") as f:
        filas = list(csv.DictReader(f))
    for r in filas:
        r["likes"] = int(r["likes"])
        r["comentarios"] = int(r["comentarios"])
        r["fecha_d"] = datetime.strptime(r["fecha"], "%Y-%m-%d").date()
    return filas


def por_cuenta(filas):
    d = {}
    for r in filas:
        d.setdefault(r["cuenta"], []).append(r)
    return d


def baseline(posts):
    """Mediana de likes (ignorando ocultos) y de comentarios."""
    likes = [p["likes"] for p in posts if p["likes"] >= 0]
    coments = [p["comentarios"] for p in posts]
    return {
        "n": len(posts),
        "likes_ocultos": all(p["likes"] < 0 for p in posts),
        "med_likes": statistics.median(likes) if likes else None,
        "med_coments": statistics.median(coments) if coments else 0,
        "ultimo": max(p["fecha_d"] for p in posts),
        "pct_carrusel": round(
            100 * sum(1 for p in posts if p["tipo"] in ("S", "I")) / len(posts)
        ),
    }


def cmd_stats(filas):
    hoy = date.today()
    print(f"{'cuenta':<22}{'n':>4}{'med.lk':>8}{'med.cm':>8}{'%estat':>8}{'dias':>7}  estado")
    print("-" * 76)
    for cuenta, posts in sorted(por_cuenta(filas).items()):
        b = baseline(posts)
        dias = (hoy - b["ultimo"]).days
        estado = []
        if dias > 60:
            estado.append("INACTIVA")
        if b["likes_ocultos"]:
            estado.append("likes ocultos -> usar comentarios")
        if b["pct_carrusel"] >= 60:
            estado.append("fuente de FORMATOS")
        elif b["pct_carrusel"] <= 15:
            estado.append("fuente de ANGULOS")
        lk = "oculto" if b["med_likes"] is None else f"{b['med_likes']:.0f}"
        print(
            f"{cuenta:<22}{b['n']:>4}{lk:>8}{b['med_coments']:>8.0f}"
            f"{b['pct_carrusel']:>7}%{dias:>7}  {'; '.join(estado)}"
        )


def cmd_outliers(filas, dias=10, umbral=2.0):
    hoy = date.today()
    corte = hoy - timedelta(days=dias)
    print(f"Posts desde {corte} por encima de {umbral}x la mediana de su propia cuenta\n")
    hits = []
    for cuenta, posts in por_cuenta(filas).items():
        b = baseline(posts)
        for p in posts:
            if p["fecha_d"] < corte:
                continue
            if b["likes_ocultos"] or p["likes"] < 0:
                base, val, met = b["med_coments"], p["comentarios"], "cm"
            else:
                base, val, met = b["med_likes"], p["likes"], "lk"
            if not base:
                continue
            ratio = val / base
            if ratio >= umbral:
                hits.append((ratio, cuenta, p, met, val, base))
    for ratio, cuenta, p, met, val, base in sorted(hits, reverse=True):
        print(
            f"{ratio:5.1f}x  {cuenta:<20} {TIPO[p['tipo']]:<9} {p['fecha']}  "
            f"{met}={val} (mediana {base:.0f})  https://instagram.com/p/{p['shortcode']}/"
        )
    if not hits:
        print("(ninguno)")


def cmd_angles():
    if not os.path.exists(ANGLES):
        print("(sin angulos registrados)")
        return
    with open(ANGLES, encoding="utf-8") as f:
        registros = [json.loads(l) for l in f if l.strip()]
    for a in sorted(registros, key=lambda x: -len(x["cuentas"])):
        n = len(a["cuentas"])
        señal = "CONVERGE" if n >= 3 else ("emergente" if n == 2 else "aislado")
        print(f"[{señal}] {a['slug']}  ({n} cuentas, visto 1a vez {a['primera_vez']})")
        print(f"    {a['descripcion']}")
        print(f"    cuentas: {', '.join(a['cuentas'])}")
        if a.get("sugerido_en_notion"):
            print(f"    ya sugerido: {a['sugerido_en_notion']}")
        print()


def cmd_nuevos(filas, ruta):
    vistos = {r["shortcode"] for r in filas}
    with open(ruta, newline="", encoding="utf-8") as f:
        entrantes = list(csv.DictReader(f))
    nuevos = [r for r in entrantes if r["shortcode"] not in vistos]
    print(f"{len(nuevos)} nuevos de {len(entrantes)}")
    for r in nuevos:
        print(f"  {r['cuenta']:<20} {r['fecha']}  https://instagram.com/p/{r['shortcode']}/")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "stats"
    if cmd == "angles":
        cmd_angles()
    else:
        filas = cargar()
        if cmd == "stats":
            cmd_stats(filas)
        elif cmd == "outliers":
            cmd_outliers(filas, int(sys.argv[2]) if len(sys.argv) > 2 else 10)
        elif cmd == "nuevos":
            cmd_nuevos(filas, sys.argv[2])
        else:
            print(__doc__)
