---
type: index
date: 2026-10-20
last-touched: 2026-10-20
tags:
  - index
  - tema/infraestructura
  - proyecto/understanding-kids
---

# Mapa del Google Drive (jcastaneda@ y joserca95@)

Mapa legible del Drive de JR. Lo mantiene el agente `buscador-drive` (ver [[subagentes]]); se rehace cada semana. Solo metadatos: nunca contenido, nunca nombres de pacientes. El **índice completo** (una línea por archivo, con ruta, dueño, fecha, tamaño y enlace) vive fuera del Vault:

- `~/Claude/state/drive-index/jcastaneda@kidsunderstanding.com.jsonl`
- `~/Claude/state/drive-index/joserca95@gmail.com.jsonl`

Relacionado: [[mapa-de-archivos]] (lo local), [[drive]] (cómo se usa gws).

## Resumen del recorrido (2026-10-20)

| Cuenta | Elementos | Carpetas | Archivos | Propios |
|---|---|---|---|---|
| jcastaneda@kidsunderstanding.com | 22.469 | 3.333 | 19.136 | 8.612 |
| joserca95@gmail.com | 12.853 | 2.095 | 10.758 | 939 |

- Recorrido por API (`gws drive files list`, `corpora=allDrives`, sin papelera). **No hay unidades compartidas** en ninguna cuenta: todo lo de la clínica son carpetas compartidas, casi todas de `contacto@kidsunderstanding.com`.
- Las dos cuentas ven las mismas carpetas grandes de la clínica (Administración zona 14, Talleres, Fotografías, Administración CAES). jcastaneda@ ve además Inventario, Material, Evaluación, Imprimibles, contabilidad, Recibos, Yellow Me y el respaldo de la Mac.
- Rutas que empiezan en «(compartido)» = la carpeta raíz no es de JR (está en «Compartido conmigo»).

## Árbol principal (clínica)

### Administración zona 14 · `1ZJ0IzlXr-_NAR4Cj34va9mB9WZBLEI79`
Dueño contacto@. En el disco montado aparece como «Administración (1)». Ojo: el nombre real lleva espacio al inicio y al final (« Administración zona 14 »). ~5.700 elementos.

