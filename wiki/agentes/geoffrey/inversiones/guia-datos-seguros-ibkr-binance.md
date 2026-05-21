---
type: reference
date: 2026-05-21
tags: [inversiones, seguridad, ibkr, binance, datos]
---

# Guía segura para pasar datos IBKR y Binance

## Principio

No enviar contraseñas, códigos 2FA, seed phrases, API secrets en chat, capturas públicas ni Vault wiki.

## Datos que sí sirven para Fase 1

Para cada posición:

- plataforma;
- activo/ticker;
- cantidad;
- precio promedio/cost basis si aparece;
- valor actual;
- P/L si aparece;
- moneda;
- fecha de corte.

## IBKR — opciones seguras iniciales

Preferido en Fase 1:

1. Export/statement de posiciones en CSV o PDF.
2. Captura de pantalla donde se vean holdings y valores, ocultando número de cuenta si aparece.
3. Datos manuales pegados en tabla.

No enviar:

- usuario/contraseña;
- códigos 2FA;
- número completo de cuenta si no hace falta;
- enlaces de sesión.

## Binance — opciones seguras iniciales

Preferido en Fase 1:

1. Export de wallet/spot en CSV si Binance lo permite.
2. Captura de balance/portfolio ocultando datos sensibles.
3. Datos manuales por activo.

Si se crea API key read-only:

- activar lectura;
- desactivar trading spot/margin;
- desactivar withdrawals;
- desactivar internal/universal transfer;
- desactivar margin/futures/options;
- idealmente restringir IP;
- verificar permisos antes de usar;
- guardar secreto fuera del Vault.

## Revisión antes de usar APIs

Antes de conectar cualquier API:

- confirmar que es read-only;
- hacer prueba de permisos;
- documentar dónde se guardan credenciales;
- documentar qué endpoints están permitidos;
- bloquear endpoints de trading/retiro/transferencia;
- hacer dry-run y mostrar resultado a JR.

## Relacionado

- [[api-readonly-ibkr-binance]]
- [[sistema-agentes-inversiones]]
