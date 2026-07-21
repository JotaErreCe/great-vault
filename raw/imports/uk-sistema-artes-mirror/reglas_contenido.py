"""
Lineamientos de largo de copy por plantilla y campo.
Basado en lo que ya vimos que se ve bien (carrusel de alimentación aprobado)
vs. lo que se sintió vacío o forzado (piloto de artes reales).

Uso: llamar validar(plantilla, campo, texto) desde cada build_*.py al construir
el contenido. No bloquea la generación — imprime un aviso si el texto se sale
del rango, para revisar antes de aprobar.
"""

# (min_palabras, max_palabras, motivo si se sale)
REGLAS = {
    "portada": {
        "headline_main": (4, 10, "muy corto se ve pobre; muy largo empuja el resaltado a varias líneas"),
        "headline_keyword": (1, 3, "es el 'golpe' visual — si no cabe en 1 línea, pierde impacto (ver piloto 16-jul)"),
    },
    "contenido": {
        "heading": (2, 6, "título de la plantilla de contenido"),
        "body_sin_bullets": (15, 30, "sin esto el cuadro queda con mucho vacío arriba/abajo"),
        "body_con_bullets": (0, 10, "solo la frase introductoria antes de la lista, ej. 'Por ejemplo:'"),
        "bullet_item": (1, 8, "cada viñeta — una sola palabra fuerte está bien (ej. 'Arcadas')"),
        "closing_pre": (2, 8, "frase antes de la palabra clave del cierre — OPCIONAL, dejar vacío si el slide no lleva cierre"),
        "closing_keyword": (1, 4, "palabra clave del cierre — OPCIONAL, dejar vacío si el slide no lleva cierre"),
    },
    "contenido_imagen": {
        "heading": (2, 6, "la foto ya aporta peso visual, el texto puede ser más corto"),
        "body": (10, 25, "acompaña a la imagen, no compite con ella"),
    },
    "frase": {
        "quote": (4, 14, "si es más larga que esto ya no es una frase de impacto — usar plantilla de Contenido en su lugar"),
        "author": (1, 5, "nombre/atribución"),
        "context": (0, 8, "opcional, una línea"),
    },
    "cierre": {
        "heading": (2, 5, "título del cierre"),
        "body_pre": (8, 22, "cuerpo del cierre, junto con body_highlight"),
        "body_highlight": (1, 6, "frase resaltada — corta, mismo criterio que portada"),
        "closing": (4, 10, "frase final memorable, no un resumen largo"),
    },
}


def _contar(texto: str) -> int:
    return len(texto.split()) if texto else 0


def validar(plantilla: str, campo: str, texto: str) -> str | None:
    """Devuelve un mensaje de aviso si el texto se sale del rango, o None si está bien.
    Los campos vacíos ("") se consideran omitidos a propósito (todos los campos de
    contenido son opcionales en el diseño) y no se validan."""
    if not texto:
        return None
    regla = REGLAS.get(plantilla, {}).get(campo)
    if not regla:
        return None
    minimo, maximo, motivo = regla
    n = _contar(texto)
    if n < minimo:
        return f"[aviso] {plantilla}.{campo}: {n} palabras (mín. {minimo}) — {motivo}"
    if n > maximo:
        return f"[aviso] {plantilla}.{campo}: {n} palabras (máx. {maximo}) — {motivo}"
    return None


def validar_todos(plantilla: str, campos: dict) -> None:
    """Valida varios campos de una vez e imprime los avisos encontrados."""
    avisos = [validar(plantilla, campo, texto) for campo, texto in campos.items()]
    avisos = [a for a in avisos if a]
    for a in avisos:
        print(a)
    return avisos
