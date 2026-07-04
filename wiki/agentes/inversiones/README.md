---
type: index
date: 2026-05-23
tags: [index, agentes, inversiones, jordan-belfort]
---

# Sistema de agentes de inversiones — v2

## Estado operativo — sistema suspendido desde 2026-07-04

JR retiró el experimento de Jordan/Paper Lab. Esta arquitectura queda **congelada como histórico** hasta rediseño completo.

Estado vigente:

- No hay invocación operativa de Jordan.
- No hay Radar Diario ni paper trading automático activo.
- No deben correr rutinas, análisis programados, resúmenes nocturnos ni operaciones simuladas.
- Estos documentos solo sirven como antecedente para reconstruir una versión nueva del sistema de inversiones.

Arquitectura histórica del experimento Jordan Belfort como agente conversacional directo de JR en Telegram.

## Principios

1. **JR decide en la vida real.** Ningún agente ejecuta compras, ventas, transferencias ni movimientos de dinero.
2. **Históricamente Jordan fue contacto directo de JR.** Desde 2026-07-04 queda retirado; Geoffrey no debe invocarlo por defecto.
3. **Tres mesas toman decisiones analíticas:** largo plazo, swing trading y day trading/paper trading.
4. **Las unidades informan; no deciden.** El Decision Lead de cada mesa integra sus unidades.
5. **Risk & Safety no vota, pero observa y puede advertir, limitar o recomendar no proceder.** JR recibe esas observaciones para decidir.
6. **Jordan puede pedir doble revisión y debe avisar a JR si cree que un Decision Lead está equivocado, exagerando confianza o ignorando riesgo.**
7. **Day trading está activo solo como paper trading.** No se usa dinero real hasta nueva autorización explícita de JR.
8. **Paper trading automático retirado:** el Radar Diario/Paper Trading Operator queda suspendido desde 2026-07-04; esta regla se conserva solo como antecedente histórico.

## Mapa rápido

- [[agentes/inversiones/agents/README]] — agentes reales del sistema.
- [[agentes/inversiones/lentes/README]] — checklists/lentes de análisis.
- [[agentes/inversiones/arquitectura-inversiones]] — estructura completa.
- [[agentes/inversiones/model-routing]] — asignación de modelos por componente.
- [[agentes/inversiones/protocolo-invocacion]] — flujo operativo.
- [[agentes/inversiones/parametros/long-term]] — parámetros de largo plazo.
- [[agentes/inversiones/parametros/swing-trading]] — parámetros de swing.
- [[agentes/inversiones/parametros/day-trading]] — parámetros de paper day trading.
- [[agentes/inversiones/parametros/risk-safety]] — límites y observaciones de riesgo.
- [[agentes/inversiones/formatos/decision-long-term]] — formato de respuesta long-term.
- [[agentes/inversiones/formatos/decision-swing]] — formato de respuesta swing.
- [[agentes/inversiones/formatos/decision-day-trading]] — formato de respuesta day/paper.
- [[agentes/inversiones/formatos/veto-risk]] — formato de observación de Risk.
- [[agentes/inversiones/formatos/journal-entry]] — journal de decisión/trade.

## Relacionado

- [[agentes/jordan-belfort/AGENT]]
- [[agentes/geoffrey/inversiones/sistema-agentes-inversiones]]
