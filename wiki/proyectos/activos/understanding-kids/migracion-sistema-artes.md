---
type: resource
date: 2026-07-21
last-touched: 2026-07-21
tags:
  - resource
  - tema/automatizacion
  - tema/infraestructura
  - proyecto/understanding-kids
status: pendiente-de-ejecutar
---

# Runbook — Migrar el sistema de artes a la Mac Mini

Guía **autosuficiente** para mudar la automatización de artes de [[understanding-kids|UK]]/[[integracion-sensorial|IS]] desde la laptop de [[jr]] (`jotaerre`) a la **Mac Mini (`jr`)**, que está encendida 24/7.

> **Por qué migrar:** las tareas programadas solo corren **con la app de Claude abierta** en una Mac encendida a la hora del cron. La laptop se apaga o se queda sin batería (viajes), así que los domingos/jueves se pierden corridas. La Mac Mini resuelve eso.
>
> **Estado:** pendiente. JR viaja hasta el **1 de agosto de 2026** ([[viajes/florida-familia-castaneda-2026]]); ejecutar después de esa fecha.
>
> Sistema documentado en [[proyectos/activos/understanding-kids/sistema-artes-redes]].

---

## 0. El riesgo #1 — leer esto antes que nada

El "motor" del sistema (plantillas, guías, fuentes, logos, llaves) vive en:

```
~/Documents/Understanding Kids/Artes/Sistema/
```

Esa carpeta está en **iCloud** y la premisa de esta migración es que **se sincroniza sola** a la Mac Mini. Eso solo ocurre si en la Mini está activo *Escritorio y Documentos en iCloud Drive* con la misma Apple ID.

**Verificar ANTES de cualquier otra cosa, en la Mac Mini:**

```bash
ls "$HOME/Documents/Understanding Kids/Artes/Sistema/" | head
```

- ✅ Si lista `build_portada.py`, `GUIA_MAESTRA_ESTILO.md`, etc. → seguir con el paso 1.
- ❌ Si la carpeta NO existe → **no hay que copiar nada a mano ni volver a la laptop.** Hay un **espejo del motor completo dentro del vault**, que llega por Syncthing (probado entre las dos máquinas). Restaurar con:

```bash
VAULT="$HOME/documents/Great Vault"     # en la Mac Mini
mkdir -p "$HOME/Documents/Understanding Kids/Artes/Sistema"
rsync -a "$VAULT/raw/imports/uk-sistema-artes-mirror/" \
         "$HOME/Documents/Understanding Kids/Artes/Sistema/"
mkdir -p "$HOME/Documents/Understanding Kids/Artes/Pendientes de Revision" \
         "$HOME/Documents/Understanding Kids/Artes/Aprobadas"
```

Con eso el sistema queda operativo aunque iCloud nunca funcione. Aun así, **conviene activar iCloud después** (Escritorio y Documentos con la Apple ID de JR): así las mejoras futuras a las plantillas viajan solas y las carpetas de revisión se ven desde ambas máquinas. Detalles del espejo: `raw/imports/uk-sistema-artes-mirror/_LEEME-ESPEJO.md`.

⚠️ Ojo: los archivos de iCloud pueden estar "en la nube" sin descargar (aparecen con ☁️). Forzar descarga antes de correr nada:
```bash
find "$HOME/Documents/Understanding Kids/Artes/Sistema" -type f -exec cat {} + > /dev/null 2>&1
```

---

## 1. Inventario: qué viaja solo y qué hay que montar

| Pieza | Dónde vive | ¿Llega sola a la Mini? |
|---|---|---|
| Motor: `build_*.py`, guías, fuentes y logos (base64), `pexels_key.txt` | `~/Documents/Understanding Kids/Artes/Sistema/` | ✅ iCloud — **y espejo de respaldo en el vault** (`raw/imports/uk-sistema-artes-mirror/`, vía Syncthing). Nunca queda varado |
| Carpetas de revisión (`Pendientes de Revision/`, `Aprobadas/`) | `~/Documents/Understanding Kids/Artes/` | ✅ iCloud |
| Este vault (contexto para cualquier AI) | `~/Great Vault` (laptop) · `~/documents/Great Vault` (Mini) | ✅ Syncthing — **ojo: la ruta difiere entre máquinas** |
| Copias de las tareas programadas | `Sistema/scheduled-tasks-backup/*.SKILL.md` | ✅ iCloud (hay que **recrearlas**, §3) |
| Artes publicados y destino final | Google Drive `jcastaneda@kidsunderstanding.com` | ✅ nube — solo instalar Drive for Desktop |
| Calendario y tendencias | Notion (nube) | ✅ solo reconectar el MCP |
| **Claude Code + Python/Playwright** | local | ❌ **instalar** (§2) |
| **Conexiones MCP** (Notion, Apify, Drive, tareas) | perfil local de la app | ❌ **reconectar** (§4) |
| **Tareas programadas activas** | `~/.claude/scheduled-tasks/` | ❌ **recrear** (§3) |
| **Permiso de Apple Mail** (correo a Magoo) | permisos de macOS | ❌ **conceder** (§5) |

---

## 2. Instalar dependencias en la Mac Mini

```bash
# 1. Claude Code — instalador OFICIAL firmado.
#    NO usar npm: en arm64 entrega un binario sin firmar que macOS mata
#    ("permission denied" / "killed"). Este bug ya se sufrió en la laptop.
curl -fsSL https://claude.ai/install.sh | bash

# 2. Python 3 (el del sistema sirve) + Playwright con Chromium
pip3 install playwright
python3 -m playwright install chromium

# 3. Verificación
python3 -c "from playwright.sync_api import sync_playwright; print('playwright OK')"
```

