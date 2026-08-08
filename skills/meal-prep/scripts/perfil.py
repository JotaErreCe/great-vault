#!/usr/bin/env python3
"""Perfiles y bitácoras de peso para el skill meal-prep.

Dos personas: JR y Magoo. Cada una con su perfil, sus targets y su bitácora.
Todo vive dentro del vault para que Syncthing lo lleve a la otra Mac.
La ruta del vault se resuelve por host — nunca se hardcodea.

Uso:
    perfil.py vault-path
    perfil.py existe            [--persona jr|magoo|ambos]
    perfil.py get               --persona jr
    perfil.py set               --persona magoo --json '{...}'
    perfil.py calcular          --persona jr
    perfil.py peso 83.4         --persona jr [--nota "..."]
    perfil.py tendencia         --persona jr
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

PERSONAS = {"jr": "JR", "magoo": "Magoo"}

FACTORES_ACTIVIDAD = {
    "sedentario": 1.20,
    "ligero": 1.375,
    "moderado": 1.55,
    "intenso": 1.725,
    "atleta": 1.90,
}

PISO_KCAL = {"hombre": 1500, "mujer": 1200}

# Energía extra por lactancia (OMS / Academy of Nutrition and Dietetics)
KCAL_LACTANCIA = {"exclusiva": 500, "parcial": 330, "no": 0}
# Con lactancia el piso sube y el ritmo se limita: bajar rápido afecta la producción
PISO_LACTANCIA = 1800
MAX_KG_SEMANA_LACTANCIA = 0.5


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


def ruta_perfil(persona: str) -> Path:
    return dir_datos() / f"perfil-{persona}.md"


def ruta_log(persona: str) -> Path:
    return dir_datos() / f"log-peso-{persona}.md"


BLOQUE = re.compile(r"```json\n(.*?)\n```", re.DOTALL)


def leer_perfil(persona: str) -> dict:
    p = ruta_perfil(persona)
    if not p.exists():
        return {}
    m = BLOQUE.search(p.read_text(encoding="utf-8"))
    if not m:
        return {}
    try:
        return json.loads(m.group(1))
    except json.JSONDecodeError:
        return {}


def escribir_perfil(persona: str, datos: dict) -> None:
    nombre = PERSONAS[persona]
    t = datos.get("targets", {})
    filas = ""
    if t:
        filas = (
            f"| BMR | {t['bmr']} kcal |\n"
            f"| TDEE | {t['tdee']} kcal |\n"
        )
        if t.get("kcal_lactancia"):
            filas += f"| Extra por lactancia | +{t['kcal_lactancia']} kcal |\n"
            filas += f"| TDEE ajustado | {t['tdee_ajustado']} kcal |\n"
        filas += (
            f"| **Objetivo diario** | **{t['objetivo_kcal']} kcal** |\n"
            f"| Proteína | {t['proteina_g']} g |\n"
            f"| Grasa | {t['grasa_g']} g |\n"
            f"| Carbohidratos | {t['carbos_g']} g |\n"
            f"| Fibra | {t['fibra_g']} g |\n"
            f"| Déficit aplicado | {t['deficit_kcal']} kcal/día ({t['deficit_pct']}%) |\n"
            f"| Ritmo estimado | {t['kg_semana']} kg/semana |\n"
        )

    avisos = ""
    for a in t.get("avisos", []):
        avisos += f"> {a}\n\n"

    contenido = f"""---
type: reference
date: {date.today().isoformat()}
tags: [reference, dieta, salud]
---

# Perfil nutricional — {nombre}

Perfil y targets del sistema [[meal-prep]]. Generado por `perfil.py`; no editar el bloque JSON a mano salvo que sepas lo que hacés.

{avisos}## Targets vigentes

| Métrica | Valor |
|---|---|
{filas or "| — | sin calcular |"}

## Datos

```json
{json.dumps(datos, indent=2, ensure_ascii=False)}
```

## Relacionado

