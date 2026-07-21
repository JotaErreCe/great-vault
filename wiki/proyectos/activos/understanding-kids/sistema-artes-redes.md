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

> **Espejo de respaldo del motor:** `raw/imports/uk-sistema-artes-mirror/` dentro de este vault (viaja por Syncthing). Existe para que la migración a la Mac Mini no dependa de que iCloud funcione. La copia CANÓNICA sigue siendo la de iCloud; tras cambiar una plantilla, re-sincronizar el espejo con el comando de su `_LEEME-ESPEJO.md`.

Guías dentro de `Sistema/` (fuentes de verdad):
- **`GUIA_MAESTRA_ESTILO.md`** — la línea visual completa: paletas, acento por marca, semántica de color, márgenes, catálogo de plantillas, reglas para crear variaciones sin salirse de la línea, y contenido viral (§7).
- **`GUIA_PROMOS_TALLERES.md`** — sub-sistema de promoción de talleres (portada-flyer, paleta propia por campaña).
- **`MIGRACION.md`** + `setup_mac_nueva.sh` — cómo mudar todo a otra Mac. **Runbook completo y actualizado: [[proyectos/activos/understanding-kids/migracion-sistema-artes]]** (vive en el vault a propósito, para que esté disponible aunque iCloud falle).

## Línea visual (resumen; detalle en GUIA_MAESTRA)

- **Tipografía (fija):** Cocogoose Pro Bold (títulos) + Montserrat (cuerpo).
- **Fondo:** crema `#FBFAF6`. **Texto:** gris `#33363B`.
- **Acento POR MARCA:** UK = amarillo `#EEB41E` · **IS = turquesa `#3FA8C0`** (del logo IS). Lo único que cambia entre marcas es logo + acento; contactos y todo lo demás, compartido. En código: `"marca": "UK"/"IS"` en cada dict de contenido.
- **Semántica de color:** rojo terracota suave = negativo (mito/presión) · verde = positivo · amarillo/turquesa = énfasis de marca · celeste = info.
- **Contactos (ambas marcas):** FB Understanding Kids · IG @kidsunderstanding · WA +502 5926-9205 · kidsunderstanding.com.

## Pilar estratégico: autoridad en autismo (2026-07-21)

Objetivo declarado de JR: que UK/IS sean **reconocidos como autoridad en autismo**. Decisiones y hallazgos:

- **La estrategia es el CRUCE, y la puerta de entrada es SENSORIAL.** Medición con Apify (2026-07-21, 50 reels): `#integracionsensorial` tiene **mediana 89,546 vistas y máximo 2.97M**, contra **16,470 / 44,541** de `#autismo` — 5.4× más en mediana, 67× en el techo. `#autismo` está saturado (~21 posts cada 13 min) y dominado por Brasil/portugués. **Conclusión: el contenido de autismo se publica bajo el ángulo sensorial**, que además es la ventaja real de la casa. Cruces: **autismo × integración sensorial ⭐**, × alimentación, × lenguaje, × emociones, × autonomía, × juego.
- **Lenguaje identidad-primero: "niño autista"**, nunca "niño con autismo" ([[decisiones/2026-07]]).
- **Símbolo: el infinito ∞ de neurodiversidad; el 🧩 está prohibido.** No es el glifo tipográfico sino un **activo de marca dibujado** (SVG): trazo fino redondeado + "bump" de lima en las puntas + arcoíris con la paleta UK/IS. Se usa como **sello discreto** (46px, centrado, al pie; en el cierre justo sobre la línea de contacto) activándolo con `"autismo": True` en cada slide — así el ícono queda libre para el emoji del tema.
- Tono obligatorio: el autismo no es enfermedad; nunca cura/alarmismo/burla.
- Distinto de la campaña **AUT26** del Diplomado, que JR maneja aparte.

## Datos de redes: Apify (conectado 2026-07-21)

MCP de Apify activo → datos de primera mano de IG/FB/TikTok/YT **con métricas de engagement**, sin arriesgar las cuentas propias de UK (el scraping corre en la infraestructura de Apify). Reemplaza la idea descartada de usar una cuenta propia para scrapear, que era frágil y se ganaba bans.

- Actor probado: `apify/instagram-hashtag-scraper` (~$0.0026 por resultado, ~8 s por corrida).
- **Gotcha:** al leer resultados pedir solo los campos útiles (`ownerUsername,likesCount,commentsCount,type,productType,timestamp,url,caption`) — devuelve 120+ campos y ahoga el contexto.
- **Método:** ordenar por engagement (likes + comentarios×3) y buscar **outliers** (5-10× el promedio del hashtag). El outlier ES la tendencia.
- **Presupuesto: máx ~$2 USD por corrida** semanal (~$5-8/mes).

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
- **2026-07-21:** motor movido a iCloud para migración a Mac siempre-encendida; agente de tendencias creado (4 redes); Apify conectado; pilar de autismo definido con su símbolo propio.

## Estado al 2026-07-21 (para retomar sin contexto)

**✅ Funcionando:**
- Motor completo con 11 plantillas + historias, probado de punta a punta.
- Ciclo completo validado el 2026-07-20: 8 piezas generadas → aprobadas por JR → Drive + Notion + correo a Magoo.
- Los 2 agentes creados y configurados. Apify conectado y probado.
- Todo el conocimiento en las guías de `Sistema/` + este vault.

**⏳ Pendiente (en orden):**
1. **Migrar a la Mac Mini** — bloqueado hasta el **1 de agosto de 2026** (JR de viaje). Runbook: [[proyectos/activos/understanding-kids/migracion-sistema-artes]]. Mientras tanto las tareas corren en la laptop y **se pierden las corridas cuando está apagada**; se pueden disparar a mano al volver.
2. **Primera corrida real del agente de tendencias** — nunca ha corrido completo con Apify. Conviene lanzarlo a mano y revisar qué sugiere antes de confiar en el automático.
3. Formato **Reel/video** sigue sin cubrir (se reporta como "atención manual").

**Decisiones abiertas:** ninguna. Las de lenguaje y símbolo de autismo quedaron cerradas en [[decisiones/2026-07]].

## Relacionado

[[understanding-kids]] · [[integracion-sensorial]] · [[monica]] · [[visual-identity]] · [[uk-catalogo]] · [[proyectos/activos/understanding-kids/migracion-sistema-artes]] · [[proyectos/activos/understanding-kids/sistema-templates-canva]] · [[diplomado-autismo-2026]]
