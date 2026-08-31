#!/usr/bin/env python3
"""Genera una Propuesta de Honorarios en .docx a partir de un spec JSON.

Uso:
    python3 build_propuesta.py spec.json "/ruta/salida/Propuesta - X.docx"

El script copia una plantilla .docx real (que ya trae membrete, pie de página,
estilos, tema y logo) y solo reescribe word/document.xml y word/numbering.xml.
Así el resultado es idéntico en formato a las propuestas históricas.
"""

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(os.path.dirname(HERE), "assets")

# ---------------------------------------------------------------- paleta CAM
AZUL_TITULO = "25679A"    # "Propuesta de Honorarios" (título centrado)
AZUL_SECCION = "2B75AE"   # encabezados de sección (I. Trabajos a Desarrollar:)
GRIS_TEXTO = "212121"     # cuerpo
NEGRO = "000000"          # énfasis en negrita y destinatario
NAVY = "1D272F"           # relleno de encabezado de tabla (marca CAM)

FONT = '<w:rFonts w:asciiTheme="majorHAnsi" w:hAnsiTheme="majorHAnsi" w:cstheme="majorHAnsi"/>'


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def runs(texto, color=GRIS_TEXTO, bold=False, sz=None):
    """Convierte texto con **negrita** en una secuencia de <w:r>.

    Los tramos en **negrita** se emiten en negro (convención de la casa: los
    montos y los términos clave van en negrita negra sobre el gris del cuerpo).
    """
    out = []
    for i, tramo in enumerate(re.split(r"\*\*(.+?)\*\*", texto, flags=re.S)):
        if not tramo:
            continue
        # Los tramos entre ** van en negrita negra; el resto conserva el color
        # que pidió quien llamó (azul para encabezados, gris para el cuerpo).
        realce = i % 2 == 1
        rpr = FONT
        if bold or realce:
            rpr += "<w:b/><w:bCs/>"
        rpr += f'<w:color w:val="{NEGRO if realce else color}"/>'
        if sz:
            rpr += f'<w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/>'
        rpr += '<w:lang w:val="es-GT"/>'
        out.append(
            f'<w:r><w:rPr>{rpr}</w:rPr>'
            f'<w:t xml:space="preserve">{esc(tramo)}</w:t></w:r>'
        )
    return "".join(out)


def parrafo(texto="", *, style=None, jc="both", color=GRIS_TEXTO, bold=False,
            num=None, ilvl=0, ind=None, spacing=None, sz=None):
    ppr = ""
    if style:
        ppr += f'<w:pStyle w:val="{style}"/>'
    if num is not None:
        ppr += f'<w:numPr><w:ilvl w:val="{ilvl}"/><w:numId w:val="{num}"/></w:numPr>'
    if spacing:
        ppr += spacing
    if ind:
        ppr += ind
    if jc:
        ppr += f'<w:jc w:val="{jc}"/>'
    if bold:
        # La marca de párrafo lleva el mismo formato para que el número de la
        # lista (I., II., …) salga en negrita y en el azul del encabezado.
        ppr += (f"<w:rPr>{FONT}<w:b/><w:bCs/>"
                f'<w:color w:val="{color}"/>'
                + (f'<w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/>' if sz else "")
                + '<w:lang w:val="es-GT"/></w:rPr>')
    ppr = f"<w:pPr>{ppr}</w:pPr>" if ppr else ""
    return f"<w:p>{ppr}{runs(texto, color=color, bold=bold, sz=sz) if texto else ''}</w:p>"


LINEA_276 = '<w:spacing w:line="276" w:lineRule="auto"/>'


# ------------------------------------------------------------------- numbering
ABSTRACTS = {
    # clave -> (numFmt, lvlText, left, hanging)
    "romano": ("upperRoman", "%1.", 1080, 720),
    "letra": ("lowerLetter", "%1)", 720, 360),
    "numero": ("decimal", "%1.", 720, 360),
    "vineta": ("bullet", "", 720, 360),
}


