---
type: reference
date: 2026-05-21
tags: [inversiones, google-sheets, tracking]
---

# Google Sheet — schema de seguimiento de inversiones

Schema aprobado/diseñado para el sistema Jordan.

## Pestañas

1. Portfolio real
2. Trading bolsa
3. Trading cripto
4. Radar de oportunidades
5. Bolsa global
6. Cripto
7. Alertas
8. Decisiones tomadas
9. Glosario para JR
10. Histórico de reportes

## Portfolio real

| Columna | Uso |
|---|---|
| Fecha | fecha de corte |
| Plataforma | IBKR, Binance, otro |
| Activo | ticker/símbolo |
| Tipo | ETF, equity, BTC, altcoin, cash |
| Cantidad | unidades |
| Precio promedio | cost basis/promedio |
| Precio actual | precio de corte |
| Valor actual | cantidad × precio |
| Ganancia/pérdida USD | P/L USD |
| Ganancia/pérdida % | P/L % |
| Peso en portafolio | concentración |
| Riesgo | bajo/medio/alto/muy alto |
| Tendencia | alcista/lateral/bajista |
| Acción sugerida | mantener/observar/rebalancear/etc. |
| Comentario | explicación breve |

## Trading bolsa

Fecha · Activo · Tesis · Tipo de trade · Precio de entrada · Monto usado · Salida esperada · Invalidación · Riesgo asumido · Estado · Resultado · Aprendizaje

## Trading cripto

Fecha · Activo · Tesis · Tipo de trade · Precio de entrada · Monto usado · Salida esperada · Invalidación · Riesgo asumido · Señal on-chain · Supply/unlocks · Estado · Resultado · Aprendizaje

## Radar de oportunidades

Fecha · Activo · Mercado · Sector/narrativa · Tipo · Tesis resumida · Tendencia · Riesgo · Confianza · Fuente principal · Señal técnica · Señal fundamental · Señal de noticias · Señal de sentimiento · Entrada posible · Salida posible · Invalidación · Monto sugerido % · Estado · Próxima revisión

## Nota de implementación

JR aprobó crear la Google Sheet. Herramienta pendiente: en esta sesión Geoffrey tiene herramientas de lectura de Sheets, pero no una herramienta directa `create spreadsheet/update cells`; si no se habilita, se creará por export/CSV o mediante flujo Google Workspace alternativo aprobado.

## Relacionado

- [[sistema-agentes-inversiones]]
- [[formatos-reportes-alertas-inversiones]]