| Carpeta | id | Qué tiene |
|---|---|---|
| Administración Pagos | `16M7rt7HY5TB-JDnGe7MujPldL-5rbm7O` | Cierres de caja, estados de cuenta, resúmenes de fin de mes, horas trabajadas (2022-23) |
| · Resumen fin de mes | `1A1BZYhgk3eS_nlJoWasRSt2n5RY5ZS-W` | Subcarpetas Resumen 2022 a 2026 |
| · · Resumen 2026 | `1pa2PcMdj3y_Eo2nNSBr68aUejLEMFhw7` | Resúmenes mensuales de zona 14 (ver patrones abajo) |
| · Cierres de caja zona 14 | `15O_Rx7Qf4d-0mjyLkrDcObzJQd7OxiRU` | Cierre de caja 2022 a 2026 |
| · · Cierre de caja 2026 | `1MWzQOvZ7VkqeosTnFGFlgccAoVSjsP1X` | Una subcarpeta por mes con su hoja |
| · Estados de cuenta zona 14 | `1N7JWFV4gqJgB-_tQFNHOFQfHvs_yjiBt` | 2025 y 2026; PDF por banco y moneda (BI, GYT Q/US$, Recurrente Q/US$) |
| · · 2026 | `1aX7ACEvyf6dSNcRxl6KDc2nYAy12HrMB` | «Estados de cuenta <Mes>/» |
| Artes | `19OTddA7oieII4MJWxy50nL-WPrdkv4pd` | Vitrina de artes que publica Magoo |
| · 2026 | `1LT2idGH0gfX6399nHqrBJ8cbzhs7P6cQ` | Campañas, Integración Sensorial, Publicidad, Understanding Kids |
| · · Understanding Kids | `1EkzqQstoz65aXXK745vJArlXDxSQ-qsw` | Frases, Informativo, Servicios (`1x1Mr3VTimGArQ84xw-utQkgvQO3XmAaW`), Promociones, Recursos, Testimonios (estas tres vacías) |
| · · Integración Sensorial | `1wda0OWvGlrm5tjCKqDFWTYwJBxW0IzIw` | Misma estructura que UK |
| · · Campañas | `1mc3fbHku7fsJ3T07wmdVX9yHdxYspnae` | Diplomado de Autismo, Especialización Alimentación 2026 (+ Mockups) |
| · · Publicidad | `1obDOg8_MVKqMfxhFvLiytn0EkNH2jZlj` | Carpetas «subido…» |
| · Artes (JR), Flashcards, Planes | | Artes viejas 2022-2023 |
| Facturas | `1yCB31NIwmGeEj9BQRLm4oSdFWMWXMnsZ` | Terapeutas (por año, mes y quincena), Otras, Renta (2022) |
| · Terapeutas/Facturas 2026 | `1CHEoFRM_Jbbmy3FCLKgKmkEnp3QJV9ZO` | «<Mes> 2026/Primera Quincena/», «Segunda Quincena…/»; un PDF por terapeuta |
| Inscripción y políticas de pago | `1q9RApqoPRhWfGSszY6j0lyKcKJh2cpAl` | Fichas de inscripción (PDF y Forms), Manual nuevos clientes, Política de descuentos, Políticas de pago |
| · Políticas de pago | `1E6GA06y4eoDhWQvIjFoNYMghQ2G1Cmc9` | Servicios en clínica / a domicilio / virtuales (PDF 2023) |
| Expedientes | `1312VD9dy0gsGoIxBW3985TXFRRRf70OD` | Expedientes de personal: 15 expedientes activos + «Anteriores» (14) + «Practicantes». Contratos, IGSS, bono 14, vacaciones |
| Informes de Seguimiento | `1LP7FdhndZBItrBqWX62OceubNJQA0qbX` | ~3.000 elementos. Por terapeuta (11 carpetas) y dentro por paciente o por año (≈81 carpetas de pacientes en el segundo nivel, más «Terapeutas anteriores»). **Sensible** |
| Formación continua | `1j7hcmAxe4ecpJKybguBa8g9wC50pBDMS` | Diplomados, máster, cursos del equipo |
| Sociedad Anónima | `1znQiBI8kZUFH1e9klXqoJRvLi8c2y76j` | Licencias sanitaria y ambiental, representación legal, contador, QPayPro, tarjeta Pyme |
| Página web | `1eL84GwYT5AntSMxP2u0G87ot69V0jlGh` | Material gratuito, historias sociales |
| Logo | `1tqZS9tqxdH87AcgdrdEiUQcJzVSaxW6i` | Logos UK, IS, Muffin; ManualDeMarca_UnderstandingKids.pdf |
| Blog | `1SwGSN0ofSRzf8TjFfEJrft8aa3CzftZO` | 2025, 2026 |
| IGSS | `1LdQ-f6gV9uyetg9MYNhM6Glt1xT4Kthu` | Planillas 2023 |
| Otras menores | | Análisis ventas y empresa (2022), Cartas de Materiales, Contenido redes sociales, Currículum recepcionistas, Curso de vacaciones, Flyers, Parqueo, Trifoliares, Webinars, Metaverse, _Codex |

### Administración CAES · `1aPckEUvCN2YSGtUgFZU7i-UaG_Q4w2Oz`
Dueño carretera@. Pese al nombre, hoy es casi solo **personal**:
- `Expedientes ` (`1rZCZ1mcmL_DTuR2iXps6qTYECEKGO77l`): 4 expedientes activos + «SE DIO DE BAJA» (3).
- `Inventario Material` (`1Sx4oI6VCS10bTHghtYvpCA_61IHJucBq`): INVENTARIO CAES.xlsx.
- `Resumen Fin de Mes /Resumen 2026` (`1EoxW5cfv-9Vgp2dKmfhxIhddR0XPfdba` / `1NtYtZzYw0GVtOL4vgL_eqSXM_5aIWUUf`): **vacía**, y solo la ve joserca95@ (jcastaneda@ no la ve).

### Carretera
**No encontré una carpeta de administración de Carretera** en ninguna de las dos cuentas (búsqueda por nombre «Carretera» y recorrido completo). Lo único con «Carretera» en el nombre: `2025-12-11 - Walter - DATOS Carretera 2026.xlsx` (en Documentos contables, 06 Presupuestos). La cuenta carretera@ es dueña de Administración CAES, Documentos RGAE y Grabaciones; si hay carpeta de Carretera, no está compartida con JR.

