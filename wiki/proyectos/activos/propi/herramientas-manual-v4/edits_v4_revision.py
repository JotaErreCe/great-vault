# edits_v4_revision.py — cambios posteriores a la aprobación de JR, en control de cambios sobre "V4 base aprobada"
from redline import Redline
rl = Redline("unpacked/word/document.xml", "José Roberto Castañeda", start_id=20000)
R = rl.replace

# ---- Punto 2 de Ena (16-sep-2026): sin comité; autoriza el OC con acta; designación por Consejo o Asamblea ----
R("Autorizar por escrito, o delegar en el nivel gerencial o comité que designe",
  "Designar, cuando lo estime necesario, al Gerente General u otro gerente para autorizar el establecimiento o la continuidad de relaciones de negocios con Personas Expuestas Políticamente o clientes de riesgo alto, en los términos de la sección VII. La designación podrá hacerla indistintamente el Consejo de Administración o la Asamblea General de Accionistas, mediante resolución que conste en acta.")
R("Obtener la aprobación por escrito del órgano de dirección superior, o del nivel gerencial o comité en que este delegue",
  "Obtener la autorización del Oficial de Cumplimiento, o de quien designen el Consejo de Administración o la Asamblea General de Accionistas, para establecer o continuar relaciones de negocios de riesgo alto, en los términos previstos para los clientes PEP.")
R("El establecimiento o la continuidad de relaciones de negocios con clientes o contrapartes calificados como PEP requiere la autorización por escrito",
  "El establecimiento o la continuidad de relaciones de negocios con clientes o contrapartes calificados como PEP o de riesgo alto requiere la autorización del Oficial de Cumplimiento, que constará en un acta en la que se expresen los motivos de la decisión y se declare que se realizaron todas las medidas de debida diligencia aplicables. El acta se archivará en el expediente del cliente. Si el Consejo de Administración o la Asamblea General de Accionistas designan, mediante resolución que conste en acta, al Gerente General u otro gerente para otorgar esta autorización, se requerirá el dictamen previo del Oficial de Cumplimiento, y un dictamen desfavorable impedirá autorizar la relación. El detalle se desarrolla en el Procedimiento de aprobación de clientes PEP y de riesgo alto.")


# ---- Punto 6 de Ena (16-sep-2026): recepción excepcional de fondos por cuenta de terceros (sección VII, tras "Procedencia de fondos") ----
rl2 = rl  # mismo motor
_ANCLA = "Actualización de información de clientes"
rl.insert_before(_ANCLA, "Recepción excepcional de fondos por cuenta de terceros", exact=True, style_from=rl.find("Procedencia de fondos", exact=True))
rl.insert_before(_ANCLA, [
  "Propi no presta servicios de cobro, custodia, administración ni transferencia de fondos de terceros. Los pagos de los clientes se realizan directamente a las cuentas del desarrollador o propietario del inmueble.",
  "Solo de manera excepcional, y nunca como servicio ofrecido, publicitado o como canal habitual de pago, Propi podrá recibir fondos de un cliente para trasladarlos al desarrollador o propietario, cuando concurran todas las condiciones siguientes:",
  "a) que los fondos correspondan a una operación inmobiliaria concreta intermediada por Propi y su único destinatario sea el desarrollador o propietario de esa operación;",
  "b) que el cliente realice el pago desde el extranjero o que, por otra causa documentada en el expediente, el pago directo al desarrollador o propietario no sea razonablemente posible;",
  "c) que exista instrucción o mandato escrito del desarrollador o propietario para esa operación;",
  "d) que el Oficial de Cumplimiento lo autorice previamente, una vez completada la debida diligencia del cliente, incluida la verificación del origen de los fondos y, cuando los fondos provengan de países o jurisdicciones de alto riesgo según el GAFI, la debida diligencia intensificada (artículo 24 del Decreto 15-2026);",
  "e) que los fondos provengan de una cuenta bancaria a nombre del cliente, en Guatemala o en el extranjero, por transferencia bancaria, y nunca en efectivo ni desde cuentas de terceros;",
  "f) que se reciban en una cuenta bancaria de Propi destinada exclusivamente a este fin y se trasladen íntegramente al destinatario, en la misma moneda en que fueron recibidos, dentro de los tres (3) días hábiles siguientes a su acreditación, sin que Propi los invierta, los retenga, los convierta a otra moneda ni cobre cargo alguno por la recepción o el traslado. Los cargos bancarios de las transferencias correrán por cuenta del cliente o del destinatario.",
  "El Oficial de Cumplimiento llevará un registro de estas operaciones e informará de ellas al órgano de dirección superior en su informe trimestral. Si su frecuencia o volumen dejan de ser excepcionales, lo advertirá de inmediato al órgano de dirección superior para suspenderlas y evaluar si Propi realiza actividades de carácter financiero conforme al artículo 3, literal b), del Decreto 15-2026. El detalle operativo se desarrolla en el Procedimiento de recepción excepcional de fondos por cuenta de terceros.",
  ""], exact=True, style_from=rl.find("El Oficial de Cumplimiento o el personal de negocios, cuando identifiquen"))
