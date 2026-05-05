---
type: reference
date: 2026-05-05
tags: [agente, geoffrey, integraciones, gmail, reminders]
---

# Integraciones — Geoffrey

Integraciones previstas para Geoffrey. Esta página documenta roles, límites y decisiones antes de conectar skills o credenciales.

## Gmail

| Cuenta | Rol | Tratamiento |
|---|---|---|
| `joserca95@gmail.com` | Personal + AMC Legal | Triage y clasificación por cliente. Prioridad alta a temas legales. Nunca borrar correos de clientes sin aprobación. |
| `jcastaneda@kidsunderstanding.com` | Understanding Kids | Triage comercial: pedidos, soporte, proveedores, operaciones. |
| `joserca95@icloud.com` | iCloud — cobros y servicios | Vigilar cobros, suscripciones y facturas. Alertar si algo cambia, se duplica o parece anómalo. |
| `joserca95@ufm.edu` | UFM | No incluir en integración activa; JR lo revisa manualmente salvo instrucción futura. |

### Decisión pendiente

Para separar AMC Legal dentro de `joserca95@gmail.com`, preferencia recomendada: usar **labels/filtros de Gmail** en vez de depender solo de inferencia por remitente/dominio.

Pendiente de aprobación/configuración:

- Crear label `AMC Legal`.
- Crear labels por cliente activo cuando tenga volumen recurrente.
- Reglas/filtros por remitente, dominio, asunto y patrones conocidos.
- Geoffrey puede sugerir reglas, pero no modificar Gmail sin aprobación explícita.

## Relacionado

- [[geoffrey/rutinas|Rutinas — Geoffrey]] · [[geoffrey/skills-permitidas|Skills permitidas — Geoffrey]] · [[skills/index|Catálogo común de skills]]
