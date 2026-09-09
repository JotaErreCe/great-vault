# apply_edits.py — aplica el guion de cambios (Manual V3 -> V4) con control de cambios
import sys
from lxml import etree
from redline import Redline, q

AUTHOR = "José Roberto Castañeda"
rl = Redline("unpacked/word/document.xml", AUTHOR)
R, RI, D, IA, IB = rl.replace, rl.replace_in, rl.delete_para, rl.insert_after, rl.insert_before

# ---- helpers extra ----
def delete_block(needle, n, exact=False, nth=0):
    """Elimina el párrafo ancla y los n siguientes."""
    ps = rl.paras(); a = rl.find(needle, nth, exact); ia = ps.index(a)
    for p in ps[ia:ia+n+1]:
        rl._del_all_runs(p); rl._mark_para_deleted(p)
def delete_table(needle, nth=0):
    """Marca como eliminada la tabla que contiene `needle` (filas con w:trPr/w:del + runs tachados)."""
    p = rl.find(needle, nth); tbl = p
    while tbl is not None and tbl.tag != q("tbl"): tbl = tbl.getparent()
    if tbl is None: raise KeyError("no es tabla: " + needle)
    for tr in [x for x in tbl if x.tag == q("tr")]:
        trpr = tr.find(q("trPr"))
        if trpr is None:
            trpr = etree.Element(q("trPr")); ex = tr.find(q("tblPrEx"))
            tr.insert(list(tr).index(ex) + 1 if ex is not None else 0, trpr)
        m = etree.Element(q("del")); rl._mark(m); trpr.append(m)
        for pp in tr.iter(q("p")): rl._del_all_runs(pp)
    rl.log.append(("delete_table", needle[:40]))

DEC = "Decreto Número 15-2026 del Congreso de la República, Ley Integral para la Prevención y Represión del Lavado de Dinero u Otros Activos y del Financiamiento del Terrorismo"

# ================= 0. PORTADA / REGISTRO =================
R("MANUAL DE CUMPLIMIENTO DEL SISTEMA INTEGRAL DE PREVENCIÓN DEL LAVADO DE ACTIVOS", "MANUAL DE PREVENCIÓN LD/FT/FPADM")
IA("MANUAL DE PREVENCIÓN LD/FT/FPADM", "(Manual de Cumplimiento del Sistema Integral de Prevención del Lavado de Dinero u Otros Activos, del Financiamiento del Terrorismo y del Financiamiento de la Proliferación de Armas de Destrucción Masiva)", exact=True)
rl.insert_row_after("Creación del documento", ["01", "08-09-2026", "Todo", "Actualización integral al Decreto 15-2026; reestructuración como manual marco con documentos complementarios independientes"])

# ================= TABLA ELABORA / REVISA / APRUEBA (portada) =================
def set_cell(tbl, row, col, text):
    tr = [x for x in tbl if x.tag == q("tr")][row]; tc = [x for x in tr if x.tag == q("tc")][col]
    p = [x for x in tc if x.tag == q("p")][0]; rpr = rl._first_rpr(p)
    rl._del_all_runs(p); rl._ins_run(p, text, rpr)
_p = rl.find("Regional Head of Treasury"); _tbl = _p
while _tbl.tag != q("tbl"): _tbl = _tbl.getparent()
set_cell(_tbl, 1, 1, "José Roberto Castañeda Arriola"); set_cell(_tbl, 1, 2, "Asesor legal externo (AMC Legal)"); set_cell(_tbl, 1, 4, "08-09-2026")
set_cell(_tbl, 2, 4, "Pendiente"); set_cell(_tbl, 3, 4, "Pendiente")

# ================= I. INTRODUCCIÓN =================
R("perteneciendo al grupo “B” de Personas Obligadas",
  "Por consiguiente, Propi Tech, Sociedad Anónima es Persona Obligada de conformidad con el artículo 3, literal c), numeral 1, romano i, del " + DEC + ", por dedicarse a la promoción e intermediación inmobiliaria o compraventa de bienes inmuebles, y se encuentra inscrita ante la Superintendencia de Bancos a través de la Intendencia de Verificación Especial (IVE), conforme al artículo 5 de dicha Ley.")
RI("Propi adopta el siguiente manual con el propósito", "Lavado de Activos y Financiación del Terrorismo y de la Proliferación de Armas de Destrucción Masiva",
   "Lavado de Dinero u Otros Activos, el Financiamiento del Terrorismo y el Financiamiento de la Proliferación de Armas de Destrucción Masiva (LD/FT/FPADM)")
IA("Su finalidad principal consiste en controlar, generar conciencia",
   "El presente Manual es el documento marco del Sistema Integral de Prevención de Propi. Las políticas, procedimientos, reglamentos, códigos y formatos que lo desarrollan son documentos complementarios independientes, se enumeran en el Anexo «Documentos que integran el Sistema de Prevención», se aplican en su versión vigente y en ningún caso pueden contradecir lo dispuesto en este Manual, el cual prevalece.")

# ================= II. OBJETIVOS =================
RI("a) Contribuir al cumplimiento de normas, leyes, regulaciones", "lavado de activos y Financiamiento del Terrorismo", "lavado de dinero u otros activos, del financiamiento del terrorismo y del financiamiento de la proliferación de armas de destrucción masiva (LD/FT/FPADM)")
RI("b) Dar a conocer las responsabilidades de la Sociedad", "lavado de activos y Financiamiento del Terrorismo", "LD/FT/FPADM")
RI("c) Establecer las bases para incorporar los controles", "lavado de activos y Financiamiento del Terrorismo", "LD/FT/FPADM")

# ================= III. ALCANCE =================
R("El presente manual es de observancia obligatoria para todo el personal",
  "El presente Manual es de observancia obligatoria para todo el personal de Propi, sus directores, agentes, corredores externos, intermediarios y demás colaboradores, cualquiera que sea la forma jurídica de su contratación; asimismo, aplica a todas las operaciones relacionadas con los servicios prestados por Propi.")

# ================= IV. NORMATIVA APLICABLE =================
R("Ley Contra el Lavado de Dinero u Otros Activos, Decreto Número 67-2011",
  DEC + " (vigente desde el 17 de septiembre de 2026).")
IA("(vigente desde el 17 de septiembre de 2026).", [
  "El Reglamento de la Ley Integral, una vez emitido conforme a su artículo 127, y las disposiciones administrativas que emita la Superintendencia de Bancos a través de la Intendencia de Verificación Especial (artículo 52, literal e).",
  "Las resoluciones del Consejo de Seguridad de las Naciones Unidas en materia de terrorismo, financiamiento del terrorismo y financiamiento de la proliferación de armas de destrucción masiva (artículo 43).",
  "Las Recomendaciones del Grupo de Acción Financiera Internacional (GAFI), como estándar de referencia.",
  "De conformidad con el artículo 125 del Decreto 15-2026, toda referencia a la Ley Contra el Lavado de Dinero u Otros Activos (Decreto 67-2001) o a la Ley para Prevenir y Reprimir el Financiamiento del Terrorismo (Decreto 58-2005), contenida en documentos internos, formularios o disposiciones, se entenderá hecha a la Ley Integral."])
D("Reglamento de la Ley Contra el Lavado de Dinero y Otros Activos Acuerdo Gubernativo Número 118-2002")
D("Ley para Prevenir y Reprimir el Financiamiento del Terrorismo, Decreto Número 58-2005")
D("Reglamento de la Ley para Prevenir y Reprimir el Financiamiento del Terrorismo, Acuerdo Gubernativo 86-2006")

# ================= V. GLOSARIO =================
rl.delete_range("Actividades y Profesiones no Financieras Designadas", "Creación, operación o administración de personas jurídicas, otras estructuras jurídicas y compra y venta de estas.")
R("Asociados Comerciales: Personas o entidades con las que la PEP",
  "Asociados cercanos: personas naturales que, respecto de una Persona Expuesta Políticamente, figuren como socios, accionistas, representantes legales, directores o apoderados en común con ella en personas jurídicas o estructuras jurídicas, o que sean beneficiarios finales de esas mismas entidades (artículo 2, literal a, del Decreto 15-2026).")
R("Beneficiario final o real: se refiere a la(s) persona(s) natural(es)",
  "Beneficiario final: persona individual que, en última instancia y por cualquier medio o mecanismo, se beneficie de las relaciones de negocios, ejerce el control efectivo, o ambas, de las personas jurídicas o estructuras jurídicas, ya sea por medio de la titularidad del capital o participación en un porcentaje igual o mayor al quince por ciento (≥ 15 %), o por cualquier otro medio, en forma directa o indirecta. La propiedad y el control en última instancia comprenden el control directo o indirecto, solo o conjuntamente, incluso a través de una cadena de propiedad o por medio de la toma de decisiones (artículo 2, literal b).")
