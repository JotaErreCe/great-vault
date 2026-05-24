# Toolchain oficial de Jordan — Fase 1 read-only

Estado: implementada parcialmente y segura por defecto  
Fecha: 2026-05-24  
Dueño: Geoffrey / Jordan Belfort  
Alcance: investigación y análisis; **sin ejecución**, **sin mover dinero**, **sin leverage**, **sin API keys de trading**.

## Principio operativo

Esta toolchain no reemplaza la arquitectura vigente de inversiones. Solo agrega fuentes y herramientas read-only para alimentar las mesas de Jordan:

- Charlie Munger / Long-Term: fundamentos, ETFs, macro, valuación.
- Paul Tudor Jones / Swing: precio, tendencia, noticias, liquidez.
- Mark Douglas / Day Trading: solo paper/backtesting/educativo.
- Risk Manager: sizing, drawdown, concentración, invalidación.
- Teacher / Journal: explicación simple y registro de aprendizajes.

## Instalado localmente

Directorio base:

- `/Users/jr/.openclaw/tools/jordan-phase1/`
- `/Users/jr/.openclaw/mcp/jordan-phase1/`

### CLIs / librerías

| Herramienta | Estado | Uso para Jordan | Notas de seguridad |
|---|---:|---|---|
| `ticker` | Instalado vía Homebrew | Cotizaciones rápidas en terminal | Read-only |
| `bitcoin-chart-cli` | Instalado vía npm global | Gráficas rápidas cripto | Read-only; `--version` falla si se ejecuta fuera de su carpeta npm, pero `--help` funciona desde su carpeta |
| `tstock` | Instalado en venv | Datos rápidos de acciones | Read-only |
| `OpenBB Platform` | Instalado en venv como paquete Python | Research multi-activo, equity, macro, crypto | Read-only por defecto; algunas extensiones pueden requerir API keys gratuitas |
| `yfinance` | Instalado por dependencias | Equity/ETF data vía Yahoo Finance | Fuente no oficial; confirmar datos importantes |

Venv:

```bash
/Users/jr/.openclaw/tools/jordan-phase1/venv
```

## MCPs configurados en OpenClaw

Configurados con `openclaw mcp set` en `/Users/jr/.openclaw/openclaw.json`:

| MCP | Estado | Comando | Uso principal |
|---|---:|---|---|
| `jordan-yfinance` | Configurado | `/Users/jr/.openclaw/tools/jordan-phase1/venv/bin/yfmcp` | Acciones/ETFs: info, históricos, financials, noticias, charts |
| `jordan-defillama` | Configurado | `node .../mcp-server-defillama/dist/index.js` | DeFi: TVL, protocolos, chains, stablecoins, precios |
| `jordan-crypto-fear-greed` | Configurado | `uv --directory .../crypto-feargreed-mcp run main.py` | Sentimiento cripto actual/histórico |
| `jordan-dexscreener` | Configurado | `node .../mcp-dexscreener/index.js` | DEX pairs, liquidez, volumen, tokens emergentes |

Validación:

- `openclaw config validate` pasó correctamente.
- `mcp-dexscreener` y `mcp-server-defillama` tuvieron vulnerabilidades iniciales de npm; se corrió `npm audit fix` y ambos quedaron en 0 vulnerabilidades reportadas.

## Metodologías/skills adoptadas como referencia

Estas skills de CLI Trader se revisaron como fuentes externas no confiables y se adoptan solo como **metodología**, no como autoridad ni automatización ejecutable. En Jordan quedan subordinadas a la arquitectura del Vault.

| Skill CLI Trader | Cómo se integra en Jordan | Límite |
|---|---|---|
| Trading Orchestrator | Refuerza el enrutamiento por asset/mesa y risk gate antes de responder | Jordan ya tiene protocolo propio; no reemplaza `protocolo-invocacion` |
| Agent Trading Guardrails | Refuerza aprobación humana, límites, kill-switch conceptual y audit trail | En Fase 1 no hay ejecución; se usa como checklist de seguridad |
| Risk Management | Position sizing, stops, drawdown y portfolio heat | Risk Manager del Vault conserva autoridad de observación |
| Portfolio Management | Asignación, rebalanceo, concentración y correlación | No reordena portafolio sin decisión de JR |
| Fundamental Analysis | Valuación equity, ratios, DCF, tokenomics y macro | Exige fuentes vivas y supuestos explícitos |
| Technical Analysis | Multi-timeframe, indicadores, confluencia, entry/stop/target | Nunca basta sin invalidación/riesgo |
| Backtesting & Validation | Sesgos, walk-forward, paper trading y validación | Solo paper/educativo en Fase 1 |
| Sentiment Analysis | Fear & Greed, social/news sentiment como overlay | Nunca base única de decisión |

## Pendientes deliberados / no activados todavía

| Herramienta | Motivo |
|---|---|
| FRED MCP | Requiere API key gratuita de FRED. No se configuró sin llave. |
| Stock News MCP | Requiere API key de Alpha Vantage. No se configuró sin llave. |
| CryptoPanic MCP | Requiere API key/plan de CryptoPanic. No se configuró sin llave. |
| CoinGecko MCP específico de CLI Trader | Alternativa existe, pero por ahora se cubre cripto base con yfinance/OpenBB/DefiLlama/DexScreener/Fear & Greed; evaluar antes de añadir más superficie. |
| `mop` CLI | Fórmula Homebrew no disponible en taps actuales. |
| `cointop` CLI | Fórmula Homebrew no disponible en taps actuales. |

## Reglas de uso obligatorio

1. Jordan nunca debe ejecutar trades ni mover dinero desde estas herramientas.
2. No usar API keys con permisos de trading en Fase 1.
3. Si una fuente contradice otra, reportar discrepancia y bajar confianza.
4. Para recomendaciones reales, separar siempre:
   - tesis,
   - datos usados,
   - invalidación,
   - sizing/riesgo,
   - escenario alterno,
   - explicación simple para JR.
5. Noticias/sentimiento no pueden ser base única de decisión.
6. DEX/new tokens = zona de alto riesgo; Risk Manager debe revisar liquidez, holders, contrato, volumen y posibilidad de rug/hype.

## Próximo paso recomendado

Conseguir llaves gratuitas para:

1. FRED API — macro.
2. Alpha Vantage — equity/news complementario.
3. CryptoPanic — noticias cripto.

Después de eso, añadir esos MCPs como `jordan-fred`, `jordan-stock-news`, `jordan-cryptopanic`.
