from redline import Redline
rl = Redline("unpacked/word/header1.xml", "José Roberto Castañeda", start_id=12000)
rl.replace("MANUAL DE CUMPLIMIENTO DEL SISTEMA INTEGRAL DE PREVENCIÓN DE LDA/FT/FPADM", "MANUAL DE PREVENCIÓN LD/FT/FPADM")
rl.replace_in("Revisión: 00", "00", "01")
rl.replace_in("Fecha: 12-sept-24", "12-sept-24 Código: MA-SIP-24", "10-sept-26 Código: MA-SIP-26")
print("encabezado: ediciones", rl.save())