R("Cliente: toda persona natural o jurídica que mantiene o ha mantenido",
  "Cliente: persona individual, persona jurídica o estructura jurídica con la cual Propi establece, mantiene o ha mantenido una relación de negocios, a la cual se le proporciona o presta cualquier bien, producto o servicio, de forma habitual u ocasional, derivado de su giro de negocios, independientemente de cómo se le denomine (artículo 2, literal c).")
R("Compañeros de Vida: Personas que conviven",
  "Cónyuge o conviviente: persona unida a la PEP por matrimonio o por unión de hecho, incluida la relación estable de convivencia aunque no esté formalizada.")
R("Oficial de Cumplimiento: Es el funcionario nombrado por el Secretario Junta Directiva Único",
  "Oficial de Cumplimiento: funcionario o ejecutivo de alta gerencia, nombrado por el órgano de dirección superior de Propi junto con su suplente, encargado de vigilar el cumplimiento de los Programas de Prevención LD/FT/FPADM y de las obligaciones que establece el Decreto 15-2026, su reglamentación y demás disposiciones aplicables; es el único enlace entre Propi y la Superintendencia de Bancos a través de la IVE (artículo 16).")
R("Financiamiento del Terrorismo (FD)",
  "Financiamiento del Terrorismo (FT): conducta de quien, por el medio que fuere, directa o indirectamente, proporcione, provea, done, recolecte, transfiera, entregue, adquiera, posea, administre, negocie o gestione fondos, dinero, recursos económicos, activos o cualquier clase de bienes con la intención o a sabiendas de que serán utilizados, en todo o en parte, para el terrorismo, en los términos del artículo 78 del Decreto 15-2026.")
D("Lavado de Activo (LA)s: Proceso en virtud del cual")
R("Lavado de Dinero (LD): El Lavado de Dinero",
  "Lavado de Dinero u Otros Activos (LD): conducta tipificada en el artículo 73 del Decreto 15-2026, consistente en invertir, convertir, transferir, adquirir, poseer, administrar, tener, utilizar, ocultar o impedir la determinación de la verdadera naturaleza u origen de bienes o dinero, sabiendo que son producto, proceden o se originan de la comisión de un delito.")
R("Operaciones Reguladas: Toda operación o transacción de efectivo",
  "Transacciones en efectivo sujetas a registro y reporte: toda transacción en efectivo, única o estructurada, que Propi reciba de sus clientes por un monto igual o mayor a diez mil dólares de los Estados Unidos de América (US$ 10,000.00) o su equivalente en moneda nacional o cualquier otra divisa, que debe registrarse diariamente y reportarse periódicamente a la IVE (artículo 31). Los umbrales aplicables a transacciones por otros medios se rigen por el Procedimiento de Reportes vigente.")
R("Operación Sospechosa o Irregular: Todas las operaciones poco usuales",
  "Transacción inusual: transacción, operación o acto que por su monto, características o frecuencia no se ajusta al perfil de riesgo del cliente, sin una justificación económica o legal razonable (artículo 2, literal n).")
IA("Transacción inusual: transacción, operación o acto", [
  "Transacción sospechosa: transacción inusual, concluida o no, debidamente examinada y documentada por Propi que, tras analizarla y aplicar las medidas de debida diligencia, carece de fundamento económico o legal evidente y respecto de la cual Propi sospecha o tiene motivos razonables para sospechar que los fondos proceden o se destinan a una actividad delictiva o al financiamiento del terrorismo (artículo 2, literal o).",
  "Sospecha: apreciación razonada y documentada, basada en indicios objetivos o verificables, que genere motivos razonables para considerar una posible vinculación de una transacción con el LD/FT, sin que sea necesaria la certeza técnica o la prueba plena de la comisión de un ilícito (artículo 2, literal l).",
  "Transacción: toda operación financiera o comercial que implique la transferencia, adquisición, depósito, retiro, intercambio o administración de fondos, bienes, valores u otros activos, realizada por un cliente o por un tercero en su nombre, a través de Propi, siempre que genere un registro verificable, implique la movilización o disposición de activos y corresponda a los servicios regulados que presta (artículo 2, literal m)."])
R("Individuos que actualmente ocupan o hayan ocupado un cargo público relevante",
  "Persona individual que desempeña o haya desempeñado cargos públicos prominentes en Guatemala o en otro país, o a quien se le ha confiado una función prominente en una organización internacional. Los cargos públicos prominentes son los que establezca la Superintendencia de Bancos mediante la resolución anual prevista en el artículo 2, literal g), del Decreto 15-2026.")
R("Continuarán siendo sujetos de la debida diligencia ampliada aquellas personas catalogadas como PEP nacionales por un periodo igual al ejercicio de sus funciones.",
  "La condición de PEP se adquiere desde la toma legal de posesión del cargo y se mantiene durante un (1) año posterior al cese de las funciones, vencido el cual la persona deja de ser considerada PEP sin necesidad de trámite alguno. La condición de PEP es de carácter preventivo y no limita por sí sola el acceso a los servicios de Propi.", exact=True)
R("Persona Relacionada: Individuos que tienen un vínculo cercano",
  "Personas vinculadas a una PEP: para efectos de las medidas de debida diligencia adicionales del artículo 25, literal a), del Decreto 15-2026, son los parientes de la PEP dentro del primer grado de consanguinidad, su cónyuge o conviviente y sus asociados cercanos, incluidas las personas jurídicas o estructuras jurídicas en las que estos sean beneficiarios finales.")
R("Intendencia de Verificación Especial: Oficina primaria adscrita",
  "Intendencia de Verificación Especial (IVE): intendencia que forma parte de la estructura orgánica de la Superintendencia de Bancos, encargada de la recepción y análisis de información y, cuando proceda, de la difusión de inteligencia financiera a las autoridades competentes, así como de la supervisión de las Personas Obligadas en materia LD/FT; ejerce sus funciones en el ámbito estrictamente administrativo (artículos 51 y 52 del Decreto 15-2026). La persecución penal corresponde al Ministerio Público.")
IA("Intendencia de Verificación Especial (IVE): intendencia que forma parte", [
  "Persona Obligada: persona individual o jurídica comprendida en el artículo 3 del Decreto 15-2026. Propi lo es en virtud de la literal c), numeral 1, romano i, de dicho artículo.",
  "Estructura jurídica: forma de integración o asociación de personas jurídicas o individuales constituida conforme a las leyes de Guatemala o de otra jurisdicción, sin importar su naturaleza, incluidos los fideicomisos y fundaciones, y aquellas que no hayan sido formalizadas como personas jurídicas (artículo 2, literal f).",
  "Relación de negocios: cualquier relación contractual, profesional, comercial o de servicios entre Propi y el cliente (artículo 2, literal j). Para Propi se inicia con la reserva del inmueble o con la firma del contrato de Alianza Comercial, según corresponda, y se entiende finalizada con el pago de la última comisión a la Sociedad.",
  "Debida diligencia del cliente (DDC): proceso de análisis conforme a las normas, políticas, procedimientos y controles de Propi que permite identificar, conocer y verificar la identidad de los clientes, de quienes actúan en su nombre y de sus beneficiarios finales, el propósito de la relación de negocios y las transacciones que realicen (artículo 2, literal e).",
  "Riesgo LD/FT/FPADM: contingencia de pérdida, daño u otra consecuencia adversa a que está expuesta Propi de ser utilizada, directa o indirectamente, para actividades de lavado de dinero u otros activos, financiamiento del terrorismo o financiamiento de la proliferación de armas de destrucción masiva (artículo 2, literal k).",
  "Reporte de Transacción Sospechosa (RTS): reporte que Propi, a través de su Oficial de Cumplimiento, remite con prontitud, de forma exclusiva y confidencial, a la Superintendencia de Bancos a través de la IVE respecto de toda transacción sospechosa (artículo 30).",
  "Contratista y Proveedor del Estado: personas individuales o jurídicas que suscriben contratos bajo cualquier modalidad de adquisición pública o que se encuentran inscritas y precalificadas en el Registro General de Adquisiciones del Estado (artículo 2, literales d y h); dan lugar a medidas de debida diligencia adicionales (artículo 25, literal b)."])

# ================= VI. ESTRUCTURA ORGANIZATIVA =================
R("a) Conocer las disposiciones que establece la Ley contra el Lavado de Dinero y de Activos",
  "a) Conocer las disposiciones del " + DEC + ", su reglamentación y las disposiciones que emita la Superintendencia de Bancos a través de la IVE, las cuales forman parte integrante de este Manual.")
R("c) Anteponer el cumplimiento de las normas en materia de prevención del LDA/FT/FPADM, al logro de las metas comerciales",
  "c) Anteponer el cumplimiento de las normas en materia de prevención del LD/FT/FPADM al logro de las metas comerciales y asegurar que las operaciones se lleven a cabo de manera responsable y segura.")