# ---- Anexo: procedimiento de recepción excepcional (16-sep-2026) ----
rl.insert_before("El Oficial de Cumplimiento mantendrá actualizado el registro de la versión vigente",
  "16. Procedimiento de recepción excepcional de fondos por cuenta de terceros, incluidos el registro de operaciones y el formato de instrucción o mandato escrito del desarrollador o propietario.",
  style_from=rl.find("15. Cláusulas contractuales modelo"))
# ---- Matriz de riesgo en la sección XI, formato V2/V3 (17-sep-2026) ----
# ---- Punto 1 de la auditoría: tabla de AUTORIZACIÓN (17-sep-2026, instrucciones de JR) ----
from lxml import etree as _et
from redline import q
def _tbl_de(needle):
    p = rl.find(needle); t = p
    while t is not None and t.tag != q("tbl"): t = t.getparent()
    assert t is not None, needle
    return t
def _set_cell(tbl, fila, col, texto):
    tr = [x for x in tbl if x.tag == q("tr")][fila]
    tc = [x for x in tr if x.tag == q("tc")][col]
    p = [x for x in tc if x.tag == q("p")][0]
    rpr = rl._first_rpr(p)
    rl._del_all_runs(p); rl._ins_run(p, texto, rpr)
def _borrar_fila(tbl, fila):
    tr = [x for x in tbl if x.tag == q("tr")][fila]
    trpr = tr.find(q("trPr"))
    if trpr is None:
        trpr = _et.Element(q("trPr")); ex = tr.find(q("tblPrEx"))
        tr.insert(list(tr).index(ex) + 1 if ex is not None else 0, trpr)
    m = _et.Element(q("del")); rl._mark(m); trpr.append(m)
    for pp in tr.iter(q("p")): rl._del_all_runs(pp)

_aut = _tbl_de("Asesor legal externo (AMC Legal)")
_borrar_fila(_aut, 1)                                   # fila "Elabora"
_set_cell(_aut, 2, 1, "Eduardo José Francés Argueta")      # Revisa
_set_cell(_aut, 2, 2, "Accionista (Asamblea General de Accionistas)")
_set_cell(_aut, 2, 3, "Acta 05-2026, folio 15")
_set_cell(_aut, 3, 2, "Accionista (Asamblea General de Accionistas)")  # Aprueba
_set_cell(_aut, 3, 3, "Acta 05-2026, folio 15")
R("Fecha de autorización: ____/____/______",
  "Aprobado por la Asamblea General de Accionistas según acta número 05-2026, folio 15 del Libro de Actas de Asambleas Generales de Accionistas, que aprueba también el proceso de administración del Riesgo LD/FT/FPADM y la matriz de riesgo contenidos en la sección XI (artículos 8 y 12 del Decreto 15-2026). Fecha de autorización: ____/____/______")

# ---- Sección XV y funciones del OC: evaluación anual del programa (17-sep-2026, decisión de JR) ----
D = rl.delete_para; IA = rl.insert_after
D("AUDITORÍA INTERNA", exact=True)
R("La auditoría interna, o quien ejecute funciones similares dentro de Propi, deberá elaborar y ejecutar anualmente",
  "Propi evaluará anualmente el cumplimiento y la efectividad de los Programas de Prevención LD/FT/FPADM contenidos en este Manual y en sus documentos complementarios (artículo 15 del Decreto 15-2026). La evaluación estará a cargo de la auditoría interna o de quien ejerza funciones equivalentes dentro de Propi o, en su defecto, de auditores externos especializados contratados para ese efecto.")
