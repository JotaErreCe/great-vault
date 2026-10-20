---
type: reference
date: 2026-10-19
tags: [reference, vault, agentes]
---

# Great Vault: qué es y cómo se usa desde la Mac

El Great Vault (Obsidian) es la **fuente canónica** de todo lo que se sabe de [[jr]]: datos personales, familia, personas, proyectos y, desde el 19-oct-2026, lo que aprenden sus agentes ([[vault-cerebro]]). El esquema y las reglas están en [[_AI_BOOTSTRAP]] y `AGENTS.md`; esta página agrega lo práctico para un agente que corre en la Mac Mini.

## Dónde está

- Ruta real: **`~/Documents/Great Vault/`** (confirmado en la configuración de Obsidian). **No** `~/Great Vault/`.
- Hay un respaldo hermano `~/Documents/Great Vault Backup 2026-05-04/`: no se trabaja ahí.
- Está dentro de Documentos en iCloud con «Mantener descargado» (19-oct-2026) y además se replica por **Syncthing** (le llega a Geoffrey). Cambios grandes se hacen por fases.
- Lo que vive fuera del Vault (imágenes, artes, scripts, estado de agentes): [[mapa-de-archivos]].

## Puntos de entrada

1. [[_AI_BOOTSTRAP]] (el único archivo indispensable).
2. `USER.md` y [[como-trabajar-con-jr]].
3. `wiki/personas/<nombre>.md`, `wiki/proyectos/`, `wiki/agentes/<agente>/`.
4. `AGENTS.md` y [[protocolo-operativo-agentes]] para las reglas.

Estructura: `raw/` inmutable (leer y citar) · `wiki/` conocimiento (aquí se escribe) · `_templates/` · `skills/` (tooling de OpenClaw/ClawHub, no tocar) · `_sensitive.md` (solo por pedido) · raíz solo archivos de control.

## Reglas para agentes

- **Antes de escribir un nombre, fecha, parentesco o dato personal, buscarlo aquí.** Si no está, decir «no sé» y preguntar; nunca deducirlo del correo, del usuario de Telegram ni de las iniciales (ver [[como-trabajar-con-jr]]).
- Datos base que salen de aquí: JR = José Roberto Castañeda Arriola; su esposa Mónica Samayoa Mendoza de Castañeda, a quien JR llama **siempre «Magoo»** ([[monica]]); hijo [[nicolas]]; perro [[niko]].
- **`wiki/agentes/` incluye perfiles de agentes de inversión** (Livermore, Soros, Belfort, Nakamoto…) con `parametros/`: JR aclaró el 2026-08-26 que eran **una correa para un agente de trading, no su doctrina de inversión**; el sistema está suspendido desde el 4-jul-2026. No citarlos como su criterio. Sus metas reales están en [[wiki/IDENTITY]] § Metas. Ante la duda, preguntarle.
- Todo cambio en `wiki/` lleva su línea en [[wiki/log/2026-10|el log del mes]].

## Relacionado

- [[_AI_BOOTSTRAP]] · [[vault-map|Vault Map]] · [[mapa-de-archivos]] · [[vault-cerebro]]
- [[como-trabajar-con-jr]] · [[agentes]] · [[agentes/claude/AGENT|Claude]]
