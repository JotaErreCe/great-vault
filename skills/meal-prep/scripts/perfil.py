#!/usr/bin/env python3
"""Perfil y bitácora de peso para el skill meal-prep.

Todo vive dentro del vault para que Syncthing lo lleve a la otra Mac.
La ruta del vault se resuelve por host — nunca se hardcodea.

Uso:
    perfil.py vault-path
    perfil.py existe
    perfil.py get
    perfil.py set --json '{"peso_kg": 84, ...}'
    perfil.py calcular          # recalcula targets desde los stats guardados
    perfil.py peso 83.4 [--nota "..."]
    perfil.py tendencia
"""

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

CANDIDATOS_VAULT = [
    Path.home() / "Great Vault",
    Path.home() / "documents" / "Great Vault",
    Path.home() / "Documents" / "Great Vault",
]

SUBRUTA_DATOS = Path("wiki") / "proyectos" / "activos" / "dieta"

FACTORES_ACTIVIDAD = {
    "sedentario": 1.20,
    "ligero": 1.375,
    "moderado": 1.55,
    "intenso": 1.725,
    "atleta": 1.90,
}

PISO_KCAL = {"hombre": 1500, "mujer": 1200}


def vault() -> Path:
    for c in CANDIDATOS_VAULT:
        if c.is_dir():
            return c
    sys.exit(
        "No encontré el vault. Busqué en:\n  "
        + "\n  ".join(str(c) for c in CANDIDATOS_VAULT)
        + "\nNo lo recrees — preguntale a JR dónde está en esta máquina."
    )


def dir_datos() -> Path:
    d = vault() / SUBRUTA_DATOS
    d.mkdir(parents=True, exist_ok=True)
    return d


def ruta_perfil() -> Path:
    return dir_datos() / "perfil.md"


def ruta_log() -> Path:
    return dir_datos() / "log-peso.md"


# --- perfil: markdown con un bloque json embebido, legible en Obsidian ---

BLOQUE = re.compile(r"```json\n(.*?)\n```", re.DOTALL)


def leer_perfil() -> dict:
    p = ruta_perfil()
    if not p.exists():
        return {}
    m = BLOQUE.search(p.read_text(encoding="utf-8"))
    if not m:
        return {}
    try:
        return json.loads(m.group(1))
    except json.JSONDecodeError:
        return {}


def escribir_perfil(datos: dict) -> None:
    t = datos.get("targets", {})
    filas = ""
    if t:
        filas = (
            f"| BMR | {t['bmr']} kcal |\n"
            f"| TDEE | {t['tdee']} kcal |\n"
            f"| **Objetivo diario** | **{t['objetivo_kcal']} kcal** |\n"
            f"| Proteína | {t['proteina_g']} g |\n"
            f"| Grasa | {t['grasa_g']} g |\n"
            f"| Carbohidratos | {t['carbos_g']} g |\n"
            f"| Fibra | {t['fibra_g']} g |\n"
            f"| Déficit aplicado | {t['deficit_kcal']} kcal/día ({t['deficit_pct']}%) |\n"
            f"| Ritmo estimado | {t['kg_semana']} kg/semana |\n"
        )

    contenido = f"""---
type: reference
date: {date.today().isoformat()}
tags: [reference, dieta, salud]
---

# Perfil nutricional — JR

Perfil y targets del sistema [[meal-prep]]. Generado por `perfil.py`; no editar el bloque JSON a mano salvo que sepas lo que hacés.

## Targets vigentes

| Métrica | Valor |
|---|---|
{filas or "| — | sin calcular |"}

## Datos

```json
{json.dumps(datos, indent=2, ensure_ascii=False)}
```

## Relacionado

- [[wiki/proyectos/activos/dieta|Proyecto Dieta]] · [[log-peso]] · [[wiki/IDENTITY]]
"""
    ruta_perfil().write_text(contenido, encoding="utf-8")


