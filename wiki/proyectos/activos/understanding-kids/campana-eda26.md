---
type: resource
date: 2026-07-21
last-touched: 2026-07-21
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

## Qué es (datos duros)
- **Expositoras:** Dra. Davinia García (médica / neurodesarrollo) + [[monica|Mónica Samayoa]] (integración sensorial). La dupla médica+sensorial es el gancho de autoridad; **la profundidad es el diferenciador #1**.
- **Formato:** 11 sesiones en vivo (10 + bonus nutrición/alergias), **virtual con acceso a grabaciones**.
- **Fechas:** lunes 6:00–8:00 pm, **5 oct → 14 dic 2026**. **Lanzamiento: primera semana de agosto** (la campaña venía ~2 semanas retrasada).
- **Precios:** **$295** ex-alumnos de Davinia o Mónica (sin fecha límite) · **$375** Early Bird (hasta 31 ago) · **$425** general (desde 1 sep).
- **Marca:** **IS lidera, UK apoya** (logo IS). **Contactos:** los de UK (WhatsApp +502 5926-9205, etc.).
- **Público:** SOLO profesionales — (1) los que ya reciben casos y no tienen método, (2) los que quieren especializar su práctica en un nicho rentable. (Sin familias.)
- **Mensaje madre:** "Los casos de alimentación no se adivinan: se evalúan, se planifican y se acompañan."
- **Subtítulo:** "Un método clínico para los casos de alimentación que nadie te enseñó a resolver."
- **Slogan:** 2 opciones a elegir por Davinia/Mónica → «Aprendé a resolver lo que otros solo refieren» · «Comer es más complejo de lo que parece. Especializate.»

## Identidad visual (aprobada) — "Pizarra & Rojo"
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
- **Tipografía (elegida JR 2026-07-21):** **Fraunces** (títulos, serif editorial) + **Hanken Grotesk** (cuerpo). Ambas Google Fonts/OFL. Archivos woff2+base64 en `Sistema/fonts_eda26/`. PENDIENTE: cablearlas en las plantillas de campaña (hoy el motor renderiza con Cocogoose+Montserrat).

## Mecanismo de campañas (reutilizable — importante)
Convención JR 2026-07-21: **cada campaña tiene una entrada "PARÁMETROS DE CAMPAÑA" en el Calendario de Artes de Notion** (`Visuals needed`=NO, campo `Campaña`=código). Su cuerpo es el **prompt maestro** (paleta, tipografía, THEME, 60-30-10, highlighter, marca/contactos, mapeo pieza→plantilla). El agente semanal detecta piezas por el campo `Campaña`, lee ese maestro y aplica **esa** identidad — nunca la línea diaria ni el sello ∞. Documentado en `GUIA_MAESTRA_ESTILO.md §7-bis`. AUT26 sigue gestionada por JR aparte (sin entrada maestra → no se genera).

## Cronograma (9 piezas cargadas en el Calendario, Status Planning)
anuncio 5-ago · dream team 8-ago · precios 13-ago · ¿para quién? 20-ago · early bird cierra 28-ago (historia) · temario 2-sep · diferenciales 9-sep · objeciones 18-sep (CTA WhatsApp) · últimos cupos 30-sep. Cada carrusel lleva su historia. Fechas ancladas a los hitos (lanzamiento/early-bird/inicio) — confirmado por JR que NO se han corrido.

## Pendientes (para retomar)
- [x] **Tipografía elegida:** Fraunces + Hanken Grotesk (archivos en `Sistema/fonts_eda26/`). Falta: cablearla en las plantillas de campaña del motor (hoy usan Cocogoose+Montserrat).
- [x] **Identidad Visual en Notion detallada para los web devs** (hex+roles+60-30-10, tipografía con pesos/tamaños/import, botón/CTA, highlighter en CSS, contraste WCAG). Hecho 2026-07-21.
- [ ] **Link del formulario** de inscripción (lo pasa JR; irá en la página de Davinia).
- [ ] **Slogan final** (elige Davinia/Mónica entre las 2 opciones).
- [ ] **Producir fase 1** (anuncio + dream team no dependen del formulario) — JR evaluaba arrancar antes del domingo por el retraso.
- [ ] Landing page → Davinia · Formularios → Mónica.

## Relacionado
[[understanding-kids]] · [[integracion-sensorial]] · [[monica]] · [[proyectos/activos/understanding-kids/sistema-artes-redes]] · [[diplomado-autismo-2026]]
