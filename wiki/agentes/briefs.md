---
type: reference
date: 2026-05-05
tags: [agente, briefs, arquitectura, rutinas]
---

# Arquitectura de briefs multi-agente

El brief diario de JR no debe depender de que Geoffrey lea todo el Vault desde cero cada mañana. La arquitectura correcta es multi-agente: cada agente especializado produce señales de su dominio y Geoffrey consolida con visión global.

## Roles

| Rol | Responsabilidad |
|---|---|
| Agentes especializados | Revisan su dominio, detectan novedades, riesgos, oportunidades y acciones sugeridas. |
| Geoffrey | Orquesta, deduplica, prioriza por impacto para JR y redacta el brief consolidado. |
| JR | Recibe el brief final y aprueba cualquier acción externa. |

## Flujo diario

1. Cada agente especializado revisa sus fuentes autorizadas.
2. Cada agente produce un `daily signal` breve con solo novedades reales.
3. Geoffrey consulta esos signals, calendario, recordatorios e inbox autorizado.
4. Geoffrey elimina ruido, duplica temas cruzados y prioriza.
5. Geoffrey redacta el brief final en Telegram.
6. Si corresponde, Geoffrey guarda copia en `wiki/agentes/geoffrey/briefs/brief-YYYY-MM-DD.md`.

## Regla de oro

El brief consolidado no es una suma de reportes. Geoffrey debe decidir qué importa hoy para JR.

Si un agente no tiene novedades, su sección se omite. Si dos agentes reportan el mismo asunto, Geoffrey lo consolida en una sola entrada con la categoría más útil.

## Daily signal por agente

Formato recomendado:

```markdown
---
type: signal
date: YYYY-MM-DD
agent: nombre-agente
tags: [agente, signal, brief]
---

# Signal — nombre-agente — YYYY-MM-DD

## Novedades

- [Qué cambió] · [fuente]

## Riesgos / vencimientos

- [Riesgo o deadline] · [fecha/fuente]

## Acciones sugeridas

- [Acción] — [por qué importa]

## Omitir del brief

- [Tema revisado sin novedad]
```

## Orden del brief consolidado

1. Saludo, fecha y hora exacta de envío.
2. Línea editorial: lo más importante de hoy.
3. Hoy en calendario.
4. AMC Legal.
5. Inbox.
6. Proyectos.
7. Noticias.
8. Acciones sugeridas hoy.

## Prueba pendiente

Cuando estén configuradas las fuentes, hacer un brief de prueba simulando la noche del 2026-05-04 al 2026-05-05.

## Relacionado

- [[arquitectura]] · [[geoffrey/rutinas|Rutinas — Geoffrey]] · [[geoffrey/integraciones|Integraciones — Geoffrey]] · [[geoffrey/reminders|Reminders — Geoffrey]]
