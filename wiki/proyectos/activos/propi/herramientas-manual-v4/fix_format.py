# fix_format.py — corrige defectos de formato del V4 base aprobado (sin control de cambios; no toca texto)
import copy, sys, unicodedata
from lxml import etree
W="http://schemas.openxmlformats.org/wordprocessingml/2006/main"; q=lambda t:"{%s}%s"%(W,t)
XS="{http://www.w3.org/XML/1998/namespace}space"
tx=lambda e:unicodedata.normalize("NFC","".join(t.text or "" for t in e.iter(q("t"))))
doc=etree.parse("base/word/document.xml"); root=doc.getroot(); body=root.find(q("body"))
log=[]
# 1) tablas vacías
for t in [t for t in body.findall(q("tbl")) if not t.findall(q("tr"))]:
    body.remove(t); log.append("tabla vacía eliminada")
# 2) hoja en blanco: [salto][''][sdt vacío][salto] antes del título
kids=list(body)
ti=next(i for i,e in enumerate(kids) if e.tag==q("p") and tx(e).strip()=="MANUAL DE PREVENCIÓN LD/FT/FPADM")
isbreak=lambda e:e.tag==q("p") and any(b.get(q("type"))=="page" for b in e.iter(q("br")))
brk=[i for i in range(ti-1,ti-8,-1) if isbreak(kids[i])]
assert len(brk)>=2, brk
second=brk[0]; first=brk[1]
for e in kids[first+1:second+1]:   # lo que hay entre el primer salto y el segundo, incluido el segundo
    assert not tx(e).strip(), tx(e)[:40]
    body.remove(e); log.append(f"eliminado <{etree.QName(e).localname}> vacío antes del título")
# 3) negrita
FIX={ # prefijo del párrafo -> prefijo que debe quedar en negrita ("" = nada)
 "Propi adopta el siguiente manual":"Propi",
 "Financiamiento de la Proliferación de Armas de Destrucción Masiva (FPADM):":"Financiamiento de la Proliferación de Armas de Destrucción Masiva (FPADM):",
 "Financiamiento del Terrorismo (FT):":"",
 "Propi en cumplimiento a lo establecido":"Propi",
 "Propi establece que el cumplimiento de las medidas":"Propi",
 "La debida diligencia simplificada se aplicará":"",
 "En el proceso de vinculación y previo a establecer":"",
 "La verificación en listas descrita":"",
 "Propi establece como mecanismo de identificación":"Propi",
 "Personas Expuestas Políticamente Nacionales:":"Personas Expuestas Políticamente Nacionales:",
 "Personas Expuestas Políticamente Extranjeras:":"Personas Expuestas Políticamente Extranjeras:",
 "Propi verificará y actualizará periódicamente":"Propi",
 "Propi conformará un expediente":"Propi",
 "Los contratos con proveedores de servicios":"",
 "(Manual de Cumplimiento del Sistema Integral":"",
}
def unbold(rpr):
    for tag in ("b","bCs"):
        for e in rpr.findall(q(tag)): rpr.remove(e)
for p in body.iter(q("p")):
    t=tx(p)
    for pre,keep in FIX.items():
        if t.startswith(pre):
            runs=[r for r in p if r.tag==q("r") and tx(r)]
            if not runs: break
            if keep and t.startswith(keep):
                # dividir el primer run: negrita hasta `keep`, normal el resto
                r0=runs[0]; t0=tx(r0)
                if t0.startswith(keep) and len(t0)>len(keep):
                    r_norm=copy.deepcopy(r0)
                    r0.find(q("t")).text=keep; r0.find(q("t")).set(XS,"preserve")
                    r_norm.find(q("t")).text=t0[len(keep):]; r_norm.find(q("t")).set(XS,"preserve")
                    unbold(r_norm.find(q("rPr"))); r0.addnext(r_norm)
                    for r in runs[1:]:
                        if r.find(q("rPr")) is not None: unbold(r.find(q("rPr")))
                else:
                    for r in runs[1:]:
                        if r.find(q("rPr")) is not None: unbold(r.find(q("rPr")))
            else:
                for r in runs:
                    if r.find(q("rPr")) is not None: unbold(r.find(q("rPr")))
            log.append(f"negrita corregida: {t[:45]!r} (queda en negrita: {keep!r})"); break
# 4) glosario: Persona Obligada al nivel 0
for p in body.iter(q("p")):
    if tx(p).startswith("Persona Obligada: persona individual"):
        il=p.find(q("pPr")+"/"+q("numPr")+"/"+q("ilvl")); il.set(q("val"),"0"); log.append("Persona Obligada → nivel 0")
doc.write("base/word/document.xml",xml_declaration=True,encoding="UTF-8",standalone=True)
print("\n".join(log)); print("TOTAL:",len(log))
