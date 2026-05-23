---
type: reference
date: 2026-05-19
tags: [agente, geoffrey, ob1, importadores, seguridad]
---

# Importadores seguros — Geoffrey

Contrato para cualquier importador futuro desde Gmail, Calendar, Drive, SMS, web u otra fuente externa hacia el Great Vault.

## Regla central

Todo importador debe iniciar en **dry-run**. El primer output es una lista de candidatos con fingerprints, razones y riesgos. No escribe contenido crudo al Vault sin autorización granular.

## Pipeline obligatorio

1. **Scope**: fuente, rango temporal, cuentas, filtros y propósito.
2. **Read-only fetch**: lectura mínima necesaria.
3. **Redacción/minimización**: excluir tokens, credenciales, adjuntos crudos, DPI/NIT y datos no necesarios.
4. **Fingerprint**: generar hash estable por fuente+id+fecha+asunto/metadata.
5. **Deduplicación**: comparar contra candidatos previos y páginas existentes.
6. **Clasificación de confianza**: aplicar [[agentes/geoffrey/tool-authority-matrix]].
7. **Dry-run report**: candidatos, motivo de señal, destino propuesto, riesgo y acción sugerida.
8. **Aprobación**: JR confirma si se escribe, se ignora o se ajusta.
9. **Write mínimo**: si procede, destilar a `wiki/` o staging; nunca dump masivo.
10. **Log**: append en `wiki/log/YYYY-MM.md` con fuente y alcance, sin secretos.

## Formato de dry-run

| Campo | Descripción |
|---|---|
| `source` | Gmail/Calendar/Drive/SMS/web/etc. |
| `source_ref` | ID minimizado o link interno; no token ni URL sensible. |
| `fingerprint` | Hash corto estable. |
| `confidence` | T0–T5 según matriz. |
| `signal_reason` | Por qué importa. |
| `proposed_destination` | Página wiki/staging sugerida. |
| `risk` | bajo/medio/alto + razón. |
| `requires_approval` | sí/no y tipo de aprobación. |

## Fuentes inicialmente permitidas para pruebas

| Fuente | Estado | Límite Fase 2 |
|---|---|---|
| Gmail via Google Workspace MCP | autorizado read-only | Búsquedas puntuales y dry-run; sin `modify`, sin `send`, sin adjuntos masivos. |
| Google Calendar via Google Workspace MCP | autorizado read-only | Eventos concretos/día; sin crear/modificar. |
| Apple Calendar local skill | autorizado read-only | Brief/agenda; sin escritura. |
| Drive/Docs/Sheets | autorizado read-only | Solo archivos indicados o búsquedas explícitas; no mover/crear/compartir. |
| SMS/iMessage | autorizado lectura minimizada | Señales, gastos y brief; no enviar/reaccionar/marcar leído. |
| Web search | permitido | Investigación con citas; no memoria canónica sin verificación. |

## Prohibiciones

- No importar buzones completos.
- No guardar mensajes crudos como memoria.
- No descargar adjuntos masivamente.
- No crear labels/filtros ni modificar correo sin aprobación por acción.
- No promover salida de LLM a `memoria.md` sin confirmación explícita.

## Relacionado

- [[agentes/geoffrey/tool-authority-matrix]]
- [[agentes/geoffrey/ob1-fase-2]]
- [[agentes/geoffrey/skills-permitidas]]
