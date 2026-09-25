---
type: resource
date: 2026-09-24
tags:
  - resource
  - tema/producto
  - tema/ia
  - tema/productividad
---

# Goal prompt — Secretaria en esteroides

Prompt exhaustivo para arrancar el desarrollo. Contexto económico y de arquitectura en [[agente-actas-reuniones]].

> **Reescrito 2026-09-24.** La versión anterior especificaba un generador de actas legales. JR corrigió el alcance: lo que quiere es transcripción, resumen, obligaciones por parte y recordatorios. Producto distinto, no un ajuste.

---

## GOAL

Construir una **aplicación de escritorio que convierte cada reunión en cuatro cosas**: la transcripción, un resumen, la lista de obligaciones de cada parte, y recordatorios accionables para el usuario.

La metáfora operativa es **una secretaria en esteroides**: alguien que estuvo en la reunión, tomó nota de todo, y al día siguiente te dice *"tú quedaste de mandar esto, Ena quedó de confirmarte aquello, y nadie se hizo cargo de esto otro."*

El valor no está en la transcripción. Está en que **nada de lo que se prometió en una reunión se pierda**.

---

## USUARIO CERO

El desarrollador construye primero para **un usuario real con reuniones reales**: JR, abogado guatemalteco que opera simultáneamente un despacho (AMC Legal), una inmobiliaria (Propi), un caso de construcción (Disegno Casa/Altezza) y un negocio de terapias (Understanding Kids).

Su patrón de reuniones es el caso de prueba:
- Español guatemalteco con code-switching frecuente hacia el inglés
- 3 a 8 participantes
- Gente que se compromete verbalmente y nadie lleva registro
- Reuniones por Meet, Zoom, Teams, y también presenciales y por teléfono

**Si funciona para él, funciona.** No optimizar para un usuario hipotético.

---

## DECISIONES YA TOMADAS — NO RE-LITIGAR

Si crees que alguna está mal, **dilo y espera respuesta; no las cambies por tu cuenta.**

1. **Captura LOCAL, nunca bots.** No Recall.ai, no Meeting BaaS, ningún bot que se una a la reunión. Los bots cuestan ~$0.70/hora procesada y hunden el margen bruto a 30%. La captura local lo baja a $0.03–0.58/hora, con margen de 76–97%.
2. **Los recordatorios son solo para el usuario.** La app **nunca** manda correos ni notificaciones a terceros. Cero capa de envío externo, cero cuentas para otros participantes.
3. **Herramienta general para servicios profesionales**, no vertical legal. Verticales se agregan después, sobre la misma base.
4. **macOS primero.** Windows es fase posterior.
5. **Español primario**, con manejo obligatorio de code-switching español/inglés.
6. **El usuario es dueño de sus datos.** Nada de entrenar modelos con contenido de reuniones. Hay secreto profesional de por medio.

### Sobre el diferenciador — decirlo sin adornos

Al ser general, este producto **compite de frente con Otter y Fireflies**, que ya extraen action items, y con Fathom, que es gratis. Lo que queda como diferencia real es:

- **Captura local sin bot** — nadie ve un participante fantasma en la llamada
- **Calidad de extracción de compromisos en español**, que las herramientas gringas hacen mal
- **La distinción entre lo que debo yo y lo que me deben** — que las demás no modelan bien
- **Construido por un usuario intensivo real**

Eso es lo que hay. No inventar ventajas que no existen.

---

## NO-GOALS (fuera de alcance, explícitamente)

- Bot que se una a Zoom, Meet o Teams.
- Enviar correos, recordatorios o notificaciones a terceros.
- Crear cuentas para otros participantes.
- Transcripción en vivo mostrada durante la reunión.
- Traducción entre idiomas.
- Análisis de sentimiento, coaching de ventas, métricas de participación.
- Integración con CRM.
- Versión web o app móvil propia.
- Edición colaborativa.
- Generación de documentos legales formales (actas notariales, etc.) — puede venir como vertical futuro, no ahora.

