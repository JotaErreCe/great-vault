---
type: reference
date: 2026-08-10
tags: [reference, dieta, salud]
---

# Perfil nutricional — Magoo

Perfil y targets del sistema [[meal-prep]]. Generado por `perfil.py`; no editar el bloque JSON a mano salvo que sepas lo que hacés.

> **Lactancia exclusiva:** se suman 500 kcal/día antes del déficit. El piso sube a 1800 kcal y el ritmo se limita a 0.5 kg/semana — bajar más rápido puede reducir la producción de leche. Cualquier plan de pérdida de peso durante lactancia conviene confirmarlo con su médico.

> El objetivo tocó el piso calórico (1800 kcal). No recortar más — si hace falta más déficit, se sube actividad, no se baja comida.

## Targets vigentes

| Métrica | Valor |
|---|---|
| BMR | 1337 kcal |
| TDEE | 1604 kcal |
| Extra por lactancia | +500 kcal |
| TDEE ajustado | 2104 kcal |
| **Objetivo diario** | **1800 kcal** |
| Proteína | 104 g |
| Grasa | 47 g |
| Carbohidratos | 240 g |
| Fibra | 25 g |
| Déficit aplicado | 304 kcal/día (14.5%) |
| Ritmo estimado | 0.28 kg/semana |


## Datos

```json
{
  "sexo": "mujer",
  "peso_kg": 65.27,
  "estatura_cm": 160,
  "edad": 31,
  "actividad": "sedentario",
  "peso_meta_kg": 52.16,
  "lactancia": "exclusiva",
  "deficit_pct": 22,
  "targets": {
    "imc": 25.5,
    "bmr": 1337,
    "tdee": 1604,
    "kcal_lactancia": 500,
    "tdee_ajustado": 2104,
    "objetivo_kcal": 1800,
    "proteina_g": 104,
    "grasa_g": 47,
    "carbos_g": 240,
    "fibra_g": 25,
    "deficit_kcal": 304,
    "deficit_pct": 14.5,
    "kg_semana": 0.28,
    "limitado_por_piso": true,
    "avisos": [
      "**Lactancia exclusiva:** se suman 500 kcal/día antes del déficit. El piso sube a 1800 kcal y el ritmo se limita a 0.5 kg/semana — bajar más rápido puede reducir la producción de leche. Cualquier plan de pérdida de peso durante lactancia conviene confirmarlo con su médico.",
      "El objetivo tocó el piso calórico (1800 kcal). No recortar más — si hace falta más déficit, se sube actividad, no se baja comida."
    ]
  },
  "actualizado": "2026-08-10"
}
```

## Relacionado

- [[wiki/proyectos/activos/dieta|Proyecto Dieta]] · [[log-peso-magoo]] · [[recetas]]