IA("c) Anteponer el cumplimiento de las normas en materia de prevención del LD/FT/FPADM al logro",
   "d) Actuar bajo los principios y normas establecidos en el Código de Ética de Propi y cumplir las obligaciones del Reglamento Interno de Trabajo en materia de prevención del LD/FT/FPADM.")
R("1. Asamblea de Accionistas", "1. Órgano de dirección superior", exact=True)
R("Adicionalmente a las responsabilidades generales antes citadas, le corresponde:",
  "Al órgano de dirección superior de Propi, o a quien haga sus veces, además de las responsabilidades generales antes citadas, le corresponde:", exact=True)
R("Aprobar el Manual de Cumplimiento y sus modificaciones.",
  "Aprobar el presente Manual y sus modificaciones y actualizaciones (artículo 12 del Decreto 15-2026), así como el proceso de administración del Riesgo LD/FT/FPADM y sus actualizaciones (artículo 8).", exact=True)
IA("Comunicar a la IVE y a los organismos de fiscalización, supervisión o vigilancia respectivos", [
  "Autorizar por escrito, o delegar en el nivel gerencial o comité que designe, el establecimiento o continuidad de relaciones de negocios con clientes calificados como Personas Expuestas Políticamente o de riesgo alto, previo dictamen del Oficial de Cumplimiento.",
  "Garantizar al Oficial de Cumplimiento independencia, autonomía y suficientes recursos materiales, tecnológicos y personal idóneo para el cumplimiento de sus funciones (artículo 16)."])
R("Además, el Oficial de Cumplimiento no se dedicarán exclusivamente a las funciones como tales",
  "El Oficial de Cumplimiento titular y su suplente serán nombrados por el órgano de dirección superior o quien haga sus veces (artículo 16 del Decreto 15-2026). El Oficial de Cumplimiento podrá ejercer otras funciones dentro de la entidad y ostentará un cargo de alta gerencia o de similar naturaleza. Las calidades, atribuciones mínimas y condiciones de ejercicio del titular y del suplente, así como la forma y plazo para informar a la IVE su designación, renuncia, remoción o sustitución, se sujetan a la reglamentación de la Ley.")
R("Principalmente, el Oficial de Cumplimiento será el Responsable de supervisar el cumplimiento de programas, normas, procedimientos y controles internos, y de ejercer las atribuciones establecidas en el artículo 21 del Reglamento",
  "Principalmente, el Oficial de Cumplimiento será el responsable de vigilar el cumplimiento de los Programas de Prevención LD/FT/FPADM contenidos en este Manual y en sus documentos complementarios, así como de las obligaciones que establece el Decreto 15-2026, su reglamentación y demás disposiciones aplicables; y será el único enlace entre Propi y la Superintendencia de Bancos a través de la IVE (artículo 16).", nth=0)
R("Validar que el envío de los reportes de operaciones reguladas a la Super Intendencia de Bancos",
  "Validar que los reportes de transacciones en efectivo y los demás reportes que requiera la IVE sean presentados a la Superintendencia de Bancos a través de los mecanismos establecidos por la Intendencia de Verificación Especial.", nth=0)
R("Realizar análisis de las transacciones u operaciones para determinar si procede o no elaborar un reporte de operación sospechosa.",
  "Realizar el examen de las transacciones inusuales para determinar si procede o no elaborar un Reporte de Transacción Sospechosa (RTS).", nth=0, exact=True)
R("Dar respuesta oportuna a los oficios de información requerida por la Super Intendencia de Bancos",
  "Dar respuesta oportuna a los requerimientos de información de la Superintendencia de Bancos a través de la IVE, llevando archivo de estos con la debida confidencialidad.", nth=0)
RI("La función del Oficial de Cumplimiento será ejercida por una persona que resida en el país",
   "sin perjuicio de lo dispuesto en el Art. 21 de la Ley Contra el Lavado de Dinero y de Activos.", "sin perjuicio de lo dispuesto en el artículo 16 del Decreto 15-2026.")
# bloque duplicado de responsabilidades (segunda aparición): encabezado + 10 párrafos
delete_block("Responsabilidades del Oficial de Cumplimiento", 10, exact=True)
R("Además de las atribuciones establecidas en el artículo 22 de Reglamento",
  "Además de las atribuciones que establezca la reglamentación del Decreto 15-2026, el Oficial de Cumplimiento deberá desarrollar las siguientes:")
RI("Organizar la capacitación del personal en los aspectos relacionados con la prevención",
   "y remitir a la Superintendencia de Bancos, a través de la Intendencia, un reporte semestral sobre dicha capacitación",
   "y remitir a la Superintendencia de Bancos, a través de la IVE, la información sobre dicha capacitación cuando esta lo requiera")
R("Otras funciones que la Asamblea de Accionistas defina.", "Otras funciones que el órgano de dirección superior defina.", exact=True)
IA("Otras funciones que el órgano de dirección superior defina.", [
  "La identidad y la información personal del Oficial de Cumplimiento y de quienes laboren bajo su dirección tienen carácter confidencial y no podrán hacerse del conocimiento público, salvo ante la Superintendencia de Bancos a través de la IVE o por orden de juez competente (artículo 19 del Decreto 15-2026).",
  "El Oficial de Cumplimiento y las personas que laboren bajo su dirección tienen impedimento para declarar, intervenir o desempeñarse como testigos, peritos, expertos o consultores técnicos en procesos penales o de extinción de dominio relacionados con la información, documentación, expedientes y registros a los que hayan tenido acceso en el ejercicio de sus funciones y con los RTS comunicados a la IVE; el impedimento subsiste después de cesar en el cargo (artículo 20)."], exact=True)

# ================= VII. CONOCIMIENTO DE CLIENTES =================
R("De conformidad al enfoque basado en riesgo, se ha considerado para la segmentación de las debidas diligencias, el monto transaccional de pagos recibidos de un cliente.",
  "De conformidad con el enfoque basado en riesgo (artículos 8 al 11 y 22 del Decreto 15-2026), el nivel de debida diligencia aplicable a cada cliente se asigna combinando el valor de la operación con el perfil de riesgo del cliente; el perfil de riesgo solo puede elevar el nivel, nunca reducirlo. Los parámetros de valor y de perfil, así como la documentación mínima por tipo de cliente, se establecen en la Política de Conocimiento del Cliente vigente.", exact=True)
R("Se solicitará a todos los posibles clientes antes de establecer una vinculación con Propi",
  "Antes de establecer la relación de negocios, todo posible cliente deberá proporcionar la información de identificación requerida (identidad, razón social o denominación, edad, ocupación u objeto social, estado civil, domicilio, nacionalidad, personería, capacidad legal y representación) y completar el Formulario Conoce a tu Cliente y el formulario de creación de expediente que establezca la IVE, cualquiera que sea el nivel de debida diligencia aplicable, por medio de la herramienta tecnológica que designe el Oficial de Cumplimiento. Toda la información y su documentación de respaldo será revisada y aprobada por el Oficial de Cumplimiento.")