IA("Propi evaluará anualmente el cumplimiento y la efectividad de los Programas de Prevención", [
  "La modalidad, el alcance y el calendario de cada evaluación se definen en el Plan de Trabajo anual del Oficial de Cumplimiento, que este elabora durante el ejercicio anterior con el visto bueno del área legal y de la Gerencia General.",
  "Quien realice la evaluación deberá ser independiente del Oficial de Cumplimiento y de las áreas que ejecutan los controles evaluados, y no podrá haber participado en el diseño de los programas que evalúa."])
R("Se deberá emitir opinión respecto de la idoneidad y el funcionamiento de las políticas",
  "La evaluación concluirá con un informe que exprese su opinión sobre la idoneidad y el funcionamiento de las políticas y procedimientos adoptados para prevenir los delitos de LD/FT/FPADM, las deficiencias u omisiones materialmente significativas, las recomendaciones para superarlas y las medidas correctivas adoptadas. El informe se presentará al órgano de dirección superior y al Oficial de Cumplimiento, quien coordinará la evaluación y dará seguimiento a la implementación de las recomendaciones. El informe estará a disposición de la Superintendencia de Bancos a través de la Intendencia de Verificación Especial y, cuando corresponda emitir informe de aseguramiento, se remitirá copia dentro de los quince (15) días siguientes a su recepción.")
D("AUDITORÍA EXTERNA", exact=True)
D("Sin perjuicio de que el informe de aseguramiento de auditoría externa es obligatorio únicamente")
R("Instruir a la auditoría interna y externa, o quien realice funciones similares",
  "Coordinar con quien realice la evaluación anual del programa la verificación muestral del acuse de recibo o de la evidencia del envío de los reportes de transacciones sospechosas y en efectivo.")
R("Analizar e implementar las medidas correctivas derivadas de las observaciones de la auditoría interna",
  "Analizar e implementar las medidas correctivas derivadas de las observaciones de la evaluación anual del programa.")
IA("Diseñar el presente Manual y proponer su actualización.",
   "Elaborar el Plan de Trabajo anual del Oficial de Cumplimiento y someterlo a aprobación del órgano de dirección superior; el plan comprenderá, entre otras actividades, la capacitación, la evaluación anual del programa y el monitoreo y los reportes previstos para el ejercicio.", exact=True)

import matriz_block; matriz_block.build(rl)

# ---- Punto 2 de la auditoría: autorización individual del OC solo para PEP y riesgo alto ----
rl.replace_in("Diferimiento de la verificación",
  "y ninguna relación de negocios se establece sin el dictamen del Oficial de Cumplimiento",
  "y ninguna relación de negocios se establece sin que el expediente esté completo y validado conforme a la lista de verificación aplicable. La autorización individual del Oficial de Cumplimiento se requiere únicamente en los casos de clientes o contrapartes calificados como Personas Expuestas Políticamente o de riesgo alto, en los términos de esta sección")
rl.insert_after("Diferimiento de la verificación",
  "Validación de expedientes y control por muestreo. En los clientes y contrapartes de riesgo bajo y medio, el área responsable de la relación valida el expediente contra la lista de verificación aplicable —incluidos el cruce en listas y la identificación del beneficiario final— antes de habilitar la reserva o de entregar el número de cuenta. El Oficial de Cumplimiento verifica ese cumplimiento mediante revisiones por muestreo, con la periodicidad prevista en su Plan de Trabajo anual, y por excepción cuando se genere una alerta; de esas revisiones deja constancia documentada.")
rl.insert_after("Elaborar el Plan de Trabajo anual del Oficial de Cumplimiento y someterlo a aprobación",
  ["Autorizar el establecimiento o la continuidad de relaciones de negocios con clientes o contrapartes calificados como Personas Expuestas Políticamente o de riesgo alto, y verificar por muestreo la validación de los expedientes de riesgo bajo y medio.",
   "Designar, con el visto bueno de la Gerencia General y dejando constancia escrita, a la persona que lo sustituya durante sus ausencias temporales para efectos de las autorizaciones anteriores, sin que ello lo releve de su responsabilidad."])

