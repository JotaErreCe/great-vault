---
type: reference
date: 2026-05-16
tags: [agente, geoffrey, skills, seguridad]
---

# Skills permitidas — Geoffrey

Whitelist específica de Geoffrey. Una skill solo puede usarse si también existe y está auditada en [[skills/index|catálogo común de skills]].

## Regla

Geoffrey no puede usar skills no listadas aquí, aunque estén instaladas en el sistema. Si una tarea requiere una skill no autorizada, debe pedir aprobación a Master JR antes de proceder.

## Permitidas actualmente

| Skill | Alcance permitido | Condiciones |
|---|---|---|
| [[resources/apple-reminders-manual|Apple Reminders]] | Listado básico de recordatorios (con notificación); creación/modificación/eliminación requiere aprobación explícita por acción. | Lectura: permitir con advertencia de privacidad; Escritura: requerir aprobación explícita por acción; Operaciones de riesgo alto (eliminación masiva, etc.) requieren revisión especial. |
| [[gmail]] | Lectura de correos específicos para tareas explícitamente solicitadas por JR (ej.: buscar correos de Thelma sobre contrato Altezza). | Extracción agregada y minimizada; evitar guardar mensajes crudos en el Vault; marcar como leído o archiver únicamente con aprobación explícita por acción. Envío, modificación o acceso a contactos requieren aprobación explícita de JR. |
| [[google-workspace-mcp]] | Drive, Docs, Sheets, Gmail y Calendar para tareas explícitas de JR. Read-only por defecto: buscar/listar archivos, revisar metadatos, leer contenido cuando JR indique archivo/carpeta/búsqueda/contexto y apoyar brief. | No enviar Gmail/Chat, crear/editar/borrar/mover/compartir archivos, modificar Docs/Sheets, crear/modificar eventos, cambiar permisos, descargar masivamente ni guardar tokens/contenido crudo sensible en el Vault sin aprobación explícita por acción. |
| [[imsg]] | Lectura local minimizada de SMS/iMessage para tareas explícitas, gastos bancarios, señales relevantes y brief. | No enviar, reaccionar, marcar como leído, automatizar respuestas ni transcribir mensajes crudos sin aprobación explícita por acción. |
| [[apple-calendar-jr]] | Lectura local de Apple Calendar: agenda, próximos eventos, alarmas, conflictos y brief. | No crear, editar, borrar, aceptar/rechazar eventos, invitar personas ni cambiar alarmas sin aprobación explícita por acción. |
| [[openai-whisper-api]] | Transcribir audios enviados o indicados explícitamente por JR. | El audio se envía a OpenAI y puede generar costo API; no usar para audios altamente sensibles, grupos o terceros no autorizados sin confirmación específica; no guardar transcript crudo en Vault salvo instrucción clara. |

## Revocadas / no permitidas

| Skill | Estado | Motivo |
|---|---|---|
| [[wacli]] | Revocada 2026-05-16 | JR pidió desconectar completamente WhatsApp por posible violación de términos y condiciones. No usar para lectura, búsqueda, sync ni envío salvo nueva autorización explícita. |

## Candidatas pendientes de auditoría

- Apple Notes.
- Contactos/People como skill independiente si se necesita más allá de Google Workspace.

## Relacionado

- [[geoffrey/SOUL|SOUL — Geoffrey]] · [[geoffrey/AGENT|AGENT — Geoffrey]] · [[skills/index|catálogo común de skills]] · [[arquitectura]]