IA("Antes de establecer la relación de negocios, todo posible cliente deberá proporcionar", [
  "Momentos y medidas de la debida diligencia (artículo 21). Las medidas de debida diligencia se aplicarán a todos los clientes cuando: a) se inicie la relación de negocios; b) se realicen transacciones por encima de los umbrales que establezca la reglamentación; c) existan transacciones inusuales; d) surjan dudas sobre la veracidad o suficiencia de los datos obtenidos previamente; e) se contraten productos o servicios adicionales que alteren la calificación de riesgo; y f) en los demás casos previstos en la Ley y su reglamentación.",
  "Las medidas de debida diligencia consisten en: 1) identificar y verificar la información del cliente y de quienes actúan en su nombre y en qué calidad, utilizando documentos, datos e información confiable de fuentes independientes; 2) identificar al beneficiario final y tomar medidas razonables para verificar su identidad, conforme a la Política de Identificación y Verificación del Beneficiario Final vigente; 3) obtener la información necesaria para comprender el propósito de la relación de negocios; 4) establecer el perfil del cliente y asignarle un nivel de riesgo; y 5) efectuar seguimiento continuo durante la relación de negocios, examinando que las transacciones sean consistentes con el perfil, el nivel de riesgo asignado, el origen de los fondos y los parámetros de normalidad del sector.",
  "Inicio de la relación de negocios y momento de la verificación (artículo 22). Para el cliente comprador de un inmueble, la relación de negocios se inicia al momento de la reserva, con independencia de que el pago se realice después; para las desarrolladoras, corredores externos, proveedores y demás contrapartes, con la firma del contrato de Alianza Comercial. La identificación del cliente y de su beneficiario final y el cruce en listas deben completarse antes de que Propi habilite la reserva o entregue al cliente el número de cuenta para el pago. La verificación de la información se efectúa al inicio de la relación de negocios o al realizar transacciones para clientes ocasionales.",
  "Diferimiento de la verificación. Propi podrá completar la verificación de la información del cliente, de quien actúe en su nombre o del beneficiario final con posterioridad al inicio de la relación de negocios, dentro de un plazo que no excederá de tres (3) meses y, en todo caso, antes de la firma de la promesa de compraventa, únicamente cuando concurran todas las condiciones siguientes: a) que se trate de un caso determinado y debidamente justificado; b) que el Riesgo LD/FT/FPADM pueda manejarse con efectividad; c) que resulte esencial para no interrumpir el normal desarrollo de la actividad; y d) que el cliente y su beneficiario final hayan sido identificados y el cruce en listas de sanciones no haya arrojado coincidencias.",
  "Los supuestos en los que procede el diferimiento son exclusivamente los siguientes: i) persona individual nacional clasificada en riesgo bajo o medio, cuyo documento de identificación ha sido verificado y cuyo comprobante de domicilio o constancia de RTU está pendiente de entrega; ii) persona jurídica nacional cuya patente de comercio o cuyo nombramiento de representante legal se encuentra en trámite de inscripción; iii) beneficiario final extranjero cuya certificación oficial de beneficiario final, certificación de vigencia o apostilla está en gestión; y iv) referencias bancarias o comerciales pendientes de confirmación.",
  "En ningún caso procede el diferimiento cuando el cliente o su beneficiario final sea o esté vinculado a una Persona Expuesta Políticamente, cuando el cliente haya sido clasificado en riesgo alto o cuando exista una transacción inusual. El diferimiento debe ser autorizado y documentado por el Oficial de Cumplimiento en el expediente del cliente.",
  "Abstención y terminación. Propi se abstendrá de establecer relaciones de negocios o de ejecutar operaciones cuando le sea imposible aplicar las medidas de debida diligencia. Cuando la imposibilidad surja durante la relación de negocios, Propi le pondrá fin y el Oficial de Cumplimiento practicará y documentará un examen para determinar si procede un Reporte de Transacción Sospechosa (artículo 22). Los contratos con clientes y contrapartes incorporarán una cláusula de terminación por incumplimiento de los requerimientos de cumplimiento normativo.",
  "Niveles de debida diligencia. La debida diligencia simplificada solo podrá aplicarse cuando se haya identificado y verificado previamente que el tipo de cliente, producto, servicio o transacción representa un riesgo menor conforme a la evaluación de riesgo documentada; no se aplicará ante una transacción inusual y dejará de aplicarse cuando se identifique un nivel de riesgo alto (artículo 23). La debida diligencia intensificada se aplicará cuando se identifiquen riesgos altos, cuando se establezcan relaciones o transacciones con personas de países o jurisdicciones de alto riesgo según el GAFI y en las situaciones que comunique la IVE (artículo 24); su desarrollo consta en la Política de Debida Diligencia Reforzada vigente.",
  "Situaciones especiales (artículo 25). Propi adoptará medidas de debida diligencia adicionales, conforme a la Política de Debida Diligencia Reforzada, cuando el cliente o su beneficiario final sea una Persona Expuesta Políticamente, su pariente en primer grado de consanguinidad, su cónyuge o conviviente o su asociado cercano; cuando sea contratista o proveedor del Estado; cuando se trate de organizaciones sin fines de lucro que reciban o administren fondos del Estado o del extranjero, o de personas jurídicas privadas sin fines de lucro; cuando ninguna de las partes esté domiciliada en el país; cuando se trate de fideicomisos u otras estructuras jurídicas; cuando la relación o transacción no implique la presencia física de las partes, atendiendo a los riesgos de las nuevas tecnologías; y cuando las transacciones en efectivo o las transferencias de fondos superen los montos que fije la reglamentación."])
R("Propi, establece la Debida Diligencia simplificada para Clientes catalogados de bajo riesgo",
  "La debida diligencia simplificada se aplicará a los clientes clasificados en riesgo bajo conforme a la Política de Conocimiento del Cliente, en los términos del artículo 23 del Decreto 15-2026. Como mínimo se dejará constancia del tipo y número del documento de identificación del cliente en el documento que ampara la transacción.")
R("La debida diligencia estándar, será aplicada a los clientes de riesgo medio",
  "La debida diligencia estándar se aplicará a los clientes clasificados en riesgo medio conforme a la Política de Conocimiento del Cliente, evaluando además las características del cliente, su país de procedencia, su actividad económica y el país de origen de sus fondos.")
R("Así mismo, deberá solicitar la siguiente documentación mínima por tipo de cliente:",
  "La documentación mínima por tipo de cliente (persona individual o jurídica, nacional o extranjera) se establece en la Política de Conocimiento del Cliente vigente y comprende, como mínimo, el documento de identificación, el comprobante de domicilio, el número de identificación tributaria, las credenciales de representantes o apoderados, los documentos constitutivos y la nómina de accionistas o beneficiarios finales con participación igual o mayor al quince por ciento (15 %).", exact=True)
D("Tabla 1  - Requerimiento clientes", exact=True)
delete_table("Nómina de accionistas, con el detalle de los accionistas que tienen más del 10%")
R("Propi, establece que en el proceso de vinculación del cliente y previo a establecer la relación comercial con éste, se debe de consultar que el nombre del cliente persona natural o jurídica, nombre de accionistas con más del 10% de participación accionaria, representante legal, apoderado, miembros de junta directiva y  beneficiario final, por medio de la herramienta tecnológica denominada Snap Compliance",
  "En el proceso de vinculación y previo a establecer la relación de negocios, Propi verificará que el cliente, sus accionistas o socios con participación igual o mayor al quince por ciento (15 %), su representante legal, apoderados, miembros del órgano de administración y beneficiarios finales no figuren en las listas de sanciones y de cautela nacionales e internacionales que determine el Oficial de Cumplimiento (entre ellas las del Consejo de Seguridad de las Naciones Unidas, OFAC e Interpol) ni en las listas de países o jurisdicciones de alto riesgo del GAFI. La verificación se realizará por medio de la herramienta tecnológica que designe el Oficial de Cumplimiento, quien aprobará la vinculación una vez validada la información y documentación; la constancia del cruce se conservará en el expediente.")
R("Se consideran de alto riesgo las personas naturales o jurídicas que el monto total de los ingresos recibidos sobrepase los USD $10,000.00",
  "Se consideran de riesgo alto los clientes que así resulten clasificados conforme a la matriz de riesgo y a la Política de Conocimiento del Cliente, y en todo caso los comprendidos en las situaciones especiales del artículo 25 del Decreto 15-2026.")
R("Con el fin de aplicar una Debida Diligencia intensificada a los clientes de alto riesgo, se podrá requerir la siguiente información adicional",
  "La información y documentación adicional exigible en la debida diligencia intensificada se establece en la Política de Debida Diligencia Reforzada vigente y podrá comprender, entre otros:")
R("Obtener la aprobación por escrito de la Asamblea de Accionista para establecer o continuar relaciones comerciales.",
  "Obtener la aprobación por escrito del órgano de dirección superior, o del nivel gerencial o comité en que este delegue, para establecer o continuar relaciones de negocios de riesgo alto, previo dictamen del Oficial de Cumplimiento.", exact=True)
R("Propi, establece que en el proceso de vinculación del cliente y previo a establecer la relación comercial con éste, se debe de consultar que el nombre del cliente persona natural o jurídica, nombre de accionistas con más del 10% de participación accionaria, representante legal, apoderado, miembros de junta directiva y  beneficiario final, que no aparezca en listas negras",
  "La verificación en listas descrita en esta sección se aplicará con mayor rigurosidad a los clientes de riesgo alto, y toda coincidencia generará una alerta que deberá ser analizada por el Oficial de Cumplimiento antes de autorizar o continuar la relación de negocios.")
R("Propi establece como mecanismo de identificación de las Personas Expuestas Políticamente (PEP) así como sus parientes en primero y segundo grado",
  "Propi establece como mecanismo de identificación de las Personas Expuestas Políticamente (PEP), así como de sus parientes dentro del primer grado de consanguinidad, su cónyuge o conviviente y sus asociados cercanos, las siguientes medidas y procedimientos de debida diligencia adicionales, acordes al riesgo que implica relacionarse con una PEP (artículo 25, literal a, del Decreto 15-2026):")
R("Continuaran siento sujetos de la debida diligencia ampliada aquellas personas catalogadas como PEP nacionales por un periodo igual al ejercicio de sus funciones sin exceder el plazo de cinco años",
  "Las personas catalogadas como PEP continuarán sujetas a debida diligencia reforzada mientras desempeñen el cargo y durante un (1) año posterior a su cese; vencido dicho plazo dejarán de ser consideradas PEP sin necesidad de trámite alguno. Propi podrá, con base en su evaluación de riesgo documentada, mantener al cliente en riesgo alto por antecedente de exposición política, sin que ello equivalga a la condición legal de PEP.")
