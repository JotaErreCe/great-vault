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

print("EDICIONES EN REVISIÓN:", rl.save())
