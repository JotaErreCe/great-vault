---
type: reference
date: 2026-10-19
tags: [agente, claude, correo, gmail]
---

# Correo: cuentas, herramientas y reglas

Cómo lee y envía correo Claude en nombre de [[jr]], qué se confirma antes y qué no, y las trampas técnicas que ya costaron correos mal enviados.

## Cuentas y herramienta vigente: `gws` (desde 16-oct-2026)

Las dos cuentas leen y envían por **`gws`** (Google Workspace CLI, permiso `gmail.modify`), sin Apple Mail (que se trababa):

| Cuenta | Uso | Configuración |
|---|---|---|
| `jcastaneda@kidsunderstanding.com` | Clínica (UK) | Por defecto: `~/.config/gws` |
| `joserca95@gmail.com` | Personal, Propi, AMC Legal | `GOOGLE_WORKSPACE_CLI_CONFIG_DIR=$HOME/.config/gws-joserca gws …` |

- Uso: `gws gmail users messages list|get|send --params '{"userId":"me",…}'`; el envío usa `--json '{"raw":"<base64url RFC822>"}'`.
- Cliente OAuth «OpenClaw» (Desktop) del proyecto GCP `gog-cli-497208` (dueño joserca95@), en modo **Testing**: solo entran los usuarios de prueba (las dos cuentas ya están). Otra cuenta nueva hay que sumarla en Google Auth Platform → Audience.
- jcastaneda@ tiene el rol `serviceusage.serviceUsageConsumer` en ese proyecto.
- Al hacer login hay que **marcar la casilla de Gmail** en la pantalla de permisos; si no, el token queda sin scope y da 403. Si un token nuevo da 403 raro, borrar `token_cache.json` de la carpeta de configuración.
- El conector de Gmail de claude.ai solo ve joserca95@.

## Reglas de envío: rutina vs. conversación

1. **Rutinas desatendidas → envían solas, sin preguntar.** Textual de JR (17-ago-2026): «las rutinas deben quedar ya establecidas y no deben tener pasos de autorización para correos». Hoy la única rutina con correo es el **resumen diario a Magoo** (6:00, de jcastaneda@ a msamayoa@, `uk-resumen-magoo.py`, ver [[sistema-artes-redes]]). El correo semanal de artes de julio-agosto ya no existe.
2. **Cualquier correo pedido en una conversación → siempre se muestra y se espera el visto bueno.** Textual: «si te pido otro correo en otro chat OBVIO necesito revisarlo antes de que lo envíes». Aplica aunque sea al mismo destinatario y aunque JR haya dicho «mándalo»: **pedir el correo no es aprobar su contenido.** Error del 17-ago-2026: se mandó un correo a Magoo sin mostrárselo a JR.
3. **Cuenta remitente:** JR quiere que se le pregunte desde qué cuenta cada vez, salvo lo de la clínica (siempre jcastaneda@, confirmado 28-ago-2026). Propi: en la práctica joserca95@, pero se pregunta.
4. Esta excepción de rutina no se generaliza a otras tareas ni a otros correos.

## Correos a Magoo

- **«Cachetes de conejo» en TODOS los correos a Magoo** (JR, 28-ago-2026: «Siempre ponle lo de los cachetes»).
- **Conciso, siempre** («No es necesario que le mandes un texto tan largo… Siempre conciso porfa»): qué le llega y qué tiene que hacer, sin contexto técnico.
- De **tú**, nunca voseo; sin rayas largas.
- Magoo no sube nada a Drive: nunca pedírselo en un correo ([[artes-decisiones-y-lecciones]]).
- Correcciones de artes: **no se le escribe** (decisión de JR, 19-oct-2026). Magoo pide los cambios por Notion («Cambios pedidos»); la regla del 21-sep de responder su correo quedó superada ([[agentes/claude/subagentes]]).

## Propi

Ningún correo de Propi sale sin que JR apruebe el borrador completo; prosa corrida, corto, sin rayas largas; adjuntos de uno en uno y verificados. Detalle: [[propi/handoff-2026-08-24|handoff TORONJA]].

## Apple Mail (vía anterior, hasta 16-oct-2026)

Se usaba con `osascript`. Queda como referencia por si `gws` falla:

- Cuentas en Mail.app: `"Google"` = **jcastaneda@** (la clínica, no la personal) · `"iCloud"` · `"joserca95@gmail.com"` · `"joserca95@ufm.edu"`. Para mandar desde la clínica: `set sender to "jcastaneda@kidsunderstanding.com"`.
- Las carpetas especiales de Gmail (Enviados, Todos…) viven dentro de `[Gmail]`: no se direccionan por nombre directo (error -1728); hay que recorrer `every mailbox of account` y comparar el nombre. Los `INBOX`/`Sent Messages` de primer nivel son señuelos casi vacíos.
- **El heredoc no funciona** (`osascript <<'EOF'` devuelve vacío con exit 0): escribir el script a un `.scpt` y correr `osascript archivo.scpt`, o `osascript -e` para una línea.
- Recorrer propiedad por propiedad en un buzón grande es lentísimo: filtrar primero con `whose`. Nunca `whose content contains` sobre la cuenta completa (cuelga Mail). El mensaje 1 es el más reciente.
- **Responder en hilo:** `reply m without opening window` + `set content` manda la respuesta **vacía** sin error (pasó el 21-sep-2026). Lo que funciona: `reply m with opening window`, `delay 2`, fijar `sender`, `set content`, `delay 1`, `send`; y verificar en Enviados el largo del contenido.
- **Nunca `send outgoing messages`:** manda toda la bandeja de salida de todas las cuentas (el 21-ago-2026 disparó seis correos de UK en borrador). Verificar Outbox vacío, `send newMsg` y esperar a que vuelva a cero.
- Usar siempre `timeout` (`~/.local/bin/timeout`).
- La skill `apple-mail-macos` que está en `skills/` del Vault es tooling de OpenClaw, no de Claude Code.

## Relacionado

- [[agentes/claude/AGENT|Claude]] · [[como-trabajar-con-jr]] · [[correos-y-contactos]]
- [[sistema-artes-redes]] · [[propi]] · [[monica]]
