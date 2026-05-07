---
type: reference
date: 2026-05-05
tags: [agente, geoffrey, integraciones, gmail, reminders]
---

# Integraciones — Geoffrey

Integraciones previstas para Geoffrey. Esta página documenta roles, límites y decisiones antes de conectar skills o credenciales.

## Brief mañanero

La especificación operativa vive en [[geoffrey/brief-mananero|Brief mañanero — Geoffrey]]. Decisiones vigentes:

- Trato siempre de **usted**.
- Hora objetivo: 7:15 AM Guatemala; ventana aceptable 6:30–8:00 AM.
- Diario de Centro América se revisa todos los días como fuente legal/regulatoria prioritaria.
- Portafolio personal excluido por ahora; solo mercados generales si aportan.
- SMS autorizado vía [[imsg]] para lectura local minimizada; no enviar ni marcar como leído sin aprobación explícita.

## Gmail

| Cuenta | Rol | Tratamiento |
|---|---|---|
| `joserca95@gmail.com` | Personal + AMC Legal | Triage y clasificación por cliente. Prioridad alta a temas legales. Nunca borrar correos de clientes sin aprobación. |
| `jcastaneda@kidsunderstanding.com` | Understanding Kids | Triage comercial: pedidos, soporte, proveedores, operaciones. |
| `joserca95@icloud.com` | iCloud — cobros y servicios | Vigilar cobros, suscripciones y facturas. Alertar si algo cambia, se duplica o parece anómalo. |
| `joserca95@ufm.edu` | UFM | No incluir en integración activa; JR lo revisa manualmente salvo instrucción futura. |

## SMS

- Skill autorizada: [[imsg]].
- Uso para brief: detectar SMS pendientes de respuesta o señales relevantes de familia, clientes activos y contactos VIP.
- No transcribir mensajes crudos en el brief salvo instrucción explícita.
- No enviar SMS, reaccionar, marcar como leído ni modificar conversaciones sin aprobación por acción.
- Pendiente técnico: confirmar Full Disk Access en macOS si la lectura falla.

## Diario de Centro América

- Fuente: `https://dca.gob.gt/`.
- Rol: diario oficial / fuente legal-regulatoria de Guatemala.
- Uso para brief: leyes, normativa, acuerdos, nombramientos, licitaciones, avisos institucionales y cualquier publicación con impacto para AMC Legal o proyectos de Master JR.

### Decisión pendiente

Para separar AMC Legal dentro de `joserca95@gmail.com`, preferencia recomendada: usar **labels/filtros de Gmail** en vez de depender solo de inferencia por remitente/dominio.

Pendiente de aprobación/configuración:

- Crear label `AMC Legal`.
- Crear labels por cliente activo cuando tenga volumen recurrente.
- Reglas/filtros por remitente, dominio, asunto y patrones conocidos.
- Geoffrey puede sugerir reglas, pero no modificar Gmail sin aprobación explícita.

## Relacionado

- [[geoffrey/rutinas|Rutinas — Geoffrey]] · [[geoffrey/brief-mananero|Brief mañanero — Geoffrey]] · [[geoffrey/skills-permitidas|Skills permitidas — Geoffrey]] · [[skills/index|Catálogo común de skills]] · [[imsg]]