def calcular_targets(d: dict) -> dict:
    """Mifflin-St Jeor → TDEE → déficit → macros. Ver referencias/calculos.md."""
    kg = float(d["peso_kg"])
    cm = float(d["estatura_cm"])
    edad = int(d["edad"])
    sexo = d.get("sexo", "hombre").lower()
    actividad = d.get("actividad", "sedentario").lower()
    meta_kg = float(d.get("peso_meta_kg", kg))
    pct = float(d.get("deficit_pct", 22))

    bmr = 10 * kg + 6.25 * cm - 5 * edad + (5 if sexo == "hombre" else -161)
    tdee = bmr * FACTORES_ACTIVIDAD.get(actividad, 1.20)

    objetivo = tdee * (1 - pct / 100)

    # pisos: ni bajo BMR ni bajo el mínimo absoluto
    piso = max(bmr, PISO_KCAL.get(sexo, 1500))
    limitado = objetivo < piso
    if limitado:
        objetivo = piso

    # macros sobre peso objetivo, no peso actual
    base = meta_kg if meta_kg < kg else kg
    prot_g = round(base * 2.0)
    grasa_g = round(base * 0.9)
    kcal_restantes = objetivo - (prot_g * 4) - (grasa_g * 9)
    carbos_g = max(round(kcal_restantes / 4), 0)

    deficit = tdee - objetivo

    return {
        "bmr": round(bmr),
        "tdee": round(tdee),
        "objetivo_kcal": round(objetivo),
        "proteina_g": prot_g,
        "grasa_g": grasa_g,
        "carbos_g": carbos_g,
        "fibra_g": round(objetivo / 1000 * 14),
        "deficit_kcal": round(deficit),
        "deficit_pct": round(deficit / tdee * 100, 1) if tdee else 0,
        "kg_semana": round(deficit * 7 / 7700, 2),
        "limitado_por_piso": limitado,
    }


# --- bitácora de peso ---


def registrar_peso(valor: float, nota: str = "") -> None:
    p = ruta_log()
    if not p.exists():
        p.write_text(
            f"""---
type: reference
date: {date.today().isoformat()}
tags: [reference, dieta, salud]
---

# Bitácora de peso — JR

Append-only. Pesarse en las mismas condiciones: mañana, en ayunas, después del baño.
Evaluar por promedio de 7 días, nunca por un dato suelto.

| Fecha | Peso (kg) | Nota |
|---|---|---|
""",
            encoding="utf-8",
        )
    with p.open("a", encoding="utf-8") as f:
        f.write(f"| {date.today().isoformat()} | {valor} | {nota} |\n")
    print(f"Registrado: {valor} kg el {date.today().isoformat()}")


def leer_pesos() -> list:
    p = ruta_log()
    if not p.exists():
        return []
    filas = []
    for line in p.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*([\d.]+)\s*\|", line)
        if m:
            filas.append((m.group(1), float(m.group(2))))
    return filas


def tendencia() -> None:
    filas = leer_pesos()
    if len(filas) < 2:
        print("Faltan datos. Se necesitan al menos 2 pesadas; para ajustar, 3 semanas.")
        return
    print(f"{len(filas)} pesadas registradas")
    print(f"Primera: {filas[0][0]} → {filas[0][1]} kg")
    print(f"Última:  {filas[-1][0]} → {filas[-1][1]} kg")
    delta = filas[-1][1] - filas[0][1]
    print(f"Cambio total: {delta:+.2f} kg")
    if len(filas) >= 3:
        ult = [v for _, v in filas[-3:]]
        print(f"Promedio últimas 3: {sum(ult) / 3:.2f} kg")
    if len(filas) < 6:
        print("\nAviso: menos de 3 semanas de datos. No ajustar calorías todavía — es ruido de agua y sodio.")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("comando", choices=["vault-path", "existe", "get", "set", "calcular", "peso", "tendencia"])
    ap.add_argument("valor", nargs="?")
    ap.add_argument("--json", dest="payload")
    ap.add_argument("--nota", default="")
    a = ap.parse_args()

    if a.comando == "vault-path":
        print(vault())
    elif a.comando == "existe":
        print("true" if ruta_perfil().exists() else "false")
    elif a.comando == "get":
        print(json.dumps(leer_perfil(), indent=2, ensure_ascii=False))
    elif a.comando == "set":
        if not a.payload:
            sys.exit("Falta --json con los datos del perfil.")
        datos = json.loads(a.payload)
        faltan = [k for k in ("peso_kg", "estatura_cm", "edad") if k not in datos]
        if faltan:
            sys.exit(f"Faltan campos obligatorios: {', '.join(faltan)}")
        datos["targets"] = calcular_targets(datos)
        datos["actualizado"] = date.today().isoformat()
        escribir_perfil(datos)
        print(json.dumps(datos["targets"], indent=2, ensure_ascii=False))
        if datos["targets"]["limitado_por_piso"]:
            print("\nAviso: el objetivo tocó el piso calórico. No recortar más — subir actividad.", file=sys.stderr)
    elif a.comando == "calcular":
        datos = leer_perfil()
        if not datos:
            sys.exit("No hay perfil. Corré primero: perfil.py set --json '{...}'")
        datos["targets"] = calcular_targets(datos)
        datos["actualizado"] = date.today().isoformat()
        escribir_perfil(datos)
        print(json.dumps(datos["targets"], indent=2, ensure_ascii=False))
    elif a.comando == "peso":
        if not a.valor:
            sys.exit("Falta el peso. Ejemplo: perfil.py peso 83.4")
        registrar_peso(float(a.valor), a.nota)
    elif a.comando == "tendencia":
        tendencia()


if __name__ == "__main__":
    main()
