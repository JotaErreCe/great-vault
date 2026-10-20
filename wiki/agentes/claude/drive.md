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
