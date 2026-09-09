# redline.py — motor de control de cambios (w:ins / w:del) sobre word/document.xml usando lxml
import copy, datetime, re, unicodedata
from lxml import etree

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
XMLNS = "{http://www.w3.org/XML/1998/namespace}space"
def q(t): return "{%s}%s" % (W, t)
def norm(s):
    """NFC + espacios duros→normales + colapsa espacios múltiples (búsqueda robusta)."""
    s = unicodedata.normalize("NFC", s or "").replace(" ", " ").replace(" ", " ").replace(" ", " ")
    return re.sub(r"[ \t]+", " ", s)

class Redline:
    def __init__(self, path, author, start_id=9000):
        self.path = path; self.author = author; self._id = start_id
        self.tree = etree.parse(path); self.root = self.tree.getroot()
        self.body = self.root.find(q("body"))
        if self.body is None: self.body = self.root  # encabezados / pies / notas
        self.date = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        self.log = []
        self._toc = self._toc_paras()

    def _toc_paras(self):
        """Párrafos dentro de campos TOC (índice / índice de tablas): se excluyen de las búsquedas."""
        out, depth, start = [], 0, None
        for p in self.body.iter(q("p")):
            instr = "".join(x.text or "" for x in p.iter(q("instrText")))
            for fc in p.iter(q("fldChar")):
                t = fc.get(q("fldCharType"))
                if t == "begin": depth += 1
                if t == "end": depth -= 1
            if start is None and "TOC" in instr: start = True
            if start is not None:
                out.append(p)
                if depth == 0: start = None
        return out
    def _in_toc(self, p): return any(p is x for x in self._toc)

    # ---------- utilidades ----------
    def _nid(self): self._id += 1; return str(self._id)
    def _mark(self, el):
        el.set(q("id"), self._nid()); el.set(q("author"), self.author); el.set(q("date"), self.date)
    @staticmethod
    def ptext(p): return "".join(t.text or "" for t in p.iter(q("t")))
    def paras(self): return list(self.body.iter(q("p")))
    def find(self, needle, nth=0, exact=False):
        nd = norm(needle).strip()
        hits = [p for p in self.paras() if not self._in_toc(p) and ((norm(self.ptext(p)).strip() == nd) if exact else (nd in norm(self.ptext(p))))]
        if not hits: raise KeyError("PÁRRAFO NO ENCONTRADO: " + needle[:80])
        if nth >= len(hits): raise KeyError("nth fuera de rango para: " + needle[:60])
        return hits[nth]
    def count(self, needle):
        nd = norm(needle); return sum(1 for p in self.paras() if not self._in_toc(p) and nd in norm(self.ptext(p)))
    def _first_rpr(self, p):
        for r in p.iter(q("r")):
            rp = r.find(q("rPr"))
            if rp is not None: return copy.deepcopy(rp)
        return None
    def _mk_run(self, text, rpr, deleted=False):
        r = etree.Element(q("r"))
        if rpr is not None: r.append(copy.deepcopy(rpr))
        t = etree.SubElement(r, q("delText") if deleted else q("t")); t.text = text; t.set(XMLNS, "preserve")
        return r
    def _runs(self, p): return [r for r in p if r.tag == q("r")]

    # ---------- primitivas ----------
    def _del_all_runs(self, p):
        runs = self._runs(p)
        if runs:
            d = etree.Element(q("del")); self._mark(d)
            p.insert(list(p).index(runs[0]), d)
            for r in runs:
                p.remove(r)
                for t in r.iter(q("t")): t.tag = q("delText")
                for t in r.iter(q("instrText")): t.tag = q("delInstrText")
                d.append(r)
        # runs anidados (hyperlink, smartTag, sdt, fldSimple...) que no son hijos directos
        for r in list(p.iter(q("r"))):
            par = r.getparent()
            if par is None or par is p or par.tag in (q("del"), q("ins")): continue
            d2 = etree.Element(q("del")); self._mark(d2)
            par.insert(list(par).index(r), d2); par.remove(r)
            for t in r.iter(q("t")): t.tag = q("delText")
            for t in r.iter(q("instrText")): t.tag = q("delInstrText")
            d2.append(r)
    CONTAINERS = None
    def _tolerant_pattern(self, s):
        out = []
        for ch in s:
            if ch in "    \t": out.append(r"[\s   ]+")
            else:
                nfd = unicodedata.normalize("NFD", ch); nfc = unicodedata.normalize("NFC", ch)
                out.append("(?:%s|%s)" % (re.escape(nfc), re.escape(nfd)) if nfd != nfc else re.escape(ch))
        return "".join(out)
    def _ins_run(self, p, text, rpr):
        ins = etree.Element(q("ins")); self._mark(ins); ins.append(self._mk_run(text, rpr)); p.append(ins); return ins
    def _mark_para_inserted(self, p):
        ppr = p.find(q("pPr"))
        if ppr is None: ppr = etree.Element(q("pPr")); p.insert(0, ppr)
        rpr = ppr.find(q("rPr"))
        if rpr is None: rpr = etree.SubElement(ppr, q("rPr"))
        m = etree.Element(q("ins")); self._mark(m); rpr.insert(0, m)
    def _mark_para_deleted(self, p):
        ppr = p.find(q("pPr"))
        if ppr is None: ppr = etree.Element(q("pPr")); p.insert(0, ppr)
        rpr = ppr.find(q("rPr"))
        if rpr is None: rpr = etree.SubElement(ppr, q("rPr"))
        m = etree.Element(q("del")); self._mark(m); rpr.insert(0, m)

    # ---------- API ----------
    def replace(self, needle, new_text, nth=0, exact=False):
        """Sustituye TODO el texto del párrafo (del + ins)."""
        p = self.find(needle, nth, exact); rpr = self._first_rpr(p)
        self._del_all_runs(p); self._ins_run(p, new_text, rpr)
        self.log.append(("replace", needle[:50])); return p

    def replace_in(self, needle, old, new, nth=0):
        """Sustituye un fragmento dentro del párrafo: [antes] del(old) ins(new) [después]."""
        p = self.find(needle, nth); full = self.ptext(p); rpr = self._first_rpr(p)
        if p.find(q("ins")) is not None or p.find(q("del")) is not None:
            raise ValueError("replace_in sobre párrafo ya editado (usar una sola llamada o replace_token): " + needle[:50])
        m = re.search(self._tolerant_pattern(old), full)
        if not m: raise KeyError("FRAGMENTO NO ENCONTRADO: %r en %r" % (old[:40], needle[:40]))
        before, matched, after = full[:m.start()], full[m.start():m.end()], full[m.end():]
        for ch in list(p):
            if ch.tag in (q("r"), q("hyperlink"), q("smartTag"), q("fldSimple"), q("sdt")): p.remove(ch)
        if before: p.append(self._mk_run(before, rpr))
        d = etree.SubElement(p, q("del")); self._mark(d); d.append(self._mk_run(matched, rpr, deleted=True))
        ins = etree.SubElement(p, q("ins")); self._mark(ins); ins.append(self._mk_run(new, rpr))
        if after: p.append(self._mk_run(after, rpr))
        self.log.append(("replace_in", old[:40])); return p

    def delete_para(self, needle, nth=0, exact=False):
        p = self.find(needle, nth, exact); self._del_all_runs(p); self._mark_para_deleted(p)
        self.log.append(("delete", needle[:50])); return p

    def delete_range(self, first_needle, last_needle):
        """Elimina (tachado) todos los párrafos desde first hasta last inclusive."""
        ps = self.paras(); a = self.find(first_needle); b = self.find(last_needle)
        ia, ib = ps.index(a), ps.index(b)
        if ib < ia: raise ValueError("rango invertido")
        for p in ps[ia:ib+1]:
            self._del_all_runs(p); self._mark_para_deleted(p)
        self.log.append(("delete_range", first_needle[:30], last_needle[:30])); return ps[ia:ib+1]

    def _new_para_like(self, src, text, rpr=None):
        np = etree.Element(q("p"))
        ppr = src.find(q("pPr"))
        if ppr is not None:
            c = copy.deepcopy(ppr)
            # limpiar marcas previas de párrafo
            for x in c.findall(q("rPr")):
                for m in list(x):
                    if m.tag in (q("ins"), q("del")): x.remove(m)
            np.append(c)
        self._mark_para_inserted(np)
        self._ins_run(np, text, rpr if rpr is not None else self._first_rpr(src))
        return np

    def insert_after(self, needle, texts, nth=0, exact=False, style_from=None):
        """Inserta uno o varios párrafos nuevos después del párrafo ancla (formato copiado del ancla o de style_from)."""
        if isinstance(texts, str): texts = [texts]
        anchor = self.find(needle, nth, exact)
        src = self.find(style_from) if isinstance(style_from, str) else (style_from if style_from is not None else anchor)
        last = anchor
        for t in texts:
            np = self._new_para_like(src, t); last.addnext(np); last = np
        self.log.append(("insert_after", needle[:40], len(texts))); return last

    def insert_before(self, needle, texts, nth=0, exact=False, style_from=None):
        if isinstance(texts, str): texts = [texts]
        anchor = self.find(needle, nth, exact)
        src = self.find(style_from) if isinstance(style_from, str) else (style_from if style_from is not None else anchor)
        for t in texts:
            np = self._new_para_like(src, t); anchor.addprevious(np)
        self.log.append(("insert_before", needle[:40], len(texts))); return anchor

    def insert_row_after(self, needle, cells):
        """Duplica la fila de tabla que contiene `needle` y la rellena con `cells` (marcada como insertada)."""
        p = self.find(needle); tr = p
        while tr is not None and tr.tag != q("tr"): tr = tr.getparent()
        if tr is None: raise KeyError("no es fila de tabla: " + needle[:40])
        new = copy.deepcopy(tr)
        trpr = new.find(q("trPr"))
        if trpr is None:
            trpr = etree.Element(q("trPr")); ex = new.find(q("tblPrEx"))
            new.insert(list(new).index(ex) + 1 if ex is not None else 0, trpr)
        m = etree.Element(q("ins")); self._mark(m); trpr.append(m)
        tcs = [tc for tc in new if tc.tag == q("tc")]
        for tc, txt in zip(tcs, cells):
            ps = [x for x in tc if x.tag == q("p")]
            first = ps[0]; rpr = self._first_rpr(first)
            for x in ps[1:]: tc.remove(x)
            for r in self._runs(first): first.remove(r)
            for child in list(first):
                if child.tag in (q("ins"), q("del")): first.remove(child)
            self._mark_para_inserted(first); self._ins_run(first, txt, rpr)
        tr.addnext(new); self.log.append(("insert_row", needle[:40])); return new

    def replace_token(self, old, new):
        """Sustituye `old` por `new` dentro de cada run (conserva el formato del run); omite TOC y cambios ya marcados."""
        n = 0
        for p in self.paras():
            if self._in_toc(p): continue
            for r in list(p.iter(q("r"))):
                if any(a.tag in (q("ins"), q("del")) for a in r.iterancestors()): continue
                kids = [c for c in r if c.tag != q("rPr")]
                hit = next((i for i, c in enumerate(kids) if c.tag == q("t") and old in (c.text or "")), None)
                if hit is None: continue
                text, rpr, parent = kids[hit].text, r.find(q("rPr")), r.getparent()
                idx = list(parent).index(r); parent.remove(r)
                def _wrap(children):
                    rr = etree.Element(q("r"))
                    if rpr is not None: rr.append(copy.deepcopy(rpr))
                    for c in children: rr.append(c)
                    return rr
                if kids[:hit]: parent.insert(idx, _wrap(kids[:hit])); idx += 1
                parts = text.split(old)
                for i, part in enumerate(parts):
                    if part: parent.insert(idx, self._mk_run(part, rpr)); idx += 1
                    if i < len(parts) - 1:
                        d = etree.Element(q("del")); self._mark(d); d.append(self._mk_run(old, rpr, deleted=True)); parent.insert(idx, d); idx += 1
                        ins = etree.Element(q("ins")); self._mark(ins); ins.append(self._mk_run(new, rpr)); parent.insert(idx, ins); idx += 1
                        n += 1
                if kids[hit+1:]: parent.insert(idx, _wrap(kids[hit+1:])); idx += 1
        self.log.append(("replace_token", old, n)); return n

    def save(self, out=None):
        self.tree.write(out or self.path, xml_declaration=True, encoding="UTF-8", standalone=True)
        return len(self.log)
