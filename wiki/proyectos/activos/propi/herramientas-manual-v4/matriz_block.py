# matriz_block.py — sección XI: matriz de riesgo en el formato V2/V3 (Tablas 3, 4 y 5), en control de cambios
import copy, re
from lxml import etree
from redline import q
W="http://schemas.openxmlformats.org/wordprocessingml/2006/main"; XS="{http://www.w3.org/XML/1998/namespace}space"
tx=lambda e:"".join(t.text or "" for t in e.iter(q("t")))

def clean(el):
    for tag in ("bookmarkStart","bookmarkEnd","lastRenderedPageBreak","proofErr"):
        for x in list(el.iter(q(tag))): x.getparent().remove(x)
    for a in list(el.attrib):
        if "rsid" in a or "paraId" in a or "textId" in a: del el.attrib[a]
    for x in el.iter():
        for a in list(x.attrib):
            if "rsid" in a or "paraId" in a or "textId" in a: del x.attrib[a]
    return el

def set_cell_text(tc, text):
    ps=[p for p in tc if p.tag==q("p")]
    for p in ps[1:]: tc.remove(p)
    p=ps[0]; runs=[r for r in p if r.tag==q("r")]
    for r in runs[1:]: p.remove(r)
    r=runs[0]
    for t in list(r):
        if t.tag!=q("rPr"): r.remove(t)
    t=etree.SubElement(r,q("t")); t.text=text; t.set(XS,"preserve")

FILL={}  # código -> color
for code in ["5A","5B","5C","4A","4B","4C"]: FILL[code]="FF0000"
for code in ["5D","5E","4D","4E","3A","3B","3C","3D","2A","2B","2C"]: FILL[code]="FFFF00"
for code in ["3E","2D","2E","1A","1B","1C","1D","1E"]: FILL[code]="00B050"
FREQ={"FF0000":"Mensual","FFFF00":"Trimestral","00B050":"Semestral"}

