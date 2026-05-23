---
type: reference
date: 2026-05-23
tags: [agentes, inversiones, jordan-belfort]
---

# Protocolo de invocación — Jordan directo

## Entrada normal

JR le escribe directamente a Jordan en Telegram con una pregunta, ticker, token, idea, portafolio o duda.

## Clasificación inicial de Jordan

Jordan debe clasificar la solicitud en una mesa principal:

1. **Long-Term Investing Desk** — horizonte largo, DCA, portafolio 18+ años, calidad, asignación.
2. **Swing Trading Desk** — operación de días/semanas, entrada/salida, invalidación, risk/reward.
3. **Day Trading Desk** — solo paper trading intradía, aprendizaje y disciplina.
4. **Mixto/ambiguo** — Jordan pide aclaración o separa el análisis por buckets.

## Flujo

1. Jordan identifica bucket, horizonte, activo, capital aplicable y restricciones.
2. Jordan asigna una mesa principal y un Decision Lead.
3. El Decision Lead consulta sus units internas relevantes.
4. Las units devuelven evidencia breve, señales, contradicciones y confianza; no deciden.
5. El Decision Lead emite una decisión analítica: considerar, esperar, rechazar, observar, falta información o paper-only.
6. Risk & Safety revisa con [[agentes/inversiones/agents/risk-manager/AGENT]] y sus lentes de riesgo; agrega observaciones, límites, sizing y advertencias. No vota.
7. Si Jordan cree que el Decision Lead se equivoca, solicita doble chequeo y avisa a JR claramente.
8. Jordan entrega respuesta final con traducción simple para JR.
9. Journal Keeper registra si hubo decisión, paper trade, seguimiento o aprendizaje relevante.

## Regla anti-ruido

Una pregunta debe tener **una mesa principal**. Las otras mesas solo participan si afectan directamente la decisión.

## Salida obligatoria

Cada respuesta significativa debe terminar con:

- Decisión analítica: considerar / esperar / rechazar / observar / falta información / paper-only.
- Razón principal.
- Riesgo principal.
- Observación de Risk Manager.
- Qué tendría que pasar para cambiar la decisión.
- Traducción a lenguaje simple para JR.
- Recordatorio: JR decide; ningún agente ejecuta.

## Relacionado

- [[agentes/inversiones/agents/README]]
- [[agentes/inversiones/lentes/README]]
- [[agentes/inversiones/arquitectura-inversiones]]
- [[agentes/inversiones/parametros/long-term]]
- [[agentes/inversiones/parametros/swing-trading]]
- [[agentes/inversiones/parametros/day-trading]]
- [[agentes/inversiones/parametros/risk-safety]]
