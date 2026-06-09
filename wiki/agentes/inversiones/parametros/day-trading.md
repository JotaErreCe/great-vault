---
type: reference
date: 2026-06-09
tags: [inversiones, day-trading, paper-trading, parametros]
---

# Parámetros — Day Trading Desk / Paper Trading

## Estado

Activo únicamente para **paper trading**. Prohibido usar dinero real hasta autorización explícita de JR.

## Herramienta sugerida

Primera opción: **TradingView Paper Trading**, por ser gratuito/fácil para gráficos, watchlists, alertas visuales y práctica sin dinero real. Alternativas: Investopedia Simulator para acciones o paper trading del broker si está disponible, pero TradingView es la opción inicial más simple.

## Lead

Mark Douglas — Day Trading Discipline / Decision Lead.

## Objetivo

Aprender disciplina, lectura intradía y journal. No buscar dinero real.

## Capital lógico

- USD 100 lógicos por mesa (bolsa y cripto, separados).
- 1R = USD 10 (10% del capital lógico). Sizing fijo; no ajustar por "convicción".

## Threshold de confianza para abrir paper trade

- **≥ 50% de confianza del Decision Lead** → setup elegible para paper trade.
- Vigente desde 2026-06-09 (decisión JR). Ajuste anterior: ≥ 75%.
- Justificación: en paper trading USD 100 lógicos, ser ultra-selectivo bloquea el aprendizaje. Se aceptan setups B y B+; se descartan solo C y ruido.

## Reglas

- Paper trades solamente.
- Stop loss obligatorio antes de abrir; no se mueve excepto a break-even.
- Sizing fijo 1R = USD 10. No piramidar.
- Máximo sugerido inicial: 1–3 paper trades por sesión (mantener calidad del journal).
- No operar por aburrimiento.
- No perseguir velas.
- Todo paper trade debe tener setup, entrada, invalidación y salida.
- Si hay frustración, FOMO o revenge trading, detener sesión.
- Noticias/eventos de alto impacto pueden bloquear práctica.

## Métricas — control de sistema

Métricas de **decisión** sobre si el sistema funciona:

- **Expectancy** = (winrate × ganancia promedio R) − (lossrate × pérdida promedio R). Debe ser **positiva** a 30 días.
- **PnL lógico acumulado** a 30 días. Si cae por debajo de **−USD 20 (−20% del capital lógico)** → revisión obligatoria de criterios.

Métricas **descriptivas** (se reportan pero no son gatillo de decisión):

- Winrate.
- Calidad del setup.
- Respeto a invalidación.
- R/R planeado vs ejecutado.
- Emoción registrada.
- Error principal y aprendizaje.

> Regla: el winrate aislado **no** decide si el sistema sirve. Un sistema 35% winrate con R/R 3:1 es rentable; uno 70% winrate con R/R 1:2 quiebra. Decisión por expectancy + PnL.

## Output

Usar [[agentes/inversiones/formatos/decision-day-trading]].

## Relacionado

- [[agentes/inversiones/desks/day-trading/AGENT]]
- [[agentes/inversiones/learning-journal/AGENT]]