ROWS=[  # (Área, Riesgo, Prob, Cons, Medidas de control)  — orden: probabilidad ascendente, consecuencia A→E
 ("1 y 2","Inversiones en proyectos inmobiliarios por consorcios anónimos o estructuras jurídicas que dificulten identificar al beneficiario final","2","A","Identificación y verificación del beneficiario final conforme a su política; debida diligencia intensificada."),
 ("1","Alquiler de propiedades para actividades ilícitas","2","A","Conocimiento del cliente e inquilino, verificación en listas y monitoreo de la relación."),
 ("2","Compra de propiedades por organizaciones sin fines de lucro o que reciban fondos del Estado o del extranjero","3","A","Debida diligencia intensificada; verificación del origen de los fondos."),
 ("1, 2 y 3","Cobro de comisiones de Propi desde cuentas de terceros distintos de la desarrolladora contratante, en efectivo o sin factura","3","B","Facturación vinculada al contrato; pago únicamente por transferencia desde la cuenta de la desarrolladora contratante; alerta al Oficial de Cumplimiento ante cualquier tercero."),
 ("2","Suplantación de identidad o identidades falsas en la vinculación digital sin presencia física del cliente","3","C","Validación de teléfono y correo en el CRM; verificación de identidad contra documento oficial y fuentes independientes antes de la reserva."),
 ("2","Vinculación de una Persona Expuesta Políticamente o persona vinculada sin activar las medidas adicionales","3","C","Pregunta filtro en el perfilamiento; declaración jurada de PEP; cruce en listas de PEP del cliente y del beneficiario final; autorización del Oficial de Cumplimiento con acta."),
 ("2","Compra y venta repetida de propiedades (flipping)","3","C","Monitoreo de transacciones repetidas; examen de transacciones inusuales."),
 ("2","Uso de sociedades anónimas o estructuras jurídicas para la compra de propiedades","3","C","Conocimiento del cliente y verificación del beneficiario final; documentos constitutivos y de representación vigentes."),
 ("2","Reservas y desistimientos reiterados para obtener reembolsos (estructuración mediante desistimientos)","3","C","Alerta automática cuando un mismo cliente registre más de dos reservas canceladas en el año; examen del Oficial de Cumplimiento; reembolsos únicamente a la cuenta de origen."),
 ("2","Compra por clientes de jurisdicciones de alto riesgo según el GAFI, con fondos provenientes de ellas o de zonas identificadas como de alto riesgo en las evaluaciones nacionales o sectoriales de la IVE","4","A","Debida diligencia intensificada (artículo 24); verificación del origen de los fondos."),
 ("2 y 3","Recepción excepcional de fondos de clientes para su traslado a la desarrolladora (clientes en el extranjero)","4","A","Cumplimiento de las condiciones de la sección VII; cuenta exclusiva; misma moneda; traslado en tres días hábiles; registro del Oficial de Cumplimiento e informe trimestral; suspensión si deja de ser excepcional."),
 ("2","Pago de la reserva en efectivo o desde cuentas de terceros no identificados","4","B","Prohibición de efectivo; el comprobante debe estar a nombre del cliente; sin dictamen favorable del Oficial de Cumplimiento no se habilita la reserva ni se entrega el número de cuenta de la desarrolladora."),
 ("1, 2 y 3","Falsificación o alteración de documentos de identidad, de propiedad o de respaldo del origen de fondos","4","B","Verificación documental contra originales y fuentes independientes; expediente completo y dictamen del Oficial de Cumplimiento antes de la reserva."),
 ("1, 2 y 3","Intermediación de corredores externos o agentes no registrados, sin contrato ni verificación","4","B","Contrato de referidor o agente, verificación en listas, RTU y, cuando corresponda, inscripción ante la IVE antes de que acompañe a un cliente; estándares de la sección VIII."),
 ("1, 2 y 3","Estructuración o fraccionamiento de pagos por debajo de los umbrales de registro y reporte","4","B","Monitoreo de patrones de pago; registro de transacciones en efectivo; examen y, en su caso, RTS."),
 ("2","Expedientes incompletos o formularios de la IVE sin completar o sin firma en la precalificación","4","C","Revisión del expediente completo y dictamen del Oficial de Cumplimiento antes de habilitar la reserva o entregar el número de cuenta; sin dictamen favorable no hay reserva."),
 ("3","Sobrevaloración o subvaloración de propiedades","4","C","Revisión de avalúos y monitoreo de precios de mercado."),
 ("2 y 3","Compra con fondos propios sin financiamiento bancario, o sin justificación del origen de los fondos","5","A","Debida diligencia intensificada: declaraciones de ISR e IVA, estados de cuenta y documentación del origen de los fondos; dictamen del Oficial de Cumplimiento antes de la promesa y de la escrituración."),
 ("2 y 3","Compra de propiedades con fondos ilícitos","5","A","Conocimiento del cliente, monitoreo de transacciones, RTS y capacitación."),
 ("1, 2 y 3","Uso de testaferros o interpósitas personas, incluida la solicitud de escriturar a nombre de un tercero sin relación con el comprador","5","B","Verificación de identidad y de beneficiario final; declaración jurada; abstención y examen para RTS (artículo 27)."),
 ("2","Vinculación con desarrolladoras de reciente constitución, sin inscripción ante la IVE o con inconsistencias legales","5","B","Verificación de constitución, representación, patentes e inscripción ante la IVE antes de promover el proyecto; contrato de Alianza Comercial; sin filtro aprobado no se promueve."),
]

