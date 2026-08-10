---
type: reference
date: 2026-08-10
tags: [reference, dieta, compras]
---

# Supermercados en línea — qué se puede automatizar

Probado el 2026-08-10 contra los cuatro sitios que pidió JR.

## Estado por tienda

| Tienda | Plataforma | API de catálogo | Carrito | Notas |
|---|---|---|---|---|
| **La Torre** (`latorre.com.gt`) | VTEX | ✅ pública | ✅ anónimo | El mejor camino |
| **Paiz** (`paiz.com.gt`) | VTEX | ✅ pública | Sin probar | Misma mecánica que La Torre |
| **Walmart GT** (`walmart.com.gt`) | VTEX | ❌ bloqueada | — | Navegable por UI, lento |
| **PriceSmart** | Propia | ❌ no encontrada | — | Club de membresía |

`superlatorre.com` **no es La Torre** — es un dominio parqueado en GoDaddy. El bueno es `latorre.com.gt`.

## El hallazgo importante: no hace falta login

El carrito de VTEX funciona **completamente anónimo**. Verificado con `loggedIn: false` y productos dentro:

```bash
# 1. Crear carrito
curl -s -X POST "https://www.latorre.com.gt/api/checkout/pub/orderForm" \
  -H "Content-Type: application/json"
# devuelve orderFormId

# 2. Agregar producto
curl -s -X POST "https://www.latorre.com.gt/api/checkout/pub/orderForm/<orderFormId>/items" \
  -H "Content-Type: application/json" \
  -d '{"orderItems":[{"id":"<skuId>","quantity":2,"seller":"1"}]}'

# 3. Vaciar
curl -s -X POST ".../orderForm/<orderFormId>/items/removeAll" -H "Content-Type: application/json"
```

Consecuencia práctica: **el flujo completo se hace sin credenciales.** Se llena el carrito en la sesión del navegador y JR entra a pagar. Nunca hace falta que un agente teclee su contraseña — y no debe hacerlo aunque lo pida.

## Zona de entrega

Es obligatoria para precio y stock reales. En La Torre se guarda en `localStorage`:

```json
store-selector-zustand = {"option1Select":"Guatemala","option2Select":"Guatemala Zona 13",
                          "pc":"1013","store":"latorremxlatorre20calle"}
```

**JR: Zona 13** → lo atiende la tienda **La Torre 20 Calle**. Ya quedó seleccionada.

## Dos trampas al leer precios

1. **El primer resultado suele estar mal.** Buscar "pollo" y tomar lo más barato devuelve un cubito Maggi; "carne molida" devuelve caldo Malher. Hay que filtrar por `categories` (`Carnes, Embutidos y Mariscos`, `Frutas y Verduras`) y excluir embutidos, sopas y bebidas en polvo.

2. **Precio por libra ≠ precio del empaque.** En productos de peso variable la API da el precio unitario y la página muestra el estimado:

   > Pechuga Pio Lindo: API Q36.71/lb · página Q40.38 · `36.71 × 1.10 lb = 40.38` ✓

   No es un error de la API. Para comparar entre tiendas hay que normalizar a precio por libra o por kilo. El cobro final depende del peso real de lo que empaquen.

3. **Productos con `Price: 0`** son de precio por peso sin definir. No sirven para comparar.

## Flujo semanal acordado

| Cuándo | Qué |
|---|---|
| Sábado noche | Comparar precios, verificar stock en Zona 13, llenar el carrito donde salga más barato, avisarle a JR |
| Domingo mañana | JR revisa el carrito, entra a su cuenta y paga |

Datos de facturación (NIT, dirección) los ingresa JR en el checkout. **No guardarlos en el vault fuera de `_sensitive.md`.**

## Relacionado

- [[SKILL|meal-prep]] · [[wiki/proyectos/activos/dieta|Proyecto Dieta]]
