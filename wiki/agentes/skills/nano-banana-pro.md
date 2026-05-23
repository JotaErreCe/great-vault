---
type: reference
date: 2026-05-07
tags: [skill, agente, nanobanana, imagen, auditoria]
estado: auditada
---

# nano-banana-pro

## Resumen

Skill ClawHub para generar o editar imágenes con Nano Banana Pro / Gemini 3 Pro Image. Relevante para crear visuales de apoyo en presentaciones, no para el análisis de gastos en sí.

## Candidatos revisados

| Skill | Estado ClawHub | Riesgo | Observación |
|---|---:|---|---|
| `nano-banana-pro` | SUSPICIOUS | medio/alto | Owner `steipete`; script Python corto y legible; usa `google-genai`, `pillow` y `GEMINI_API_KEY`. Aunque el código observado es simple, ClawHub lo marca suspicious. |
| `gemini-nano-banana` | CLEAN | medio/alto | Usa OneKey Gateway (`DEEPNLP_ONEKEY_ROUTER_ACCESS`) y paquetes de terceros. Menos directo; credenciales y tráfico pasan por OneKey/DeepNLP. |
| `nanobanana` | SUSPICIOUS | alto | Descripción en chino, API externa no prioritaria y flag suspicious. Descartar por ahora. |
| `ppt-with-nano-banana` | CLEAN | medio | Genera PPTs estilo whiteboard con contenido chino por defecto. No encaja bien con el estilo ejecutivo de Master JR. |

## Capacidades de `nano-banana-pro`

- Lee: prompt e imagen de entrada opcional.
- Escribe/modifica: genera PNG local.
- Envía/publica: no publica, pero envía prompt/imagen a Google Gemini API.
- Usa red: Google Gemini API.
- Usa credenciales: `GEMINI_API_KEY` o API key pasada por argumento.
- Dependencias: `uv`, `google-genai`, `pillow`.

## Riesgos

- Privacidad: si se usan imágenes, estas salen hacia Google Gemini API.
- Credenciales: requiere `GEMINI_API_KEY` disponible en entorno o pasada al comando.
- Costo/cuota: puede consumir cuota pagada de Gemini.
- Seguridad: ClawHub marca `nano-banana-pro` como suspicious; aunque el script revisado no muestra comportamiento malicioso obvio, debe instalarse solo con aprobación.

## Encaje con el caso de uso

Para la PPT de gastos, Nano Banana no es indispensable. La presentación puede hacerse con gráficos locales, tablas y diseño limpio sin IA de imagen.

Útil opcionalmente para:

- Portada visual.
- Ilustraciones por rubro de gasto.
- Íconos/escenas para recomendaciones de hábitos.

No debe recibir SMS crudos ni datos financieros sensibles. Si se usa, pasar prompts agregados y no identificables.

## Recomendación

No instalar Nano Banana todavía como requisito del primer prototipo. Primero probar:

1. [[imsg]] → extracción de gastos.
2. análisis local → rubros, meses, tarjetas/cuentas, recomendaciones.
3. PPT local.
4. Canva/importación.

Si después hace falta visual generativo, instalar `nano-banana-pro` con aprobación explícita o usar las herramientas nativas de generación de imagen de OpenClaw si están disponibles.

## Decisión

Estado: auditada.
Fecha: 2026-05-07.
Auditó: Geoffrey.
Recomendación: diferir instalación; candidata preferida si se aprueba: `nano-banana-pro`, no `nanobanana`.

## Relacionado

- [[agentes/skills/index]] · [[canva]] · [[agentes/geoffrey/skills-permitidas|Skills permitidas — Geoffrey]]
