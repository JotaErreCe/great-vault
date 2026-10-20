---
type: reference
date: 2026-10-19
tags: [agente, claude, google-drive, runbook]
---

# Google Drive: montaje, cuentas y MCP

Cómo escribe y lee Claude en el Drive de la clínica (la vitrina de artes de [[understanding-kids|UK]]). Estructura de carpetas e IDs: [[mapa-de-archivos]] § Google Drive.

## Regla corta

- **Para subir o reemplazar:** el **disco montado** (`~/Library/CloudStorage/GoogleDrive-jcastaneda@kidsunderstanding.com/My Drive/…`), que usa la cuenta de la clínica, dueña de los artes. `cp` encima conserva ID, dueño e historial; `cp -R` de una carpeta completa funciona.
- **Para leer, buscar y sacar IDs o enlaces:** el MCP de Drive.
- La raíz se llama **`My Drive`** (en inglés; «Mi unidad» no existe). La carpeta real es `Administración (1)`.
- **Nunca listar la raíz del montaje** (miles de entradas, cuelga el turno): ir directo a la ruta profunda. Accesos al montaje con `timeout` o en segundo plano.
- Después de subir: verificar contra el origen por número de archivos y bytes.

## Por qué el MCP no sirve para reemplazar (28-ago-2026)

El MCP está autenticado como **joserca95@gmail.com** (personal) y los artes son de **jcastaneda@** (clínica). Verificado en vivo:
- `create_file` funciona (el archivo nuevo queda con dueño joserca95@).
- `trash_file` sobre un archivo de la clínica **falla** («The caller does not have permission»).
- `update_file` solo cambia título y carpeta, nunca el contenido.

O sea, «subir nuevo + borrar viejo» deja duplicados imposibles de limpiar y cambia el ID (rompe enlaces de Magoo). **Antes de reemplazar, comprobar el permiso de borrado, no solo el de escritura.**

## El montaje vacío (28-ago-2026, transitorio)

Síntoma: el disco montado, `test -d` en rutas profundas = true, pero `ls` devuelve vacío con exit 0 y `cp` falla en silencio. Es Google Drive para escritorio con la sesión caída. Se distingue de un cuelgue porque responde rápido, solo que con nada. Qué hacer: pedirle a JR que abra Google Drive en la Mac y revise la sesión; no pelear con el montaje ni intentarlo por API. El 7-sep-2026 se verificó que el montaje sirve (20 piezas, ~130 PNG sin errores); antes de darlo por muerto, probar la ruta profunda.

## iCloud del lado de origen

El que falla es el origen (`~/Documents/Understanding Kids`): `cp` daba `EDEADLK` («Resource deadlock avoided») con archivos evictos; se arreglaba con `brctl download "<carpeta>"` y reintentar. Desde el 19-oct-2026 Documentos está en «Mantener descargado»; para comprobar evictos: `find . -flags +dataless`.

No hay `rclone` ni `gdrive` instalados (sí `gcloud`).

## Relacionado

- [[agentes/claude/AGENT|Claude]] · [[mapa-de-archivos]] · [[sistema-artes-redes]] · [[agentes/claude/telegram-puente]]

- **«Resource deadlock avoided» = RESUELTO (20-oct-2026).** Causa: los procesos de Claude arrancan con la política de macOS `IOPOL_VFS_MATERIALIZE_DATALESS_FILES` apagada, y leer un archivo de Drive/iCloud «solo en la nube» falla con EDEADLK. Arreglo: `~/Claude/bin/con-drive <comando>` la enciende (se hereda a hijos y nietos). El puente de Telegram (`telegram-bridge.sh`), `uk-cambios-watch.sh` y `uk-cierre-watch.sh` ya arrancan con `con-drive` (respaldo en `~/Claude/respaldos/2026-10-20-con-drive/`). En una sesión que arrancó antes del cambio, anteponer `~/Claude/bin/con-drive` al comando. Precios de servicios: `Administración zona 14/Inscripción y políticas de pago/Políticas de pago/` (Servicios en clínica, a domicilio, virtuales); hoy no se da descuento (JR 20-oct-2026). JR: «necesito que tengas acceso 100% todo el tiempo sin excusas».
- **API de Drive, Docs y Sheets (20-oct-2026):** `gws` de joserca95@ ya tiene `drive.readonly`, `documents.readonly` y `spreadsheets.readonly` además de Gmail (JR autorizó por OAuth desde el celular; el truco: correr `gws auth login --scopes …` en segundo plano, mandarle el enlace a JR, que pegue la dirección `http://localhost:<puerto>/?code=…` y hacerle `curl` desde la Mac; después borrar `token_cache.json` si da 403). La de la clínica (jcastaneda@) también, el mismo día; con ella `gws drive files list` con `includeItemsFromAllDrives` encuentra todo, incluso «Compartido conmigo». Respaldos de las configuraciones previas en `~/Claude/respaldos/gws-*-pre-drive-2026-10-20`. Leer un Doc: `gws drive files export --params '{"fileId":"<id>","mimeType":"text/plain"}' --output <archivo>` (la salida tiene que estar bajo el directorio actual). El disco montado NO muestra «Compartido conmigo» ni el contenido de Docs/Sheets (son accesos directos): para eso, siempre la API.
- **Precios de servicios:** Google Doc «Servicios zona 14» (id `1KYv3NWVwwaW_-OXVZk6JsZxmAJF_sxIxahYxnpNTQvc`); hay equivalentes de Carretera y CAES. Oct-2026: terapias Q350 (lenguaje, ocupacional, conductual, educativa, psicológica), Q400 (alimentación, integración sensorial, física), Q250 (estimulación temprana, tutoría).
- **Escritura (20-oct-2026, a pedido de JR: «quiero que puedas editar, crear y ver documentos»):** las dos cuentas de `gws` tienen ahora `drive`, `documents` y `spreadsheets` completos (más `gmail.modify`). Probado creando un Doc de prueba en la clínica (mandado a la papelera). Regla: nunca borrar ni compartir nada sin preguntarle a JR. Respaldos previos: `~/Claude/respaldos/gws*-pre-escritura-2026-10-20`.

- **Búsqueda en Drive por API (20-oct-2026):** `name contains` con `corpora` NO es confiable para lo compartido: no encontró los «Resumen <Mes> 2026 — CAES» que sí existen. Para carpetas compartidas, recorrer con `'<id>' in parents` y verificar contra el disco montado.