---

## LOS CUATRO ENTREGABLES POR REUNIÓN

### 1. Transcripción
Texto completo con hablantes identificados y marcas de tiempo. Consultable y buscable. El usuario debe poder ir del resumen al fragmento exacto que lo sustenta.

### 2. Resumen
Corto y denso. Qué se discutió, qué se decidió, qué quedó abierto. **Máximo una pantalla.** Si el resumen requiere scroll, está mal hecho.

Separar explícitamente tres cosas que la gente confunde:
- **Decisiones** — se resolvió algo
- **Obligaciones** — alguien se comprometió a hacer algo
- **Temas abiertos** — se habló y no se resolvió

### 3. Obligaciones por parte
El corazón del producto. Ver sección propia abajo.

### 4. Recordatorios
Solo los del usuario, y solo tras su aprobación. Ver sección de entrega.

---

## EXTRACCIÓN DE OBLIGACIONES — EL CORAZÓN

Cada obligación detectada debe tener:

| Campo | Descripción |
|---|---|
| **Quién** | Participante concreto, mapeado a una persona real. Nunca "el equipo" ni "alguien" |
| **Qué** | Acción concreta: verbo + objeto. "Enviar el contrato de bodega a Thelma", no "dar seguimiento" |
| **Cuándo** | Fecha explícita, relativa resuelta a fecha real ("la próxima semana" → fecha), o sin fecha |
| **Condición** | Si el compromiso depende de algo: "si el cliente aprueba, entonces..." |
| **Firmeza** | `firme` / `tentativo` / `mencionado` — ver abajo |
| **Evidencia** | El fragmento textual exacto que lo sustenta, con marca de tiempo |
| **Confianza** | Qué tan seguro está el modelo |

### La distinción que define el producto

**Separar obligaciones en dos cubetas, y tratarlas distinto:**

- **MÍAS** (del usuario) → se convierten en recordatorios propuestos
- **DE OTROS** → van a un tablero de seguimiento, para que el usuario decida a quién perseguir y cuándo

Esta separación es lo que las herramientas horizontales hacen mal y es la razón de ser de la app.

**Tercera cubeta: huérfanas.** Cuando se dijo que algo hay que hacer pero nadie lo asumió — *"alguien tiene que revisar eso"*— marcarlo explícitamente como **sin dueño**. Esas son las que más se pierden en la vida real.

### Niveles de firmeza — no todo lo que se dice es un compromiso

- **Firme**: "Te lo mando mañana", "Yo me encargo"
- **Tentativo**: "Voy a tratar de verlo esta semana", "Déjame revisarlo"
- **Mencionado**: "Habría que actualizar eso en algún momento"

**Solo lo firme genera recordatorio automático.** Lo tentativo se muestra aparte. Lo mencionado vive en el resumen y no molesta a nadie.

Confundir estos tres niveles es el defecto más probable del producto. Una app que te llena de recordatorios por cada cosa que alguien dijo de paso se desinstala en una semana.

### Regla dura de fidelidad

Una obligación **solo puede existir si alguien realmente se comprometió en la reunión**. Prohibido inferir, completar o suponer compromisos razonables que no se dijeron. Si no hay fragmento que lo sustente, no existe.

---

## ENTREGA

### Canal primario: correo al usuario

Al terminar el procesamiento, un correo con:
1. Asunto con el título de la reunión y la fecha
2. El resumen de una pantalla
3. **Tus pendientes** — obligaciones del usuario, con fecha
4. **Pendientes de otros** — quién quedó de qué, para seguimiento
5. **Sin dueño** — lo que quedó en el aire
6. Enlace a la transcripción completa

El correo es la interfaz principal. Debe ser útil leído en el teléfono, sin abrir nada más.

### Canal secundario: llevar los recordatorios al teléfono

