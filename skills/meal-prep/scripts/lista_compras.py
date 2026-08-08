#!/usr/bin/env python3
"""Lista de compras: menú semanal → Apple Reminders (lista compartida con Magoo).

Lee la sección `## Ingredientes` del menú, resta lo que ya está en despensa.md,
agrupa por pasillo y lo empuja a Recordatorios.

Formato esperado en el menú:
    ## Ingredientes
    - Pechuga de pollo | 1.5 kg | Carnes
    - Güisquil | 4 u | Verduras

Por el manual de Reminders de JR, escribir requiere aprobación explícita:
por eso el modo por defecto es --dry-run.

Uso:
    lista_compras.py --menu <ruta.md>                  # dry-run (por defecto)
    lista_compras.py --menu <ruta.md> --escribir       # escribe en Reminders
    lista_compras.py --check-lista
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True  # el vault lo sincroniza Syncthing: nada de __pycache__
sys.path.insert(0, str(Path(__file__).parent))
from perfil import dir_datos  # noqa: E402

LISTA_DESTINO = "🛒 Súper"

ORDEN_PASILLOS = [
    "Verduras", "Frutas", "Carnes", "Pescadería", "Lácteos",
    "Abarrotes", "Panadería", "Congelados", "Otros",
]


def osa(script: str) -> str:
    r = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"AppleScript falló: {r.stderr.strip()}")
    return r.stdout.strip()


def listas_existentes() -> list:
    out = osa(
        'tell application "Reminders"\n'
        ' set o to ""\n'
        " repeat with l in lists\n"
        '  set o to o & name of l & "\n"\n'
        " end repeat\n"
        " return o\n"
        "end tell"
    )
    return [x for x in out.splitlines() if x.strip()]


def parsear_ingredientes(ruta: Path) -> list:
    if not ruta.exists():
        sys.exit(f"No existe el menú: {ruta}")
    texto = ruta.read_text(encoding="utf-8")
    m = re.search(r"^##\s*Ingredientes\s*$(.*?)(?=^##\s|\Z)", texto, re.M | re.S)
    if not m:
        sys.exit(f"El menú no tiene sección '## Ingredientes': {ruta}")

    items = []
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line.startswith("-"):
            continue
        partes = [p.strip() for p in line.lstrip("-").split("|")]
        if not partes or not partes[0]:
            continue
        items.append({
            "nombre": partes[0],
            "cantidad": partes[1] if len(partes) > 1 else "",
            "pasillo": partes[2] if len(partes) > 2 else "Otros",
        })
    if not items:
        sys.exit("La sección '## Ingredientes' está vacía.")
    return items


def leer_despensa() -> set:
    p = dir_datos() / "despensa.md"
    if not p.exists():
        return set()
    fuera = set()
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("-"):
            nombre = line.lstrip("-").split("|")[0].strip().lower()
            if nombre:
                fuera.add(nombre)
    return fuera


def agrupar(items: list) -> dict:
    g = {}
    for it in items:
        g.setdefault(it["pasillo"], []).append(it)
    return dict(sorted(
        g.items(),
        key=lambda kv: ORDEN_PASILLOS.index(kv[0]) if kv[0] in ORDEN_PASILLOS else 99,
    ))


def etiqueta(it: dict) -> str:
    return f"{it['nombre']} — {it['cantidad']}" if it["cantidad"] else it["nombre"]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--menu", type=Path)
    ap.add_argument("--lista", default=LISTA_DESTINO)
    ap.add_argument("--escribir", action="store_true", help="Escribe en Reminders (requiere OK de JR)")
    ap.add_argument("--check-lista", action="store_true")
    a = ap.parse_args()

    existentes = listas_existentes()

    if a.check_lista:
        print("Listas en Recordatorios:")
        for l in existentes:
            print(f"  · {l}")
        print(f"\n'{a.lista}': {'existe' if a.lista in existentes else 'NO EXISTE'}")
        if a.lista not in existentes:
            print(
                "\nCrearla a mano en la app (AppleScript no puede definir tipo Comestibles\n"
                "ni compartir por iCloud):\n"
                "  Recordatorios › Archivo › Lista nueva\n"
                f"  Nombre: {a.lista}  ·  Tipo: Comestibles\n"
                "  Botón Compartir → invitar a Magoo con permiso de edición"
            )
        return

    if not a.menu:
        ap.error("Falta --menu (o usá --check-lista)")

    items = parsear_ingredientes(a.menu)
    fuera = leer_despensa()

    comprar = [i for i in items if i["nombre"].lower() not in fuera]
    omitidos = [i for i in items if i["nombre"].lower() in fuera]

    grupos = agrupar(comprar)

    print(f"Lista de compras — {a.menu.name}")
    print(f"Destino: {a.lista}\n")
    for pasillo, lst in grupos.items():
        print(f"  {pasillo}")
        for it in lst:
            print(f"    · {etiqueta(it)}")
        print()
    print(f"Total: {len(comprar)} ítems")
    if omitidos:
        print(f"Omitidos por despensa ({len(omitidos)}): {', '.join(i['nombre'] for i in omitidos)}")

    if not a.escribir:
        print("\n[dry-run] No se escribió nada. Para escribir de verdad, con OK de JR:")
        print(f"  python3 {Path(__file__).name} --menu {a.menu} --escribir")
        return

    if a.lista not in existentes:
        sys.exit(
            f"\nLa lista '{a.lista}' no existe. Hay que crearla en la app primero "
            f"(tipo Comestibles + compartida). Corré --check-lista para las instrucciones."
        )

    n = 0
    for pasillo, lst in grupos.items():
        for it in lst:
            nombre = etiqueta(it).replace("\\", "\\\\").replace('"', '\\"')
            osa(
                f'tell application "Reminders" to make new reminder '
                f'at list "{a.lista}" with properties {{name:"{nombre}"}}'
            )
            n += 1
    print(f"\nListo: {n} ítems agregados a '{a.lista}'. Magoo ya los ve en su iPhone.")


if __name__ == "__main__":
    main()