- [[wiki/proyectos/activos/dieta|Proyecto Dieta]] · [[log-peso-{persona}]] · [[recetas]]
"""
    ruta_perfil(persona).write_text(contenido, encoding="utf-8")


def calcular_targets(d: dict) -> dict:
    """Mifflin-St Jeor → TDEE → lactancia → déficit → macros. Ver referencias/calculos.md."""
    kg = float(d["peso_kg"])
    cm = float(d["estatura_cm"])
    edad = int(d["edad"])
    sexo = d.get("sexo", "hombre").lower()
    actividad = d.get("actividad", "sedentario").lower()
    meta_kg = float(d.get("peso_meta_kg", kg))
    pct = float(d.get("deficit_pct", 22))
    lactancia = str(d.get("lactancia", "no")).lower()

    avisos = []

    bmr = 10 * kg + 6.25 * cm - 5 * edad + (5 if sexo == "hombre" else -161)
    tdee = bmr * FACTORES_ACTIVIDAD.get(actividad, 1.20)

    # Lactancia: energía extra ANTES de aplicar el déficit
    extra = KCAL_LACTANCIA.get(lactancia, 0)
    tdee_ajustado = tdee + extra
    if extra:
        avisos.append(
            f"**Lactancia {lactancia}:** se suman {extra} kcal/día antes del déficit. "
            f"El piso sube a {PISO_LACTANCIA} kcal y el ritmo se limita a "
            f"{MAX_KG_SEMANA_LACTANCIA} kg/semana — bajar más rápido puede reducir la producción de leche. "
            "Cualquier plan de pérdida de peso durante lactancia conviene confirmarlo con su médico."
        )

    imc = kg / ((cm / 100) ** 2)

    objetivo = tdee_ajustado * (1 - pct / 100)

    # Pisos.
    # El piso absoluto no se cruza nunca. El piso de BMR solo aplica con IMC < 30:
    # con obesidad, las reservas de grasa cubren la diferencia y comer bajo el BMR
    # es práctica clínica estándar. Aplicarlo ahí dejaría un déficit inútilmente lento.
    piso = PISO_KCAL.get(sexo, 1500)
    if imc < 30:
        piso = max(piso, bmr)
    if extra:
        piso = max(piso, PISO_LACTANCIA)

    limitado = objetivo < piso
    if limitado:
        objetivo = piso
        avisos.append(
            f"El objetivo tocó el piso calórico ({piso} kcal). No recortar más — "
            "si hace falta más déficit, se sube actividad, no se baja comida."
        )

    deficit = tdee_ajustado - objetivo
    kg_semana = deficit * 7 / 7700

    # Tope de ritmo: nunca más de 1% del peso corporal por semana
    max_kg = kg * 0.01
    if kg_semana > max_kg:
        deficit = max_kg * 7700 / 7
        objetivo = tdee_ajustado - deficit
        kg_semana = max_kg
        avisos.append(
            f"Déficit recortado al tope de 1% del peso corporal ({max_kg:.2f} kg/semana). "
            "Más rápido cuesta masa muscular."
        )

    # Señal de que la meta puede no ser el objetivo correcto
    if imc < 25:
        avisos.append(
            f"**IMC actual {imc:.1f} — ya está en rango saludable (18.5-24.9).** "
            "Perder peso desde aquí no mejora la salud por sí solo. Si lo que se busca es "
            "verse y sentirse mejor, eso viene de proteína y fuerza, no de más déficit. "
            "Vale la pena revisar si la meta correcta es bajar de peso o cambiar composición."
        )

    # Tope de ritmo durante lactancia
    if extra and kg_semana > MAX_KG_SEMANA_LACTANCIA:
        deficit = MAX_KG_SEMANA_LACTANCIA * 7700 / 7
        objetivo = tdee_ajustado - deficit
        kg_semana = MAX_KG_SEMANA_LACTANCIA
        avisos.append("Déficit recortado para no pasar de 0.5 kg/semana durante lactancia.")

    # Macros sobre peso objetivo, no peso actual
    base = meta_kg if meta_kg < kg else kg
    prot_g = round(base * 2.0)
    grasa_g = round(base * 0.9)
    kcal_restantes = objetivo - (prot_g * 4) - (grasa_g * 9)
    carbos_g = max(round(kcal_restantes / 4), 0)

    if carbos_g < 50:
        avisos.append(
            "Los carbohidratos quedaron muy bajos. Revisar: puede que el déficit sea "
            "demasiado agresivo o el peso meta poco realista."
        )

    return {
        "imc": round(imc, 1),
        "bmr": round(bmr),
        "tdee": round(tdee),
        "kcal_lactancia": extra,
        "tdee_ajustado": round(tdee_ajustado),
        "objetivo_kcal": round(objetivo),
        "proteina_g": prot_g,
        "grasa_g": grasa_g,
        "carbos_g": carbos_g,
        "fibra_g": round(objetivo / 1000 * 14),
        "deficit_kcal": round(deficit),
        "deficit_pct": round(deficit / tdee_ajustado * 100, 1) if tdee_ajustado else 0,
        "kg_semana": round(kg_semana, 2),
        "limitado_por_piso": limitado,
        "avisos": avisos,
    }


def registrar_peso(persona: str, valor: float, nota: str = "") -> None:
    p = ruta_log(persona)
    if not p.exists():
        p.write_text(
            f"""---
