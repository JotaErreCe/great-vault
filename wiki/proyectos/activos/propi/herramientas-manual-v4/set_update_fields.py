from lxml import etree
W="http://schemas.openxmlformats.org/wordprocessingml/2006/main"; q=lambda t:"{%s}%s"%(W,t)
p="unpacked/word/settings.xml"; t=etree.parse(p); r=t.getroot()
if r.find(q("updateFields")) is None:
    u=etree.Element(q("updateFields")); u.set(q("val"),"true")
    for tag in ["hdrShapeDefaults","footnotePr","endnotePr","compat","docVars","rsids","mathPr","attachedSchema","themeFontLang","clrSchemeMapping","doNotIncludeSubdocsInStats","doNotAutoCompressPictures","forceUpgrade","captions","readModeInkLockDown","smartTagType","schemaLibrary","shapeDefaults","doNotEmbedSmartTags","decimalSymbol","listSeparator"]:
        el=r.find(q(tag))
        if el is not None: el.addprevious(u); break
    else: r.append(u)
    t.write(p,xml_declaration=True,encoding="UTF-8",standalone=True)
