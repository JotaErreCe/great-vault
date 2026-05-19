---
type: reference
date: 2026-05-19
tags: [skill, agente, audio, transcripcion, openai]
estado: aprobada
---

# openai-whisper-api

## Resumen

Skill para transcribir archivos de audio usando OpenAI Audio Transcriptions API vía `curl`.

## Origen

- Ruta bundled: `/opt/homebrew/lib/node_modules/openclaw/skills/openai-whisper-api/`
- Ruta instalada Geoffrey: runtime `skills/openai-whisper-api/`
- Fuente: OpenClaw bundled skill.
- API: OpenAI `/v1/audio/transcriptions`.

## Capacidades

- Lee: archivos de audio locales provistos por JR o recibidos como attachment.
- Escribe/modifica: genera archivos `.txt` o `.json` de transcripción cuando se le indica.
- Envía/publica: no.
- Borra: no.
- Usa red: sí, envía el audio a OpenAI para transcripción.
- Usa credenciales: `OPENAI_API_KEY` desde entorno/config; no debe imprimirse ni guardarse en el Vault.

## Riesgos

- Privacidad: el audio sale a OpenAI; no usar para audios altamente sensibles sin confirmación específica.
- Costo: cada transcripción puede generar costo API según duración/modelo.
- Exactitud: puede fallar con ruido, múltiples voces, nombres propios o spanglish; revisar antes de usar como evidencia.

## Condiciones de uso

Permitido para Geoffrey:

- Transcribir audios enviados por JR en Telegram directo o archivos que JR indique explícitamente.
- Guardar transcripciones en workspace temporal o adjuntarlas en respuesta.
- Guardar en Vault solo si JR lo pide o si se destila como conocimiento durable siguiendo [[protocolo-operativo-agentes]].

Prohibido sin aprobación explícita:

- Transcribir audios de terceros no autorizados.
- Transcribir en grupos por defecto si puede exponer privacidad.
- Guardar audio crudo o transcript completo en el Vault sin necesidad clara.
- Imprimir o registrar API keys.

## Decisión

Estado: aprobada para Geoffrey bajo condiciones anteriores.
Fecha: 2026-05-19.
Aprobó: JR solicitó instalar el transcriptor de OpenAI y lo necesario para transcribir audios.

## Relacionado

- [[skills/index]]
- [[geoffrey/skills-permitidas]]
- [[protocolo-operativo-agentes]]
- [[geoffrey/importadores-seguros]]
