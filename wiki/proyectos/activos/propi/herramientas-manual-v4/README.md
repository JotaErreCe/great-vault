# Herramientas — Manual de Cumplimiento V4 (control de cambios)

Motor y guion con los que se generó `IVE/Manual de Cumplimiento V4.docx` (2026-09-08) a partir de V3, con todos los cambios marcados como control de cambios de Word a nombre de **José Roberto Castañeda**.

## Archivos
- `redline.py` — motor lxml de control de cambios sobre `word/document.xml` (`replace`, `replace_in`, `replace_token`, `delete_para`, `delete_range`, `insert_after/before`, `insert_row_after`). Excluye automáticamente los párrafos dentro de campos TOC. Normaliza NFC/NBSP en las búsquedas.
- `apply_edits.py` — guion de las ~145 ediciones (sigue el orden del `guion-cambios-manual-v4.md`). Incluye `delete_table` y el pase final de nomenclatura LD/FT/FPADM.
- `document.clean.xml` — `document.xml` de la **base limpia**: V3 con todos los cambios de 2024 aceptados (ins/del/moveFrom/moveTo/prChange) y los 12 comentarios de la ronda 2024 retirados; runs fusionados.
- `V3 base (cambios 2024 aceptados).docx` — esa base empaquetada. Es el "documento idéntico al V3" sobre el que se trabajó; se usa como `--original` en la validación.

## Regenerar / iterar (p. ej. insertar la matriz de riesgo mañana)
```bash
mkdir -p v4 && cd v4
unzip -oq "V3 base (cambios 2024 aceptados).docx" -d unpacked
cp document.clean.xml unpacked/word/document.xml
python3 apply_edits.py                      # aplica las ediciones sobre document.xml
(cd unpacked && zip -Xrq "../Manual de Cumplimiento V4.docx" .)
python3 "$SKILL_DOCX/scripts/office/validate.py" "Manual de Cumplimiento V4.docx" \
  --original "V3 base (cambios 2024 aceptados).docx" --author "José Roberto Castañeda"
```
Requisitos: `python3` con `lxml`; skill `docx` (validate.py). No requiere LibreOffice.

## Lecciones (para no repetir)
- `find()` no exacto puede caer en entradas del índice (TOC) → hoy el motor las excluye; usar `exact=True` en títulos/leyendas cortas.
- Los `moveFrom/moveTo` de 2024 debían aceptarse en la base o la validación ve texto duplicado.
- `replace_in` reconstruye el párrafo con el formato del primer run: para tokens sueltos usar `replace_token` (conserva formato y tabuladores).
- Tras aceptar en Word, actualizar el índice (F9): las entradas del TOC no se tocan por diseño.

## Actualización 2026-09-08 (tarde)
- `accept_2024.py` — acepta cambios rastreados de autores distintos de JR en cualquier parte (document, header1, footnotes). Quedaban restos de Astrid/JR-2024 en `header1.xml`, `footnotes.xml` y `tblPrExChange` del cuerpo; ya están aceptados en la base.
- `apply_header.py` + `header1.clean.xml` — ediciones del encabezado (título, Revisión 01, Fecha 08-sept-26) con control de cambios. Correr después de `apply_edits.py`, con `unpacked/word/header1.xml` copiado desde `header1.clean.xml`.
- Verificación final: el único autor de revisiones en todas las partes es José Roberto Castañeda; comentarios de 2024 retirados.

## Actualización 2026-09-08 (noche) — base reconstruida
- La aceptación de 2024 se rehace con `accept_full.py` desde el V3 original: además de ins/del/moves a nivel run, **fusiona los párrafos cuya marca de párrafo estaba eliminada o movida (rPr/del, rPr/moveFrom)** y quita comentarios. Sin esto quedaban 10 párrafos numerados vacíos (a)-j)) y frases partidas ("Asimismo, se / deberá agregar…"). Base: 816 párrafos. Sustituye a `accept_2024.py`.
- Orden de regeneración: `cp -R <V3 original unzip> base2; python3 accept_full.py base2/word/{document,header1,footnotes}.xml; merge_runs.py base2/; vaciar comments*.xml, people.xml y core.xml; zip → "V3 base (cambios 2024 aceptados).docx"`. Luego `apply_edits.py` y `apply_header.py` sobre copias de esas partes.
