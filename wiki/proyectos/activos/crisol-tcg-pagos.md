---
type: nota
date: 2026-09-01
tags:
  - tema/tcg
  - tema/fintech
  - proyecto/crisol-tcg
---

# Crisol TCG — Pagos con Recurrente

Conocimiento operativo de la pasarela, asimilado de los clippings de ayuda de Recurrente (2026-08-31). Fuente primaria: [[¿Cómo funcionan los pagos por transferencia bancaria?]] y [[Cómo pagar por transferencia bancaria]].

## Lo esencial

- **La transferencia bancaria es un método DENTRO del checkout de Recurrente**, no un flujo aparte del comercio. El cliente elige «Transferencia» en el checkout de Recurrente y ve ahí mismo: referencia, monto, beneficiario, cuenta y banco.
- **Confirmación automática, sin comprobantes**: Recurrente detecta la transferencia por la referencia y la acredita en ~10 minutos (más si el banco demora). El comercio no confirma nada a mano.
- Acepta **cualquier banco de Guatemala**, en Q o USD. Solo pagos locales (ACH), nada internacional.
- **Sin costo** para el comercio en transferencias (la comisión de tarjeta sí aplica en ese método).
- Límite: Q25,000 / $4,000 por transacción; arriba de Q20,000 puede demorar por horarios ACH.
- Riesgo operativo: si el cliente altera monto o referencia, el pago no se vincula solo — queda como pago huérfano identificado por nombre del titular.

## Implicaciones para la plataforma (fase 2)

1. El método «transferencia» del checkout propio se **simplifica**: redirige al checkout de Recurrente igual que tarjeta — mueren los datos bancarios manuales y la confirmación de comprobante en el admin.
2. El webhook `checkout.completed` cubre ambos métodos → un solo camino de confirmación de pago.
3. La expiración del pedido sin pagar la decide Crisol (JR: 2 horas).
4. El caso «pago huérfano» (referencia alterada) queda como alerta manual en el panel.

## Relacionado

- [[crisol-tcg]] — el proyecto
- [[crisol-tcg-proveedores]]