def abstract_xml(idx, clave):
    fmt, texto, left, hanging = ABSTRACTS[clave]
    rpr = ('<w:rPr><w:rFonts w:ascii="Symbol" w:hAnsi="Symbol" w:hint="default"/></w:rPr>'
           if clave == "vineta" else "")
    niveles = [
        f'<w:lvl w:ilvl="0"><w:start w:val="1"/><w:numFmt w:val="{fmt}"/>'
        f'<w:lvlText w:val="{esc(texto)}"/><w:lvlJc w:val="left"/>'
        f'<w:pPr><w:ind w:left="{left}" w:hanging="{hanging}"/></w:pPr>{rpr}</w:lvl>'
    ]
    for lvl in range(1, 9):
        niveles.append(
            f'<w:lvl w:ilvl="{lvl}"><w:start w:val="1"/><w:numFmt w:val="lowerLetter"/>'
            f'<w:lvlText w:val="%{lvl + 1}."/><w:lvlJc w:val="left"/>'
            f'<w:pPr><w:ind w:left="{left + 720 * lvl}" w:hanging="360"/></w:pPr></w:lvl>'
        )
    return (f'<w:abstractNum w:abstractNumId="{idx}"><w:multiLevelType w:val="hybridMultilevel"/>'
            + "".join(niveles) + "</w:abstractNum>")


NUM_SECCIONES = 1  # numId reservado para los romanos de las secciones


def numbering_xml(instancias):
    """instancias: clave ('letra', 'numero', …) de cada lista de contenido, en orden.

    numId 1 numera las secciones (I., II., III.) y es continuo a lo largo del
    documento. Cada lista de contenido recibe además su propio abstractNum, no
    solo su propio numId: compartir un abstractNum hace que la segunda lista
    continúe la numeración de la primera (c, d, e en vez de a, b, c), y un
    startOverride no basta para evitarlo en todos los renderizadores.
    """
    cuerpo = abstract_xml(0, "romano")
    cuerpo += "".join(abstract_xml(i + 1, clave)
                      for i, clave in enumerate(instancias))
    cuerpo += f'<w:num w:numId="{NUM_SECCIONES}"><w:abstractNumId w:val="0"/></w:num>'
    for i in range(len(instancias)):
        cuerpo += (f'<w:num w:numId="{i + 2}"><w:abstractNumId w:val="{i + 1}"/>'
                   '<w:lvlOverride w:ilvl="0"><w:startOverride w:val="1"/></w:lvlOverride>'
                   "</w:num>")
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            '<w:numbering xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
            + cuerpo + "</w:numbering>")


# ---------------------------------------------------------------------- tabla
def celda(texto, ancho, *, fill=None, bold=False, jc="left", vmerge=None,
          color=NEGRO, sz="20"):
    tcpr = f'<w:tcW w:w="{ancho}" w:type="dxa"/>'
    if vmerge == "restart":
        tcpr += '<w:vMerge w:val="restart"/>'
    elif vmerge == "cont":
        tcpr += "<w:vMerge/>"
    tcpr += ('<w:tcBorders>'
             '<w:top w:val="single" w:sz="4" w:space="0" w:color="auto"/>'
             '<w:left w:val="single" w:sz="4" w:space="0" w:color="auto"/>'
             '<w:bottom w:val="single" w:sz="4" w:space="0" w:color="auto"/>'
             '<w:right w:val="single" w:sz="4" w:space="0" w:color="auto"/>'
             '</w:tcBorders>')
    if fill:
        tcpr += f'<w:shd w:val="clear" w:color="auto" w:fill="{fill}"/>'
    tcpr += '<w:vAlign w:val="center"/>'
    p = (f'<w:p><w:pPr><w:jc w:val="{jc}"/></w:pPr>'
         + (runs(texto, color=color, bold=bold, sz=sz) if texto else "")
         + "</w:p>")
    return f"<w:tc><w:tcPr>{tcpr}</w:tcPr>{p}</w:tc>"


