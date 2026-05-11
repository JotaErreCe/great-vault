---
type: reference
date: 2026-05-05
tags: [agente, geoffrey, skills, seguridad]
---

# Skills permitidas — Geoffrey

Whitelist específica de Geoffrey. Una skill solo puede usarse si también existe y está auditada en [[skills/index|catálogo común de skills]].

## Regla

Geoffrey no puede usar skills no listadas aquí, aunque estén instaladas en el sistema. Si una tarea requiere una skill no autorizada, debe pedir aprobación a Master JR antes de proceder.

## Permitidas actualmente

| Skill | Alcance permitido | Condiciones |
|---|---|---|
| [[apple-reminders]] | Listado básico de recordatorios (con notificación); creación/modificación/eliminación requiere aprobación explícita por acción. | Lectura: permitir con advertencia de privacidad; Escritura: requerir aprobación explícita por acción; Operaciones de riesgo alto (eliminación masiva, etc.) requieren revisión especial. |
| [[gmail]] | Lectura de correos específicos para tareas explícitamente solicitadas por JR (ej.: buscar correos de Thelma sobre contrato Altezza). | Extracción agregada y minimizada; evitar guardar mensajes crudos en el Vault; marcar como leído o archiver únicamente con aprobación explícita por acción. Envío, modificación o acceso a contactos requieren aprobación explícita de JR. |
| [[google-workspace-mcp]] | Drive, Docs y Sheets para tareas explícitas de JR. Read-only por defecto: buscar/listar archivos, revisar metadatos y leer contenido cuando JR indique archivo/carpeta/búsqueda o contexto. | No enviar Gmail/Chat, crear/editar/borrar/mover/compartir archivos, modificar Docs/Sheets, cambiar permisos, descargar masivamente ni guardar tokens/contenido crudo sensible en el Vault sin aprobación explícita por acción. |

## Candidatas pendientes de auditoría

- Calendar.
- WhatsApp.

## Relacionado

- [[geoffrey/SOUL|SOUL — Geoffrey]] · [[geoffrey/AGENT|AGENT — Geoffrey]] · [[skills/index|catálogo común de skills]] · [[arquitectura]]
