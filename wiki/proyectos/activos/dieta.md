---
type: proyecto
date: 2026-08-08
estado: activo
fecha-inicio: 2026-08-08
tags: [proyecto, estado/activo, dieta, salud, tema/salud]
---

# Dieta y meal prep

Sistema de pérdida de peso de JR basado en meal prep semanal. Cocinan JR y [[monica|Magoo]] para los dos: almuerzo y cena de los 7 días, 14 comidas por semana. El criterio de diseño es que sea fácil de cocinar y sostenible con un bebé de meses en casa — no que sea óptimo en papel.

## Cómo funciona

El sistema vive en el skill `meal-prep` (`skills/meal-prep/SKILL.md`), que se invoca solo cuando JR habla de dieta, calorías, menú o lista de compras.

| Pieza | Dónde | Qué hace |
|---|---|---|
| Skill `meal-prep` | `skills/meal-prep/` | Menús, cálculos, batch cooking, lista de compras |
| MCP `opennutrition` | `~/.local/share/mcp-opennutrition` | 326,759 alimentos con macros reales. Local, sin internet, sin API key |
| `perfil.py` | `skills/meal-prep/scripts/` | Targets calóricos y bitácora de peso |
| `lista_compras.py` | `skills/meal-prep/scripts/` | Menú → Apple Reminders compartido con Magoo |

Los datos viven en `wiki/proyectos/activos/dieta/` (dentro del vault, así Syncthing los lleva a la Mac Mini).

## Decisiones tomadas

- **Skill propio, no de terceros.** Se evaluó `nutritional-specialist` (ailabs-393): solo guarda preferencias, no calcula nada, y persiste en `~/.claude/` — fuera del vault, no sincroniza. Descartado.
- **Datos nutricionales del MCP, no del modelo.** El error al ojo en aceites y cortes de carne es de 30-50%, suficiente para borrar el déficit completo.
- **Componentes, no platos.** Se cocinan proteínas, carbos y vegetales por separado y se recombinan. Evita el hartazgo del tercer día.
- **Una sesión el domingo + congelador** (elegido 2026-08-08). Comida cocinada aguanta 3-4 días, así que lun-mié va al refri y jue-dom al congelador. Consecuencia: el ceviche y las ensaladas solo caben al inicio de la semana.
- **Factor de actividad 1.25** — golf en carrito, sin gym. Una ronda en carrito son ~600-800 kcal, bastante menos de lo que parece.
- **Lista de compras en Recordatorios, no en Notas.** Recordatorios tiene tipo *Comestibles* que clasifica por pasillo y se comparte por iCloud.

## Estado

- [x] MCP `opennutrition` instalado y registrado (2026-08-08)
- [x] Skill `meal-prep` construido y probado
- [x] Biblioteca de componentes y 7 fórmulas con macros verificados (`dieta/recetas.md`)
- [x] Despensa base (`dieta/despensa.md`)
- [ ] Perfil de JR — faltan **peso, estatura, edad, peso meta**
- [ ] Lista `🛒 Súper` en Recordatorios (crear en la app, tipo Comestibles, compartir con Magoo)
- [ ] Primer menú semanal
- [ ] Báscula de cocina — sin pesar, el gramaje es adivinanza

## Relacionado

- [[wiki/IDENTITY]] · [[monica]] · [[nicolas]]
- [[wiki/resources/apple-reminders-manual|Manual de Apple Reminders]]
- [[wiki/index]] · [[dashboard]]
