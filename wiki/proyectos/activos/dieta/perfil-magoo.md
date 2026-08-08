---
type: reference
date: 2026-08-08
tags: [reference, dieta, salud]
---

# Perfil nutricional — Magoo

Perfil y targets del sistema [[meal-prep]]. Generado por `perfil.py`; no editar el bloque JSON a mano salvo que sepas lo que hacés.

> **Lactancia exclusiva:** se suman 500 kcal/día antes del déficit. El piso sube a 1800 kcal y el ritmo se limita a 0.5 kg/semana — bajar más rápido puede reducir la producción de leche. Cualquier plan de pérdida de peso durante lactancia conviene confirmarlo con su médico.

> El objetivo tocó el piso calórico (1800 kcal). No recortar más — si hace falta más déficit, se sube actividad, no se baja comida.

> **IMC actual 21.2 — ya está en rango saludable (18.5-24.9).** Perder peso desde aquí no mejora la salud por sí solo. Si lo que se busca es verse y sentirse mejor, eso viene de proteína y fuerza, no de más déficit. Vale la pena revisar si la meta correcta es bajar de peso o cambiar composición.

## Targets vigentes

| Métrica | Valor |
|---|---|
| BMR | 1228 kcal |
| TDEE | 1474 kcal |
| Extra por lactancia | +500 kcal |
| TDEE ajustado | 1974 kcal |
| **Objetivo diario** | **1800 kcal** |
| Proteína | 104 g |
| Grasa | 47 g |
| Carbohidratos | 240 g |
| Fibra | 25 g |
| Déficit aplicado | 174 kcal/día (8.8%) |
| Ritmo estimado | 0.16 kg/semana |


## Datos

```json
{
  "sexo": "mujer",
  "peso_kg": 54.4,
  "estatura_cm": 160,
  "edad": 31,
  "actividad": "sedentario",
  "peso_meta_kg": 52.2,
  "lactancia": "exclusiva",
  "deficit_pct": 22,
  "targets": {
    "imc": 21.2,
    "bmr": 1228,
    "tdee": 1474,
    "kcal_lactancia": 500,
    "tdee_ajustado": 1974,
    "objetivo_kcal": 1800,
    "proteina_g": 104,
    "grasa_g": 47,
    "carbos_g": 240,
    "fibra_g": 25,
    "deficit_kcal": 174,
    "deficit_pct": 8.8,
    "kg_semana": 0.16,
    "limitado_por_piso": true,
    "avisos": [
      "**Lactancia exclusiva:** se suman 500 kcal/día antes del déficit. El piso sube a 1800 kcal y el ritmo se limita a 0.5 kg/semana — bajar más rápido puede reducir la producción de leche. Cualquier plan de pérdida de peso durante lactancia conviene confirmarlo con su médico.",
      "El objetivo tocó el piso calórico (1800 kcal). No recortar más — si hace falta más déficit, se sube actividad, no se baja comida.",
      "**IMC actual 21.2 — ya está en rango saludable (18.5-24.9).** Perder peso desde aquí no mejora la salud por sí solo. Si lo que se busca es verse y sentirse mejor, eso viene de proteína y fuerza, no de más déficit. Vale la pena revisar si la meta correcta es bajar de peso o cambiar composición."
    ]
  },
  "actualizado": "2026-08-08"
}
```

## Relacionado

- [[wiki/proyectos/activos/dieta|Proyecto Dieta]] · [[log-peso-magoo]] · [[recetas]]