RI("Identificación de Personas Relacionadas: Los posibles clientes deberán de completar el Formulario de Conoce a tu Cliente",
   "por medio de la herramienta Snap Compliance la cual", "por medio de la herramienta tecnológica que designe el Oficial de Cumplimiento, la cual")
R("Declaración formal: el posible cliente deberá declarar de manera formal si él o alguna persona relacionada es considerada una PEP",
  "Declaración formal: el posible cliente deberá suscribir la Declaración Jurada de Persona Expuesta Políticamente, en la que manifieste si él, su cónyuge o conviviente, sus parientes en primer grado de consanguinidad o sus asociados cercanos ostentan o han ostentado dentro del último año la condición de PEP y, en caso afirmativo, proporcionar la documentación de respaldo. Por cada beneficiario final identificado se suscribirá además la Declaración Jurada correspondiente.")
R("Además, en este mismo formulario deberán establecer el nombramiento de sus familiares en primer y segundo grado",
  "En la misma declaración se identificará a los parientes en primer grado de consanguinidad, al cónyuge o conviviente y a los asociados cercanos, quienes serán verificados en las listas de cautela por medio de la herramienta tecnológica que designe el Oficial de Cumplimiento.")
RI("Una vez concluida la evaluación del cliente, se procederá a archivar la información proporcionada por el cliente en un Registro",
   "manteniéndose una copia en la plataforma Snap Compliance", "manteniéndose una copia en la herramienta tecnológica que designe el Oficial de Cumplimiento")
R("Cuando se determine que un posible cliente es una Persona Políticamente Expuesta o Persona Relacionada, dicha condición se mantendrá durante el tiempo que ocupe el cargo y por un período de tres (3) años",
  "Cuando se determine que un posible cliente o su beneficiario final es una Persona Expuesta Políticamente, dicha condición se mantendrá durante el tiempo que ocupe el cargo y por un período de un (1) año después de haberlo dejado (artículo 2, literal g, y artículo 25, literal a, del Decreto 15-2026).")
R("La Asamblea de Accionistas para establecer o continuar relaciones comerciales con aquellos clientes o contrapartes calificadas como PEP",
  "El establecimiento o la continuidad de relaciones de negocios con clientes o contrapartes calificados como PEP requiere la autorización por escrito del órgano de dirección superior, o del nivel gerencial o comité en que este delegue, previo dictamen favorable del Oficial de Cumplimiento, quien dejará constancia de su aprobación en el expediente.")
RI("El potencial cliente o sus representantes legales, miembros de la Administración o Junta Directiva, accionistas que posean más de un 10% del capital social",
   "accionistas que posean más de un 10% del capital social", "accionistas o socios con participación igual o mayor al quince por ciento (15 %) del capital social")
IA("Comercialicen productos y/o presten servicios ilegales.",
   "Utilicen o pretendan utilizar cuentas anónimas, cifradas, con nombres ficticios, interpósitas personas o cualquier esquema que dificulte, distorsione o impida conocer la verdadera identidad del cliente o de su beneficiario final (artículo 27 del Decreto 15-2026).", exact=True)
RI("En el caso que algún Cliente de riesgo se encuentre bajo alguna de las causales anteriores",
   "se deberá enviar el reporte respectivo a la Super Intendencia de Bancos a travez de la Intendencia de Verificación Especial",
   "se practicará el examen previsto en el artículo 22 del Decreto 15-2026 y, de proceder, se remitirá el Reporte de Transacción Sospechosa a la Superintendencia de Bancos a través de la Intendencia de Verificación Especial")
R("Propi verificará y actualizará periódicamente los datos recolectados de los clientes que por su naturaleza puedan variar",
  "Propi verificará y actualizará periódicamente los datos de los clientes que por su naturaleza puedan variar (dirección, teléfono, actividad económica, origen de los recursos, composición accionaria, beneficiarios finales, entre otros). Para los clientes clasificados en riesgo alto la actualización se realizará por lo menos una vez al año (artículo 22 del Decreto 15-2026); para los demás niveles, con la periodicidad que establezca la Política de Conocimiento del Cliente y, en todo caso, ante cualquier evento que modifique el perfil o el riesgo del cliente.")
R("Cuando Propi, luego de realizar un análisis con los elementos objetivos de riesgo del cliente, determine la existencia de elementos suficientes",
  "Cuando Propi, luego de realizar un análisis con los elementos objetivos de riesgo del cliente, determine la existencia de elementos suficientes para considerar que existe un Riesgo LD/FT/FPADM que no puede ser mitigado, o cuando le resulte imposible aplicar las medidas de debida diligencia, pondrá fin a la relación contractual o de negocios. Deberá documentar la evidencia de este análisis y practicar el examen que permita determinar la procedencia de un Reporte de Transacción Sospechosa, conforme a los artículos 22 y 30 del Decreto 15-2026, por los medios establecidos por la IVE.")
R("En ningún momento, el cliente de quien se recibió la Transferencia Sospechosa deberá ser notificado",
  "En ningún momento se notificará ni alertará al cliente de que se está examinando alguna transacción, de que se ha remitido un Reporte de Transacción Sospechosa o de que existe una investigación por parte de autoridad competente (artículo 38 del Decreto 15-2026). Toda comunicación de rechazo o terminación se fundará en causas comerciales o contractuales, conforme al texto modelo aprobado por el Oficial de Cumplimiento.")
R("Previo a dar por terminada una relación contractual según el párrafo anterior",
  "Previo a dar por terminada una relación contractual conforme a los párrafos anteriores, el Oficial de Cumplimiento aplicará el procedimiento de examen y reporte previsto en la sección X de este Manual y en el Procedimiento de Reportes vigente.")

# ================= VIII. EMPLEADOS =================
RI("Adicionalmente, previo a cualquier contratación o en cualquier momento de la relación laboral",
   "listas negras internacionales y nacionales como por ejemplo la lista negra de la Interpol, la lista de la OFAC, listas de países de alto riesgo del GAFI, listas de países o jurisdicciones con nula o bajo tributación y listas de cautela.",
   "listas de sanciones y de cautela nacionales e internacionales, incluidas las listas emitidas por el Consejo de Seguridad de las Naciones Unidas, la OFAC, Interpol y las listas de países o jurisdicciones de alto riesgo del GAFI (artículo 12, literal a, del Decreto 15-2026).")
IA("Adicionalmente, previo a cualquier contratación o en cualquier momento de la relación laboral", [
  "En ningún caso Propi contratará o nombrará como personal, director, agente, corredor, intermediario o colaborador, cualquiera que sea la forma jurídica de su contratación, a personas que figuren en las listas emitidas por el Consejo de Seguridad de las Naciones Unidas, ni a quienes hayan sido condenados por los delitos de lavado de dinero u otros activos o financiamiento del terrorismo, mientras no hayan transcurrido cinco (5) años de cumplida la pena (artículo 12, literal a).",
  "Los estándares de esta sección se aplican también a los directores, agentes, corredores externos e intermediarios que actúen por cuenta de Propi. Las obligaciones laborales del personal en materia de prevención del LD/FT/FPADM y el régimen disciplinario se desarrollan en el Reglamento Interno de Trabajo y en el Código de Ética."])

# ================= IX. PROVEEDORES =================
R("De conformidad al enfoque basado en riesgo, se ha considerado para la segmentación de las debidas diligencias, el monto transaccional de pagos realizados a un proveedor.",
  "De conformidad con el enfoque basado en riesgo, la segmentación de la debida diligencia de proveedores, la documentación mínima por tipo de proveedor, los umbrales aplicables a compras únicas y el formulario correspondiente se establecen en la Política de Conocimiento de Proveedores vigente.", exact=True)
D("La documentación mínima por solicitar por tipo de proveedor será la siguiente:")
D("Tabla 2  -  Requerimientos proveedores", exact=True)
delete_table("Constancia de Registro ante la Intendencia de Verificación Especial")
D("Adicionalmente,", exact=True)
R("Propi establece que en el proceso de vinculación del proveedor y previo a establecer la relación comercial con éste, se debe completar el “Formulario de Conoce a tu Proveedor”",
  "Adicionalmente, en el proceso de vinculación del proveedor y previo a establecer la relación comercial, se completará el Formulario Conoce a tu Proveedor por medio de la herramienta tecnológica que designe el Oficial de Cumplimiento, y se verificará que el proveedor, sus accionistas o socios con participación igual o mayor al quince por ciento (15 %), su representante legal, apoderados, miembros del órgano de administración y beneficiarios finales no figuren en listas de sanciones y de cautela nacionales e internacionales; toda coincidencia generará una alerta que analizará el Oficial de Cumplimiento.")
