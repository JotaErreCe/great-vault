---
type: resource
date: 2026-10-19
tags:
  - resource
  - tema/marketing
  - tema/branding
  - proyecto/understanding-kids
---

# Artes UK/IS: decisiones de JR y lecciones aprendidas

Lo que Claude aprendió trabajando el [[sistema-artes-redes|sistema de artes]] y que **no está** en las guías: decisiones de JR con su porqué, errores que no se repiten y trampas técnicas. Viene de las memorias de Claude (jul-oct 2026), pasadas al Vault en la fase F4 de [[vault-cerebro]]. Las reglas visuales completas siguen en [[guia-maestra-estilo]] y [[guia-promos-talleres]]; las plantillas en [[plantillas-artes]]; el flujo en [[sistema-artes-redes]].

> Fechas en cada regla. Si algo de aquí contradice a [[sistema-artes-redes]], manda esa página (es el estado de octubre).

## Copy (complementa la guía §3)

- **Tono humano, no de IA** (JR, 16-jul-2026): «explorar» → «conocer»; evitar «descubre», «potencia», «impulsa», «eleva» salvo que JR los use primero. Ante la duda, la palabra más simple.
- **Caption** (5-ago-2026): máximo 5 hashtags (techo, no meta); nunca punto pegado antes de emoji (`?` y `!` sí); tuteo. Lo revisa `verificar_caption.py`.
- Los dos teléfonos escritos a mano en el copy de cada caption nuevo: la plantilla no lo cubre.

## Revisión de JR del 17-ago-2026 (16 piezas)

1. **Historias sin logo de la casa** (el logo ya está en la foto de perfil). `LOGO_EN_HISTORIAS = False` en `build_story.py`. Excepción: historias de campaña con `co_logo`.
2. **Rejilla 2×2 de `build_infografia` solo con 4 o 6 elementos.** Con 3 o 5 quedaba un hueco (JR lo marcó cuatro veces). La plantilla elige sola: 4/6 → `grid`; 3/5 → `rows`. Layout `centro`: 2×2 de fotos con el titular al medio.
3. **Las listas sueltas no comunican.** JR rechazó «Estrategias: En casa / En el juego / En la comida»: «necesitamos transmitir un mensaje que no se está transmitiendo». Las etiquetas dicen algo («En casa: la ropa, el baño, la hora de dormir»); si un concepto necesita explicación, va su propio slide.
4. **Fotos permanentes** en `Artes/Fotos/`; nunca referenciar `/private/tmp/...` (las corridas de julio y agosto no se pudieron re-renderizar).
5. **No repetir foto** entre piezas ni entre el post y su historia; la historia no cuenta todo el post («si la historia ya dice todo, ¿para qué ir a ver el post?»).
6. **Talleres pre-grabados = PRODUCTO**: `build_promo.py` con theme propio (`THEME_TALLERES`), una pieza por taller («que tengan más fuerza»).
7. **Publicidad de servicios: complementaria** de lo que ya está en Drive, no repetir portada→señales→cómo trabajamos→CTA. Ángulo aprobado: comparativa «cómo está hoy» vs «a dónde queremos llegar». Revisar `Artes/2026/Publicidad/` antes.
8. **Imágenes de producto de terceros:** si UK no vende el producto y es publicidad gratuita, JR aceptó imágenes del listado de Amazon; las baja JR (la navegación externa está bloqueada para Claude). Sin imágenes reales del producto, la pieza no se hace (se canceló el esterilizador UV-C).

## Correcciones del 21-sep-2026 (preferencias de JR)

- Carruseles de **máximo 10 imágenes**: se consolida antes que pasarse.
- El carrusel se lee **como una sola historia**, con frases puente; si el título usa un término («desborde»), el carrusel lo conecta con lo que explica.
- **Nada apretado:** aire entre bloques; en tablas, preguntas centradas.
- El cierre puede ser **una frase protagonista + el logo**, sin «¡Ponte en Contacto!», pero siempre con la barra de los dos teléfonos.
- **Sin comilla decorativa** en frases que no son citas.
- Lección de la auditoría del 21-sep: una corrección en local no está cerrada hasta que esté en Drive y Magoo lo sepa (EDA26 Objeciones y Temario se corrigieron el 10-sep en local, pero Drive siguió con la versión del 7-sep). Al cerrar, verificar el `modifiedTime` en Drive. *(Superado: desde el 16-oct el cierre lo hace `uk-cierre`, y el 19-oct-2026 JR decidió que a Magoo no se le escribe por correcciones: ella pide cambios por Notion. Ver [[agentes/claude/subagentes]].)*

## Campañas: la fuente es Notion

