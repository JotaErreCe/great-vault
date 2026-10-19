---
type: proyecto
date: 2026-10-19
estado: en-revision
tags:
  - proyecto
  - estado/activo
  - prioridad/alta
  - tema/infraestructura
  - tema/automatizacion
---

# Vault como cerebro: plan de centralización

> **Estado:** borrador para revisión de [[jr]]. No se ha movido nada todavía.
> **Pedido de JR (19-oct-2026):** «El vault es el cerebro de todo, no archivos sueltos en la Mac.»
> «Tiene que tener información de absolutamente todo.» Las imágenes y los artes **no** van adentro,
> pero el Vault tiene que saber dónde están.

## Por qué

Hoy lo que se sabe de cada sistema está repartido en tres lugares y ninguno tiene el cuadro completo:

| Lugar | Qué tiene | Problema |
|---|---|---|
| Este Vault | Notas y wiki | La página del sistema de artes está congelada en julio; hay una copia vieja del motor (agosto) con una llave de Pexels adentro |
| `~/Documents/Understanding Kids/Artes/Sistema/` | Guías, plantillas `.py`, fuentes, logos, artes | Las guías vivas (las que se usan cada semana) están aquí, no en el Vault |
| `~/.claude/` y `~/Claude/` | Memorias de Claude, instrucciones de las tareas automáticas, scripts | Reglas y aprendizajes que solo Claude ve |

El 19-oct además se trabó todo por iCloud. Eso ya quedó resuelto: JR puso «Mantener descargado» en
Documentos (el Vault y Understanding Kids tienen 0 archivos en la nube), y se apagó el auto-update de
Claude porque cada versión nueva volvía a pedir permisos de macOS.

## La regla de qué va dónde

| Tipo | Dónde vive | Ejemplos |
|---|---|---|
| **Conocimiento** (lo que se lee para entender o decidir) | **Vault**, `wiki/` | Guías de estilo, reglas de marca y copy, cómo funciona cada sistema, decisiones, aprendizajes de Claude |
| **Mapa** de todo lo que está afuera | **Vault**, una nota | Dónde están logos, fotos, fuentes, artes, scripts; qué es cada cosa y para qué sirve |
| **Imágenes y archivos de trabajo** | Afuera (taller), donde están hoy | Logos, fotos, fuentes, PNG de artes, renders, cachés |
| **Estado de un agente** (lo que necesita para correr) | Afuera, `~/.claude/` y `~/Claude/` | Instrucciones de tareas programadas, scripts de `bin/`, LaunchAgents. El Vault los **documenta**; no los contiene |
| **Secretos** | Solo `_sensitive.md` o `~/.claude/secrets/` | Llaves de API, tokens. Nunca en `wiki/` ni `raw/` |

Esto respeta [[AGENTS]]: el Vault es conocimiento; el estado de runtime queda fuera.

## Decisiones que necesito de JR

**D1. ¿Las plantillas `.py` entran al Vault?**
Recomiendo **no**. Las plantillas cargan fuentes y logos desde su propia carpeta y escriben renders
HTML y cachés ahí mismo (13 scripts dependen de eso). Si se mueven al Vault: o se rompe el render, o
el Vault se llena de imágenes y cachés, que es justo lo que no quieres. En cambio, el Vault tendría
una página que explica cada plantilla (para qué sirve, qué recibe, qué reglas aplica) y apunta al
archivo.

**D2. ¿Sigue haciendo falta la copia diaria a Drive?**
Se aprobó cuando el plan era sacar los archivos de iCloud. Con «Mantener descargado», iCloud sigue
siendo el respaldo y el Vault además tiene su propio historial (git) y Syncthing. Recomiendo **no
hacerla** por ahora.

**D3. La copia vieja del motor y la llave de Pexels.**
`raw/imports/uk-sistema-artes-mirror/` es una copia de agosto, desactualizada, con la llave de Pexels
y fuentes y logos convertidos a texto. Syncthing la replica. Recomiendo:
borrarla del Vault (es `raw/`, por eso pido permiso), pasar la llave a `_sensitive.md` y **cambiar la
llave de Pexels**, porque ya se copió a otro equipo. El historial de git no lo toco (reescribirlo es
destructivo).

**D4. Las memorias de Claude.**
Recomiendo que el conocimiento pase a páginas del Vault (fuente de verdad) y que cada memoria de
Claude quede como una regla corta con el enlace a su página. Así lo que aprende Claude lo puede leer
también Geoffrey y tú desde Obsidian.

**D5. Geoffrey.**
Todo lo que entre al Vault le llega por Syncthing. ¿Está bien que vea el sistema de artes y las
reglas de Claude?