R("Para aquellos proveedores con los que se realice una compra única",
  "Para los proveedores con los que se realice una compra única, la exigencia del Formulario Conoce a tu Proveedor y de la documentación aplicable se rige por los umbrales que establezca la Política de Conocimiento de Proveedores vigente.")

# ================= X. MONITOREO Y REPORTES =================
R("POLITICAS PARA EL MONITOREO Y REPORTE DE OPERACIONES IRREGULARES, SOSPECHOSAS Y REGULADAS",
  "POLÍTICAS PARA EL MONITOREO, DETECCIÓN Y REPORTE DE TRANSACCIONES INUSUALES, SOSPECHOSAS Y EN EFECTIVO", exact=True)
R("El Oficial de Cumplimiento efectuará un monitoreo permanente de las transacciones llevadas a cabo con los clientes.",
  "Propi establecerá e implementará políticas, procedimientos, controles y sistemas de monitoreo de todas las transacciones y operaciones que realiza, adecuados al volumen y complejidad de sus actividades, que generen alertas en función del Riesgo LD/FT/FPADM y permitan identificar transacciones inusuales con prontitud (artículo 28 del Decreto 15-2026). El Oficial de Cumplimiento efectuará un monitoreo permanente de las transacciones llevadas a cabo con los clientes.", exact=True)
R("Para determinar cómo operaciones irregulares que deben ser analizadas por el Oficial de Cumplimiento",
  "Para determinar las transacciones inusuales que deben ser analizadas por el Oficial de Cumplimiento, este deberá considerar aquellas transacciones de ingreso o egreso que, por sus montos, medios de pago, frecuencia o tipo de cliente, no se ajusten al perfil de riesgo del cliente sin una justificación económica o legal razonable, o que activen alguna de las señales de alerta definidas.")
R("Para la determinación de los escenarios de riesgo o alertas que se deberán monitorear permanentemente",
  "Para la determinación de las señales de alerta que se deberán monitorear permanentemente, Propi, por medio del Oficial de Cumplimiento, definirá y mantendrá actualizadas las señales de alerta conforme a su evaluación del Riesgo LD/FT/FPADM y a las tipologías, tendencias y patrones de LD/FT que comunique la IVE (artículos 28 y 52, literal g, del Decreto 15-2026). Es obligación del Oficial de Cumplimiento revisar y actualizar permanentemente estas señales para asegurar que se encuentren apegadas a la realidad del negocio y sus operaciones.")
R("REPORTE INTERNO DE OPERACIONES IRREGULARES O SOSPECHOSAS", "REPORTE INTERNO DE TRANSACCIONES INUSUALES O SOSPECHOSAS", exact=True)
R("Cualquier empleado de Propi que conozca información sobre la actividad sospechosa de algún cliente o proveedor",
  "Cualquier empleado, director, agente, corredor o colaborador de Propi que conozca información sobre una transacción inusual o sobre la actividad sospechosa de algún cliente o proveedor está en la obligación de notificarlo de inmediato al Oficial de Cumplimiento, utilizando el Formulario de Reporte Interno de Transacciones Inusuales o Sospechosas, conforme al Procedimiento de Reporte Interno vigente. Todo reporte recibido por el Oficial de Cumplimiento ingresará al examen previsto en el siguiente literal.")
R("ANÁLISIS DE TRANSACCIONES IRREGULARES", "ANÁLISIS DE TRANSACCIONES INUSUALES", exact=True)
R("Las transacciones que se identifiquen como irregulares debido a que cumplen con los criterios anteriormente mencionados",
  "Las transacciones identificadas como inusuales, concluidas o no, ingresarán a un proceso de examen a fin de determinar si tienen o no un fundamento económico o legal aparente y, en su caso, si procede remitir el Reporte de Transacción Sospechosa (RTS) a la Superintendencia de Bancos a través de la IVE, por los mecanismos que esta ponga a disposición (artículos 29 y 30 del Decreto 15-2026).")
R("El Oficial de Cumplimiento cuenta con 15 días hábiles para realizar el análisis",
  "El Oficial de Cumplimiento examinará las transacciones inusuales con prontitud, dentro de los plazos internos que establezca el Procedimiento de Reportes vigente. Concluido el examen, el Oficial de Cumplimiento, o su suplente, registrará en el expediente correspondiente un resumen de sus observaciones, así como las del funcionario o empleado que detectó la operación.")
R("Como consecuencia del análisis efectuado, tomando como base lo establecido en la Ley contra el Lavado de Dinero y Activos, su Reglamento e Instructivo",
  "Como consecuencia del examen efectuado, y con base en el Decreto 15-2026, su reglamentación y las disposiciones de la IVE, el Oficial de Cumplimiento calificará la transacción de la siguiente manera:")
R("Si existen suficientes elementos de juicio para considerarlas operaciones sospechosas",
  "Si la transacción inusual carece de fundamento económico o legal evidente o si, a pesar de tener apariencia de legalidad, existen motivos razonables para sospechar que los fondos proceden o se destinan a una actividad delictiva o al financiamiento del terrorismo, se calificará como transacción sospechosa y se elaborará el Reporte de Transacción Sospechosa (RTS), que se remitirá con prontitud a la IVE utilizando los medios y formas que esta establezca y dentro de los plazos del Procedimiento de Reportes vigente.")
R("No se considera una operación sospechosa, por tanto se considera como una “Operación Normal” y el caso se da por cerrado.",
  "Si la transacción tiene fundamento económico o legal aparente, se considerará una transacción normal y el caso se dará por cerrado, dejando constancia del examen.", exact=True)
R("REPORTE DE OPERACIONES SOSPECHOSAS (ROS) Y REPORTE DE TENTATIVA DE OPERACIÓN SOSPECHOSA",
  "REPORTE DE TRANSACCIÓN SOSPECHOSA (RTS) Y REPORTE DE TENTATIVA DE TRANSACCIÓN SOSPECHOSA", exact=True)
R("El Reporte de Operaciones Sospechosas es anónimo y como tal, se envía a nombre de Propi.",
  "El Reporte de Transacción Sospechosa se remite a nombre de Propi, de forma exclusiva y confidencial, y goza de garantía de confidencialidad (artículo 30 del Decreto 15-2026). El Oficial de Cumplimiento es el único autorizado para enviar los RTS a la IVE, utilizando exclusivamente los medios, procedimientos, condiciones y plazos establecidos por esta (artículo 33). Propi es responsable de que la información proporcionada sea completa y coincida con sus registros.")
RI("Dentro de la documentación a remitir junto con el reporte de operación sospechosa se incluye:", "reporte de operación sospechosa", "Reporte de Transacción Sospechosa")
RI("De igual forma, procederá el  Reporte de tentativa de operación sospechosa", "reportadas a la IVE como una operación sospechosa tentada", "reportadas a la IVE como una transacción sospechosa no concluida (tentativa)")
R("Queda terminantemente prohibido informar al cliente que su operación será reportada como sospechosa.",
  "Queda terminantemente prohibido revelar a terceros, incluido el cliente, que se ha remitido o comunicado un RTS, información, documentación, expedientes o registros a la IVE o a autoridad competente, o que se está examinando alguna transacción o realizándose alguna investigación; la prohibición subsiste aun después de que las personas hayan cesado en sus funciones (artículo 38 del Decreto 15-2026). Propi, sus directores, gerentes, funcionarios, oficiales de cumplimiento, representantes legales y empleados quedan exentos de responsabilidad legal por haber proporcionado de buena fe información a las autoridades competentes, incluida la comunicación de RTS (artículo 37).", exact=True)
R("REPORTE DE OPERACIONES REGULADAS", "REGISTRO Y REPORTE DE TRANSACCIONES EN EFECTIVO Y OTROS REPORTES", exact=True)
R("El Oficial de Cumplimiento realizará monitoreo de las transacciones diarias de los clientes, con la finalidad de identificar transacciones que superen el umbral permitido por la ley",
  "Propi llevará y mantendrá un registro diario de toda transacción en efectivo, sea única o estructurada, que reciba de sus clientes por un monto igual o mayor a diez mil dólares de los Estados Unidos de América (US$ 10,000.00) o su equivalente en moneda nacional o cualquier otra divisa, y remitirá a la IVE el reporte periódico de dichas transacciones (artículo 31 del Decreto 15-2026). Asimismo, remitirá los demás reportes, ocasionales o periódicos, que requiera la IVE, incluido el reporte mensual de operaciones inmobiliarias que corresponda a su sector (artículo 32), utilizando exclusivamente los medios y plazos que esta establezca (artículo 33).")
R("Operación individual en efectivo. Se entenderá por transacción en efectivo que realiza un cliente en un solo evento",
  "Los criterios para identificar transacciones individuales y múltiples en efectivo, los umbrales aplicables a transacciones por otros medios y los plazos de presentación de cada reporte se desarrollan en el Procedimiento de Reportes vigente, en concordancia con el Decreto 15-2026, su reglamentación y las disposiciones de la IVE.")
