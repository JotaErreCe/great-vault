---
type: resource
date: 2026-07-21
last-touched: 2026-10-19
tags:
  - resource
  - tema/marketing
  - tema/campana
  - proyecto/understanding-kids
status: activa
---

# Campaña EDA26 — Especialización Clínica en Dificultades de la Alimentación 2026

Campaña de lanzamiento de una **especialización clínica para profesionales** sobre dificultades de la alimentación infantil, de [[understanding-kids|UK]] / [[integracion-sensorial|IS]]. Nota de continuidad (consolidada el 2026-07-21) — resume TODO lo decidido para no perderlo en compresión de contexto.

> **Guía de campaña (Notion, production-ready para Davinia):** https://app.notion.com/p/3b1780c047628112b1b5c41b42f03802
> **Entrada de PARÁMETROS (prompt maestro, en el Calendario de Artes):** https://app.notion.com/p/3b2780c047628167a618dd1314f0f26b
> **Mockups / identidad (Drive):** `Administración/Artes/2026/Campañas/Especialización Alimentación 2026 - Mockups/` (ref aprobada: `paleta_final_pizarra_rojo.png`).
> **Documento maestro / temario (Drive):** doc "Especialización Clínica en Dificultades de la Alimentación" (11 sesiones).

## Estado al 2026-10-19 (corrige lo de abajo)

Pasado al Vault desde las memorias de Claude (F4 de [[vault-cerebro]]). Donde esta sección choca con las de abajo (escritas en julio-agosto), manda esta; y sobre todo manda la entrada **PARÁMETROS** de Notion.

- **Paleta v2 «Azul & Ámbar» (JR, 10-ago-2026), reemplaza a «Pizarra & Rojo»:** fondo `#F8F8F5`, texto `#22303B`, primario azul `#2E7FA6`, acento/CTA ámbar `#F0B024`, highlighter ámbar 38 %. JR rechazó el rojo («no me encantó») y el conjunto apagado («se ve muy The Office»). La entrada PARÁMETROS de Notion ya está en la v2.
- **Tipografía cableada** (10-ago-2026): Fraunces + Hanken Grotesk ya se usan en el motor vía `theme["font_title"]` / `theme["font_body"]` (el pendiente de abajo está cerrado).
- **Logos:** toda pieza lleva los **dos** logos (IS y Dra. Davinia García), pero **solo en el cierre** (`lockup_logos()`); portada y flyer de historia van sin logo, con la línea de texto «Con la Dra. Davinia García y Mónica Samayoa». Badge en contorno; el ámbar relleno queda solo para el CTA.
- **Slogan:** «Aprende a resolver lo que hoy refieres» (JR bajó lo brusco de «…lo que otros solo refieren»).
- **Inscripciones por WhatsApp (+502 5926-9205) desde el 15-sep-2026, hasta nuevo aviso:** la página de Davinia dejó de funcionar (le congelaron el dominio). Davinia ofreció enlaces de Stripe; **JR decidió WhatsApp**. Ninguna pieza manda a una web ni promete sticker de enlace; en el arte no se menciona el dominio ni el motivo («por causas ajenas a nosotros»). Pieza que lo anuncia: `2026-09-16 - IS EDA26 Aviso inscripciones por WhatsApp`; cuando la página vuelva, esa historia se retira **(sin verificar si ya volvió)**.
- **Deuda:** las historias de texto de `2026-08-10 … post ancla` y `2026-08-20 … para quien es` salieron sin el azul (bug de `paleta_story`, ver [[artes-decisiones-y-lecciones]]); JR decide si se rehacen.
- Reglas de producción de campaña: ~4 historias por pieza (flyer + 3 de texto), sin repetir layout; nunca dos slides con el mismo formato seguidos.

## Qué es (datos duros)
- **Expositoras:** Dra. Davinia García (médica / neurodesarrollo) + [[monica|Mónica Samayoa]] (integración sensorial). La dupla médica+sensorial es el gancho de autoridad; **la profundidad es el diferenciador #1**.
- **Formato:** 11 sesiones en vivo (10 + bonus nutrición/alergias), **virtual con acceso a grabaciones**.
- **Fechas:** lunes 6:00–8:00 pm, **5 oct → 14 dic 2026**. **Lanzamiento: primera semana de agosto** (la campaña venía ~2 semanas retrasada).
- **Precios:** **$295** ex-alumnos de Davinia o Mónica (sin fecha límite) · **$375** Early Bird (hasta 31 ago) · **$425** general (desde 1 sep).
- **Marca:** **IS lidera, UK apoya** (logo IS). **Contactos:** los de UK (WhatsApp +502 5926-9205, etc.).
- **Público:** SOLO profesionales — (1) los que ya reciben casos y no tienen método, (2) los que quieren especializar su práctica en un nicho rentable. (Sin familias.)
- **Mensaje madre:** "Los casos de alimentación no se adivinan: se evalúan, se planifican y se acompañan."
- **Subtítulo:** "Un método clínico para los casos de alimentación que nadie te enseñó a resolver."
- **Slogan:** 2 opciones a elegir por Davinia/Mónica → «Aprende a resolver lo que otros solo refieren» · «Comer es más complejo de lo que parece. Especialízate.»
- **Trato/idioma:** TODO en **tú neutro** (panregional), nunca voseo. Decisión JR 2026-08-06. Aplica a copy, artes y a mis chats con JR → ver memoria [[feedback_style]].

