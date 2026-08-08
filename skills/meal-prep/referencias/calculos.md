# Cálculos — déficit, macros y ajustes

Referencia para el skill `meal-prep`. Todos los cálculos con el peso en **kg** y la estatura en **cm** (convertir si JR da libras o pies).

Conversiones: `1 lb = 0.4536 kg` · `1 ft = 30.48 cm` · `1 in = 2.54 cm`

## 1. BMR — Mifflin-St Jeor

Es la fórmula con mejor validación para población general (superó a Harris-Benedict en las revisiones de la Academy of Nutrition and Dietetics).

```
Hombre:  BMR = (10 × kg) + (6.25 × cm) − (5 × edad) + 5
Mujer:   BMR = (10 × kg) + (6.25 × cm) − (5 × edad) − 161
```

## 2. TDEE — gasto total

```
TDEE = BMR × factor de actividad
```

| Factor | Descripción realista |
|---|---|
| 1.20 | Escritorio, casi nada de caminata deliberada |
| 1.375 | Ejercicio ligero 1-3 días/semana, o mucha caminata |
| 1.55 | Ejercicio moderado 3-5 días/semana |
| 1.725 | Ejercicio fuerte 6-7 días/semana |
| 1.90 | Trabajo físico + entreno diario |

**Nota para el caso de JR:** juega golf. Una ronda caminando de 18 hoyos son ~1,200-1,600 kcal y 8-10 km; en carrito, ~600-800. Si juega 1-2 veces por semana, eso lo sube de 1.20 a 1.375 aunque el resto de su semana sea de escritorio. Preguntar si camina o usa carrito antes de asignar factor.

## 3. Déficit

```
Objetivo = TDEE − déficit
```

- **Déficit recomendado:** 20-25% del TDEE. Es el rango donde se pierde grasa sin sacrificar músculo ni adherencia.
- 1 kg de grasa ≈ 7,700 kcal. Un déficit de 500 kcal/día ≈ **0.45 kg/semana**.
- **Ritmo sano:** 0.5-1% del peso corporal por semana. Más rápido cuesta masa muscular y casi siempre rebota.

### Pisos que no se cruzan

- Nunca por debajo del **BMR**.
- Nunca por debajo de **1,500 kcal/día** (hombre) o **1,200 kcal/día** (mujer).
- Si `TDEE − 25%` cae bajo el piso, usar el piso y compensar con actividad, no recortando más.

## 4. Macros

**Proteína primero.** Es lo que protege la masa muscular en déficit y lo que más sacia.

```
Proteína:  1.8 – 2.2 g por kg de peso objetivo   → 4 kcal/g
Grasa:     0.8 – 1.0 g por kg de peso objetivo   → 9 kcal/g   (mínimo 0.6 g/kg, es hormonal)
Carbos:    lo que sobre de las calorías          → 4 kcal/g
```

Usar **peso objetivo**, no peso actual, cuando hay bastante sobrepeso — si no, el número de proteína sale inflado e imposible de comer.

```
kcal_carbos = objetivo − (g_proteína × 4) − (g_grasa × 9)
g_carbos = kcal_carbos ÷ 4
```

**Fibra:** apuntar a 14 g por cada 1,000 kcal. Es lo que hace que un déficit no se sienta como hambre constante.

### Reparto en 14 comidas + desayuno

Con almuerzo y cena preparados y el desayuno libre:

- Desayuno: ~25% de las calorías del día
- Almuerzo: ~35%
- Cena: ~30%
- Margen libre (café, fruta, algo dulce): ~10%

Ese 10% no es relleno: es el espacio que evita que el plan se rompa el viernes.

## 5. Verificación con datos reales

Cada componente del menú se valida contra el MCP `opennutrition` (`search-food-by-name` → `nutrition_100g` × gramaje ÷ 100). No estimar de memoria: el error típico al ojo en aceites, salsas y cortes de carne es del 30-50%, suficiente para borrar el déficit completo.

**Los tres que siempre se subestiman:** aceite de cocina (1 cda = 120 kcal), crema y aderezos, y el tamaño real de la porción de arroz.

## 6. Recalibración

El TDEE baja conforme baja el peso. Recalcular el BMR **cada 4-5 kg perdidos** o cada 8 semanas, lo que ocurra primero. Si no, el déficit se disuelve solo y aparece la meseta.

Los ajustes por tendencia están en la tabla del `SKILL.md`, flujo 4. Solo se ajusta con 3 semanas de datos: menos que eso es leer ruido de agua y sodio, no grasa.