# ---- Punto 3 de la auditoría: salida de operaciones en curso (Arts. 22 ¶3, 30, 38) ----
rl.insert_after("Abstención y terminación. Propi se abstendrá", [
  "Salida de operaciones en curso. Cuando la abstención o la terminación deba producirse respecto de una operación ya iniciada, la decisión la adopta el Oficial de Cumplimiento y consta en acta en la que se expresen los motivos, el estado de la operación, el destino de los fondos y la decisión sobre la comisión; el área comercial la ejecuta conforme a esa acta.",
  "Según el estado de la operación: a) si aún no se ha habilitado la reserva, no se habilita ni se entrega el número de cuenta para el pago; b) si la reserva está pagada y la operación no se ha escriturado, se comunica la terminación por causas comerciales o contractuales y se instruye la devolución de los fondos a la misma cuenta de origen del cliente; c) si la promesa de compraventa está firmada o la escrituración está programada, Propi se retira de la intermediación, no participa en el cierre ni gestiona el pago, y las consecuencias contractuales se rigen por lo pactado entre el cliente y el desarrollador o propietario.",
  "Propi no facturará ni cobrará comisión por la operación de la que se retire por esta causa; si la comisión ya se hubiere percibido, el Oficial de Cumplimiento documentará la decisión sobre su devolución.",
  "Las comunicaciones se harán conforme a los textos modelo aprobados por el Oficial de Cumplimiento para cada destinatario —cliente, desarrolladora o propietario, corredor externo y notario—, fundadas únicamente en causas comerciales o contractuales, sin referencia alguna al examen practicado, al Reporte de Transacción Sospechosa ni a la prevención del LD/FT/FPADM (artículo 38 del Decreto 15-2026).",
  "El acta, las comunicaciones y la evidencia de la devolución de los fondos se archivarán en el expediente por el plazo de cinco años y la persona se incluirá en la Lista de Control interna de personas no aceptadas. Lo anterior es independiente del examen y del eventual Reporte de Transacción Sospechosa, así como de las medidas de inmovilización y aviso al Ministerio Público que proceden ante coincidencias con las listas del Consejo de Seguridad de las Naciones Unidas (artículos 30, 43 y 44 del Decreto 15-2026).",
])
rl.replace_in("14. Formatos:",
  "texto modelo de comunicación de rechazo o terminación",
  "textos modelo de comunicación de rechazo o terminación, por destinatario (cliente, desarrolladora o propietario, corredor externo y notario)")

# ---- Punto 4 de la auditoría: RTS ante coincidencia confirmada en listas del CSNU (Art. 30) ----
rl.insert_after("De existir coincidencia con los nombres o datos de identificación",
  "Toda coincidencia confirmada, sea en la vinculación o durante la relación de negocios, obliga además a remitir con prontitud el Reporte de Transacción Sospechosa a la Superintendencia de Bancos a través de la IVE (artículo 30 del Decreto 15-2026).")

# ---- Punto 5 de la auditoría: universo único de colaboradores obligados (Art. 12, literal b) ----
rl.replace_in("El presente Manual es de observancia obligatoria",
  "cualquiera que sea la forma jurídica de su contratación; asimismo",
  "cualquiera que sea la forma jurídica de su contratación (en adelante, los colaboradores obligados); asimismo")
rl.replace_in("Luego de concluir con su proceso de capacitación anual",
  "el personal de Propi deberá someterse a una prueba",
  "los colaboradores obligados deberán someterse a una prueba")
rl.replace_in("Todo el personal de nuevo ingreso",
  "Todo el personal de nuevo ingreso, contratado o subcontratado, deberá recibir la inducción sobre prevención de LD/FT/FPADM durante los 30 días posteriores a su ingreso. El área de recursos humanos o su equivalente, en coordinación con el Oficial de Cumplimiento, son los encargados de programar la inducción a los empleados y personal subcontratado.",
  "Todo colaborador obligado de nuevo ingreso deberá recibir la inducción sobre prevención de LD/FT/FPADM durante los 30 días posteriores a su ingreso o a su vinculación. El área de recursos humanos o su equivalente, en coordinación con el Oficial de Cumplimiento, son los encargados de programar la inducción del personal; la de los directores, agentes, corredores e intermediarios la programa el Oficial de Cumplimiento.")