### Otras carpetas compartidas de la clínica (raíz en «Compartido conmigo»)

| Carpeta | id | Dueño | Qué tiene |
|---|---|---|---|
| Talleres zona 14 | `19XFN_MxgAklPxWg2wtIUQUrqAcY9JMi9` | contacto@ | Una carpeta por taller, curso o diplomado (~30), con artes, material y fichas; «Talleres antiguos» |
| Fotografías Understanding Kids | `1qcyRclIIg7JzuTTNO4rYWk55gya6X6EB` | contacto@ | Fotos por taller y servicio, Equipo, Clínica, Artes viejas |
| Evaluación Understanding Kids | `1RVXwc9yOGKmucTFXOPn65YRVlouPUMmk` | contacto@ | Protocolos y manuales de evaluación por área (Autismo, TDAH, Lenguaje, Alimentación…) |
| Imprimibles zona 14 | `1T1LngBhqpe22jlCZCkAk9Qr63nm-8mHN` | contacto@ | Material imprimible por área |
| Material | `1HQq_Rei_4vtME4b-CNT6jWx3OnPnMRci` | contacto@ | Material terapéutico y escolar (Campoalegre, Inglés, Lenguaje…) |
| Inventario | `1-xV1-WtwD7eP4DnycNTwgfwXqER26mhG` | contacto@ | Imágenes de juguetes (1.348), historial de inventarios, formato de precio de venta de juguetes 2026 |
| Documentos contables para JR - Elder, Walter y Francisco | `1aVKI7AAuhcTrE9g6DMaCTt-65qdd90KD` | msamayoa@ | La carpeta de contabilidad que armó Magoo (ago-2026): 01 Minutas … 09 Soportes |
| · 02 Estados financieros y balances | `1tohs65oTxBkCXxibXUtRlE6hR_tgzYIM` | msamayoa@ | Por año 2022-2026, más EEFF Junio 2026 suelto |
| Recibos 2026 | `1BMx1qKbpRVjmW_PaiA5Busbe2gZrOgK_` | msamayoa@ | Recibos Google Workspace, Facebook, pruebas UVG |
| Planificación 2026 | `1tWQENHzkScRdAjy75zulf-Ll6NkPj7Wz` | msamayoa@ | Diplomados Autismo e IS |
| Cuentos para JR · Contenidos y fotos · Octubre 2026 | `1t6t7yLvBzxU7xBJvgXDq1glHVBT0vZQE` | msamayoa@ | 7 cuentos con fotos |
| Documentos RGAE | `1sZMsEcIJ_RRoqcefSuFNn2flCZywyVEW` | carretera@ | Papelería RGAE (actas, patentes, arrendamiento, recibo de luz) |
| Grabaciones / Grabaciones 2026 | `1D0zKau49ZSohwMWjFP0L-bhqB5oMCqkU` | carretera@ | Grabaciones de 2026 |
| Meet Recordings | `1_81MU_5Av3tAdIYYFhxw29VM93K5qN65` | contacto@ | Grabaciones de Meet |
| Formatos de cartas | `11HI2B9dD1DpilStbANADd52dvs7ANxMO` | contacto@ | Respuestas del formulario de candidatas a terapeutas |
| Planes terapeuticos | `1GfKDThUJwQ0tUVlufdIOUtC6CSGaTiYd` | contacto@ | 9 carpetas de pacientes. **Sensible** |
| Planes de estimulación temprana | `1h6Delhyfg5Xp5F-vx_STC6NQWLJsWZeA` | contacto@ | Planes por paciente. **Sensible** |
| Yellow Me | `12j995Td7UOvn6ITOOMvaGEXTwTyfUYNE` | contacto@ | Tienda de juguetes (2023-2025) |

