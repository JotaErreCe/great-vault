---
type: reference
date: 2026-06-09
tags: [inversiones, radar-diario, news-scan, paper-trading]
---

# Radar Diario — Flujo canónico v2

Doc canónica del Radar Diario de Jordan Belfort. Define qué se barre, cuándo, cómo se filtra y qué se produce. Aplica desde 2026-06-10.

## Propósito

Detectar **proactivamente** oportunidades del día — técnicas y por noticias — y, cuando corresponda, autorizar paper trades dentro del marco aprobado por JR.

## Ventanas

| Ventana | Hora (America/Guatemala) | Foco |
|---------|--------------------------|------|
| Pre-apertura | 7:00 AM | News scan global + setup técnico bolsa + cripto overnight |
| Mediodía | 12:30 PM | News scan intradía + revalidación setups abiertos |
| Cierre | 4:30 PM | News scan post-cierre + cierre paper trades intradía + journal |
| Resumen nocturno | 8:30 PM | Reporte final del día (existente) |

## Módulo 1 — Scan técnico (existente)

- Watchlist bolsa/ETF y cripto.
- Tendencia, soportes/resistencias, RSI, volumen, eventos cercanos.
- Aplica lentes técnico y macro-event-risk.

## Módulo 2 — News scan (nuevo, 2026-06-09)

Barrido sistemático de catalizadores que pueden mover precio o abrir setups nuevos.

### Fuentes

- **Macro / política monetaria**: Fed, BCE, datos CPI/PPI/empleo, geopolítica relevante.
- **Bolsa**: earnings del día, guidance, M&A, splits, upgrades/downgrades analyst, SEC filings relevantes.
- **Cripto**: listings Binance/Coinbase, hacks, token unlocks, anuncios protocolo, ETF flows, decisiones regulatorias.

### Herramientas

- `brave-search` para barrido general.
- `yfinance_get_ticker_news` para news por ticker.
- Defillama / Dexscreener para cripto on-chain.

### Filtro de relevancia (descartar ruido)

Una noticia entra al radar **solo** si cumple al menos uno:

1. Toca un activo en el universo operable (IBKR o Binance).
2. Abre un setup técnico nuevo (gap, ruptura, sobrerreacción, volumen anómalo).
3. Cambia tesis activa de un ticker ya en watchlist o portfolio real.
4. Mueve macro de forma estructural (Fed cut/hike, dato shock, crisis).

Se descarta:

- Clickbait / opinión sin hecho nuevo.
- Repetición de noticia ya descontada.
- Eventos sin impacto direccional claro.

### Output del módulo

Sección "Oportunidades surgidas de noticias hoy" con, por candidato:

- Ticker / token + plataforma operable.
- Catalizador (1 línea, fuente con timestamp).
- Tesis corta (long / short / observar).
- Setup técnico asociado.
- Confianza del Decision Lead (%).
- Decisión analítica: considerar / esperar / rechazar / observar / paper-only.

## Módulo 3 — Paper trading automático (existente, actualizado)

- Solo dentro del Radar Diario o con orden explícita de JR.
- Threshold: **≥ 50% confianza** del Decision Lead para abrir (ver [[agentes/inversiones/parametros/day-trading]]).
- Sizing fijo 1R = USD 10 sobre USD 100 lógicos.
- Stop obligatorio antes de abrir; mueve a break-even cuando el sistema lo dicta.
- Ejecuta Paper Trading Operator; registra Journal Keeper; mide Performance Analyst.

## Módulo 4 — Riesgo y veto (Risk Manager)

- Bloquea entradas si hay evento binario inminente no entendido.
- Bloquea entradas si la noticia detectada implica volatilidad fuera de tolerancia.
- Sus observaciones aparecen en todo output significativo.

## Métricas del Radar Diario

- Cantidad de candidatos detectados (técnico vs news scan, por separado).
- Conversión a paper trade.
- Expectancy acumulada y PnL lógico a 30 días.

> Métrica de decisión: **expectancy positiva** a 30 días. Si el PnL lógico cae < −USD 20 a 30 días, revisión obligatoria. Winrate solo descriptivo.

## Relacionado

- [[agentes/inversiones/protocolo-invocacion]]
- [[agentes/inversiones/parametros/day-trading]]
- [[agentes/inversiones/parametros/swing-trading]]
- [[agentes/inversiones/lentes/news-events]]
- [[agentes/inversiones/lentes/sentiment]]
- [[agentes/inversiones/lentes/macro-event-risk]]
- [[agentes/inversiones/agents/paper-trading-operator/AGENT]]
- [[agentes/inversiones/agents/risk-manager/AGENT]]
