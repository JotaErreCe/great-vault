---
type: reference
date: 2026-10-19
tags: [agente, claude, telegram, voz]
---

# Notas de voz por Telegram

JR puede mandar **notas de voz** por Telegram en vez de escribir. Todo está instalado en la Mac (sin API de pago).

## Flujo

1. El mensaje llega con `attachment_file_id` en la etiqueta `<channel>`.
2. `download_attachment` con ese id devuelve una ruta local.
3. `~/Claude/bin/transcribir-vn.sh <ruta>` imprime el texto.

**Nunca usar `Read` sobre el audio:** no lee audio, hay que transcribir.

## Qué modelo y por qué

Medido el 8-sep-2026 en la M2 de 8 GB, sobre 13 s de español guatemalteco:

| Modelo | Tiempo | Resultado |
|---|---|---|
| `base` | 5.5 s | «mil quetzales» bien, pero «cambiarle» → «cambiale» |
| `small` sin prompt | 9.5 s | **«mil QUE SALES»**: corrompió un precio |
| `medium` | 42.2 s | todo correcto, 4 veces más lento |
| `small` + `--initial_prompt` | 10.7 s | **todo correcto** |

Por eso el script usa `small` con un **prompt de vocabulario de la clínica** (quetzales, preuniversitarios, Magoo, Davinia, integración sensorial, CAES, zona 14…). Sin ese prompt, `small` inventa palabras justo en cifras y nombres propios. Un modelo más grande no es automáticamente mejor: el sesgo de vocabulario rinde más que el tamaño. Corre a ~0.75× tiempo real (una nota de un minuto tarda unos 45 s).

## Regla al usar una nota de voz

Una transcripción es una aproximación. **Antes de actuar sobre cifras, fechas, precios o nombres propios que vengan de una nota de voz, confirma lo entendido en una línea** (igual que manda `~/Claude/CLAUDE.md` para las correcciones).

**(sin verificar al 8-sep-2026):** que un audio real de Telegram llegue con `attachment_file_id`. La transcripción está probada con un `.ogg/opus` del mismo formato; faltaba el tramo del puente.

## Relacionado

- [[agentes/claude/AGENT|Claude]] · [[agentes/claude/telegram-puente]] · [[agentes/claude/persona-tio-iroh]]
