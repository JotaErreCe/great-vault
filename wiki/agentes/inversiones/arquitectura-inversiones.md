---
type: reference
date: 2026-05-23
tags: [agentes, inversiones, jordan-belfort]
---

# Arquitectura de inversiones v2

```text
JR — Usuario final / decide
└── Jordan Belfort — CIO / Investment Mentor / Auditor final / agente directo en Telegram
    ├── Long-Term Investing Desk
    │   └── Charlie Munger — Long-Term Decision Lead
    │       ├── Macro & Market Regime Unit
    │       ├── News & Events Unit
    │       ├── Sentiment Unit
    │       ├── Equity Research Unit
    │       ├── Crypto Research Unit
    │       ├── Market Structure & Liquidity Unit
    │       └── DCA & Allocation Unit
    ├── Swing Trading Desk
    │   └── Paul Tudor Jones — Swing Trading Decision Lead
    │       ├── Macro & Market Regime Unit
    │       ├── News & Events Unit
    │       ├── Sentiment Unit
    │       ├── Equity Research Unit
    │       ├── Crypto Research Unit
    │       ├── Market Structure & Liquidity Unit
    │       ├── Technical Analysis Unit
    │       ├── Price Action Unit
    │       ├── SMC Unit
    │       ├── Quant & Indicators Unit
    │       └── Trade Planning Unit
    ├── Day Trading Desk — paper trading only
    │   └── Mark Douglas — Day Trading Discipline / Decision Lead
    │       ├── Macro & Event Risk Unit
    │       ├── News & Events Unit
    │       ├── Sentiment Unit
    │       ├── Equity Intraday Unit
    │       ├── Crypto Intraday Unit
    │       ├── Market Structure & Liquidity Unit
    │       ├── Intraday Technical Analysis Unit
    │       ├── Intraday Price Action Unit
    │       ├── Intraday SMC Unit
    │       ├── VWAP / Momentum Unit
    │       └── Execution Planning Unit
    ├── Risk & Safety Branch
    │   └── Risk Manager — Observations / Limits / Position Sizing
    │       ├── Bear Case Analyst
    │       ├── Black Swan Simulator
    │       ├── Compliance & Safety Officer
    │       ├── Position Sizing Analyst
    │       ├── Drawdown Monitor
    │       └── Correlation & Concentration Analyst
    ├── Learning & Journal Branch
    │   ├── Journal Keeper
    │   ├── Performance Analyst
    │   └── Teacher
    └── Paper Trading Operations
        └── Paper Trading Operator — paper execution / Alpaca / TradingView journal
```

## Autoridad

| Rol | Autoridad |
|---|---|
| JR | Decide si actúa o no. |
| Jordan | Audita, integra, enseña, pide doble chequeo y entrega respuesta final a JR. |
| Charlie Munger | Decision Lead para largo plazo. |
| Paul Tudor Jones | Decision Lead para swing trading. |
| Mark Douglas | Decision Lead para day trading en paper. |
| Risk Manager | No vota; emite observaciones, límites, sizing y advertencias para JR. |
| Paper Trading Operator | Ejecuta operaciones simuladas paper-only cuando el Radar Diario o una orden explícita lo autoriza. |
| Performance Analyst | Calcula desempeño, métricas, comparaciones y dashboard; no decide ni ejecuta. |
| Units | Informan; no deciden. |
| Geoffrey | No invoca a Jordan por defecto; mantiene Vault/artifacts/continuidad cuando JR lo solicite. |

## Regla de diseño

La arquitectura usa **agentes reales** donde hay juicio/responsabilidad y **units como lentes/checklists estructurados** donde solo hay análisis de soporte. Esta es la forma óptima final: evita 40 agentes opinando y conserva profundidad analítica. Si una unit demuestra valor recurrente, puede convertirse en agente dedicado después.

Agentes reales: [[agentes/inversiones/agents/README]].  
Lentes/checklists: [[agentes/inversiones/lentes/README]].

## Model routing

La asignación aprobada por JR vive en [[agentes/inversiones/model-routing]]: Jordan decide con `gpt-5.5`, analiza con **Nemotron 3 Super** y opera/registra/mide con **Qwen**.

## Relacionado

- [[agentes/inversiones/protocolo-invocacion]]
- [[agentes/inversiones/agents/README]]
- [[agentes/inversiones/model-routing]]
- [[agentes/inversiones/lentes/README]]
- [[agentes/inversiones/agents/charlie-munger/AGENT]]
- [[agentes/inversiones/agents/paul-tudor-jones/AGENT]]
- [[agentes/inversiones/agents/mark-douglas/AGENT]]
- [[agentes/inversiones/agents/risk-manager/AGENT]]
- [[agentes/inversiones/agents/journal-keeper/AGENT]]
- [[agentes/inversiones/agents/paper-trading-operator/AGENT]]
- [[agentes/inversiones/agents/performance-analyst/AGENT]]
- [[agentes/inversiones/agents/teacher/AGENT]]
