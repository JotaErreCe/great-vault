---
type: reference
date: 2026-05-07
tags: [skill, agente, google-workspace, drive, docs, sheets, seguridad]
estado: aprobada
---

# google-workspace-mcp

## Resumen

Skill MCP para gestionar Google Workspace desde OpenClaw: Drive, Docs, Sheets, Calendar, Gmail, Chat, People y Slides.

## Origen

- Ruta local de skill: `/Users/jr/.openclaw/workspace/skills/google-workspace-mcp/SKILL.md`
- Paquete runtime: `@presto-ai/google-workspace-mcp`
- Servidor MCP: `google-workspace` vía `mcporter`
- Fuente pública revisada: ClawHub `google-workspace-mcp`
- Config local: `/Users/jr/.mcporter/mcporter.json`
- Credenciales: almacenadas cifradas por el paquete en `~/.config/google-workspace-mcp/`; no guardar tokens en el Vault.

## Capacidades

- Lee: perfil Google autenticado, Drive, Docs, Sheets, Slides, Calendar, Gmail, Chat y People según scopes concedidos.
- Escribe/modifica: Docs, Drive, Calendar, Gmail, Chat y otros endpoints cuando se usen herramientas de escritura.
- Envía/publica: Gmail y Google Chat tienen herramientas de envío; Calendar puede crear/responder eventos.
- Borra: Calendar/Drive/Gmail pueden tener operaciones destructivas o modificadoras según herramienta.
- Usa red: sí, APIs de Google y servidor de refresh del paquete.
- Usa credenciales: OAuth de la cuenta Google autorizada por JR.

## Riesgos

- Riesgos técnicos: dependencia de `mcporter`, `npx` y paquete npm externo; OAuth puede requerir reautenticación.
- Riesgos de privacidad: acceso amplio a archivos, correo, calendario, chats y contactos si se invocan esas herramientas.
- Riesgos externos: envío de correo/chat, cambios en documentos, eventos o archivos podrían comprometer a JR frente a terceros.

## Condiciones de uso

- Permitido por defecto: operaciones read-only y minimizadas para tareas explícitas de JR, especialmente buscar/listar Drive, leer metadatos, localizar Docs/Sheets y resumir información solicitada.
- Permitido con cuidado: leer contenido de Docs/Sheets solo cuando JR indique el archivo, carpeta, búsqueda o contexto de la tarea.
- Prohibido sin aprobación explícita por acción: enviar Gmail/Chat, crear/editar/borrar/mover/compartir archivos, modificar Docs/Sheets, crear/actualizar/borrar eventos, cambiar permisos, archivar/marcar correo, o descargar/exportar material sensible de forma masiva.
- Prohibido: guardar tokens, callback URLs OAuth, mensajes crudos, documentos completos sensibles o dumps de Drive en el Vault.

## Verificación local

- OAuth completado y credenciales cifradas localmente el 2026-05-07.
- Verificado `people.getMe` con la cuenta de JR.
- Verificado `drive.search` read-only para documentos/hojas.
- Verificado `sheets.getMetadata` en una hoja encontrada sin leer celdas.
- Verificado que existen Google Docs encontrados; no se leyó contenido sin objetivo explícito.

## Decisión

Estado: aprobada limitada.
Fecha: 2026-05-07.
Aprobó: Master JR, para Drive + Docs + Sheets; se mantiene política read-only por defecto.

## Relacionado

- [[skills/index]] · [[geoffrey/skills-permitidas|Skills permitidas — Geoffrey]] · [[geoffrey/integraciones|Integraciones — Geoffrey]]
