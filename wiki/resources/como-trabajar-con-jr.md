---
type: reference
date: 2026-10-19
tags: [reference, agentes, preferencias, jr]
---

# Cómo trabajar con JR

Preferencias de trabajo de [[jr]] que valen para cualquier agente (Claude, Geoffrey y los que vengan). Complementa las reglas comunes de `USER.md` y [[_AI_BOOTSTRAP]] (conciso por TDAH, no inventar, no comprometerlo con terceros ni gastar dinero sin permiso), que no se repiten aquí. Viene de lo que JR le fue diciendo a Claude entre julio y octubre de 2026.

## Idioma y tono

- **Siempre tú neutro, nunca voseo** (dicho explícitamente el 2026-08-06 y repetido el 17-ago): en el chat con él, en correos escritos en su nombre y en todo contenido (copy, artes, Notion, campañas). Nada de «vos, tenés, podés, avisame, especializate»; sí «tú, tienes, puedes, avísame, especialízate». A JR le molesta el voseo.
- **Nunca rayas ni guiones largos (—) en sus textos** (24-ago-2026: «Quita los — por favor. No los uses en mis textos nunca.»). Usar comas, paréntesis, dos puntos o punto y seguido.
- **Tono humano, no de IA.** Palabras simples y cotidianas.
- Separar lo técnico de lo entendible: lo que va a lectores no técnicos no lleva jerga.
- Por Telegram, Claude habla con la voz del Tío Iroh ([[agentes/claude/persona-tio-iroh]]); los datos siguen exactos.

## Proceso

- **Preguntar antes, con opciones concretas** (opción múltiple cuando aplique, la recomendada primero) en decisiones estratégicas: cliente objetivo, precios, mensaje. Todo lo ambiguo se pregunta; nunca suponer.
- Las preguntas van **en el chat**, nunca dentro de los entregables.
- Revisar «título por título» cuando lo pida.
- Respaldar las decisiones con una investigación (web o datos reales) y citar fuentes (regla del 16-oct-2026).
- **Production-ready:** lo que va a terceros (p. ej. Notion para Davinia) sale sin comentarios de IA, sin placeholders visibles y con datos reales.
- **Nunca inventar** precios, fechas, cupos, estadísticas, nombres ni parentescos. Antes de un dato personal, buscar en el Vault ([[great-vault]]); si no está, decir «no sé» y preguntar. Error del 26-ago-2026: se firmó un correo como «José Rodrigo» adivinando por las iniciales. JR: «Tienes acceso al Vault, no? Deberías ya de saber cómo accesar a la información o preguntar antes.»
- A Mónica se la llama **siempre «Magoo»**.
- Correos pedidos en una conversación: se muestran y se espera su visto bueno antes de enviar ([[agentes/claude/correo]]).

## Un tema a la vez

JR (19-oct-2026): «No me des un listado de cosas por hacer de diferentes temas. Yo soy un humano, no una AI y necesito hacer un tema a la vez.»

- Un mensaje = un tema. Con el detalle suficiente para decidir (qué hay hoy, qué se propone y por qué) y una o dos preguntas como máximo.
- Lo demás espera en cola y no se menciona hasta cerrar el tema en curso.
- Aplica también a los reportes de agentes: solo lo del tema en curso.

## Aprender siempre y guardarlo en el Vault

JR, 19-oct-2026: **«me interesa que aprendas siempre y que lo vayas guardando en el Vault».** Todo aprendizaje durable (preferencias, reglas, cómo funciona algo, errores que no se repiten) se escribe en el Vault, en la página que corresponde, con su línea en el log. El Vault es la fuente de verdad; la memoria de cada agente guarda solo la regla corta y el enlace ([[vault-cerebro]], [[escribir-memoria]]).

**Por qué:** JR revisa con criterio de producto, le importan el detalle y el tono humano, y quiere un solo cerebro que puedan leer él (en Obsidian), Claude y Geoffrey.

## Relacionado

- [[jr]] · [[_AI_BOOTSTRAP]] · [[great-vault]] · [[escribir-memoria]]
- [[agentes/claude/AGENT|Claude]] · [[agentes/geoffrey/AGENT|Geoffrey]] · [[protocolo-operativo-agentes]]

- **Para revisar desde el celular, PDF o imagen** (JR, 20-oct-2026): nada de DOCX ni archivos que haya que descargar. Si hay cambios sobre una versión anterior, resaltarlos. En la Mac: `textutil -convert html` y luego Chrome headless `--print-to-pdf`.

- **Informes = one pager o lo más conciso posible** (JR, 20-oct-2026; aclaró: no tiene que ser una sola página, pero sí tan directo como un one pager): «Que sea más conciso. Un one pager porfa. Detallado, pero conciso y directo.» Todo análisis o informe que se le mande va en una página: tablas chicas y viñetas, sin prosa larga; el detalle completo queda aparte por si lo pide.

## Formato de informes (JR, 22-oct-2026)
- Solo **Problemas / Datos / Propuesta**, en viñetas cortas. Nada de one-pagers de dos páginas («mucha verborrea»).
- Recordatorios puntuales: launchd de una sola vez (StartCalendarInterval con mes/día) falló 2 veces (22-oct 10:00 y 23-oct 05:30, lo salvó el respaldo). Todo recordatorio puntual va con un respaldo `sleep` en segundo plano, o solo con `sleep`.
- Acceso completo al disco (23-oct-2026): JR lo dio a `claude`, la versión 2.1.304, Claude y node. Cada versión nueva de Claude Code aparece aparte en la lista y hay que activarla de nuevo (por eso no hay auto-update).

## Mac mini servidor: cuelgues al abrir Documentos (22-oct-2026)
- El Vault vive en ~/Documents (local, sincronizado por Syncthing y git; no es iCloud). macOS protege Documentos con permiso de privacidad: los procesos sin pantalla (corridas de artes, el puente) pueden quedarse esperando un permiso que nadie contesta. La corrida de cambios del 21-oct quedó 26 h colgada y la de cierre 12 h.
- Arreglo: tope de 3 h con timeout en uk-cambios-watch.sh y uk-cierre-watch.sh (respaldos en ~/Claude/respaldos/*.2026-10-22). Pendiente: Acceso total al disco para claude y Terminal (Ajustes → Privacidad y seguridad), con alguien frente a la Mac.
- Antes de culpar a iCloud, probar con timeout y mirar si el archivo está en ~/Documents (local) o en Mobile Documents (iCloud).