**D6. Alcance de esta primera vuelta.**
Propongo empezar por: sistema de artes de UK, conocimiento de Claude y lo pendiente de la casa nueva.
Propi, AMC Legal, finanzas y los demás proyectos van en una segunda vuelta, con su propio inventario.

## Fases

Cada fase la ejecuta un agente; Claude revisa antes de pasar a la siguiente. Nada se borra sin
respaldo previo.

**F0. Respaldo.** Copia comprimida de `~/.claude/projects/-Users-jr-Claude/memory/`,
`~/.claude/scheduled-tasks/`, `~/Claude/CLAUDE.md`, `~/Claude/bin/` y de las guías de `Sistema/`, en
`~/Claude/respaldos/2026-10-vault-cerebro/`.

**F1. Seguridad (si D3 = sí).** Sacar la copia vieja del motor, mover la llave a `_sensitive.md`,
avisar a JR para que cambie la llave en Pexels y actualizar la nueva donde la use `buscar_foto.py`.

**F2. El sistema de artes en el Vault.**
- Pasar las guías vivas al Vault con nombre en minúsculas:
  `GUIA_MAESTRA_ESTILO.md` → [[guia-maestra-estilo]], `GUIA_PROMOS_TALLERES.md` → [[guia-promos-talleres]],
  `tendencias_referentes.md` → [[tendencias-referentes]], dentro de
  `wiki/proyectos/activos/understanding-kids/`. Pasan a ser la fuente de verdad: las tareas las leen
  desde el Vault.
- Reescribir [[sistema-artes-redes]] con el estado real de octubre: flujo con Notion, revisión,
  correcciones, cierre, tendencias, avisos por Telegram, verificadores, Fotos.
- Una página por plantilla (o una sola con secciones): qué hace, qué recibe, guardarraíles.
- Marcar [[migracion-sistema-artes]] y `memorias-claude/` como obsoletos y enlazar a lo nuevo.

**F3. El mapa.** Crear [[mapa-de-archivos]] en `wiki/resources/`: cada carpeta del taller (Artes,
Fotos, Logos, Fuentes, Pendientes, Aprobadas, Descartadas, Sistema, `~/Claude/bin`, LaunchAgents,
Drive de la vitrina), qué contiene, quién la usa y cada cuánto cambia. Sin imágenes, solo rutas y
descripciones.

**F4. Lo que sabe Claude.**
- Una página por tema en `wiki/agentes/claude/` (igual que Geoffrey tiene `agentes/geoffrey/`):
  rol de coordinador, Telegram y su watchdog, avisos, notas de voz, correo, Drive, tareas programadas
  (qué hace cada una, cuándo corre y dónde están sus instrucciones), LaunchAgents.
- Lo que es de un proyecto va a la página del proyecto (reglas de copy y de marca a UK, Propi a Propi).
- Las memorias quedan como reglas cortas con enlace (D4). `~/Claude/CLAUDE.md` se adelgaza y apunta
  al Vault.

**F5. Lo pendiente.** `~/Claude/pendiente-vault/`: la página de la casa nueva y la guía de
electrodomésticos (solo la versión vigente; las anteriores quedan en el respaldo) entran al Vault.
Las fotos y los planos quedan afuera y van al mapa.

**F6. Rutas.** Actualizar las rutas de las guías en las instrucciones de `uk-artes-semanales` y
`uk-tendencias-virales`, en los prompts de `uk-cierre` y `uk-cambios`, en `CLAUDE.md` y en las
memorias. Al final, buscar que no quede ninguna ruta vieja.

**F7. Prueba.** Antes del domingo 25-oct:
- Las dos tareas leen las guías desde el Vault (prueba en seco, sin generar ni publicar nada).
- Un render de prueba de una plantilla a una carpeta temporal, para confirmar que nada se rompió.
- `verificar_marca.py` y `verificar_caption.py` en verde sobre Pendientes.
- Si algo falla, se vuelve atrás con el respaldo de F0 y se pausa hasta después del domingo.

**F8. Bitácora.** Registro en [[2026-10|wiki/log/2026-10]] y la decisión en
[[wiki/decisiones/2026-10|decisiones de octubre]].

## Riesgos

- **Domingo 25-oct:** si F7 no pasa antes, se pausa y las tareas corren con las rutas de siempre.
- **Syncthing / Geoffrey:** cambios grandes en el Vault le llegan a otro equipo; por eso se hace por fases.
- **Rutas escondidas:** 86 scripts de `Sistema/` tocan rutas, pero son de artes, que no se mueven.
  Solo cambian las rutas de las guías.

## Relacionado

- [[understanding-kids]]
- [[sistema-artes-redes]]
- [[great-vault]] · [[AGENTS]] · [[protocolo-operativo-agentes]]
- [[agentes]]