type: reference
date: {date.today().isoformat()}
tags: [reference, dieta, salud]
---

# Bitácora de peso — {PERSONAS[persona]}

Append-only. Pesarse en las mismas condiciones: mañana, en ayunas, después del baño.
Evaluar por promedio de 7 días, nunca por un dato suelto.

| Fecha | Peso (kg) | Nota |
|---|---|---|
""",
            encoding="utf-8",
        )
    with p.open("a", encoding="utf-8") as f:
        f.write(f"| {date.today().isoformat()} | {valor} | {nota} |\n")
    print(f"[{PERSONAS[persona]}] Registrado: {valor} kg el {date.today().isoformat()}")


def leer_pesos(persona: str) -> list:
    p = ruta_log(persona)
    if not p.exists():
        return []
    filas = []
    for line in p.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*([\d.]+)\s*\|", line)
        if m:
            filas.append((m.group(1), float(m.group(2))))
    return filas


def tendencia(persona: str) -> None:
    filas = leer_pesos(persona)
    print(f"--- {PERSONAS[persona]} ---")
    if len(filas) < 2:
        print("Faltan datos. Se necesitan al menos 2 pesadas; para ajustar, 3 semanas.\n")
        return
    print(f"{len(filas)} pesadas · {filas[0][0]}: {filas[0][1]} kg → {filas[-1][0]}: {filas[-1][1]} kg")
    print(f"Cambio total: {filas[-1][1] - filas[0][1]:+.2f} kg")
    if len(filas) >= 3:
        ult = [v for _, v in filas[-3:]]
        print(f"Promedio últimas 3: {sum(ult) / 3:.2f} kg")
    if len(filas) < 6:
        print("Aviso: menos de 3 semanas de datos. No ajustar calorías todavía — es ruido de agua y sodio.")
    print()


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("comando", choices=["vault-path", "existe", "get", "set", "calcular", "peso", "tendencia"])
    ap.add_argument("valor", nargs="?")
    ap.add_argument("--persona", default="ambos", choices=["jr", "magoo", "ambos"])
    ap.add_argument("--json", dest="payload")
    ap.add_argument("--nota", default="")
    a = ap.parse_args()

    def una(cmd_name):
        if a.persona == "ambos":
            sys.exit(f"'{cmd_name}' necesita --persona jr | magoo")
        return a.persona

    if a.comando == "vault-path":
        print(vault())

    elif a.comando == "existe":
        objetivo = PERSONAS if a.persona == "ambos" else {a.persona: PERSONAS[a.persona]}
        for k in objetivo:
            print(f"{k}: {'true' if ruta_perfil(k).exists() else 'false'}")

    elif a.comando == "get":
        if a.persona == "ambos":
            print(json.dumps({k: leer_perfil(k) for k in PERSONAS}, indent=2, ensure_ascii=False))
        else:
            print(json.dumps(leer_perfil(a.persona), indent=2, ensure_ascii=False))

    elif a.comando == "set":
        p = una("set")
        if not a.payload:
            sys.exit("Falta --json con los datos del perfil.")
        datos = json.loads(a.payload)
        faltan = [k for k in ("peso_kg", "estatura_cm", "edad", "sexo") if k not in datos]
        if faltan:
            sys.exit(f"Faltan campos obligatorios: {', '.join(faltan)}")
        if datos["sexo"].lower() == "mujer" and "lactancia" not in datos:
            sys.exit(
                "Falta el campo 'lactancia' (exclusiva | parcial | no). "
                "Cambia el cálculo por cientos de calorías — no se puede asumir."
            )
        datos["targets"] = calcular_targets(datos)
        datos["actualizado"] = date.today().isoformat()
        escribir_perfil(p, datos)
        print(json.dumps(datos["targets"], indent=2, ensure_ascii=False))

    elif a.comando == "calcular":
        p = una("calcular")
        datos = leer_perfil(p)
        if not datos:
            sys.exit(f"No hay perfil de {PERSONAS[p]}. Corré primero: perfil.py set --persona {p} --json '{{...}}'")
        datos["targets"] = calcular_targets(datos)
        datos["actualizado"] = date.today().isoformat()
        escribir_perfil(p, datos)
        print(json.dumps(datos["targets"], indent=2, ensure_ascii=False))

    elif a.comando == "peso":
        p = una("peso")
        if not a.valor:
            sys.exit("Falta el peso. Ejemplo: perfil.py peso 83.4 --persona jr")
        registrar_peso(p, float(a.valor), a.nota)

    elif a.comando == "tendencia":
        for k in (PERSONAS if a.persona == "ambos" else {a.persona: None}):
            tendencia(k)


if __name__ == "__main__":
    main()
