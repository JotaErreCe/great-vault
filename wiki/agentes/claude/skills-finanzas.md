---
type: reference
date: 2026-10-19
tags: [agente, claude, finanzas, skills, seguridad]
---

# Skills de finanzas en solo lectura (Binance e IBKR)

JR pidió el **2026-08-26**: «Me gustaría que tuvieras skills para ver mi Binance y mi Interactive Brokers en "Only View" mode.» Construidas ese día en `~/.claude/skills/binance-view/` y `~/.claude/skills/ibkr-view/`. Contexto de inversiones de JR: [[finanzas/inversiones|inversiones]].

## Reglas duras

- **Nunca operan.** Si JR pide comprar, vender, retirar o transferir: negarse y decirle que lo haga desde la app. Estas skills no crecen hacia trading.
- **Nunca pedirle a JR una API key, un secret o un token por Telegram ni por chat** (queda en el historial del teléfono, del bot y del servidor). Que los escriba directo en el archivo desde la computadora.
- Credenciales en `~/.claude/secrets/` (700), archivos `binance.env` e `ibkr.env` (600). Los scripts avisan si el archivo quedó legible por otros y nunca imprimen la key, el secret ni el token. Valores: nunca en el Vault.

## Binance

REST firmada (HMAC-SHA256), solo GET. Muestra saldos distintos de 0 con su valor aproximado en USDT y lee `/sapi/v1/account/apiRestrictions`: **avisa si la key tiene permisos peligrosos** (trading, futuros, retiros, transferencias); debería tener solo «Enable Reading».

**Libro FIFO (`binance_ledger.py`, 26-ago-2026).** JR: «el tracking de ganancia no es real sino estimado porque se come centavos si lo hago por promedios». Lecciones:
- `myTrades` no es todo: hay que unir trades spot, **Convert** (`/sapi/v1/convert/tradeFlow`, ventanas de 30 días), compras fiat (`/fiat/payments` y `/fiat/orders`, 89 días), depósitos, retiros y `dribblet`. Las posiciones de ETH, XRP y DOGE de JR vinieron de Convert.
- Las comisiones cobradas en BNB se dan de baja; los retiros bajan lotes **sin realizar ganancia**.
- Binance no lista pares deslistados (BUSD viejos): parte de 2021 queda invisible (~1.1 % del total en el caso de JR). Por eso el script **cuadra contra el saldo real** y muestra la diferencia. Para cerrarla: export manual (Wallet → Transaction History).
- Salidas en `~/Documents/binance-libro/`; caché en `~/.claude/secrets/`. Resultado al 26-ago-2026 en esa carpeta (no se copia aquí: es un corte, no un dato vivo).

## IBKR

**Flex Web Service**, no Client Portal API, a propósito: es un servicio de reportes, no expone trading y no necesita gateway Java ni login diario. Flujo SendRequest → ReferenceCode → GetStatement, con reintentos por el código 1019. El dato es **del último corte del reporte, no en vivo**: decir siempre la fecha.

## Estado

Al 26-ago-2026 el código compilaba y la conectividad estaba probada; faltaba que JR generara las llaves de solo lectura. El 19-oct-2026 existe `binance.env` pero **no existe `ibkr.env`** ([[mapa-de-archivos]]): `ibkr-view` no tendría credenciales **(sin verificar si se guardaron en otro lado)**.

## Relacionado

- [[agentes/claude/AGENT|Claude]] · [[finanzas/inversiones|inversiones]] · [[mapa-de-archivos]] · [[great-vault]]