Además: instalar **Google Drive for Desktop** e iniciar sesión con `jcastaneda@kidsunderstanding.com`. Verificar que exista:
```bash
ls "$HOME/Library/CloudStorage/GoogleDrive-jcastaneda@kidsunderstanding.com/My Drive/Administración/Artes/2026/"
```
> Nota: esa ruta lleva el **correo**, no el usuario del Mac, así que es idéntica en ambas máquinas. Las rutas del sistema usan `~`, así que funcionan igual con el usuario `jotaerre` o `jr`. **La única ruta que cambia entre máquinas es la del vault.**

`buscar_foto.py` usa `curl` por dentro (el Python de python.org falla SSL) — `curl` ya viene con macOS, no hay que instalar nada.

---

## 3. Recrear las dos tareas programadas

Los prompts completos están respaldados en `Sistema/scheduled-tasks-backup/`. En la Mac Mini, pedirle a Claude:

> «Recreá las dos tareas programadas del sistema de artes de UK usando los prompts de `~/Documents/Understanding Kids/Artes/Sistema/scheduled-tasks-backup/`: `uk-artes-semanales` (cron `0 18 * * 0`, domingos 18:00) y `uk-tendencias-virales` (cron `0 18 * * 4`, jueves 18:00). Usá el contenido de cada SKILL.md tal cual.»

| Tarea | Cron | Qué hace |
|---|---|---|
| `uk-artes-semanales` | dom 18:00 | Lee el Calendario de Artes de Notion + tendencias Aprobadas → genera carruseles + historias + captions → deja todo en `Artes/Pendientes de Revision/` |
| `uk-tendencias-virales` | jue 18:00 | Rastrea tendencias virales en IG/FB/YouTube/TikTok (vía Apify) → sugiere en la base 🔥 Tendencias de Notion |

⚠️ **Las tareas solo corren con la app de Claude abierta.** En la Mac Mini hay que dejarla abierta permanentemente — ese es todo el punto de la migración.

---

## 4. Reconectar los MCP

En la app de Claude de la Mac Mini, conectar:

| MCP | Para qué | Notas |
|---|---|---|
| **Notion** | Calendario de Artes + base 🔥 Tendencias | Data sources: calendario `collection://175780c0-4762-81ec-a2a0-000bf5fe9eac` · tendencias `collection://c8b3310c-b24a-49f9-8a3f-3dd4c60c5359` |
| **Apify** | Datos de IG/FB/TikTok/YT para el agente de tendencias | Cuenta de JR. Presupuesto acordado: **máx ~$2 USD por corrida** |
| **Tareas programadas** | Correr los dos agentes | — |
| Canva (opcional) | Solo lectura de artes viejos | No lo usa el flujo actual |

💡 Tras crear cada tarea, correrla **una vez a mano ("Run now")** para aprobar de antemano los permisos de herramientas. Si no, la primera corrida automática se queda esperando un permiso a las 18:00 y no genera nada.

---

## 5. Correo a Magoo (paso 4 del cierre)

El cierre de cada aprobación termina con un correo a **msamayoa@kidsunderstanding.com** desde **jcastaneda@kidsunderstanding.com**, enviado vía `osascript` + Apple Mail.

En la Mac Mini hay que: tener esa cuenta configurada en Mail.app y **conceder el permiso de automatización** la primera vez (macOS lo pide solo). Probar con un borrador antes de confiarlo a la rutina.

---

## 6. Prueba de humo (antes de darlo por migrado)

```bash
cd "$HOME/Documents/Understanding Kids/Artes/Sistema"
python3 -c "
import build_portada
build_portada.render({'marca':'IS','autismo':True,'icon':'🫂',
  'headline_main':'Prueba de migración','headline_keyword':'funciona'}, '_prueba.png')
"
```
Debe generar `_prueba.png` (1080×1350) con: fondo crema, Cocogoose, subrayado **turquesa** (acento IS) y el **sello del infinito** abajo. Si eso sale bien, el motor está sano. Borrar el archivo después.

Checklist final:
- [ ] iCloud sincroniza `Artes/Sistema/` (§0)
- [ ] Playwright renderiza (§6)
- [ ] Google Drive montado con la cuenta correcta
- [ ] MCP de Notion y Apify conectados
- [ ] Las 2 tareas creadas y corridas una vez a mano
- [ ] Apple Mail autorizado
- [ ] **Tareas DESACTIVADAS en la laptop** (§7)

---

## 7. Apagar la laptop como generadora

Al terminar, **deshabilitar o borrar** `uk-artes-semanales` y `uk-tendencias-virales` en la laptop. Si quedan activas en las dos máquinas se duplica el trabajo (y el gasto de Apify).

> El cruce contra Drive evita duplicar *artes*, pero no evita gastar dos veces en Apify ni mandarle a Magoo dos correos.

---

## 8. Alternativas si la Mac Mini no funciona

- **a) Cambiar el horario** de las tareas a un momento en que la laptop sí esté encendida (ej. lunes 9am). Cambio de 1 minuto, sin migrar nada.
- **b) Corrida manual:** las tareas se pueden disparar a mano cualquier día ("corré la tarea de artes semanales"). El cruce contra Drive evita duplicados, así que correrla tarde no rompe nada.
- **c) Agente en la nube — NO viable hoy:** los agentes programados en la nube no pueden renderizar con Playwright local ni ver el Drive montado. Requeriría re-arquitectura (render en servidor + Drive API).

## Relacionado

[[proyectos/activos/understanding-kids/sistema-artes-redes]] · [[understanding-kids]] · [[integracion-sensorial]] · [[viajes/florida-familia-castaneda-2026]]
