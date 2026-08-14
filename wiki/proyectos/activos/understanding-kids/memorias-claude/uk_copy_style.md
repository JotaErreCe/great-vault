---
name: uk-copy-style
description: Preferencias de JR para el copy de contenido de Understanding Kids (evitar tono AI)
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c5d2da67-1c63-46c7-a0d4-78f10ddf6cd4
  modified: 2026-08-05T17:46:52.694Z
---

Para el copy de los artes/contenido de [[project-understanding-kids]], JR pide un tono **humano, no de IA**. Evitar palabras que suenan a robot/marketing genérico.

Ejemplos concretos dados por JR (2026-07-16):
- "explorar" → usar "conocer" ("Escríbenos para conocer cómo..." en vez de "para explorar cómo...").

**Reglas duras de caption (JR 2026-08-05):**
1. **Máximo 5 hashtags por caption.** Cinco es el techo, no la meta.
2. **Nunca un punto pegado antes de un emoji.** ✗ "árbol. 🌳" → ✓ "árbol 🌳". El emoji ya cierra la frase. `?` y `!` sí se permiten antes de emoji porque cargan significado.
3. **Tuteo, no voseo** (observado en los captions que JR aprueba: "puedes", "guárdalo", "te contamos"), aunque JR hable de vos en el chat.

Guardarraíl ejecutable: `verificar_caption.py --todas "<carpeta>"` en la carpeta del Sistema revisa 1 y 2 sobre todos los `caption.txt`. Se corre junto con `verificar_marca.py` antes de reportar una corrida. Ver [[uk-template-system]].

**Why:** JR es quien escribe/aprueba el contenido de la clínica y le molesta el tono artificial; quiere que suene como habla una persona real.
**How to apply:** al redactar cualquier copy para UK, preferir verbos y frases cotidianas/humanas; evitar "explorar", "descubre", "potencia", "impulsa", "eleva" y similares de jerga de marketing salvo que JR los use primero. Ante la duda, elegir la palabra más simple y directa.
