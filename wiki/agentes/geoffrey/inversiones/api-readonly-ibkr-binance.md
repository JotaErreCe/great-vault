---
type: reference
date: 2026-05-21
tags: [inversiones, api, ibkr, binance, seguridad]
---

# API read-only — IBKR y Binance

Investigación inicial para conectar portafolios de JR en modo solo lectura.

## Conclusión corta

- **Binance:** sí permite API keys con lectura habilitada y trading/retiros/transferencias deshabilitados.
- **IBKR:** sí tiene APIs para ver portafolio/cuenta, pero para cuenta individual normalmente requiere Client Portal Gateway local + autenticación/2FA. La separación “solo lectura” debe validarse con configuración concreta del flujo; por seguridad, Fase 1 queda manual/CSV hasta probar en sandbox local.

## Binance

Documentación oficial consultada:

- Binance API Key Permission: `https://developers.binance.com/docs/wallet/account/api-key-permission`
- Binance Request Security: `https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/request-security`

Hallazgos:

- Binance muestra permisos de key como `enableReading`, `enableWithdrawals`, `enableInternalTransfer`, `enableMargin`, `enableFutures`, `enableSpotAndMarginTrading`, `enableVanillaOptions`, etc.
- Los métodos tienen tipos de seguridad: `USER_DATA` para información privada de cuenta; `TRADE` para colocar/cancelar órdenes.
- Por defecto, una API key no puede tradear salvo que se habilite trading en API Management.

Configuración objetivo para JR:

- `enableReading: true`
- `enableWithdrawals: false`
- `enableInternalTransfer: false`
- `enableMargin: false`
- `enableFutures: false`
- `enableSpotAndMarginTrading: false`
- `enableVanillaOptions: false`
- IP restriction: recomendable si el flujo técnico lo permite.

## IBKR

Documentación oficial consultada:

- IBKR Trading Web API: `https://www.interactivebrokers.com/campus/ibkr-api-page/web-api-trading/`
- IBKR Client Portal API v1: `https://www.interactivebrokers.com/campus/ibkr-api-page/cpapi-v1/`

Hallazgos:

- IBKR Web API permite ver información de portafolio en tiempo real, market data, contratos y también trading.
- Para clientes retail/individuales, IBKR indica uso de **Client Portal Gateway**, un programa Java local que enruta requests tras autenticación.
- Requiere cuenta IBKR Pro, cuenta fondeada y 2FA.
- La documentación describe capacidad de “view real-time portfolio information” y “intra-day portfolio updates”.

Riesgo operativo:

- IBKR mezcla capacidades de lectura y trading dentro del ecosistema API. Antes de guardar credenciales o automatizar, hay que verificar si el método de acceso puede quedar efectivamente sin capacidad operativa o si requiere controles externos: no exponer endpoints de trading, no guardar sesión persistente, no permisos de escritura, y gateway local controlado.

## Política de implementación

Fase 1:

- no conectar APIs todavía;
- usar CSV/statements/exports/manual;
- crear esquema de Sheet y reportes;
- diseñar guía segura de exportación.

Fase 2:

- prueba Binance read-only con key sin trading/retiro/transferencia;
- guardar credenciales fuera del Vault, nunca en `wiki/`;
- comprobar permisos vía endpoint de API restrictions antes de leer balances.

Fase 3:

- prueba IBKR Client Portal Gateway local con sesión manual y endpoints de portafolio;
- bloquear explícitamente cualquier endpoint de order/trade;
- si no puede garantizarse read-only, usar exports/manual.

## Relacionado

- [[sistema-agentes-inversiones]]
- [[guia-datos-seguros-ibkr-binance]]