D("Operaciones múltiples en efectivo. Son transacciones en efectivo iguales o inferiores a USD $10,000.00")
D("Operación individual – otro medio. Son transacciones en otro medio")
D("Operaciones múltiples - transacciones en otro medio.")
R("En el caso que Propi no pudiera cumplir con el plazo establecido por la IVE para la entrega de documentos",
  "En caso de que Propi no pudiera cumplir con el plazo establecido por la IVE para la entrega de información, documentación, expedientes o registros, el Oficial de Cumplimiento solicitará una prórroga por escrito, a más tardar dos (2) días antes del vencimiento del plazo original, explicando los motivos que la justifiquen (artículo 36 del Decreto 15-2026). Propi prestará su colaboración a la IVE proporcionando acceso inmediato y gratuito a sus fuentes, sistemas de información, registros y documentos, sin que pueda oponerse confidencialidad alguna (artículo 35).")
# ---- X-bis NUEVA: ONU / congelamiento (después de la prórroga; encabezado con estilo de "ATENCIÓN DE REQUERIMIENTOS DE INFORMACIÓN")
IA("En caso de que Propi no pudiera cumplir con el plazo establecido por la IVE", "CUMPLIMIENTO DE LAS RESOLUCIONES DEL CONSEJO DE SEGURIDAD DE LAS NACIONES UNIDAS", style_from="ATENCIÓN DE REQUERIMIENTOS DE INFORMACIÓN")
IA("CUMPLIMIENTO DE LAS RESOLUCIONES DEL CONSEJO DE SEGURIDAD DE LAS NACIONES UNIDAS", [
  "Propi controlará permanentemente y verificará si sus clientes, o quienes pretendan iniciar una relación de negocios, se encuentran designados en las listas de personas, entidades o grupos emitidas y mantenidas por el Consejo de Seguridad de las Naciones Unidas en virtud de las resoluciones S/RES/1267 (1999), 1988 (2011), 1989 (2011) y 2253 (2015), relativas al terrorismo; 1718 (2006), 1737 (2006) y 2231 (2015), relativas al financiamiento de la proliferación de armas de destrucción masiva; y 1373 (2001), y sus sucesivas (artículo 43 del Decreto 15-2026).",
  "De existir coincidencia con los nombres o datos de identificación de las referidas listas, Propi procederá de inmediato a limitar con efecto preventivo la disposición de los fondos o activos del cliente o controlados por este que se encuentren bajo su administración o a su cargo por cualquier motivo, así como sus frutos, y lo comunicará por escrito al Ministerio Público en un plazo que no excederá de veinticuatro (24) horas, adjuntando la documentación correspondiente. La medida se levantará únicamente al recibir notificación de juez competente que así lo ordene o cuando el Consejo de Seguridad revoque la designación (artículo 44).",
  "Está prohibido informar al cliente o a terceros sobre la coincidencia, la limitación preventiva o la comunicación al Ministerio Público. Propi y sus funcionarios quedan exentos de responsabilidad penal, civil o administrativa por haber aplicado la limitación con efecto preventivo conforme a la Ley (artículo 43). Propi remitirá a la IVE el reporte periódico sobre si detectó o no coincidencias, en la forma y plazo que esta establezca.",
  "El paso a paso operativo se desarrolla en el Procedimiento de inmovilización y reporte ante coincidencia en listas del Consejo de Seguridad de las Naciones Unidas, documento complementario de este Manual."], exact=True, style_from="En caso de que Propi no pudiera cumplir con el plazo establecido por la IVE")

# ================= XI. ENFOQUE BASADO EN RIESGO / MATRIZ =================
R("MATRIZ DE RIESGO", "ENFOQUE BASADO EN RIESGO Y MATRIZ DE RIESGO", exact=True)
R("A través de la matriz de riesgo queremos estimar el impacto potencial",
  "Propi administra su Riesgo LD/FT/FPADM mediante un proceso integral de identificación, evaluación y mitigación, proporcional a la naturaleza, volumen y complejidad de sus actividades, que le permite asignar sus recursos y establecer medidas idóneas conforme a los riesgos identificados. Dicho proceso, su metodología y sus actualizaciones son aprobados por el órgano de dirección superior y constan debidamente documentados (artículo 8 del Decreto 15-2026).")
IA("El riesgo de LDA/FT/FPADM se materializa a través de los riesgos asociados", [
  "Identificación del riesgo (artículo 9). Propi identifica el Riesgo LD/FT/FPADM al que está expuesta por sus actividades y modelo de negocio mediante una metodología que establece sus factores de riesgo, considerando como mínimo la base de clientes, la ubicación geográfica, los canales de distribución y los bienes, productos o servicios ofrecidos, e identifica las variables y eventos de riesgo en cada uno de esos factores.",
  "Evaluación del riesgo (artículo 10). Propi evalúa periódicamente cómo el riesgo identificado le puede afectar, mediante una autoevaluación sobre el negocio en su conjunto y las evaluaciones particulares de la relación comercial con sus clientes, analizando la probabilidad de ocurrencia y el posible impacto, y considerando los resultados de las evaluaciones nacionales o sectoriales que le comunique la IVE.",
  "Mitigación del riesgo (artículo 11). Con base en el riesgo evaluado, Propi implementa las políticas, procedimientos, controles y sistemas de información que le permiten monitorear, informar y controlar su nivel de riesgo. Propi realizará el proceso de administración del riesgo previo al lanzamiento de nuevos bienes, productos o servicios y previo al uso o adopción de nuevas tecnologías o prácticas comerciales.",
  "La matriz de riesgo consolidada de Propi, con sus segmentos (clientes, desarrolladoras, corredores externos, proveedores y empleados), variables, niveles y frecuencias de monitoreo, se incorpora como Anexo de este Manual y se actualiza conforme a lo previsto en esta sección sin necesidad de modificar el cuerpo del Manual."])
rl.delete_range("Competitivo:", "Variación en las tasas de interés")
R("En la siguiente matriz de riesgos, la probabilidad de que ocurra cada riesgo se clasifica en una escala del 1 al 5",
  "La matriz de riesgo consolidada y su metodología de calificación (probabilidad, consecuencia, nivel de riesgo y frecuencia de monitoreo) constan en el Anexo «Matriz de riesgo consolidada» de este Manual.")
D("Tabla 3 - Matriz de riesgos", exact=True)
delete_table("Catastrófica A")
D("Riesgos operacionales internos identificados:")
D("Para cada riesgo se han definido controles y acciones a tomar para mitigar su impacto")
D("Tabla 4 - Líneas de negocio", exact=True)
delete_table("Nombre de las líneas de negocio")
D("Tabla 5 - Evaluación de riesgos", exact=True)
delete_table("Riesgo identificado")
IA("Verde: al menos semestral", "[ESPACIO RESERVADO — ANEXO: MATRIZ DE RIESGO CONSOLIDADA. Se incorporará la matriz consolidada una vez revisada y aprobada.]", exact=True)

# ================= XII. CONFIDENCIALIDAD =================
IA("Dado a la naturaleza de la información que se maneja en", [
  "La identidad y la información personal del Oficial de Cumplimiento y de las personas que laboren bajo su dirección son confidenciales (artículo 19 del Decreto 15-2026). Queda prohibido a Propi, sus directores, gerentes, administradores, funcionarios, oficiales de cumplimiento, representantes legales y empleados revelar a terceros que se ha remitido un RTS o información a la IVE o a autoridad competente, o que se examina alguna transacción o se realiza alguna investigación; la prohibición subsiste después del cese en las funciones (artículo 38).",
  "La confidencialidad establecida en este Manual no podrá oponerse a los requerimientos de información de la Superintendencia de Bancos a través de la IVE ni de las autoridades competentes (artículo 35 del Decreto 15-2026)."])

# ================= XIII. CONSERVACIÓN =================
R("De acuerdo con la disposición establecida en la Ley contra el Lavado de Dinero y Activos; y su Reglamento, se resguardarán los documentos del cliente",
  "De conformidad con el artículo 34 del Decreto 15-2026, que establece un plazo mínimo de conservación de cinco (5) años, Propi adopta como política propia resguardar los documentos del cliente en un expediente único por un período de al menos quince (15) años, contado desde la finalización de la relación de negocios, la cual se entiende concluida con el pago de la última comisión a la Sociedad. El expediente único estará conformado con la documentación establecida en la Política de Conocimiento del Cliente y en la Política de Identificación y Verificación del Beneficiario Final.")
R("Mantener por un período no menor de quince (15) años a través de medios impresos, digitales o electrónicos",
  "Mantener por un período no menor de quince (15) años, a través de medios impresos, digitales o electrónicos que garanticen su integridad, correcta lectura, inalterabilidad, adecuada conservación y fácil localización, toda la documentación que ampara las operaciones o transacciones realizadas con los clientes, así como la correspondencia comercial, los expedientes y los resultados de los análisis o exámenes realizados; dichos registros deben ser suficientes para permitir la reconstrucción íntegra de cada operación y atender los requerimientos de las autoridades competentes (artículo 34 del Decreto 15-2026).")
