---
type: reference
date: 2026-05-27
tags: [agentes, inversiones, jordan-belfort, modelos, paper-trading]
---

# Model routing — Sistema de inversiones

Ruteo aprobado por JR para Jordan y la estructura de inversiones. Esta página define **qué familia de modelo debe usar cada componente**; la configuración runtime debe mapear estos nombres al alias/modelo exacto disponible en OpenClaw.

## Principios

- **Decisiones y auditoría:** usar `gpt-5.5` u `opus` donde un error de criterio pueda contaminar la estrategia.
- **Análisis pesado de mercado:** usar **Nemotron 3 Super** para tesis, setups, contradicciones y lectura técnica/profunda.
- **Operación estructurada, registro y métricas:** usar **Qwen** para ejecución paper, Google Sheets, journal, cálculos y tareas determinísticas.
- **Explicación a JR:** usar `sonnet` o Qwen cuando el objetivo sea claridad y costo eficiente.
- **Guardrail:** ningún modelo puede operar live trading, dinero real, margen, leverage, futuros u opciones. Paper trading automático solo existe dentro del módulo aprobado.

## Asignación por componente

| Componente | Modelo preferido | Backup | Motivo |
|---|---|---|---|
| Jordan Belfort / CIO final | `gpt-5.5` | `opus` | Integración, auditoría final, criterio y comunicación con JR. |
| Risk Manager | `gpt-5.5` | `opus` | Detectar excesos, errores de endpoint, riesgo operativo y sesgos. |
| Compliance & Safety Officer | `gpt-5.5` | `opus` | Bloquear live trading/leverage/errores de configuración. |
| Charlie Munger / Long-term | Nemotron 3 Super | `opus` | Tesis profunda, calidad, paciencia, contradicciones. |
| Paul Tudor Jones / Swing | `gpt-5.5` | Nemotron 3 Super | Balance macro/técnico y decisión táctica. |
| Mark Douglas / Day/Paper | Nemotron 3 Super | `gpt-5.5` | Disciplina, setups, lectura intradía y consistencia. |
| Technical Analysis Units | Nemotron 3 Super | `gpt-5.5` | Niveles, estructura, momentum, invalidaciones. |
| Macro / Research Units | Nemotron 3 Super | `gpt-5.5` | Síntesis profunda de mercado y contexto. |
| News / Sentiment Units | Qwen | `sonnet` | Filtrar ruido, resumir señales y clasificar relevancia. |
| Paper Trading Operator | Qwen | `gpt-5.5` | Ejecución paper, control de endpoint, órdenes simuladas y estado. |
| Journal Keeper | Qwen | `sonnet` | Registro estructurado y trazabilidad. |
| Performance Analyst | Qwen | `sonnet` | ROI, winrate, drawdown, expectancy, profit factor y dashboard. |
| Google Sheets / Data Writer | Qwen | `sonnet` | Escritura estructurada y fórmulas/datos tabulares. |
| Teacher | `sonnet` | Qwen | Explicación clara en lenguaje simple para JR. |

## Regla operativa

Jordan decide con `gpt-5.5`, analiza con **Nemotron 3 Super** y opera/registra/mide con **Qwen**.

## Relacionado

- [[agentes/inversiones/arquitectura-inversiones]]
- [[agentes/inversiones/agents/README]]
- [[agentes/inversiones/protocolo-invocacion]]
- [[agentes/inversiones/parametros/day-trading]]