Documentos sueltos clave (raíz compartida):
- **Servicios zona 14** (Doc) `1KYv3NWVwwaW_-OXVZk6JsZxmAJF_sxIxahYxnpNTQvc`, contacto@, editado 2026-10-20. **No encontré** equivalentes «Servicios Carretera» ni «Servicios CAES» en ninguna cuenta.
- Guía interna para terapeutas — Honorarios y pagos por servicio (Doc) `1DyGf-4iNjdP8k5Dh2QdnI6P3M6dJZZqsJIglBX3u-pc`, msamayoa@.
- Manual de información para recepción — Understanding Kids (Doc) `13junOrj3XE-LAY0p1SXnVXzo41yH9cSPBfmlN8uWmoo`, msamayoa@.
- Listado de procesos (Doc) `1dI1p9cB2TdaoNY0LXEbpffW9_QEX7wN7bJRcYlY2uWw`; Misión, Visión y Valores.docx `1gEmu5xNvfa4hP26Z7hc8UHS1sLDig4hv`; Notas - Reunión semanal UK `1WEPCuKh_RpC_kZJwHmw_K7P_hHPaogzsfUHf4JN2EP8`.
- Clínica 2 - Flujo de Caja.xlsx `1XI4Lq_NQ_bEoJcuiQpGqqTtLlTR3jKTm` e Inversiones Multidisciplinarias Clinica 2 PTTO 2025.xlsx `1LDA2IqgupHgLVaCvuy_EupJLOcJAltkh` (msamayoa@, may-2025).

## Mi unidad de jcastaneda@

- `Contratos` (`192yKHl6vhWFE9v5vdGjtSQaAhbAy0b7V`): **Plantillas Maestras 2026** (`1w3KCIXC8y7BPVoSMK1zuZLCUuoIXRDoa`: Contratación, Adendas, Terminación), Para Firma 2026-08, Revisados (2022).
- `Understanding Kids` (`1rsNGI0Cf4M47V-kJpmAkicDx7m5isp5q`): documentos, entrevistas y tipografía viejos (2021-2024).
- Sueltos: «Understanding Kids - Master Financial Sheet» `1Eur1BxfFHk2vpOUxHu_IsuoiO4HRaJVyR387kAcdd6s` (abr-2026), «Flujo de Caja UK» (2022), «Base de Datos - UK» (2022), «Numeros de Cuenta» (2024), «Calendario de Publicaciones» (2024).
- Accesos directos «Administración» → zona 14 y → CAES.
- **My MacBook Pro / Understanding Kids** (`18jFAvDNDZwxquQweaTTvseuv72mbYVjR`, 7.403 elementos): copia que sube Google Drive para escritorio de la carpeta local `~/Documents/Understanding Kids`. Incluye `Artes/` (Aprobadas, Pendientes de Revision, Sistema, Fotos, _Descartadas), `Contratos/`, `Pagos/`, `Asambleas/`, `Documentos S.A./`, `Campañas/` y 4.827 archivos de `vendor/nano-banana-mcp-local`. También `Contratos/Servicios Profesionales` con los contratos 2026 de terapeutas (editados 2026-10-20).

## Mi unidad de joserca95@ (personal)

- `UFM` (`10OClaxpPc4slTcbp64iOY1dqBE4CRS02`, 851): Derecho y Administración, apuntes de la universidad.
- `Control de Gastos - Casa`, `Clientes`, `Taiwan`, `Nosh`, `Rakuten Kobo`.
- Compartido conmigo, lo grande: Propi (`Docs, Alianzas comerciales Propi GT` `1E4rKEIVQse5LeRlZ5n_yY0IKRS00H3fb`, `MANUALES PROPI` `1xqinfCruD0hlG4kHvHjwSiBu0P6BOIAi`, `IVE - SIB` `1maH7e8yeYAQGYf1t8tkKS0fJeeukuQMa`), VI Semestre (2013), 2021 MOFA - Taiwan, opciones de cabañas y casa z. 15, y unas 450 piezas sueltas (fotos, contratos, PDFs).

## Dónde está cada documento recurrente