## Identidad visual v1 — "Pizarra & Rojo" (REEMPLAZADA el 10-ago-2026 por la v2, ver arriba)
Se iteró mucho; se descartó terracota y toda paleta que se pareciera a UK (para no chocar con Davinia). Método coherente: base sofisticada + 1 acento, saturación pareja (refs workovereasy / Figma). Distinta a propósito de la línea diaria de UK/IS.

| Rol | Hex |
|---|---|
| Fondo — claro cálido | `#F6F4F1` |
| Texto — gris pizarra | `#263039` |
| Primario — azul pizarra | `#35617A` |
| Acento / CTA — rojo | `#D44B45` |
| Apoyo — rosa tenue | `#F0DAD3` |

- **Proporción 60-30-10** (60 fondo, 30 pizarra, 10 rojo). Rojo nunca como fondo grande.
- **Resaltado:** highlighter translúcido rojo **~28%** (`rgba(212,75,69,0.28)`) sobre palabras clave — NO barra sólida.
- **Codificado en el motor:** `THEME_EDA26` en `build_promo.py` (con clave `cta`=rojo y `highlight`).
- **Tipografía (elegida JR 2026-07-21):** **Fraunces** (títulos, serif editorial) + **Hanken Grotesk** (cuerpo). Ambas Google Fonts/OFL. Archivos woff2+base64 en `Sistema/fonts_eda26/` (ahora con los 5 pesos: Fraunces 600/700 + Hanken 400/600/700). PENDIENTE: cablearlas en las plantillas de campaña (hoy el motor renderiza con Cocogoose+Montserrat).
- **Paquete de fuentes para web devs (self-host):** 5 woff2 + `fuentes.css` (@font-face + variables de paleta) + licencias OFL, subido a Drive `Campañas/Especialización Alimentación 2026/Tipografías/` → https://drive.google.com/drive/folders/1yIzi-YP9tclh2C7Cw6nQK7DAoepgLIlA . Link ya puesto en Notion §Identidad Visual (recomendado self-host; alternativa = @import de Google Fonts). ⚠️ Carpeta PRIVADA: falta darle acceso a los devs de Davinia.

> **Nota de estructura (2026-08-06):** la sección **Identidad Visual** del Notion se reorganizó para dos lectores: arriba, lenguaje simple (Cómo se ve y se siente · Los colores con "para qué se usa" · Cómo combinarlos · Las tipografías); abajo, un toggle plegable **"🛠️ Para quien programe la web"** con todo el tecnicismo (hex, 60-30-10, CSS, contraste WCAG, pesos, self-host/@import). El submenú "Inversión" se eliminó y los 3 precios pasaron al bloque Datos del encabezado.

