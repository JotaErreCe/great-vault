---
type: reference
date: 2026-05-13
tags: [agente, briefs, arquitectura, rutinas]
---

# Arquitectura de briefs multi-agente

El brief diario de JR es consolidado por Geoffrey. La especificación vigente y obligatoria está en [[agentes/geoffrey/brief-mananero|Brief mañanero — Geoffrey]]. Esta página describe la arquitectura general; si contradice a Geoffrey, prevalece la especificación de Geoffrey.

## Estado actual

- El brief diario se envía por Telegram directo.
- La automatización debe hacerse con cron de OpenClaw, no con heartbeat genérico.
- Nombre esperado del job: `Geoffrey Morning Brief`.
- Hora objetivo: 7:15 AM Guatemala.
- Cron: `15 7 * * *` con `--tz America/Guatemala`.

## Roles

| Rol | Responsabilidad |
|---|---|
| Agentes especializados | Revisan su dominio, detectan novedades, riesgos, oportunidades y acciones sugeridas. |
| Geoffrey | Orquesta, deduplica, prioriza por impacto para JR y redacta el brief consolidado. |
| JR | Recibe el brief final y aprueba cualquier acción externa. |

## Flujo diario

1. Geoffrey se despierta por cron.
2. Lee [[agentes/geoffrey/brief-mananero|Brief mañanero — Geoffrey]], [[agentes/geoffrey/rutinas|Rutinas — Geoffrey]] y fuentes mínimas.
3. Audita calendario, Reminders, comunicaciones disponibles y DCA/radar legal.
4. Omite ruido y fuentes sin señal accionable.
5. Redacta el brief final en Telegram.
6. Si corresponde, guarda copia en `wiki/agentes/geoffrey/briefs/brief-YYYY-MM-DD.md` y registra hallazgos duraderos en el Vault.

## Regla de oro

El brief consolidado no es una suma de reportes. Geoffrey debe decidir qué importa hoy para JR.

Si un agente no tiene novedades, su sección se omite. Si dos fuentes reportan el mismo asunto, Geoffrey lo consolida en una sola entrada con la categoría más útil.

## Formato vigente resumido

El brief debe entrar directo a:

1. 📅 Lo que le depara el día.
2. 📬 Comunicaciones relevantes.
3. ⚖️ Radar legal Guatemala / DCA.
4. 🧑‍💼 Radar de cliente, solo si aplica.
5. ✅ Reminders / qué haceres.
6. ✅ Puedo ejecutar con aprobación.

No incluir como secciones fijas:

- Noticias.
- Frentes abiertos.
- Pendientes acumulados.
- Puede ignorar hoy.
- Top 3.
- Mapa de Atención.
- Riesgo de arrastre.

## Daily signal por agente especializado

Formato recomendado si en el futuro hay agentes especializados:

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

## Relacionado

- [[arquitectura]] · [[agentes/geoffrey/rutinas|Rutinas — Geoffrey]] · [[agentes/geoffrey/brief-mananero|Brief mañanero — Geoffrey]] · [[agentes/geoffrey/integraciones|Integraciones — Geoffrey]] · [[agentes/geoffrey/reminders|Reminders — Geoffrey]]
