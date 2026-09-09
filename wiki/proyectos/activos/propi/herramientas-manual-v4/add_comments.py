# add_comments.py — agrega comentarios de Word (autor JR) anclados a párrafos por texto
import datetime, re, unicodedata
from lxml import etree
W="http://schemas.openxmlformats.org/wordprocessingml/2006/main"; q=lambda t:"{%s}%s"%(W,t)
AUTHOR="José Roberto Castañeda"; INI="JRC"
DATE=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
def norm(s): return re.sub(r"\s+"," ",unicodedata.normalize("NFC",s or ""))
COMMENTS=[
 ("Propi no difiere la verificación de la información del cliente",
  ["Art. 22, diferimiento de la verificación — decisión del 8-sep-2026 (JR).",
   "La ley permite, en casos determinados y justificados, completar la verificación hasta 3 meses después de iniciada la relación, siempre que los supuestos consten en el Manual.",
   "Opción 1 (ADOPTADA): no diferir. La reserva no se habilita ni se entrega el número de cuenta hasta el dictamen del Oficial de Cumplimiento. Es lo acordado con Ena y Thelma el 26-27 de agosto; es más estricto que la ley y por tanto cumple. Ventajas: es lo que Propi ya opera, no crea un carril que nadie administra y evita justificar caso por caso ante la IVE.",
   "Opción 2 (DESCARTADA): permitir el diferimiento en cuatro supuestos tasados: i) persona individual nacional de riesgo bajo o medio con comprobante de domicilio o RTU pendiente; ii) persona jurídica con patente o nombramiento en trámite de inscripción; iii) beneficiario final extranjero con certificación o apostilla en gestión; iv) referencias pendientes. Siempre antes de la promesa de compraventa, nunca con PEP, riesgo alto o transacción inusual, y autorizado por el OC en el expediente.",
   "Si Ena prefiere la opción 2 para no perder reservas por papeleo menor, hay que reincorporar esos supuestos en este párrafo y ajustar el flujo comercial (PC-21)."]),
]
doc=etree.parse("unpacked/word/document.xml"); root=doc.getroot()
ct=etree.parse("unpacked/word/comments.xml"); croot=ct.getroot()
nid=100
for needle, paras in COMMENTS:
    p=next(p for p in root.iter(q("p")) if norm(needle) in norm("".join(t.text or "" for t in p.iter(q("t")))))
    cid=str(nid); nid+=1
    c=etree.SubElement(croot,q("comment")); c.set(q("id"),cid); c.set(q("author"),AUTHOR); c.set(q("date"),DATE); c.set(q("initials"),INI)
    for i,txt in enumerate(paras):
        cp=etree.SubElement(c,q("p"))
        if i==0:
            r=etree.SubElement(cp,q("r")); etree.SubElement(r,q("annotationRef"))
        r=etree.SubElement(cp,q("r")); t=etree.SubElement(r,q("t")); t.text=txt; t.set("{http://www.w3.org/XML/1998/namespace}space","preserve")
    idx=1 if (len(p) and p[0].tag==q("pPr")) else 0
    s=etree.Element(q("commentRangeStart")); s.set(q("id"),cid); p.insert(idx,s)
    e=etree.SubElement(p,q("commentRangeEnd")); e.set(q("id"),cid)
    r=etree.SubElement(p,q("r")); ref=etree.SubElement(r,q("commentReference")); ref.set(q("id"),cid)
    print("comentario", cid, "anclado en:", needle[:50])
doc.write("unpacked/word/document.xml",xml_declaration=True,encoding="UTF-8",standalone=True)
ct.write("unpacked/word/comments.xml",xml_declaration=True,encoding="UTF-8",standalone=True)