Tras revisar, el usuario decide **cuáles pendientes propios convertir en recordatorios**, y la app se los pasa a la app de recordatorios de su teléfono.

**Restricción técnica real — no prometer sincronización perfecta:**

| Plataforma | Vía viable | Calidad |
|---|---|---|
| **Apple** | EventKit desde la app de escritorio (ya validado en este equipo), o archivo `.ics` adjunto | Buena |
| **Google** | Google Tasks API o Google Calendar API | Buena |
| **Samsung** | No hay API pública de Samsung Reminder. Vía `.ics` hacia Samsung Calendar | Limitada |

Implementar Apple y Google como integración real. Para Samsung, entregar `.ics` y **decir claramente en la interfaz que es la opción con menos soporte**. No fingir paridad.

La entrega es **siempre con aprobación explícita**. La app propone; el usuario confirma. Nunca escribe recordatorios sin que los vea.

---

## ARQUITECTURA

```
Captura local (macOS)
   ↓ dos pistas: audio del sistema + micrófono
Transcripción + diarización
   ↓
Extracción (Claude) → resumen + obligaciones + decisiones + temas abiertos
   ↓
Correo al usuario
   ↓ con aprobación
Recordatorios → Apple / Google / .ics
```

### Captura
- **ScreenCaptureKit / Core Audio taps** (macOS 14.2+) para audio del sistema.
- Micrófono como **pista separada**. Dos pistas mejoran muchísimo la diarización: el usuario siempre es identificable sin ambigüedad.
- Funciona con cualquier fuente: Meet, Zoom, Teams, llamada en altavoz, reunión presencial.
- **Indicador visible y permanente mientras graba.** Nunca grabación silenciosa.

### Transcripción
- Proveedor elegido en Fase 0.
- Candidatos: **Deepgram Nova-3 Multilingual** (~$0.55/hr, el mejor en code-switching) y **AssemblyAI Universal-2** ($0.15/hr + $0.02 diarización).
- **Modo sin nube con Whisper on-device** (whisper.cpp o MLX en Apple Silicon) para reuniones confidenciales. Costo marginal cero.
- Diarización obligatoria. El usuario renombra hablantes una vez y el sistema los recuerda entre reuniones.

### Extracción
- **Modelo: `claude-sonnet-5`.**
- **Batch API** — el procesamiento no es sensible a latencia, baja el costo 50%.
- **Prompt caching** para el system prompt y los esquemas, que son estables.
- **Structured outputs** para que las obligaciones salgan con esquema validado, no texto libre que hay que parsear.
- Presupuesto: ~15,000 tokens de entrada y ~2,500 de salida por hora de reunión ≈ **$0.028 en batch**.

---

## MODELO DE DATOS

- **Reunión**: id, título, fecha/hora, duración, fuente, ruta de audio, estado de procesamiento
- **Participante**: nombre, rol, correo, hablante asignado — persistente entre reuniones
- **Segmento**: hablante, marca de tiempo inicio/fin, texto, confianza
- **Obligación**: quién, qué, cuándo, condición, firmeza, cubeta (mía/de otros/huérfana), evidencia (referencia a segmento), estado, confianza
- **Decisión**: qué se resolvió, evidencia
- **Tema abierto**: qué quedó sin resolver, evidencia
- **Recordatorio**: obligación origen, destino (Apple/Google/ics), estado de entrega

Almacenamiento **local por defecto**, cifrado en reposo. **El audio se borra automáticamente** pasado un plazo configurable (por defecto 30 días). Transcripción y obligaciones se conservan.

---

## CONSENTIMIENTO

La captura local evita el bot visible, pero **no elimina la obligación de avisar que se graba**.

