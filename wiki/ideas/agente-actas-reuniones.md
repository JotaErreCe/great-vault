---
type: idea
date: 2026-09-22
tags:
  - idea
  - tema/producto
  - tema/legal
  - tema/ia
  - prioridad/baja
---

# Agente de actas de reunión — análisis y viabilidad

Cómo funcionan los agentes tipo diio / Otter / Fireflies / Read AI, y si tiene sentido construir uno vertical para el mercado legal guatemalteco. Precios verificados al 2026-09-22.

**Estado: análisis, no ejecución.** Ver [[#Puerta de decisión]].

---

## Las tres arquitecturas

| | Cómo capta | Costo marginal | Fricción |
|---|---|---|---|
| **A. Bot que se une** (diio, Otter, Fireflies, Read AI) | Chrome headless en servidor entra como participante | **Alto** — contenedor corriendo en vivo por reunión | Visible, intrusivo, expuesto legalmente |
| **B. Nativo** (Zoom RTMS, Google Meet Media API) | WebSocket de la plataforma; sin bot | Medio | Requiere aprobación del admin del workspace |
| **C. Local** (Granola) | Audio del sistema + micrófono en la máquina del usuario | **Casi cero** | Requiere app de escritorio |

Notas técnicas:
- **Zoom RTMS** entrega audio, video, transcripción y eventos en vivo. Solo recibe — no se puede enviar media de vuelta.
- **Teams** no tiene equivalente nativo: sigue exigiendo un bot vía Microsoft Graph.
- **Captura local en macOS**: ScreenCaptureKit / Core Audio taps. En Windows: WASAPI loopback.

## La pipeline

```
Calendario → Captura → Diarización → Transcripción → Resumen (LLM) → Distribución
```

**La diarización es el cuello de botella real.** Transcribir es commodity; saber *quién* dijo qué es lo que hace útil el resumen. En español latinoamericano con code-switching, ahí se cae la mayoría de herramientas gringas.

---

## Costos de infraestructura (verificados 2026-09)

### Bots como servicio (arquitectura A)

| Proveedor | Precio |
|---|---|
| Recall.ai | $0.50/hr grabación + $0.15/hr transcripción + $0.05/hr storage |
| MeetStream | ~$0.45/hr todo incluido |
| Skribby | $0.35/hr |
| Meeting BaaS | $0.35–0.50/hr, diarización incluida |
| Attendee / Vexa | Autohospedado, open source |

### Transcripción (ASR)

| Proveedor | Precio | Nota |
|---|---|---|
| AssemblyAI Universal-2 | $0.15/hr + $0.02 diarización | El más barato capaz |
| AssemblyAI Pro Realtime | $0.45/hr | Streaming |
| Deepgram Nova-3 Multilingual | ~$0.55/hr | **Mejor para code-switching español/inglés** |
| Gladia | $0.61/hr | Todo incluido |
| Whisper local | $0 marginal | Corre en Apple Silicon |

### LLM para el resumen

Una hora de reunión ≈ **15,000 tokens de entrada + 2,500 de salida**.

| Modelo | Entrada $/M | Salida $/M | Costo por hora de reunión |
|---|---|---|---|
| Claude Haiku 4.5 | $1.00 | $5.00 | **$0.028** |
| Claude Sonnet 5 | $2.00 | $10.00 | **$0.055** |

Con **Batch API el costo baja 50%** — y los resúmenes de reunión no son sensibles a latencia, así que aplica perfecto: Sonnet 5 en batch ≈ **$0.028/hora**.

---

## Por qué el modelo de bots no es negocio

| Concepto | Con bots (Recall.ai) |
|---|---|
| Costo por hora procesada | ~$0.70 |
| Usuario intensivo: 15 hrs/mes | ~$10.50 de costo |
| Precio de mercado | $8.33–$29/usuario/mes |
| **Margen bruto a $15/mes** | **~30%** |

Un SaaS normal opera a **75–85% de margen bruto**. Con bots esto no es un negocio de software: es reventa de infraestructura con costo marginal por hora. Por eso Otter limita a 300 minutos en su plan gratis.

---

## El giro: arquitectura local

Mover la captura a la máquina del usuario **elimina el costo dominante**.

| Configuración | Costo por hora de reunión |
|---|---|
| Bot + ASR nube + LLM | **~$0.73** |
| Local + Deepgram + Sonnet 5 batch | **~$0.58** |
| Local + AssemblyAI + Sonnet 5 batch | **~$0.20** |
| **Local + Whisper on-device + Sonnet 5 batch** | **~$0.03** |

**Reducción del 96% en costo marginal.** Eso convierte el modelo de reventa de infraestructura en un negocio de software de verdad.

---

## El ángulo: actas legales en Guatemala

### Mercado

- **~31,000 abogados colegiados** en Guatemala (Embajada EE.UU., feb 2026). Todos pueden ejercer como notarios.
- Mercado atendible real: los que hacen volumen transaccional, corporativo, notarial o de cumplimiento. Estimación conservadora **2–5% → 600 a 1,500 profesionales**.

### La propuesta de valor no es la transcripción, es el documento

El valor no está en el texto crudo sino en lo que sale al final:
- Acta de junta directiva en formato guatemalteco
- Minuta de reunión con cliente, con compromisos y plazos
- Registro con sello de tiempo para expedientes de Persona Obligada (ver [[propi-aml-compliance]])

### Justificación de precio

A la tarifa de [[amc-legal]] (**USD 90/hr**), redactar un acta toma 30–60 min. Si la herramienta ahorra 40 min por reunión y hay 8 reuniones al mes:

**5.3 horas ahorradas × USD 90 = USD 480/mes de tiempo facturable recuperado.**

Cobrar **USD 49/mes** es trivialmente justificable.

### Unidad económica a USD 49/mes

Usuario intensivo: 20 horas de reunión al mes.

| Configuración | Costo/mes | **Margen bruto** |
|---|---|---|
| Local + Deepgram | $11.60 | **76%** |
| Local + AssemblyAI | $4.00 | **92%** |
| Local + Whisper on-device | $1.20 | **97.5%** |

**Todas cierran.** Compárese con el 30% del modelo de bots.

### Escenarios de ingreso

| Usuarios pagando | MRR | ARR |
|---|---|---|
| 50 | $2,450 | **$29,400** |
| 200 | $9,800 | **$117,600** |
| 500 | $24,500 | **$294,000** |

Punto de equilibrio con costo de desarrollo de ~$30,000: **entre 50 y 70 usuarios**.

---

## Riesgos

1. **La app de escritorio es más difícil que el bot.** Se cambia costo de infraestructura por costo de ingeniería. macOS + Windows, permisos de audio, actualizaciones. **3–5 meses** para una v1 sólida.
2. **Distribución.** El abogado guatemalteco no compra SaaS por internet. Es venta de relación — CANG, gremios, referidos. Esa es la barrera real, no la técnica.
3. **Calidad del ASR en español jurídico.** Hay que validarla antes de escribir una línea de código de producto.
4. **Consentimiento.** La captura local evita el bot visible, pero **no elimina la obligación de consentimiento**. El marco guatemalteco hay que verificarlo aparte — no asumir que aplica la doctrina estadounidense.

### Contexto legal internacional (por si hay clientes fuera)

- **11 estados de EE.UU. exigen consentimiento de todas las partes**: California, Florida, Illinois, Massachusetts, Maryland, Montana, Nevada, New Hampshire, Pennsylvania, Washington y Connecticut. **Basta un participante en uno de esos estados para que su ley gobierne toda la llamada.**
- **Ninguna jurisdicción reconoce hoy que ver el bot en la lista de participantes sea notificación o consentimiento válido.**
- **Demandas colectivas activas contra Otter, Fireflies y Granola.** La moción de Otter se argumentó el **20 de mayo de 2026** ante la jueza Eumi K. Lee — primera prueba federal de si las leyes de escuchas alcanzan a un bot en videollamada.
- GDPR: Art. 6 exige base legal para procesar voz; los identificadores biométricos de voz caen en categoría especial del Art. 9.

---

## Puerta de decisión

**No ejecutar por ahora.** El análisis dice que el modelo cierra, pero la capacidad no está.

Reconsiderar cuando se cumpla **alguna**:

1. Se libera tiempo real — hoy hay 8 proyectos activos y un bebé de 6 meses
2. Aparece un socio técnico que tome la app de escritorio
3. Un cliente de [[amc-legal]] pide explícitamente este flujo y financia el piloto

**Si alguna vez se ejecuta: vertical y local. Nunca horizontal ni con bots.**

### Primer paso barato, si se quiere validar

Antes de construir nada: grabar 5 reuniones reales (Propi, Disegno Casa, UK), pasarlas por Deepgram y AssemblyAI, y comparar la calidad de diarización y del acta generada. **Costo: menos de USD 5.** Eso responde el riesgo #3 sin comprometer nada.

---

## Relacionado

- [[amc-legal]] — la tarifa que define el valor del tiempo ahorrado
- [[propi-aml-compliance]] — conservación documental como caso de uso
- [[nas-casero]] — mismo patrón de análisis: costo marginal vs. suscripción
- [[wiki/index]]
