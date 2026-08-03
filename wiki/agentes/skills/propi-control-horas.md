---
type: reference
date: 2026-08-03
tags: [skill, agente, propi, google-sheets, amc-legal, seguridad]
estado: aprobada
---

# propi-control-horas

## Resumen

Skill/protocolo para actualizar el Google Sheet de control de horas de Propi/AMC Legal preservando fórmulas y formato mensual.

## Origen

- Ruta local ejecutable: `/Users/jr/.openclaw/workspace-geoffrey/skills/propi-control-horas/SKILL.md`
- Scripts auxiliares: `/Users/jr/.openclaw/workspace-geoffrey/scripts/propi/`
- Fixture de prueba Julio 2026: `/Users/jr/.openclaw/workspace-geoffrey/outputs/propi-control-horas-test/`
- Spreadsheet Propi: `1rbSuqzkzE9YJFtMv3csD1oqfjsgv9eIyoWFan5B1j7M`

## Capacidades

- Lee: Excel local de reporte de cobro, metadata del Google Sheet, rangos necesarios de la hoja.
- Escribe/modifica: pestañas y celdas del Google Sheet si JR aprueba la acción.
- Envía/publica: no.
- Borra: solo pestañas temporales o defectuosas con aprobación explícita.
- Usa red: sí, Google Sheets API.
- Usa credenciales: token cifrado local del Google Workspace MCP en `~/.config/google-workspace-mcp/`; tokens nunca van al Vault.

## Regla operativa Propi

Para cada nuevo mes:

1. **No reconstruir desde cero.**
2. Leer metadata del Sheet y ubicar la pestaña fuente: mes inmediatamente anterior correcto.
3. Duplicar la pestaña fuente con API oficial (`duplicateSheet`).
4. Renombrar la copia al mes destino.
5. Sobreescribir solo los datos variables:
   - mes en encabezado;
   - descripciones/rubros;
   - minutos;
   - filas sobrantes dentro del bloque de rubros;
   - totales solo si la plantilla no los calcula por fórmula.
6. Preservar formato, fórmulas, anchos, estilos y estructura de la pestaña fuente.
7. Verificar por API/export:
   - existe exactamente una pestaña destino;
   - no quedan pestañas `Hoja`, `Copia`, `TEST` no autorizadas;
   - cliente/mes correctos;
   - rubros correctos;
   - minutos y horas totales correctos;
   - base/exceso correctos.

## Acceso Google

Ruta confiable esperada:

- `~/.config/google-workspace-mcp/gemini-cli-workspace-token.json` — token OAuth cifrado.
- `~/.config/google-workspace-mcp/.gemini-cli-workspace-master-key` — master key local.
- Loader histórico funcional: `scripts/write-propi-junio-2026-direct.js`.

Estado auditado el 2026-08-03:

- La master key existe.
- El token cifrado falta.
- `mcporter` está configurado pero `~/.mcporter/credentials.json` tiene `entries: {}` y el servidor queda offline/timeout.
- `gws` existe pero no tiene OAuth client/credenciales configuradas.
- Conclusión: hay que restaurar/rehacer una vez el OAuth y verificarlo con `scripts/propi/google-token-check.js`; después no depender de Chrome/UI.

## Seguridad

- Read-only por defecto.
- Writes/deletes sobre Google Sheets requieren aprobación explícita por acción de JR.
- Pruebas deben hacerse en copia/pestaña `TEST Geoffrey ...` o localmente en `outputs/`.
- No imprimir tokens, cookies, callback URLs OAuth sensibles ni dumps de Drive.
- No usar DevTools/Chrome para edición fina de Sheets si la API oficial está disponible.

## Prueba Julio 2026

Fixture local creado el 2026-08-03:

- Carpeta: `/Users/jr/.openclaw/workspace-geoffrey/outputs/propi-control-horas-test/`
- Fuente: `AMC Legal/Clientes/Propi/Reporte de Cobro/Control de Horas - Propi - Julio 2026.xlsx`
- Total esperado: 11 rubros, 605 min, 10.083333 h.
- Base: Q3,500.00.
- Exceso: US$166.67.

## Lección crítica

El 2026-08-03 Geoffrey falló al crear/corregir `Julio 2026` reconstruyendo/pegando datos en vez de duplicar correctamente `Junio 2026` y tocar solo datos. Para este Sheet, la plantilla mensual —formato y fórmulas— es parte del dato y debe preservarse.

## Decisión

Estado: aprobada para Geoffrey como protocolo específico de Propi.
Fecha: 2026-08-03.
Aprobó: Master JR, al pedir crear una skill/protocolo para que Drive/Sheets no se vuelva a improvisar.

## Relacionado

- [[agentes/skills/index]] · [[agentes/geoffrey/skills-permitidas|Skills permitidas — Geoffrey]] · [[google-workspace-mcp]] · [[propi]]
