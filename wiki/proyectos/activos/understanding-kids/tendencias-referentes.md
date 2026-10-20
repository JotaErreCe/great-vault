---
type: resource
date: 2026-10-19
last-touched: 2026-10-19
tags:
  - resource
  - proyecto/understanding-kids
  - tema/marketing
  - tema/automatizacion
fuente: "~/Documents/Understanding Kids/Artes/Sistema/tendencias_referentes.md"
---

> **Fuente de verdad desde 2026-10-19.** Las tareas y los agentes la leen desde aquí (fase F6 de [[vault-cerebro]]). `Sistema/tendencias_referentes.md` quedó como aviso de mudanza: los cambios se hacen solo en esta página.
>
> Copia fiel de la lista de cuentas referentes que revisa el agente `uk-tendencias-virales` para detectar formatos que se replican.

> El estado entre corridas (posts vistos, ángulos, convergencia) vive afuera, en `Sistema/tendencias/` (`ledger.py`, `posts.csv`, `angles.jsonl`, `runlog.md`); ver [[mapa-de-archivos]].

---

# Cuentas referentes para el detector de tendencias

Cuentas que marcan tendencia en el nicho (autismo, integración sensorial, desarrollo, alimentación, lenguaje, crianza). El agente las revisa cada corrida: **cuando varias hacen el MISMO formato en pocos días, esa es la señal temprana para subirse.**

> Edita esta lista libremente. Sembrada el 2026-07-21 con las cuentas de mayor engagement del primer sondeo con Apify. **Revisada con datos el 2026-08-03** — ver `tendencias/ledger.py stats`.

## Cómo se dividen (revisión 2026-08-03)

Las cuentas hacen **dos trabajos distintos** y conviene no mezclarlos:

- **Fuente de ÁNGULOS** — publican casi solo reels, pero sus captions son artículos completos. De acá salen los temas y los encuadres.
- **Fuente de FORMATOS** — publican carruseles. Son las únicas cuya estructura de slides se puede estudiar y copiar.

**No descartar reels al momento de raspar.** El mejor hallazgo del 2026-08-03 salió entero de captions de reels. El filtro "¿esto sobrevive sin el video?" se aplica al sugerir, no al raspar.

## Instagram — activas

| Handle | Rol | % estáticos | Mediana |
|---|---|---|---|
| paupautista | ángulos | 0% | 2,086 lk |
| mimamaterapeuta | ángulos | 0% | 262 lk |
| integrandosuenos | ángulos | 6% | 90 lk |
| idalbadugarte | mixta | 17% | 71 lk |
| mamiterapeuta.cl | mixta | 33% | 296 lk |
| alimento.red | mixta | 33% | 10 lk |
| centrocrecemx | **formatos** | 94% | 30 lk |
| ft.ferchm | **formatos** | 72% | likes ocultos → usar comentarios (mediana 2) |

## Instagram — INACTIVAS (⚠️ revisar, JR)

Detectadas por el ledger el 2026-08-03. **No estaban marcadas y se usaron como fuente de tendencias.**

- **autismoguia** — último post **2024-07-15** (749 días). Cuenta muerta hace dos años.
- **sofiavera_rubio** — último post **2025-03-28** (493 días).

> Consecuencia: dos entradas de la base 🔥 Tendencias del 2026-07-21 citan posts de **2022** de estas cuentas como si fueran virales del momento. Decidir si se sacan de la lista o se reemplazan.

## Candidatas (pendiente de aprobación de JR)

Descubiertas el 2026-08-03 con `keywordSearch` sobre frases de ángulo. **Todas publican carruseles o estáticos**, que es justo el hueco de la lista actual. No las agregué solo: revísalas y sube las que te sirvan.

- to.ninoskaquezada — carrusel, 832 lk
- tu.terapeuta.infantil — estático, 459 lk
- diversifikate.cl — carrusel, 204 lk / **157 comentarios** (usa gancho de comentario)
- centrocumbres.cl — carrusel, 208 lk
- to.sensorial — estático
- to.sensorykids — carrusel
- terapeutaocupacional_profevero — carrusel
- to.teresanarvaez — estático
- asociacionsurestea — estático
- judithamon — ratio de comentarios >1 (gancho de comentario en su forma más agresiva)

## Facebook (URLs de página)

*(Pendiente.)* Facebook no tiene búsqueda por hashtag, así que aquí van **URLs de páginas** concretas (ej. `https://www.facebook.com/NombreDePagina`). Sembrar cuando JR pase su lista de referentes/competidores en FB. Mientras esté vacío, el agente intenta encontrar la página FB de los referentes de arriba vía WebSearch, pero no inventa URLs.

## Competidores locales GT (prioridad — pendiente de JR)

*(Vacío.)* Los referentes locales son los más valiosos para detectar qué está funcionando en el mercado guatemalteco específicamente. Agregar aquí handles de IG y URLs de FB.

## Relacionado

- [[sistema-artes-redes]] — flujo de tendencias
- [[guia-maestra-estilo]] — §7 contenido viral
- [[understanding-kids]]
- [[vault-cerebro]]
