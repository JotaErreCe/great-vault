---
type: proyecto
date: 2026-09-24
estado: activo
last-touched: 2026-09-25
tags:
  - proyecto
  - estado/activo
  - prioridad/media
  - tema/producto
  - tema/ia
---

# Quedamos (app de reuniones, nombre provisional)

App de escritorio macOS que convierte cada reunión en transcripción, resumen de una pantalla, obligaciones de cada parte y recordatorios solo para JR. "Una secretaria en esteroides": que nada de lo prometido en una reunión se pierda. Inspiración: Granola.

> Código y datos: `~/Claude/quedamos/` (Mac Pro). Goal completo: [[agente-actas-goal-prompt]]. Análisis económico: [[agente-actas-reuniones]].

---

## 📝 Descripción

Captura local (micrófono y audio del sistema en pistas separadas, nunca bots), transcripción (Whisper local o Deepgram/AssemblyAI según cierre la Fase 0), extracción con Claude de obligaciones en tres cubetas (mías / de otros / huérfanas) y tres niveles de firmeza (firme / tentativo / mencionado), correo al usuario y, con aprobación explícita, recordatorios en Apple Recordatorios o .ics. Regla suprema: una obligación existe solo si alguien se comprometió y hay cita textual que lo sustente.

---

## 🎯 Objetivos

1. Cerrar la Fase 0: validar el ASR con cinco reuniones reales en español guatemalteco (Deepgram vs AssemblyAI vs Whisper local).
2. Prototipo usable por JR: grabar, transcribir, extraer, correo, recordatorios propios.
3. Cero obligaciones inventadas; cero obligaciones firmes perdidas.

---

## 📌 Decisiones clave

| Fecha | Decisión | Motivo |
|-------|----------|--------|
| 2026-09-24 | Captura local, nunca bots; recordatorios solo al usuario; herramienta general; macOS primero; español con code-switching; no entrenar con datos del usuario | Decisiones cerradas por JR en el goal |
| 2026-09-24 | JR delegó las decisiones de la noche ("decide por mí, quiero ver la app mañana") | Se construyó el prototipo antes de cerrar Fase 0, con el ASR detrás de una interfaz intercambiable |
| 2026-09-25 | Whisper local corre con VAD Silero + `-mc 0` + `-sns` | Con flags por defecto alucinó en bucle y perdió 36 de 86 min de la reunión de prueba; con VAD: 0 bucles y 2.7 min de proceso |
| 2026-09-25 | Extracción de la noche hecha en sesión de Claude Code con el prompt de `fase0/prompts` | No hay ANTHROPIC_API_KEY ni `claude` CLI logueado en la Mac Pro |

---

## ✅ Próximos pasos

- [ ] JR: llaves de Deepgram (USD 200 gratis) y AssemblyAI (USD 50 gratis) en `fase0/.env`
- [ ] JR: llave de Anthropic API (arnés y app)
- [ ] JR: cuatro grabaciones más (Propi, Disegno Casa, UK, una por Meet/Zoom)
- [ ] Correr `uv run fase0/run.py all` y decidir el ASR con `fase0/reports/comparativo.md`
- [ ] JR: revisar el prompt `fase0/prompts/extraccion_system.md` y el correo generado de la reunión del 2026-05-19
- [ ] JR: abrir `app/build/Quedamos.app`, revisar la reunión cargada, dar permisos de micrófono y audio del sistema y grabar una reunión de prueba (Fase 1)
- [ ] Leer `docs/2026-09-25-reporte-para-JR.md` (qué se hizo la noche del 24 al 25 y qué falta)

---

## 🔗 Relacionado

- [[agente-actas-goal-prompt]] · [[agente-actas-reuniones]]
- [[understanding-kids]] (la reunión de prueba: [[reunion-2026-05-19-magoo-jr]])
- [[wiki/index]]
