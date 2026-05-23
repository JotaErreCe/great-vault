---
type: reference
date: 2026-05-06
tags: [skill, correo, gmail, referencia]
estado: auditada
---

# gmail

## Resumen

Gmail API integration with managed OAuth. Read, send, and manage emails, threads, labels, and drafts via the Maton gateway.

## Origen

- Ruta / paquete: Skill OpenClaw disponible en repositorio oficial (ej.: openclaw/skills)
- Fuente: https://github.com/openclaw/skills (skill gmail-skill) y documentación en playbooks.com/skills/openclaw/skills/gmail
- Versión observada: 1.0.6 (según clawbot.ai)

## Capacidades

- Lee: bandeja de entrada, carpetas específicas, mensajes individuales, metadatos (remitente, asunto, fecha), threads, labels, drafts.
- Escribe/modifica: marcar como leído/no leído, archivar, eliminar, aplicar etiquetas, crear drafts.
- Envía/publica: enviar nuevos mensajes, responder, reenviar, enviar drafts.
- Borra: eliminar mensajes permanentemente o mover a papelera.
- Usa red: sí, requiere conexión a los servidores de Google a través del gateway de Maton.
- Usa credenciales: sí, requiere autenticación OAuth2 mediante Maton API key (token gestionado, no credenciales directas).

## Riesgos

- Riesgos técnicos: dependencia de conectividad y disponibilidad del gateway de Maton y de la API de Google; posible fallo si el servicio está caído o sin red.
- Riesgos de privacidad: acceso completo al historial de correos, incluyendo información sensible, financiera, personal y confidencial (ej.: asuntos legales, financieros, personales).
- Riesgos externos: posibilidad de enviar correos no deseados, modificar o eliminar correos importantes, exposición de credenciales si la Maton API key se filtra o el entorno se compromete.

## Condiciones de uso

- Permitido: lectura de correos específicos para tareas explícitamente solicitadas por JR (ej.: buscar correos de Thelma sobre contrato Altezza).
- Permitido: extracción agregada y minimizada; evitar guardar mensajes crudos en el Vault.
- Permitido: marcar como leído o archiver correos procesados únicamente con aprobación explícita por acción.
- Prohibido sin aprobación explícita: enviar correos, modificar o eliminar correos, acceder a contactos o configuración de cuenta, usar credenciales para otros servicios.
- Para análisis: trabajar localmente; a Canva/Nanobanana solo deben ir datos agregados y aprobados.

## Decisión

Estado: auditada
Fecha: 2026-05-06
Auditó: Geoffrey (agente)
Aprobó: 

## Relacionado

- [[agentes/skills/index]] · [[agentes/geoffrey/skills-permitidas|skills permitidas — Geoffrey]] · [[arquitectura]]
