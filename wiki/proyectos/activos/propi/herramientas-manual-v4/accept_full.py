# accept_full.py — acepta TODOS los cambios rastreados (cualquier autor) incluidas marcas de párrafo y filas; quita comentarios
import sys, unicodedata
from lxml import etree
W="http://schemas.openxmlformats.org/wordprocessingml/2006/main"; q=lambda t:"{%s}%s"%(W,t)
def accept(path):
    t=etree.parse(path); root=t.getroot(); n=0
    # 1) inserciones / moveTo a nivel run: desenvolver
    for tag in ("ins","moveTo"):
        for el in list(root.iter(q(tag))):
            par=el.getparent()
            if etree.QName(par).localname in ("rPr","trPr","tblPrEx","tcPr"): continue
            idx=par.index(el)
            for ch in list(el): par.insert(idx,ch); idx+=1
            par.remove(el); n+=1
    # 2) eliminaciones / moveFrom a nivel run: quitar
    for tag in ("del","moveFrom"):
        for el in list(root.iter(q(tag))):
            par=el.getparent()
            if etree.QName(par).localname in ("rPr","trPr","tblPrEx","tcPr"): continue
            par.remove(el); n+=1
    # 3) filas: trPr/ins → quitar marca; trPr/del → quitar fila
    for tr in list(root.iter(q("tr"))):
        trpr=tr.find(q("trPr"))
        if trpr is None: continue
        if trpr.find(q("del")) is not None: tr.getparent().remove(tr); n+=1; continue
        for m in trpr.findall(q("ins")): trpr.remove(m); n+=1
    # 4) marcas de párrafo: ins → quitar marca; del → fusionar con el párrafo siguiente
    for p in list(root.iter(q("p"))):
        ppr=p.find(q("pPr")); rpr=ppr.find(q("rPr")) if ppr is not None else None
        if rpr is None: continue
        for m in rpr.findall(q("ins"))+rpr.findall(q("moveTo")): rpr.remove(m); n+=1
    for p in list(root.iter(q("p"))):
        ppr=p.find(q("pPr")); rpr=ppr.find(q("rPr")) if ppr is not None else None
        if rpr is None: continue
        marks=rpr.findall(q("del"))+rpr.findall(q("moveFrom"))
        if not marks: continue
        for m in marks: rpr.remove(m); n+=1
        nxt=p.getnext()
        while nxt is not None and nxt.tag in (q("bookmarkStart"),q("bookmarkEnd"),q("proofErr")): nxt=nxt.getnext()
        content=[c for c in p if c.tag!=q("pPr")]
        if nxt is not None and nxt.tag==q("p"):
            ins_at=1 if (len(nxt) and nxt[0].tag==q("pPr")) else 0
            for c in content: nxt.insert(ins_at,c); ins_at+=1
            p.getparent().remove(p)
        # si no hay párrafo siguiente (fin de celda/cuerpo) se conserva el párrafo sin la marca
    # 5) cambios de formato y marcas de rango
    for tag in ("rPrChange","pPrChange","tblPrChange","tblPrExChange","trPrChange","tcPrChange","sectPrChange","numberingChange","tblGridChange",
                "moveFromRangeStart","moveFromRangeEnd","moveToRangeStart","moveToRangeEnd","cellIns","cellDel","cellMerge"):
        for el in list(root.iter(q(tag))): el.getparent().remove(el); n+=1
    # 6) comentarios
    for tag in ("commentRangeStart","commentRangeEnd"):
        for el in list(root.iter(q(tag))): el.getparent().remove(el); n+=1
    for ref in list(root.iter(q("commentReference"))):
        r=ref.getparent(); r.getparent().remove(r); n+=1
    t.write(path,xml_declaration=True,encoding="UTF-8",standalone=True); return n
if __name__=="__main__":
    for p in sys.argv[1:]: print(p,"aceptados:",accept(p))