- La identidad visual de una campaña se lee **solo** de su entrada «PARÁMETROS DE CAMPAÑA» en el Calendario de Artes (`Visuals needed` = NO, campo `Campaña` con el código). Si el `THEME_*` de `build_promo.py` y Notion no coinciden, **manda Notion** y se corrige el código. La guía local solo apunta a Notion.
- **Por qué (26-ago-2026):** `GUIA_MAESTRA_ESTILO.md` todavía describía la paleta v1 rechazada de EDA26; un agente que la leyera habría pintado la campaña del color equivocado.
- **Bug del 28-ago-2026:** `paleta_story()` no pasaba `theme["title"]`; en EDA26 el azul no existía en las historias de texto (`bloque`, `lista`). Ningún verificador lo cazaba (`verificar_marca.py` omite campañas a propósito); lo vio JR: «No uso el color de la campaña». Arreglado en la plantilla. **Deuda:** las historias de texto ya publicadas de `2026-08-10 … post ancla` y `2026-08-20 … para quien es` salieron sin azul; JR decide si se rehacen **(sin verificar si ya decidió)**.
- **Lección:** al verificar una corrección, mirar si la pieza está **bien**, no solo si la corrección rompió algo.
- Estado de EDA26 (paleta v2, logos, slogan, WhatsApp): [[campana-eda26]].

## Logos sobre foto y co-formadores (10-ago-2026)

- **Ningún logo sobre la foto** en portada de feed ni flyer de historia (JR: «quita el logo de las portadas, no me gusta cómo queda»): `logos=False`; la autoría va como línea de texto `content["firma"]`.
- **Donde aparece el logo de la casa, aparece también el del co-formador. Nunca uno solo.** Vive en el theme (`co_logo`), y el par va **solo en el cierre** con `lockup_logos()`.
- Troquel (`hacer_sticker.py`): decisión final de formas geométricas (IS/UK círculo, Davinia rectángulo redondeado, blanco con opacidad 0.88). Rechazados por JR, no repetir: tarjeta blanca («se ve pegada»), halo con `drop-shadow` («parece que están brillando»), contorno colapsado en rectángulo. El código sigue disponible para otras campañas.
- **Jerarquía de color en promos:** el badge va en contorno (`badge_style = "outline"`) y el relleno del acento queda exclusivo del CTA. `texto_sobre(hex)` decide por luminancia si el texto de badge/CTA va oscuro o blanco.

## Marca y colores

- Los colores de marca **no** están en Canva, ni en el código viejo, ni en Drive (circular), ni en IG, ni en los logos. **La fuente es JR** (verificado 3-ago-2026). UK `#FBFAF6` + `#EEB41E`; IS `#F4F9FA` + `#3FA8C0`.
- Las 4 piezas de IS de julio publicadas salieron con fondo de UK (antes del 3-ago el crema estaba fijo para las dos marcas); pendiente decidir si se regeneran **(sin verificar)**.
- Cuentas de IG: UK **@kidsunderstanding**, IS **@integracionsensorial_byuk** (IS sí tiene cuenta propia; en el arte se imprimen los contactos de UK).
- **Por qué no Canva:** la API no crea elementos ni cambia fondos (julio 2026); por eso HTML/CSS + Playwright.
- Nanobanana quedó configurado pero sin cuota (los proyectos de JR no tienen facturación). Pollinations dejó de ser gratis (402) y JR decidió el 1-oct-2026 no cargarle saldo.

## Reparto de tareas con Magoo (28-ago-2026)

JR: «Tú tienes que subir los artes a Drive. Ella debe subirlos ÚNICAMENTE a redes.» Magoo no toca Drive: toma los archivos y publica en IG y FB con sus stickers. Nunca pedirle en un correo que suba algo a Drive. Al publicar, Magoo renombra la carpeta de Drive a «subido».

## Notion (Calendario de Artes)

- El campo **`Fotos` no se llena por API** (probado 23-ago-2026 con tres formatos: «File not found» / «User cannot access file id»). Lo que funciona: subir con `file_uploads` e insertar los PNG en el **cuerpo** de la página bajo «## 🎨 Arte generado — <carpeta>». Si Cloudflare responde 403 con HTML, re-codificar el PNG y reintentar.
- **Vistas:** la API sí maneja vistas (`/v1/views`, Notion-Version 2026-03-11; un board exige `group_by.sort = {"type":"manual"}`). El 16-oct-2026 se crearon 6 vistas (Tablero, Calendario UK, Calendario IS, Mi revisión, Para Magoo, Todas) y se borraron las viejas; respaldos en `~/Claude/notion-backups/`.
- Un PATCH de opciones de status **reemplaza** la lista: mandar siempre todas con su id. Los **grupos** de status no se cambian por API.
- El filtro de status devolvió filas equivocadas tras la migración: los scripts re-chequean el estado de cada fila del lado del cliente.
- Comentarios por API dieron 403 (16-oct-2026); se anota en el cuerpo de la página.
- «Visuals needed» es imprescindible (JR lo borró por error y lo restauró). `Fotos` es donde Magoo sube referencias.

## Permisos de las corridas desatendidas (13-ago-2026)

Un prompt de permisos deja colgada la corrida del domingo y esa semana no sale nada. El allowlist de `~/Claude/.claude/settings.local.json` estaba lleno de comandos literales de una sola vez; se reemplazó por reglas **por patrón** acotadas a artes. **Regla: nunca agregar comandos literales al allowlist.** Hoy la configuración de usuario corre en `bypassPermissions` (verificado 19-oct-2026); cambiar eso es decisión de JR.

## Relacionado

- [[sistema-artes-redes]] · [[guia-maestra-estilo]] · [[guia-promos-talleres]] · [[plantillas-artes]]
- [[campana-eda26]] · [[understanding-kids]] · [[agentes/claude/AGENT|Claude]] · [[agentes/claude/subagentes]]
