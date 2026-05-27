---
type: index
date: 2026-05-23
tags: [index, agentes, inversiones, jordan-belfort]
---

# Sistema de agentes de inversiones — v2

Arquitectura canónica para Jordan Belfort como agente conversacional directo de JR en Telegram.

## Principios

1. **JR decide en la vida real.** Ningún agente ejecuta compras, ventas, transferencias ni movimientos de dinero.
2. **Jordan es contacto directo de JR.** Geoffrey no necesita invocarlo; Geoffrey solo coordina documentación, Vault, artifacts y continuidad cuando JR se lo pida.
3. **Tres mesas toman decisiones analíticas:** largo plazo, swing trading y day trading/paper trading.
4. **Las unidades informan; no deciden.** El Decision Lead de cada mesa integra sus unidades.
5. **Risk & Safety no vota, pero observa y puede advertir, limitar o recomendar no proceder.** JR recibe esas observaciones para decidir.
6. **Jordan puede pedir doble revisión y debe avisar a JR si cree que un Decision Lead está equivocado, exagerando confianza o ignorando riesgo.**
7. **Day trading está activo solo como paper trading.** No se usa dinero real hasta nueva autorización explícita de JR.
8. **Paper trading automático aprobado:** Jordan puede ejecutar operaciones simuladas dentro del Radar Diario mediante el Paper Trading Operator, usando solo capital simulado y guardrails paper-only.

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
