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
import matriz_block; matriz_block.build(rl)
print("EDICIONES EN REVISIÓN (con matriz):", rl.save())
