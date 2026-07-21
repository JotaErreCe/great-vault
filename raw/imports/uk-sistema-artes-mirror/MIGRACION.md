# Migración del sistema de artes a una Mac siempre encendida

Objetivo (JR 2026-07-21): que las tareas automáticas corran en una máquina que
esté prendida 24/7 (la **Mac Mini `jr`**), porque la MacBook a veces se queda sin
batería o se apaga en viajes.

## 0. Por qué ahora es fácil

El "motor" del sistema (plantillas, guías, fuentes, logos, scripts) se movió a
**iCloud**: `~/Documents/Understanding Kids/Artes/Sistema/`. Con "Escritorio y
Documentos" de iCloud activado en ambas Macs, esa carpeta **aparece sola** en la
Mac Mini — no hay que copiar código a mano, y cuando se mejora una plantilla en
una Mac, la otra la recibe automáticamente. Las rutas del sistema son relativas a
`~/`, así que funcionan igual con el usuario `jotaerre` o `jr`.

## 1. Qué compone el sistema

| Pieza | Dónde vive | Cómo llega a la Mac Mini |
|---|---|---|
| Motor (plantillas, guías, fuentes, logos, `pexels_key.txt`, este runbook) | `~/Documents/Understanding Kids/Artes/Sistema/` | ✅ iCloud lo sincroniza solo |
| Carpetas de revisión (`Pendientes de Revision/`, `Aprobadas/`) | `~/Documents/Understanding Kids/Artes/` | ✅ iCloud |
| Prompts de las 2 tareas | `Sistema/scheduled-tasks-backup/*.SKILL.md` | ✅ iCloud (se recrean en la Mini, ver §3) |
| Memoria de Claude | `~/.claude/projects/-Users-jotaerre-Claude/memory/` | ⚠️ copiar a mano una vez |
| MCPs (Notion, Canva, tareas programadas) | config de Claude Code / `~/.claude.json` | ⚠️ reconectar (login OAuth) |
| Google Drive montado | `~/Library/CloudStorage/GoogleDrive-jcastaneda@…/` | ⚠️ instalar Drive for Desktop |
| Apple Mail (correo a Magoo) | Mail.app + osascript | ⚠️ que la cuenta jcastaneda@ esté en Mail |

## 2. Setup automático (lo que sí se puede scriptear)

En la Mac Mini, con la carpeta `Sistema` ya sincronizada por iCloud:

```bash
bash ~/Documents/Understanding\ Kids/Artes/Sistema/setup_mac_nueva.sh
```

Ese script instala Claude Code (instalador oficial firmado, **no npm** — el de npm
da binario corrupto en arm64), Playwright + Chromium, y hace una prueba de render.
Al final imprime los pasos manuales que faltan.

Nota técnica: `buscar_foto.py` usa `curl` por dentro (no `requests`) porque el
Python de python.org falla SSL — `curl` viene con macOS, no hay que instalar nada.

## 3. Pasos manuales (una vez, en la Mac Mini)

1. **iCloud:** Ajustes → tu cuenta → iCloud → iCloud Drive → activar "Escritorio y
   Documentos". Esperá a que baje `~/Documents/Understanding Kids/Artes/`.
2. **Google Drive para escritorio:** instalar y entrar con `jcastaneda@kidsunderstanding.com`.
   Verificar: `ls ~/Library/CloudStorage/GoogleDrive-jcastaneda@kidsunderstanding.com/My\ Drive/Administración/Artes/`
3. **Apple Mail:** que la cuenta `jcastaneda@kidsunderstanding.com` esté configurada
   (para el correo de cierre a Magoo).
4. **MCPs en Claude Code:** conectar Notion (workspace de UK), Canva y tareas
   programadas (login OAuth de cada uno).
5. **Memoria:** copiar `~/.claude/projects/-Users-jotaerre-Claude/memory/` de la
   MacBook a la misma ruta en la Mini (por AirDrop o un USB). Ojo: la subcarpeta
   lleva el nombre del usuario; en la Mini será `-Users-jr-...` — pedirle a Claude
   que la recree con el nombre correcto si hace falta.
6. **Recrear las 2 tareas:** abrir Claude Code en la Mini y pedir:
   > "Recreá dos tareas programadas desde los SKILL.md en
   > `~/Documents/Understanding Kids/Artes/Sistema/scheduled-tasks-backup/`:
   > `uk-artes-semanales` (cron `0 18 * * 0`, domingos 18:00) y
   > `uk-tendencias-virales` (cron `0 18 * * 4`, jueves 18:00), usando el contenido
   > de cada archivo como prompt."
7. **Pre-aprobar permisos:** correr cada tarea una vez con "Run now" para que
   apruebe de una los permisos de Bash/MCP y no se frene en cada corrida futura.
8. **En la MacBook vieja:** DESACTIVAR ambas tareas (que no corran en dos máquinas
   y dupliquen). Se hace desde el panel "Scheduled" de Claude Code.
9. **Dejar Claude Code ABIERTO** en la Mac Mini. Las tareas corren mientras la app
   está abierta; si está cerrada a la hora del cron, corren al reabrirla.

## 4. Alternativas (si algo de lo anterior no aplica)

- **Solo cambiar el horario:** si preferís no migrar todavía, mové el cron a una
  hora en que la MacBook sí esté encendida. Cambio de 1 línea, sin migrar nada.
- **Corrida manual:** cualquier tarea se dispara a mano ("corré la tarea de artes
  semanales"). El cruce contra Drive evita duplicados, así que correrla tarde o
  dos veces no rompe nada.
- **Si iCloud NO sincroniza `~/Documents`** (p. ej. no está activado "Escritorio y
  Documentos"): copiar la carpeta `Sistema/` a mano por AirDrop una vez, y de ahí
  en adelante mantenerla sincronizada manualmente al hacer cambios. Todo lo demás
  del runbook sigue igual.
- **Agente en la nube (hoy no viable):** los agentes en la nube de Claude no pueden
  renderizar con Playwright local ni ver el Drive montado. Requeriría re-arquitectura
  (render en servidor + Drive API). Solo si algún día ninguna Mac local sirve.

## 5. Qué NO depende de la máquina

- Notion, Canva y el contenido del Drive viven en la nube — nada que migrar.
- El vault de Obsidian se sincroniza aparte por Syncthing (rutas distintas por
  máquina: MacBook `~/Great Vault`, Mac Mini `~/documents/Great Vault`).

---
*Últ. actualización: 2026-07-21. Al mover el motor a iCloud, la migración pasó de
"copiar todo a mano" a "que iCloud haga su trabajo + 9 pasos de una vez".*