- Antes de grabar, la app **exige confirmar** que se informó a los participantes.
- Generar texto de aviso en español, listo para pegar en la invitación de calendario.
- Registrar el consentimiento con sello de tiempo junto a la reunión.
- Permitir marcar participantes que no consintieron → excluir sus intervenciones.
- **Advertencia cuando haya participantes en jurisdicciones de consentimiento de todas las partes.** Once estados de EE.UU. lo exigen: California, Florida, Illinois, Massachusetts, Maryland, Montana, Nevada, New Hampshire, Pennsylvania, Washington y Connecticut. Basta uno para gobernar toda la llamada.

**Verificar el marco guatemalteco por separado.** No asumir que aplica la doctrina estadounidense.

---

## FASES Y CRITERIOS DE SALIDA

| Fase | Entregable | Criterio de salida |
|---|---|---|
| **0. Validación** | Informe comparativo de ASR sobre 5 reuniones reales | Un proveedor da diarización utilizable y obligaciones correctas con <10 min de corrección |
| **1. Núcleo** | Captura + transcripción + resumen + correo | Grabar una reunión real y recibir el correo útil sin intervención |
| **2. Obligaciones** | Extracción con las tres cubetas y niveles de firmeza | En 10 reuniones reales: ninguna obligación firme perdida, menos de 1 falso positivo por reunión |
| **3. Recordatorios** | Aprobación + entrega a Apple y Google | Un pendiente pasa de la reunión al teléfono sin fricción |
| **4. Confianza** | Trazabilidad, consentimiento, cifrado, retención | Auditoría propia: ninguna obligación sin evidencia en transcripción |
| **5. Segundo usuario** | Onboarding, cuenta, empaque | Alguien fuera del círculo cercano lo usa una semana sin soporte |

**Fase 0 es puerta, no trámite.** No escribir código de producto hasta cerrarla.

---

## BARRA DE CALIDAD

- **Cero obligaciones inventadas.** Un pendiente que nadie prometió destruye la confianza en todo el sistema. Es defecto crítico.
- **Cero obligaciones firmes perdidas.** Es el peor fallo posible: el usuario confía y se le cae algo.
- Procesamiento tras la reunión: **menos de 5 minutos** para una hora de audio.
- No colgarse ni perder audio en reuniones de 3 horas.
- Si falla el ASR en la nube, el audio se conserva y se reintenta. **Nunca se pierde una grabación.**
- El correo debe ser legible y accionable **en un teléfono, sin abrir la app**.

---

## EXTENSIBILIDAD FUTURA

Construir de modo que se puedan agregar verticales sobre la misma base, sin rehacer el núcleo:

- Plantillas de documento por profesión (actas legales, notas clínicas, reportes de obra)
- Agrupación de obligaciones por expediente, cliente o proyecto
- Vistas de seguimiento por persona: *"todo lo que Ena me debe"*
- Detección de compromisos incumplidos entre reuniones: *"esto lo prometiste hace tres semanas"*

**No construir nada de esto ahora.** Solo no cerrarse las puertas en el modelo de datos.

---

## QUÉ PREGUNTAR ANTES DE ASUMIR

1. ¿Swift/SwiftUI nativo, o Electron con helper nativo para audio?
2. ¿El correo sale de un servidor propio o desde la cuenta del usuario?
3. ¿Hay backend, o todo vive local y solo el LLM es remoto?
4. ¿Cuál es el plazo de retención de audio que quiere por defecto?
5. ¿Modo sin nube desde v1, o después?

---

## PRIMER PASO

Ejecutar **Fase 0**: tomar 5 grabaciones reales de reuniones en español guatemalteco, procesarlas por Deepgram y AssemblyAI, generar resumen y obligaciones con ambas, y entregar el informe comparativo.

Costo estimado: **menos de USD 5**. No escribir código de producto hasta que ese informe exista y su criterio de salida se cumpla.

---

## Relacionado

- [[agente-actas-reuniones]] — análisis de arquitecturas, costos y unidad económica
- [[apple-reminders-manual]] — cómo se escriben recordatorios en el sistema de JR