def tabla_xml(spec):
    """spec: {"titulo": str|None, "columnas": [str], "anchos": [int]?,
              "filas": [[str]], "total": [str]?}"""
    cols = spec["columnas"]
    total_ancho = 8544
    anchos = spec.get("anchos")
    if not anchos:
        primera = int(total_ancho * 0.30)
        resto = total_ancho - primera
        anchos = [primera] + [resto // (len(cols) - 1)] * (len(cols) - 1)
        anchos[-1] += total_ancho - sum(anchos)
    grid = "".join(f'<w:gridCol w:w="{a}"/>' for a in anchos)

    filas = []
    if spec.get("titulo"):
        filas.append(
            "<w:tr>" + f'<w:tc><w:tcPr><w:tcW w:w="{total_ancho}" w:type="dxa"/>'
            f'<w:gridSpan w:val="{len(cols)}"/>'
            '<w:tcBorders>'
            '<w:top w:val="single" w:sz="4" w:space="0" w:color="auto"/>'
            '<w:left w:val="single" w:sz="4" w:space="0" w:color="auto"/>'
            '<w:bottom w:val="single" w:sz="4" w:space="0" w:color="auto"/>'
            '<w:right w:val="single" w:sz="4" w:space="0" w:color="auto"/>'
            '</w:tcBorders>'
            f'<w:shd w:val="clear" w:color="auto" w:fill="{NAVY}"/>'
            '<w:vAlign w:val="center"/></w:tcPr>'
            '<w:p><w:pPr><w:jc w:val="center"/></w:pPr>'
            + runs(spec["titulo"], color="FFFFFF", bold=True, sz="20")
            + "</w:p></w:tc></w:tr>"
        )
    filas.append(
        "<w:tr><w:trPr><w:tblHeader/></w:trPr>"
        + "".join(celda(c, anchos[i], bold=True, jc="center") for i, c in enumerate(cols))
        + "</w:tr>"
    )
    # Una celda con "^" se fusiona verticalmente con la de arriba (columna
    # "Concepto" de las tablas de gastos, que abarca varias filas).
    cuerpo_filas = spec["filas"]
    for f, fila in enumerate(cuerpo_filas):
        celdas = []
        for i, v in enumerate(fila):
            if v == "^":
                celdas.append(celda("", anchos[i], vmerge="cont"))
                continue
            siguiente = cuerpo_filas[f + 1] if f + 1 < len(cuerpo_filas) else None
            merge = ("restart" if siguiente and len(siguiente) > i
                     and siguiente[i] == "^" else None)
            celdas.append(celda(v, anchos[i], vmerge=merge,
                                jc="right" if i == len(cols) - 1 else "left"))
        filas.append("<w:tr>" + "".join(celdas) + "</w:tr>")
    if spec.get("total"):
        t = spec["total"]
        filas.append(
            "<w:tr>"
            + "".join(
                celda("", anchos[i], vmerge="cont") if v == "^" else
                celda(v, anchos[i], bold=True,
                      jc="right" if i == len(cols) - 1 else "left")
                for i, v in enumerate(t)
            )
            + "</w:tr>"
        )

    return ("<w:tbl><w:tblPr>"
            f'<w:tblW w:w="{total_ancho}" w:type="dxa"/>'
            '<w:jc w:val="center"/>'
            '<w:tblCellMar><w:left w:w="70" w:type="dxa"/><w:right w:w="70" w:type="dxa"/></w:tblCellMar>'
            '<w:tblLook w:val="04A0" w:firstRow="1" w:lastRow="0" w:firstColumn="1"'
            ' w:lastColumn="0" w:noHBand="0" w:noVBand="1"/>'
            "</w:tblPr>"
            f"<w:tblGrid>{grid}</w:tblGrid>"
            + "".join(filas) + "</w:tbl>")


# ------------------------------------------------------------------- cuerpo
def construir_cuerpo(spec):
    listas = []  # claves de numeración en orden de aparición
    xml = []

    # Aire superior (las propuestas históricas arrancan bajo el filete del encabezado)
    for _ in range(spec.get("aire_superior", 3)):
        xml.append(parrafo(jc=None))

    xml.append(parrafo(spec["fecha"], jc="right"))
    xml.append(parrafo(jc=None))

    for linea in spec["destinatario"]:
        xml.append(parrafo(linea, jc=None, color=NEGRO, bold=True))
    xml.append(parrafo(jc=None))

    xml.append(parrafo("Propuesta de Honorarios", jc="center",
                       color=AZUL_TITULO, bold=True))

    xml.append(parrafo(spec["saludo"], style="NormalWeb"))
    xml.append(parrafo(spec["intro"], style="NormalWeb"))

    def nueva_lista(tipo):
        listas.append(tipo)
        return len(listas) + 1  # numId 1 está reservado para las secciones

    for sec in spec["secciones"]:
        xml.append(parrafo(sec["titulo"], style="NormalWeb", num=NUM_SECCIONES,
                           color=AZUL_SECCION, bold=True))
        for bloque in sec.get("bloques", []):
            if "p" in bloque:
                xml.append(parrafo(bloque["p"], style="NormalWeb"))
            elif "texto" in bloque:  # párrafo suelto sin espaciado web
                xml.append(parrafo(bloque["texto"], spacing=LINEA_276))
            elif "lista" in bloque:
                n = nueva_lista(bloque.get("tipo", "letra"))
                for item in bloque["lista"]:
                    if isinstance(item, dict):  # ítem con sublista
                        xml.append(parrafo(item["item"], style="ListParagraph",
                                           num=n, spacing=LINEA_276))
                        n2 = nueva_lista(item.get("tipo", "letra"))
                        for sub in item.get("sub", []):
                            xml.append(parrafo(sub, style="ListParagraph",
                                               num=n2, ilvl=0, spacing=LINEA_276,
                                               ind='<w:ind w:left="1440" w:hanging="360"/>'))
                    else:
                        xml.append(parrafo(item, style="ListParagraph", num=n,
                                           spacing=LINEA_276))
            elif "tabla" in bloque:
                xml.append(tabla_xml(bloque["tabla"]))
                xml.append(parrafo(jc=None))

    xml.append(parrafo(
        "-------------------------------------O-------------------------------------",
        style="NormalWeb", jc="center"))
    xml.append(parrafo(spec.get(
        "cierre",
        "Quedo a su disposición para cualquier duda o comentario relacionado a lo anterior."),
        jc=None))
    xml.append(parrafo(jc=None))
    xml.append(parrafo("Atentamente,", jc=None))
    xml.append(parrafo(spec.get("firma", "José Roberto Castañeda Arriola"), jc=None))
    if spec.get("telefono"):
        xml.append(parrafo(spec["telefono"], jc=None))

    return "".join(xml), listas


# --------------------------------------------------------------------- main
def generar(spec, salida):
    plantilla = os.path.join(
        ASSETS, f"plantilla-{spec.get('plantilla', 'membrete')}.docx")
    if not os.path.exists(plantilla):
        sys.exit(f"No existe la plantilla: {plantilla}")

    cuerpo, listas = construir_cuerpo(spec)

    with tempfile.TemporaryDirectory() as tmp:
        with zipfile.ZipFile(plantilla) as z:
            z.extractall(tmp)
        doc = os.path.join(tmp, "word", "document.xml")
        x = open(doc, encoding="utf-8").read()
        if "<!--CUERPO-->" not in x:
            sys.exit("La plantilla no tiene el marcador <!--CUERPO-->")
        open(doc, "w", encoding="utf-8").write(x.replace("<!--CUERPO-->", cuerpo))
        open(os.path.join(tmp, "word", "numbering.xml"), "w",
             encoding="utf-8").write(numbering_xml(listas))

        salida = os.path.abspath(salida)
        os.makedirs(os.path.dirname(salida), exist_ok=True)
        if os.path.exists(salida):
            os.remove(salida)
        subprocess.run(["zip", "-Xrq", salida, "."], cwd=tmp, check=True)
    return salida


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    with open(sys.argv[1], encoding="utf-8") as f:
        spec = json.load(f)
    print(generar(spec, sys.argv[2]))
