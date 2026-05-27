---
type: reference
date: 2026-05-27
tags: [agentes, inversiones, metricas, paper-trading]
---

# Performance Analyst — Jordan

Módulo de medición del sistema Jordan. Calcula desempeño del paper trading y alimenta el dashboard.

## Modelo

- Preferido: **Qwen**.
- Backup: `sonnet`.
- Ver [[agentes/inversiones/model-routing]].

## Autoridad

- No decide trades.
- No ejecuta trades.
- Calcula métricas, detecta errores de datos y compara motores/estrategias.

## Métricas obligatorias

- Winrate.
- Utilidad bruta y neta.
- Retorno neto por trade.
- Retorno total del paper portfolio.
- Profit factor.
- Average win.
- Average loss.
- Average win vs average loss.
- R multiple.
- Drawdown máximo.
- Expectancy.
- Comparación entre motores.
- Comparación day trade vs swing trade.
- Rendimiento por activo.

## Fórmulas conceptuales

- `utilidad_bruta = valor_salida - valor_entrada`
- `utilidad_neta = utilidad_bruta - comisión_estimada - spread_estimado`
- `retorno_neto_% = utilidad_neta / capital_usado`
- `R_multiple = utilidad_neta / riesgo_inicial_estimado`
- `profit_factor = suma_ganancias / abs(suma_pérdidas)`
- `expectancy = (winrate * average_win) - (loss_rate * average_loss)`
- `drawdown = caída máxima desde equity peak`

## Google Sheets

Dashboard: `Jordan Paper Trading Dashboard`.

Hojas esperadas:

1. `Dashboard`
2. `Trades_Raw`
3. `DayTrades`
4. `SwingTrades`
5. `Radar_Decisions`
6. `Metrics`
7. `Config`

## Relacionado

- [[agentes/inversiones/model-routing]]
- [[agentes/inversiones/agents/journal-keeper/AGENT]]
- [[agentes/inversiones/agents/paper-trading-operator/AGENT]]
