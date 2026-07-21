---
type: resource
date: 2026-07-21
last-touched: 2026-07-21
tags:
  - resource
  - tema/marketing
  - tema/branding
  - tema/automatizacion
  - proyecto/understanding-kids
status: operativo
---

# Sistema de artes para redes — UK / IS (operativo)

Sistema **automatizado** de generación de artes para Instagram/Facebook de [[understanding-kids|Understanding Kids]] (UK) y su submarca [[integracion-sensorial|Integración Sensorial]] (IS). Reemplaza el enfoque de Canva (ver §Historia). Operativo y probado de punta a punta el 2026-07-20.

> **Sustituye a** [[proyectos/activos/understanding-kids/sistema-templates-canva|sistema-templates-canva]] (enfoque Canva, descartado). Fundamento de marca: [[visual-identity]].

## Qué es (en 1 línea)

Plantillas **HTML/CSS renderizadas con Playwright** → PNG 1080×1350 (posts) y 1080×1920 (historias). Control total, gratis, reproducible. Se abandonó Canva porque su API no deja diseñar bien (no crea elementos nuevos, no cambia fondos, edición a ciegas por coordenadas).

## Dónde vive

**`~/Documents/Understanding Kids/Artes/`** (en **iCloud**, se sincroniza solo entre Macs):
- `Sistema/` — el motor: scripts `build_*.py`, guías, fuentes y logos embebidos (base64), `pexels_key.txt`, runbook de migración. Autocontenido; rutas relativas a `~/` (funciona con usuario `jotaerre` o `jr`).
- `Pendientes de Revision/` — artes recién generados, esperando el OK de JR.
- `Aprobadas/` — artes ya cerrados (subidos a Drive + Notion).

Guías dentro de `Sistema/` (fuentes de verdad):
- **`GUIA_MAESTRA_ESTILO.md`** — la línea visual completa: paletas, acento por marca, semántica de color, márgenes, catálogo de plantillas, reglas para crear variaciones sin salirse de la línea, y contenido viral (§7).
- **`GUIA_PROMOS_TALLERES.md`** — sub-sistema de promoción de talleres (portada-flyer, paleta propia por campaña).
- **`MIGRACION.md`** + `setup_mac_nueva.sh` — cómo mudar todo a otra Mac.

## Línea visual (resumen; detalle en GUIA_MAESTRA)

- **Tipografía (fija):** Cocogoose Pro Bold (títulos) + Montserrat (cuerpo).
- **Fondo:** crema `#FBFAF6`. **Texto:** gris `#33363B`.
- **Acento POR MARCA:** UK = amarillo `#EEB41E` · **IS = turquesa `#3FA8C0`** (del logo IS). Lo único que cambia entre marcas es logo + acento; contactos y todo lo demás, compartido.
- **Semántica de color:** rojo terracota suave = negativo (mito/presión) · verde = positivo · amarillo/turquesa = énfasis de marca · celeste = info.
- **Contactos (ambas marcas):** FB Understanding Kids · IG @kidsunderstanding · WA +502 5926-9205 · kidsunderstanding.com.

## Plantillas (build_*.py)

portada · contenido · contenido+imagen · frase/cita · infografía (tarjetas) · pasos · comparación 2 columnas · dato/dona (solo cifra real con fuente) · cierre (CTA+contacto) · promo (talleres) · story (4 tipos de historia). Regla: cada carrusel lleva 1-2 materiales visuales, VARIANDO el tipo (no siempre tarjetas). Fotos reales vía `buscar_foto.py` (Pexels, en inglés); nunca IA para niños.

## Automatización (2 agentes programados)

Corren en Claude Code (tareas programadas). **Requieren la app abierta** en una Mac encendida a la hora del cron → objetivo: mudarlos a la Mac Mini siempre-encendida (ver `MIGRACION.md`).

1. **`uk-artes-semanales`** (domingos 18:00): lee el **🗓️ Calendario de Artes** de Notion (briefs que escribe [[monica|Magoo]] en el campo Text) + las tendencias Aprobadas → genera carruseles + historias + captions → guarda en `Pendientes de Revision/`. **Excluye la campaña del Diplomado (AUT26)** — JR la maneja aparte. Reels/video = "atención manual".
2. **`uk-tendencias-virales`** (jueves 18:00): rastrea tendencias virales en **Instagram, Facebook, YouTube y TikTok** relacionadas con el contenido de la clínica y las sugiere en la base Notion **🔥 Tendencias** (Status "Sugerida"). Filtro de marca: clínica seria (descarta miedo, política, burla a niños).

## Flujo operativo

```
Magoo nutre Calendario de Artes ─┐        Agente tendencias (jue) → 🔥 Tendencias
                                 ▼               │ JR/Magoo aprueban
        Corrida semanal (dom 18:00) ◄─── lee Aprobadas ┘
                   │ genera artes + historias + caption
                   ▼
        iCloud: Artes/Pendientes de Revision/
                   │ JR revisa → "aprobadas"
                   ▼
   CIERRE (4 pasos): Drive → comentario Notion + Status Done
   → mover a Aprobadas/ → correo a Magoo (msamayoa@)
                   ▼
        Magoo publica desde Meta Business Suite (manual)
```

- **Drive destino:** `Administración/Artes/2026/<Página>/<Tipo>/` (Informativo, Frases, Testimonios, Promociones, Servicios, Recursos).
- **Publicar NO se automatiza** (Magoo programa desde Meta con los archivos de Drive; los stickers de historias los pone ella).

## Historia (por qué cambió)

- **2026-07-07:** primer intento con Canva MCP (nota [[proyectos/activos/understanding-kids/sistema-templates-canva|sistema-templates-canva]]). Se topó con que la API de Canva no crea elementos ni cambia fondos.
- **2026-07-16 →:** pivote a HTML/CSS + Playwright. 5 plantillas base aprobadas por JR, luego ampliadas (promos, historias, semántica de color, acento por marca).
- **2026-07-20:** ciclo completo probado (8 piezas generadas, aprobadas, subidas a Drive + Notion, correo a Magoo).
- **2026-07-21:** motor movido a iCloud para migración a Mac siempre-encendida; agente de tendencias creado (4 redes).

## Relacionado

[[understanding-kids]] · [[integracion-sensorial]] · [[monica]] · [[visual-identity]] · [[uk-catalogo]] · [[proyectos/activos/understanding-kids/sistema-templates-canva]] · [[diplomado-autismo-2026]]
