# Lista de compras compartida en Apple Reminders

Referencia para el skill `meal-prep`. Responde la duda de JR sobre si la lista del súper va en Reminders o en Notas.

## Reminders, no Notas

**Recordatorios** tiene desde iOS 17 / macOS Sonoma un tipo de lista dedicado, **Comestibles (Groceries)**, que agrupa lo que se agrega por pasillo automáticamente: produce, lácteos, carnes, panadería, congelados. Se comparte por iCloud y las dos personas ven los cambios en vivo; cuando Magoo marca algo en el súper, JR lo ve al instante.

**Notas** solo tiene listas de verificación genéricas: sin clasificación por pasillo, y peor para agregar desde script.

Para lista de compras compartida, Recordatorios gana claro.

## Setup manual — una sola vez

Estas dos cosas **solo se pueden hacer desde la app**. AppleScript no expone ni el tipo de lista ni el compartir por iCloud; no hay forma de automatizarlas.

1. Abrir **Recordatorios** → **Archivo › Lista nueva**
2. Nombre: `🛒 Súper` · **Tipo de lista: Comestibles**
3. Con la lista seleccionada, botón de **Compartir** (persona con `+`) → invitar a Magoo con su Apple ID → permitir que edite

Hecho eso, el script ya puede escribir en la lista y Magoo la ve en su iPhone.

## Estado actual de Reminders de JR

Auditado el 2026-08-08: existe **una sola lista**, `🏠 Personal`. Las cuatro secciones estándar del manual (✅ Tareas, 🔁 Recurrentes, 📅 Próximos, 💡 Algún día) viven como secciones dentro de esa lista — exactamente el caso que el manual advierte que no se confunda con listas.

`🛒 Súper` todavía no existe. Hay que crearla con el procedimiento de arriba antes del primer uso.

## Qué puede y qué no puede AppleScript

| Acción | ¿Automatizable? |
|---|---|
| Leer listas y recordatorios | Sí |
| Agregar recordatorio a una lista existente | Sí |
| Marcar como completado | Sí |
| Crear lista nueva (tipo estándar) | Sí |
| **Definir tipo Comestibles** | **No — solo en la app** |
| **Compartir por iCloud** | **No — solo en la app** |
| Leer o escribir secciones dentro de una lista | No expuesto |

## Regla de autoridad

El [[wiki/resources/apple-reminders-manual|manual de Reminders]] de JR es explícito: crear, mover, editar o borrar recordatorios **requiere aprobación explícita**. Consultar y proponer, no.

Por eso `lista_compras.py` corre en `--dry-run` por defecto: arma la lista, la muestra, y espera el visto bueno antes de escribir nada.
