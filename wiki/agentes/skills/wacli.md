---
type: reference
date: 2026-05-14
tags: [skill, agente, whatsapp, seguridad, reference]
estado: rechazada
---

# wacli

## Resumen

CLI para autenticar, sincronizar, buscar historial y enviar mensajes de WhatsApp a terceros desde macOS/CLI.

## Origen

- Skill OpenClaw: `/opt/homebrew/lib/node_modules/openclaw/skills/wacli/SKILL.md`
- Homepage: https://wacli.sh
- Fórmula Homebrew: `steipete/tap/wacli`
- Binario instalado: `wacli` 0.8.1 observado al instalar el 2026-05-14.

## Capacidades

- Lee: chats y mensajes sincronizados en store local `~/.wacli` cuando se autentica/sincroniza.
- Escribe/modifica: store local de sincronización; puede hacer backfill.
- Envía/publica: sí, mensajes de WhatsApp directos/grupos y archivos.
- Borra: no observado como capacidad principal en skill revisada.
- Usa red: sí, WhatsApp.
- Usa credenciales: sesión/QR de WhatsApp; depende del teléfono/cuenta de JR.

## Riesgos

- Riesgo externo alto: puede enviar mensajes a terceros o grupos.
- Privacidad: expone historial de WhatsApp, incluyendo familia, clientes y asuntos legales.
- Técnico: backfill/sync depende del teléfono y puede ser incompleto.

## Condiciones de uso

- Permitido: autenticar/sincronizar solo con aprobación de JR; buscar historial o chats para tareas explícitas de JR y con extracción minimizada.
- Permitido para brief: señales agregadas/relevantes, sin transcribir mensajes crudos salvo instrucción explícita.
- Prohibido sin aprobación explícita por acción: enviar mensajes, archivos, responder, reaccionar, modificar conversaciones o iniciar backfills amplios.
- Para envíos autorizados: confirmar destinatario exacto + texto final antes de enviar.
- No usar para responder al chat actual con JR; OpenClaw enruta respuestas normales.

## Verificación local

- 2026-05-14: skill habilitada y binario `wacli` instalado; OpenClaw reporta `wacli ✓ Ready`.
- Pendiente: autenticación QR/sync inicial cuando JR decida usar WhatsApp.

## Decisión

Estado: aprobada limitada.
Fecha: 2026-05-14.
Aprobó: Master JR, al pedir habilitar las skills necesarias para Geoffrey, bajo guardrails de no enviar ni modificar sin aprobación explícita.

## Relacionado

- [[skills/index]] · [[geoffrey/skills-permitidas|Skills permitidas — Geoffrey]] · [[geoffrey/integraciones|Integraciones — Geoffrey]]


## Revocación — 2026-05-16

JR pidió desconectar completamente WhatsApp porque conectar Geoffrey/`wacli` puede violar términos y condiciones de WhatsApp. Estado: revocada/rechazada para Geoffrey y para uso operativo general salvo nueva autorización explícita.

Acción ejecutada: `wacli auth logout`; store local `~/.wacli` eliminado; verificación posterior mostró autenticación falsa y store vacío.