rl.replace_in("Propi entregará a todos los funcionarios",
  "a todos los funcionarios, empleados, personal temporal o subcontratado el Código de Ética",
  "a los colaboradores obligados el Código de Ética")
rl.replace_in("El presente Manual o sus modificaciones se darán a conocer",
  "a todos los funcionarios, empleados, directores, agentes, corredores e intermediarios de Propi",
  "a los colaboradores obligados")

# ---- Punto 6 de la auditoría: un solo criterio para el nivel de DDC (Arts. 21.4 y 22 ¶1) ----
rl.replace_in("De conformidad con el enfoque basado en riesgo",
  "el nivel de debida diligencia aplicable a cada cliente se asigna combinando el valor de la operación con el perfil de riesgo del cliente; el perfil de riesgo solo puede elevar el nivel, nunca reducirlo",
  "el nivel de debida diligencia aplicable a cada cliente se asigna conforme al nivel de riesgo que se le haya asignado (bajo, medio o alto); el valor de la operación se pondera como uno de los factores de esa clasificación y, además, obliga a aplicar las medidas de debida diligencia cuando supere los umbrales que establezca la reglamentación")

# ---- Punto 7 de la auditoría: exención de responsabilidad conforme al Art. 37 ----
rl.replace_in("Queda terminantemente prohibido revelar a terceros",
  "Propi, sus directores, gerentes, funcionarios, oficiales de cumplimiento, representantes legales y empleados quedan exentos de responsabilidad legal por haber proporcionado de buena fe información a las autoridades competentes, incluida la comunicación de RTS (artículo 37).",
  "Propi, sus directores, gerentes, administradores, funcionarios, oficiales de cumplimiento, representantes legales y empleados debidamente autorizados quedan exentos de responsabilidad legal por haber proporcionado de buena fe a las autoridades competentes información, documentación, expedientes y registros, siempre que se cumplan las disposiciones del Decreto 15-2026, su reglamentación y demás disposiciones aplicables, incluida la comunicación de RTS a la Superintendencia de Bancos a través de la IVE (artículo 37).")

# ---- Punto 8 de la auditoría: automatismo solo para listas del CSNU (Arts. 43 y 22) ----
rl.replace_in("El potencial cliente o sus representantes legales",
  "u otra lista que Propi, a través de su Oficial de Cumplimiento, establezca.",
  "u otras listas de sanciones y de cautela nacionales e internacionales que determine el Oficial de Cumplimiento. La coincidencia con las listas del Consejo de Seguridad de las Naciones Unidas impide la vinculación; las coincidencias con las demás listas generarán una alerta que el Oficial de Cumplimiento analizará y confirmará antes de rechazar o terminar la relación.")

# ---- Cierre de la matriz: colores = nivel de riesgo (Arts. 8 a 10) ----
rl.insert_after("Verde: al menos semestral",
  "El color resulta de cruzar la probabilidad con la consecuencia conforme a la Tabla 3 y expresa el nivel de riesgo: rojo, alto; amarillo, medio; verde, bajo.")

# ---- Cierre previo al envío: señales de alerta en el Anexo (Art. 12, c) y conservación (Art. 34) ----
rl.replace_in("7. Procedimiento de Reportes",
  "reporte mensual sectorial y tablero de monitoreo, con sus plazos internos y umbrales.",
  "reporte mensual sectorial y tablero de monitoreo, con sus plazos internos y umbrales; incluye el catálogo de señales de alerta y los escenarios de monitoreo por línea de negocio, que el Oficial de Cumplimiento mantiene actualizados.")
rl.replace_in("Propi mantendrá, por un período no menor",
  "dichos registros deben ser suficientes para permitir la reconstrucción íntegra de cada operación y atender los requerimientos de las autoridades competentes (artículo 34 del Decreto 15-2026).",
  "así como los demás registros relacionados con el cumplimiento de las obligaciones del Decreto 15-2026, entre ellos el registro de transacciones en efectivo, los reportes remitidos y sus acuses, las actas de autorización, los expedientes de proveedores, empleados y corredores, la evidencia de capacitación, los informes de la evaluación anual y la evaluación de riesgo; dichos registros deben ser suficientes para permitir la reconstrucción íntegra de cada operación y atender los requerimientos de las autoridades competentes (artículo 34 del Decreto 15-2026).")

print("EDICIONES EN REVISIÓN (con matriz):", rl.save())
