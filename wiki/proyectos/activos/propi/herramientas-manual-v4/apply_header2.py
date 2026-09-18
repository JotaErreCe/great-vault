# apply_header2.py — revisión 02 y fecha de presentación (control de cambios, autor JR)
from redline import Redline
h = Redline("unpacked/word/header1.xml", "José Roberto Castañeda", start_id=30000)
h.replace_token("01", "02")
h.replace_token("10-sept-26", "17-sept-26")
print("header:", h.save())