## Notion EXHAUSTIVO (2026-07-21)
La guía de campaña en Notion es la fuente detallada y quedó completa para producción y para los web devs de Davinia. Además de estrategia/identidad, incluye: **temario completo de las 11 sesiones**, **guion pieza por pieza** (hook + estructura de slides + CTA por cada uno de los 9 artes), **voz y copy** (do/don't), **objeciones con respuesta (FAQ)**, **especificaciones de arte** (formatos, zonas seguras, nomenclatura EDA26, dónde se guardan), **hashtags** y **checklist de lanzamiento**. No reproducir todo acá: el Notion manda.

## Mecanismo de campañas (reutilizable — importante)
Convención JR 2026-07-21: **cada campaña tiene una entrada "PARÁMETROS DE CAMPAÑA" en el Calendario de Artes de Notion** (`Visuals needed`=NO, campo `Campaña`=código). Su cuerpo es el **prompt maestro** (paleta, tipografía, THEME, 60-30-10, highlighter, marca/contactos, mapeo pieza→plantilla). El agente semanal detecta piezas por el campo `Campaña`, lee ese maestro y aplica **esa** identidad — nunca la línea diaria ni el sello ∞. Documentado en `GUIA_MAESTRA_ESTILO.md §7-bis`. AUT26 sigue gestionada por JR aparte (sin entrada maestra → no se genera).

## Cronograma (rediseñado 2026-08-06 — 6 piezas de feed + reels + historias)
**Feed (6):** teaser 5-ago (imagen+historias, sin datos) · **post ancla** "expositoras, precios e info" 8-ago (carrusel) · ¿para quién? 20-ago · objeciones 1-sep (CTA WhatsApp) · temario 9-sep · últimos cupos 30-sep.
**Reels (manual, fuera del sistema):** Davinia ~15-ago (mirada médica) · Mónica ~25-ago (mirada sensorial).
**Historias:** capa continua por fecha (encuesta "¿recibís casos?", reposteo de reels, cuenta regresiva Early Bird 27–31 ago, recordatorios con link, Q&A 16–27 sep, cuenta regresiva al inicio) — tabla en Notion §Plan de Contenidos.
**Contenido paralelo/orgánico:** píldoras de valor (1 dato clínico/semana), testimonios/prueba social, detrás de cámaras, caso corto anonimizado, Q&A en vivo.

### Decisiones JR 2026-08-06 (rediseño)
- Se **eliminó "Diferenciales"** (casi no hay cursos comparables → comparación forzada).
- **"Dream Team" es término SOLO interno** — nunca en pieza pública (usar "las expositoras" / "quiénes te van a enseñar"); no hacer pieza dedicada tipo "conocé al equipo": la doble autoridad se reparte en el post ancla y en los reels.
- **Pieza 1 = teaser** sin datos (expectativa); **pieza 2 = post ancla** que unifica expositoras + precios + info general.
- Más peso a **historias** (antes había 1 sola) y a **reels personales** de cada expositora.
- **Nomenclatura de artes:** `EDA26_<CÓDIGO>_C##` (carrusel) / `_ST` (historia). Códigos: TSR (teaser), ANCLA (post ancla), PARAQUIEN, OBJ (objeciones), TEM (temario), CIERRE (últimos cupos).
- **Especificaciones (Notion):** se limpió la jerga del motor (build_promo.py / THEME_EDA26 / sello ∞) a lenguaje simple porque el doc lo ve Davinia; los nombres técnicos exactos viven en el vault y en la entrada de PARÁMETROS del Calendario.

**Guion por pieza (Notion):** ✅ reescrito 2026-08-06 a las 6 piezas (teaser + post ancla nuevos, objeciones antes de temario, sin Diferenciales ni "Dream team") + guion corto de los 2 reels.

**Calendario de Artes:** ✅ re-sincronizado 2026-08-06 al plan de 6 (sin borrar entradas: "Anuncio"→Teaser, "Dream team"→Post ancla, "Precios"/"Diferenciales"→Reels Davinia/Mónica marcados `Visuals needed=NO`). Entradas ahora: Teaser 5-ago · Post ancla 8-ago · Reel Davinia 15-ago (manual) · ¿Para quién? 20-ago · Reel Mónica 25-ago (manual) · Early Bird historia 28-ago · Objeciones 1-sep · Temario 9-sep · Últimos cupos 30-sep, + entrada PARÁMETROS. La entrada PARÁMETROS se actualizó (tipografía Fraunces/Hanken + mapeo de piezas nuevo); sigue marcando que el motor aún renderiza con Cocogoose/Montserrat hasta cablear las fuentes.

## Pendientes (para retomar)
- [x] **Tipografía elegida:** Fraunces + Hanken Grotesk (archivos en `Sistema/fonts_eda26/`). Falta: cablearla en las plantillas de campaña del motor (hoy usan Cocogoose+Montserrat).
- [x] **Identidad Visual en Notion detallada para los web devs** (hex+roles+60-30-10, tipografía con pesos/tamaños/import, botón/CTA, highlighter en CSS, contraste WCAG). Hecho 2026-07-21.
- [ ] **Compartir la carpeta Tipografías de Drive** con los devs de Davinia (hoy privada) — link en Notion §Identidad Visual.
- [x] **Diploma:** confirmado por JR que SÍ se entrega → agregado al FAQ del Notion.
- [x] **Formas de pago (confirmado por Magoo 2026-08-07):** SÍ hay pago en **cuotas**; se acepta **tarjeta y PayPal**, **NO transferencia**; **factura: SÍ**. Agregado al FAQ del Notion y cerrado en el checklist.
- [ ] **Link del formulario** de inscripción (lo pasa JR; irá en la página de Davinia).
- [ ] **Slogan final** (elige Davinia/Mónica entre las 2 opciones).
- [ ] ⭐ **Revisar cronograma por fecha** y reacomodar artes si hace falta (evaluar al revisar la sección "Plan de Contenidos" del Notion, título por título).
- [ ] **Producir fase 1** (anuncio + dream team no dependen del formulario) — JR evaluaba arrancar antes del domingo por el retraso.
- [ ] Landing page → Davinia · Formularios → Mónica.

## Relacionado
[[understanding-kids]] · [[integracion-sensorial]] · [[monica]] · [[proyectos/activos/understanding-kids/sistema-artes-redes]] · [[diplomado-autismo-2026]] · [[artes-decisiones-y-lecciones]]
