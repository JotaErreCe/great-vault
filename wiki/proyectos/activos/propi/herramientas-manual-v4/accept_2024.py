# accept_2024.py — acepta TODOS los cambios rastreados de autores distintos de JR en una parte XML
import sys
from lxml import etree
W="http://schemas.openxmlformats.org/wordprocessingml/2006/main"; q=lambda t:"{%s}%s"%(W,t)
JR="José Roberto Castañeda"
def accept(path):
    t=etree.parse(path); root=t.getroot(); n=0
    others=lambda el: el.get(q("author")) and el.get(q("author"))!=JR
    # 1) inserciones y movimientos destino: se conservan (desenvolver); marcas de párrafo: quitar
    for tag in ("ins","moveTo"):
        for el in list(root.iter(q(tag))):
            if not others(el): continue
            par=el.getparent()
            if etree.QName(par).localname in ("rPr","trPr","tblPrEx"): par.remove(el); n+=1; continue
            idx=par.index(el)
            for ch in list(el): par.insert(idx,ch); idx+=1
            par.remove(el); n+=1
    # 2) eliminaciones y movimientos origen: se descartan
    for tag in ("del","moveFrom"):
        for el in list(root.iter(q(tag))):
            if not others(el): continue
            el.getparent().remove(el); n+=1
    # 3) cambios de formato y marcas de rango
    for tag in ("rPrChange","pPrChange","tblPrChange","tblPrExChange","trPrChange","tcPrChange","sectPrChange","numberingChange","tblGridChange",
                "moveFromRangeStart","moveFromRangeEnd","moveToRangeStart","moveToRangeEnd"):
        for el in list(root.iter(q(tag))):
            if el.get(q("author")) and not others(el): continue
            el.getparent().remove(el); n+=1
    t.write(path,xml_declaration=True,encoding="UTF-8",standalone=True); return n
if __name__=="__main__":
    for p in sys.argv[1:]: print(p, "aceptados:", accept(p))