def build(rl, v3_path="document.clean.xml"):
    v3=etree.parse(v3_path).getroot(); body=v3.find(q("body")); kids=list(body)
    tbls=[e for e in kids if e.tag==q("tbl")]
    t3,t4,t5=[clean(copy.deepcopy(t)) for t in (tbls[4],tbls[5],tbls[6])]
    cap={}
    for e in kids:
        if e.tag==q("p") and tx(e).strip().startswith(("Tabla 3 -","Tabla 4 -","Tabla 5 -")): cap[tx(e).strip()[:7]]=e
    def caption(key, text):
        p=clean(copy.deepcopy(cap[key])); runs=[r for r in p if r.tag==q("r")]
        for r in runs[1:]: p.remove(r)
        r=runs[0]
        for x in list(r):
            if x.tag!=q("rPr"): r.remove(x)
        t=etree.SubElement(r,q("t")); t.text=text; t.set(XS,"preserve"); return p
    # --- Tabla 3: correcciones ---
    for t in t3.iter(q("t")):
        if t.text=="Ocacional": t.text="Ocasional"
    r4=t3.findall(q("tr"))[3]; tcs=r4.findall(q("tc"))
    assert tx(tcs[-1]).strip()=="5D", tx(tcs[-1]); tcs[-1].find(q("p")).iter(q("t")).__next__().text="4E"
    for tc in t3.iter(q("tc")):
        if tx(tc).strip()=="4C": tc.find(q("tcPr")+"/"+q("shd")).set(q("fill"),"FF0000")
    # --- Tabla 5: filas nuevas ---
    rows=t5.findall(q("tr")); tpl=copy.deepcopy(rows[2])
    for r in rows[2:]: t5.remove(r)
    for area,riesgo,p,c,ctrl in ROWS:
        code=p+c; fill=FILL[code]; tr=copy.deepcopy(tpl); tcs=tr.findall(q("tc"))
        for i,val in enumerate([area,riesgo,p,c,code,FREQ[fill],ctrl]): set_cell_text(tcs[i],val)
        shd=tcs[4].find(q("tcPr")+"/"+q("shd")); shd.set(q("fill"),fill); shd.set(q("val"),"clear")
        t5.append(tr)
    # --- párrafos nuevos (formato del V3) ---
    src=next(e for e in kids if e.tag==q("p") and tx(e).startswith("Para cada riesgo se han definido"))
    def para_like(text):
        p=clean(copy.deepcopy(src)); runs=[r for r in p if r.tag==q("r")]
        for r in runs[1:]: p.remove(r)
        r=runs[0]
        for x in list(r):
            if x.tag!=q("rPr"): r.remove(x)
        t=etree.SubElement(r,q("t")); t.text=text; t.set(XS,"preserve"); return p
    # ===== ediciones =====
    rl.replace("La matriz de riesgo consolidada de Propi, con sus segmentos",
      "La matriz de riesgo institucional de Propi, que evalúa los riesgos de LD/FT/FPADM por línea de negocio y por fase de su flujo comercial, consta en esta sección con su escala de calificación (probabilidad, consecuencia, nivel de riesgo y frecuencia de monitoreo). Las matrices de riesgo por segmento de contraparte (clientes, fiadores, desarrolladoras, corredores externos, colaboradores y proveedores), que califican a cada contraparte con la misma escala, se desarrollan en las políticas de conocimiento correspondientes y se actualizan conforme a lo previsto en esta sección sin necesidad de modificar este Manual.")
    rl.replace_in("Eventos de riesgo identificados por factor", "constan en la matriz de riesgo consolidada:", "constan en la matriz de riesgo institucional de esta sección y en las matrices por segmento de las políticas de conocimiento:")
    intro=para_like("En la siguiente matriz de riesgos, la probabilidad de que ocurra cada riesgo se clasifica en una escala del 1 al 5, donde 1 indica «extremadamente improbable» y 5 indica «frecuente». Las consecuencias asociadas a cada riesgo se han categorizado de A a E, siendo A «catastrófica» y E «insignificante». El nivel de riesgo resulta de la combinación de ambas y determina la frecuencia mínima de monitoreo.")
    anchor=rl.find("De acuerdo con la colorimetría de la matriz")
    for el in (intro, caption("Tabla 3","Tabla 3 - Matriz de riesgos"), t3):
        rl.mark_inserted(el); anchor.addprevious(el)
    rl.log.append(("insert_before_colorimetria",3))
    rl.insert_elements_after("Verde: al menos semestral", [
        para_like("Para cada riesgo se han definido controles y acciones para mitigar su impacto o reducir su probabilidad. Los riesgos se han evaluado para las líneas de negocio de Propi y para cada fase de su flujo comercial, desde la captación del cliente hasta la escrituración y el cobro de comisiones:"),
        caption("Tabla 4","Tabla 4 - Líneas de negocio"), t4,
        caption("Tabla 5","Tabla 5 - Evaluación de riesgos"), t5], exact=True)
    rl.delete_para("[ESPACIO RESERVADO")
    # consistencia: la matriz institucional está en el Manual; las de segmento, en las políticas
    rl.replace("Aprobar, a propuesta del Oficial de Cumplimiento, las políticas que desarrollan este Manual y la matriz de riesgo consolidada",
      "Aprobar, a propuesta del Oficial de Cumplimiento, las políticas que desarrollan este Manual, incluidas las matrices de riesgo por segmento de contraparte que estas contienen.")
    rl.replace_in("El Oficial de Cumplimiento será responsable de la custodia del documento original", "las políticas y la matriz de riesgo consolidada con su metodología serán aprobadas por el órgano de dirección superior", "las políticas, incluidas las matrices de riesgo por segmento que contienen, serán aprobadas por el órgano de dirección superior")
    rl.replace_in("Los siguientes documentos desarrollan este Manual, son independientes de él", "Las políticas y la matriz de riesgo consolidada con su metodología son aprobadas por el órgano de dirección superior", "Las políticas, incluidas las matrices de riesgo por segmento que contienen, son aprobadas por el órgano de dirección superior")
    rl.replace("6. Matriz de riesgo consolidada y su metodología",
      "6. Matrices de riesgo por segmento de contraparte (clientes, fiadores, desarrolladoras, corredores externos, colaboradores y proveedores), contenidas en las políticas de conocimiento respectivas y calificadas con la escala de la sección XI.")
