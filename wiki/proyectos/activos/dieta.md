---
type: proyecto
date: 2026-08-08
estado: activo
fecha-inicio: 2026-08-08
tags: [proyecto, estado/activo, dieta, salud, tema/salud]
---

# Dieta y meal prep

Sistema de pérdida de peso de **JR y [[monica|Magoo]]** — los dos tienen el objetivo, cada uno con su perfil y su target calórico. Se cocina una sola vez para los dos: almuerzo y cena de los 7 días, 14 comidas por semana, con gramaje distinto para cada quien. El criterio de diseño es que sea fácil de cocinar y sostenible con un bebé de meses en casa — no que sea óptimo en papel.

El rol pedido no es "generador de menús" sino **guía nutricional**: recomendar concreto, iterar según resultados, y sostener el hábito en el tiempo.

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
- [x] Cuestionario inicial redactado (`dieta/cuestionario.md`)
- [x] Sistema convertido a dos personas, con salvaguarda de lactancia
- [x] Lista `Groceries` creada por JR y compartida con Magoo (2026-08-08)
- [x] Perfil de JR — 127 kg, 1.89 m, 30 años, IMC 35.6 → **2,076 kcal/día**
- [x] Perfil de Magoo — 54.4 kg, 1.60 m, 31 años, IMC 21.2, lactancia exclusiva → **1,800 kcal/día**
- [x] Primer menú semanal (`menu-2026-08-10.md`) + hoja para la empleada
- [ ] **Báscula de cocina** — sin pesar, el gramaje es adivinanza
- [ ] Chequeo médico base de JR (glucosa, lípidos, presión, hígado) — IMC 35.6
- [ ] Magoo: confirmar el plan con su doctora (lactancia exclusiva)
- [ ] Confirmar qué días exactos va la empleada (se asumió lun/mié/vie)

## Restricciones de JR que definen el menú

Muy melindroso. Vegetales que **sí** come: brócoli, papa, zanahoria cocida, pepino, tomate, cebolla, cilantro. Todo lo demás (güisquil, ejote, espinaca, repollo) queda fuera. Come frijol, huevo y aguacate.

Odia cocinar — **cocina la empleada, 3 días por semana**. El entregable no es un plan de prep para JR sino instrucciones para ella.

**Martes:** los suegros llevan cena, tarde (8-9 pm), sin cuidar dieta. Está incorporado al plan como cena libre semanal, no como excepción.

**Historial:** hace 3 meses cortó harinas procesadas y le fue excelente hasta que un cheat day sin límite lo tumbó. Por eso el diseño usa flexibilidad diaria planificada en vez de días libres.

## Salvaguarda de lactancia

Nicolás nació el 6 de marzo de 2026. `perfil.py` **se niega a calcular** un perfil de mujer sin el campo `lactancia`. Con lactancia exclusiva: +500 kcal/día antes del déficit, piso de 1,800 kcal, máximo 0.5 kg/semana. Probado: con los mismos datos, la diferencia entre lactando y no lactando es de **390 kcal diarias**.

## Relacionado

- [[wiki/IDENTITY]] · [[monica]] · [[nicolas]]
- [[wiki/resources/apple-reminders-manual|Manual de Apple Reminders]]
- [[wiki/index]] · [[dashboard]]
