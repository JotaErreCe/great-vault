---
type: reference
date: 2026-05-16
tags: [agente, geoffrey, integraciones, gmail, reminders]
---

# Integraciones — Geoffrey

Integraciones previstas para Geoffrey. Esta página documenta roles, límites y decisiones antes de conectar skills o credenciales.

## Brief mañanero

La especificación operativa vive en [[geoffrey/brief-mananero|Brief mañanero — Geoffrey]]. Decisiones vigentes:

- Trato siempre de **usted**.
- Hora objetivo: 7:15 AM Guatemala; ventana aceptable 6:30–8:00 AM.
- Diario de Centro América se revisa todos los días como fuente legal/regulatoria prioritaria.
- El brief entra directo a lo que le depara el día; no inicia con resumen, Top 3 ni Mapa de Atención.
- Portafolio y finanzas personales excluidos por ahora, salvo solicitud explícita de JR.
- Noticias generales excluidas por ahora; no reintroducirlas como sección del brief salvo instrucción explícita de JR.
- SMS autorizado vía [[imsg]] para lectura local minimizada; no enviar ni marcar como leído sin aprobación explícita.

## Gmail

| Cuenta | Rol | Tratamiento |
|---|---|---|
| `joserca95@gmail.com` | Personal + AMC Legal | Triage y clasificación por cliente. Prioridad alta a temas legales. Nunca borrar correos de clientes sin aprobación. |
| `jcastaneda@kidsunderstanding.com` | Understanding Kids | Triage comercial: pedidos, soporte, proveedores, operaciones. |
| `joserca95@icloud.com` | iCloud — cobros y servicios | Vigilar cobros, suscripciones y facturas. Alertar si algo cambia, se duplica o parece anómalo. |
| `joserca95@ufm.edu` | UFM | No incluir en integración activa; JR lo revisa manualmente salvo instrucción futura. |

## SMS / iMessage

- Skill autorizada: [[imsg]].
- Estado runtime 2026-05-14: habilitada y `imsg ✓ Ready`.
- Uso para brief: detectar SMS pendientes de respuesta o señales relevantes de familia, clientes activos y contactos VIP.
- No transcribir mensajes crudos en el brief salvo instrucción explícita.
- No enviar SMS, reaccionar, marcar como leído ni modificar conversaciones sin aprobación por acción.
- Pendiente técnico: confirmar Full Disk Access en macOS si la lectura falla.

## WhatsApp

- **Estado 2026-05-16: desconectado y desautorizado por instrucción expresa de JR.**
- Motivo: JR indicó que conectar Geoffrey/`wacli` a WhatsApp puede violar términos y condiciones de WhatsApp y pidió desconexión completa.
- Acción ejecutada: `wacli auth logout` exitoso; store local `~/.wacli` eliminado; verificación posterior mostró `AUTHENTICATED false`, `CONNECTED false`, `MESSAGES 0`, `CHATS 0`, `CONTACTS 0`, `GROUPS 0`.
- Geoffrey **no debe usar WhatsApp/wacli**, ni lectura, sync, búsqueda, backfill, envío ni perfil, salvo nueva aprobación explícita de JR tras revisar riesgos/TOS.
- Si una tarea requiere WhatsApp, pedir a JR una alternativa o nueva autorización documentada.

## Apple Calendar

- Skill autorizada: [[apple-calendar-jr]] y, para Google Calendar, [[google-workspace-mcp]].
- Estado runtime 2026-05-14: `apple-calendar-jr ✓ Ready`; script local probado con próximos eventos y alarmas.
- Uso para brief: agenda del día, próximos eventos, alarmas faltantes, conflictos y ventanas reales.
- No crear, editar, borrar, aceptar/rechazar eventos, invitar personas ni cambiar alarmas sin aprobación explícita por acción.

## Audio / transcripción

- Skill autorizada: [[openai-whisper-api]].
- Estado runtime 2026-05-19: skill instalada en workspace Geoffrey y OpenClaw configurado para audio con OpenAI (`gpt-4o-mini-transcribe`) + fallback local Whisper CLI (`base`).
- Prueba: OpenAI API respondió `insufficient_quota`; fallback local Whisper funcionó con audio sintético de prueba.
- Uso permitido: transcribir audios enviados o indicados explícitamente por JR, preferentemente en Telegram directo.
- Privacidad/costo: OpenAI envía audio a API externa y puede costar; fallback local no envía audio fuera de la Mac, pero puede ser menos exacto.
- No guardar audio crudo ni transcript completo en el Vault salvo instrucción clara; destilar conocimiento durable según [[protocolo-operativo-agentes]].

## Diario de Centro América

- Fuente: `https://dca.gob.gt/`.
- Rol: diario oficial / fuente legal-regulatoria de Guatemala.
- Uso para brief: leyes, normativa, acuerdos, nombramientos, licitaciones, avisos institucionales y cualquier publicación con impacto para AMC Legal o proyectos de Master JR.

## Google Workspace

- Skill autorizada: [[google-workspace-mcp]].
- Alcance pedido por Master JR: Drive + gestión de archivos de Sheets, Docs, etc.
- Estado: OAuth completado y pruebas read-only exitosas el 2026-05-07.
- Uso permitido por defecto: buscar/listar archivos en Drive, revisar metadatos, localizar Docs/Sheets y leer contenido cuando JR indique el archivo/carpeta/búsqueda o contexto.
- No hacer sin aprobación explícita por acción: enviar Gmail/Chat, crear/editar/borrar/mover/compartir archivos, cambiar permisos, modificar Docs/Sheets, crear eventos, archivar/marcar correo o descargar/exportar material sensible de forma masiva.
- No guardar tokens, callback URLs OAuth, dumps de Drive ni documentos crudos sensibles en el Vault.

### Decisión pendiente

Para separar AMC Legal dentro de `joserca95@gmail.com`, preferencia recomendada: usar **labels/filtros de Gmail** en vez de depender solo de inferencia por remitente/dominio.

Pendiente de aprobación/configuración:

- Crear label `AMC Legal`.
- Crear labels por cliente activo cuando tenga volumen recurrente.
- Reglas/filtros por remitente, dominio, asunto y patrones conocidos.
- Geoffrey puede sugerir reglas, pero no modificar Gmail sin aprobación explícita.

## Relacionado

- [[geoffrey/rutinas|Rutinas — Geoffrey]] · [[geoffrey/brief-mananero|Brief mañanero — Geoffrey]] · [[geoffrey/skills-permitidas|Skills permitidas — Geoffrey]] · [[skills/index|Catálogo común de skills]] · [[imsg]] · [[openai-whisper-api]]