R("En caso de que en algún momento Propi, a través del Oficial de Cumplimiento, decida realizar la Destrucción de Registros",
  "En caso de que en algún momento Propi, a través del Oficial de Cumplimiento, decida realizar la destrucción de registros cuyo plazo de conservación haya vencido, el Oficial de Cumplimiento elaborará, como práctica interna de control, un informe con por lo menos dos (2) meses de anticipación a la fecha prevista, que conservará en sus registros y pondrá a disposición de la IVE cuando esta lo requiera. Este informe deberá contener, como mínimo, la siguiente información:")

# ================= XIV. CAPACITACIÓN =================
R("Cada año, el Oficial de Cumplimiento, deberá diseñar y someter a aprobación del Secretario Junta Directiva Único",
  "Cada año, el Oficial de Cumplimiento deberá diseñar y someter a aprobación del órgano de dirección superior un Plan de Capacitación Anual, de ejecución continua, para el personal, directores, agentes, corredores, intermediarios y demás colaboradores de Propi cuyo puesto o cargo requiera comprender el Riesgo LD/FT/FPADM, en función de sus responsabilidades (artículo 12, literal b, del Decreto 15-2026). El plan incluirá toda la temática de prevención y control de los riesgos de LD/FT/FPADM y servirá de apoyo para identificar situaciones inusuales o sospechosas en el manejo de las operaciones.")
RI("Luego de concluir con su proceso de capacitación anual el personal de Propi deberá someterse a una prueba de conocimientos",
   "que se realizará de manera electrónica.", "que se realizará de manera electrónica, como mecanismo idóneo para verificar que ha adquirido las competencias según su puesto o cargo (artículo 12, literal b, del Decreto 15-2026).")

# ================= XV. ÓRGANOS DE CONTROL =================
RI("La auditoría interna, o quien ejecute funciones similares dentro de Propi deberá elaborar y ejecutar de forma anual",
   "en el presente manual y la regulación vigente.", "en el presente Manual, en sus documentos complementarios y en la regulación vigente (artículo 15 del Decreto 15-2026).")
R("El Oficial de Cumplimiento será responsable de coordinar la realización de una Auditoría Externa anual",
  "Sin perjuicio de que el informe de aseguramiento de auditoría externa es obligatorio únicamente para las entidades sujetas a la vigilancia e inspección de la Superintendencia de Bancos, Propi, como práctica propia, podrá contratar una auditoría externa anual o a auditores especializados de su elección para evaluar el cumplimiento y la efectividad de sus Programas de Prevención LD/FT/FPADM (artículo 15 del Decreto 15-2026). El Oficial de Cumplimiento será responsable de coordinar dicha evaluación y de dar seguimiento a sus recomendaciones.")

# ================= XVI. SANCIONES =================
IA("La terminación del contrato individual de trabajo por incumplimiento de las presentes obligaciones",
   "El régimen disciplinario aplicable al personal se rige por el Reglamento Interno de Trabajo de Propi, el cual desarrolla las obligaciones laborales en materia de prevención del LD/FT/FPADM. Sin perjuicio de lo anterior, el incumplimiento de las obligaciones del Decreto 15-2026 expone a la Sociedad a las sanciones administrativas previstas en sus artículos 65 al 72 (amonestación o multa de US$ 500.00 a US$ 300,000.00, agravada en caso de ocultamiento, y requerimiento de planes de acción), sin perjuicio de las responsabilidades penales y civiles correspondientes.")

# ================= XVII. DIVULGACIÓN =================
RI("El presente manual o sus modificaciones se darán a conocer a todos los funcionarios y empleados contratados y subcontratados de Propi",
   "funcionarios y empleados contratados y subcontratados de Propi", "funcionarios, empleados, directores, agentes, corredores e intermediarios de Propi, quienes firmarán constancia de su conocimiento")

# ================= XVIII. VIGENCIA =================
R("El presente Manual entrará en vigor a partir de la fecha de su aprobación por la Asamblea de Accionistas de Propi.",
  "El presente Manual entrará en vigor a partir de la fecha de su aprobación por el órgano de dirección superior de Propi. Su contenido será revisado como mínimo cada año a partir de dicha fecha, así como cuando existan cambios relevantes en el modelo operativo o de negocios, cuando se emita el Reglamento del Decreto 15-2026 o disposiciones de la Superintendencia de Bancos a través de la IVE que lo hagan necesario y, en general, ante cualquier modificación de la regulación en materia de prevención del LD/FT/FPADM.")
R("El Oficial de Cumplimiento será la responsable de custodia del documento original",
  "El Oficial de Cumplimiento será responsable de la custodia del documento original y de su administración, y estará facultado para proponer cambios, modificaciones y actualizaciones, las cuales deberán ser aprobadas por el órgano de dirección superior (artículo 12 del Decreto 15-2026). Las políticas, procedimientos, formatos y demás documentos complementarios que integran el Sistema de Prevención son documentos independientes: el Oficial de Cumplimiento propondrá su emisión y actualización y serán aprobados por el nivel que determine el órgano de dirección superior, sin que ello requiera modificar este Manual, siempre que no lo contradigan; en caso de conflicto prevalece el Manual. La divulgación de este Manual y de sus documentos complementarios al personal será responsabilidad del Oficial de Cumplimiento en coordinación con Recursos Humanos, o quien ejecute funciones similares.")
R("Fecha de autorización: 12/08/2024", "Fecha de autorización: ____/____/______")
R("José Mario Ávila Palomo", "Nombre y cargo: ______________________________", nth=1)

# ================= XIX. ANEXO — DOCUMENTOS DEL SISTEMA =================
IA("Nombre y cargo: ______________________________", "ANEXO — DOCUMENTOS QUE INTEGRAN EL SISTEMA DE PREVENCIÓN", style_from="VIGENCIA Y MODIFICACIONES")
IA("ANEXO — DOCUMENTOS QUE INTEGRAN EL SISTEMA DE PREVENCIÓN", [
  "Los siguientes documentos desarrollan este Manual, son independientes de él y se aplican en su versión vigente aprobada por el nivel que determine el órgano de dirección superior. En ningún caso pueden contradecir lo dispuesto en este Manual, el cual prevalece; toda contradicción se resolverá a favor del Manual y dará lugar a la corrección inmediata del documento complementario.",
  "1. Política de Identificación y Verificación del Beneficiario Final.",
  "2. Política de Personas Expuestas Políticamente.",
  "3. Política de Conocimiento del Cliente (KYC / debida diligencia), incluida la documentación mínima por tipo de cliente y los parámetros de valor y perfil para la asignación del nivel de diligencia.",
  "4. Política de Debida Diligencia Reforzada (EDD).",
  "5. Política de Conocimiento de Proveedores, incluida la documentación mínima por tipo de proveedor y los umbrales de compra única.",
  "6. Matriz de riesgo consolidada y su metodología (Anexo).",
  "7. Procedimiento de Reportes: Reporte de Transacción Sospechosa, tentativa, transacciones en efectivo, reporte mensual sectorial y tablero de monitoreo, con sus plazos internos y umbrales.",
  "8. Procedimiento de inmovilización y reporte ante coincidencia en listas del Consejo de Seguridad de las Naciones Unidas.",
  "9. Procedimiento de aprobación de clientes Personas Expuestas Políticamente y de riesgo alto.",
  "10. Procedimiento de Reporte Interno de Transacciones Inusuales o Sospechosas.",
  "11. Manuales de procedimiento operativo (onboarding, aprobación y escalamiento).",
  "12. Reglamento Interno de Trabajo.",
  "13. Código de Ética.",
  "14. Formatos: Declaración Jurada de Beneficiario Final; Declaración Jurada de Persona Expuesta Políticamente; formulario de creación de expediente del cliente establecido por la IVE (IVE-RE-23 o el que lo sustituya); Formulario Conoce a tu Cliente; Formulario Conoce a tu Proveedor; Formulario de Reporte Interno; Lista de Asistencia de Capacitación.",
  "El Oficial de Cumplimiento mantendrá actualizado el registro de la versión vigente de cada documento complementario y de la fecha de su aprobación."], exact=True, style_from="El Oficial de Cumplimiento será responsable de la custodia del documento original")

# ================= NOMENCLATURA UNIFORME LD/FT/FPADM (regla 8 del guion) =================
for _old in ("LDA/FT/FPADM", "LA/FT/FPADM", "LDA/FT"):
    print("  nomenclatura", _old, "->", rl.replace_token(_old, "LD/FT/FPADM"))
n = rl.save()
print("EDICIONES APLICADAS:", n)