| Tipo | Dónde | Patrón de nombre |
|---|---|---|
| Resumen mensual zona 14 | AZ14/Administración Pagos/Resumen fin de mes /Resumen <año>/ | Desde jul-2026: «Resumen <Mes> 2026 — Zona 14» dentro de «Resumen Mes de <Mes> 2026/». Antes, nombres sueltos («Resumen Mes de Marzo 2026», «Resumen del mes de enero 2026: zona 14»). Magoo ya creó Octubre, Noviembre y Diciembre 2026 |
| Resumen mensual Carretera / CAES | **No existen** en lo que JR ve. La carpeta CAES/Resumen Fin de Mes/Resumen 2026 está vacía | |
| Cierre de caja zona 14 | AZ14/Administración Pagos/Cierres de caja zona 14 /Cierre de caja <año>/ | «Cierre de caja Mes de <Mes>/» con una hoja dentro |
| Estados de cuenta bancarios | AZ14/Administración Pagos/Estados de cuenta zona 14 /<año>/ | «Estados de cuenta <Mes>/» con PDF por banco y moneda |
| Estados financieros (contador) | Documentos contables…/02 Estados financieros y balances/<año>/ | «AAAA-MM-DD - <Francisco/Walter> - Inversiones Multidisciplinarias Estados…» |
| Honorarios del contador | Documentos contables…/05 Honorarios del contador/<año>/ | «AAAA-MM-DD - Elder - Inv. Multidisciplinarias Honorarios…» |
| Impuestos y SAT | Documentos contables…/03 Impuestos y SAT (`1JOkfKLLR3b9mzbSELz23sWRDtKYk8QQB`) | |
| Facturas de terapeutas | AZ14/Facturas /Terapeutas/Facturas <año>/<Mes>/<Quincena>/ | PDF con nombre de la terapeuta |
| Precios de servicios | Doc «Servicios zona 14»; Inscripción y políticas de pago/Política de descuentos .pdf (`1qLGrLN2fctW91a_k9fp8cUYL2Un9KmNG`, ene-2026); Guía interna de honorarios (pago a terapeutas) | |
| Políticas de pago | AZ14/Inscripción y políticas de pago/Políticas de pago/ (2023) | |
| Fichas de inscripción | AZ14/Inscripción y políticas de pago/: Form «Ficha de inscripción 2026 zona 14» `1ZEBWF4Yxh3AugzjGEUvj1nZ_TpegfZOQs3zC5vcESGQ`; talleres: dentro de cada carpeta de Talleres zona 14 | |
| Contratos de terapeutas | Plantillas: Mi unidad/Contratos/Plantillas Maestras 2026. Firmados: AZ14/Expedientes/<persona>/Contrato… y CAES/Expedientes /<persona>/CONTRATO | |
| Artes publicadas | AZ14/Artes/2026/<Marca>/<Tipo>/ ; Magoo renombra a «subido…» al publicar | |
| Informes de pacientes | AZ14/Informes de Seguimiento/<terapeuta>/<paciente o año>/ | |
| Manuales de evaluación | Evaluación Understanding Kids/<área>/ | «Manual de Evaluación …» |

## Desorden, duplicados y versiones que confunden

- **Secreto en Drive:** el respaldo de la Mac sube `Understanding Kids/.secrets/` (contiene `gemini_api_key`, abr-2026). Conviene excluir esa carpeta del respaldo o rotar la llave.
- Resumen 2026 de zona 14: mezcla de hojas sueltas y subcarpetas; dos hojas para mayo («Resumen Mes de Mayo /Resumen del Mes de Mayo» y «Resumen Mes de Mayo 2026») y dos para septiembre («Resumen Mes de Septiembre » de contacto@ y «Resumen Septiembre 2026 — Zona 14» de msamayoa@); carpeta con errata «Reseumen Mes de abril»; junio va en «Resumen de Junio/».
- Cierre de caja 2026: la carpeta «Cierre de caja del mes de Febrero» contiene las hojas de enero, febrero y marzo.
- Dos «Copia de Resumen mes de diciembre 2025» en la Mi unidad de joserca95@ (abr-2026).
- Nombres con espacios al inicio o al final (« Administración zona 14 », «Facturas », «Expedientes », «Resumen fin de mes ») rompen búsquedas exactas.
- «Administración CAES» no tiene administración: solo expedientes de personal e inventario.
- Contratos repartidos en 4 lugares: Mi unidad/Contratos, My MacBook Pro/…/Contratos, AZ14/Expedientes y sueltos en la raíz compartida.
- Respaldo de la Mac con 4.827 archivos de código (`vendor/nano-banana-mcp-local`) y carpetas técnicas (`.superpowers`, `tmp`, `output`).
- Mi unidad de jcastaneda@ con 5 «Hoja de cálculo sin título» y 4 «Documento sin título».
- 131 pares de archivos con el mismo nombre en la misma carpeta en jcastaneda@ y 120 en joserca95@ (sin contar el respaldo de la Mac).
- Políticas de pago de 2023 conviven con la Política de descuentos 2026.

## Cambios desde el mapa anterior

Primer mapa (2026-10-20). No hay versión anterior con la cual comparar.
