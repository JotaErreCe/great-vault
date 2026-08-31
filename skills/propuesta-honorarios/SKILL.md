---
name: propuesta-honorarios
description: Redacta y genera Propuestas de Honorarios en .docx con el formato de AMC/CAM Legal (José Roberto Castañeda Arriola). Úsalo cuando JR pida armar, cotizar o mandar una propuesta a un cliente, cotizar honorarios por un trámite o servicio jurídico (constitución de sociedad, nombramientos, mandatos, residencias, permisos de trabajo, actas notariales, revisión de contratos, asesoría por hora), o cuando diga "hazme una propuesta para X".
---

# Propuesta de Honorarios — AMC / CAM Legal

Genera el documento con `scripts/build_propuesta.py`, que copia una plantilla `.docx`
real (membrete, pie de página, logo, estilos y tema originales) y solo reescribe el
cuerpo. Nunca armes el `.docx` desde cero: perderías el membrete y la tipografía.

```bash
python3 scripts/build_propuesta.py spec.json "/ruta/Propuesta - Cliente - Asunto.docx"
```

Guarda las propuestas en `~/Documents/AMC Legal/Propuestas/`, con el nombre
`Propuesta - <Asunto>.docx` o `Propuesta <Cliente> - <Asunto>.docx`.

## Antes de escribir

Necesitas cinco datos. Si falta alguno, pregunta antes de generar — no inventes montos.

1. **Cliente y destinatario.** Persona o entidad a quien va dirigida.
2. **Qué se va a hacer.** El desglose de trabajos, en el nivel de detalle que el
   cliente necesita para entender qué está pagando.
3. **Honorarios.** Monto fijo, tarifa por hora, o mensualidad. Siempre "+ IVA".
4. **Gastos.** Si el trámite los tiene (registrales, timbres, aranceles), van en
   sección aparte con estimado y, si conviene, tabla de desglose.
5. **Plazo estimado**, cuando aplique.

## Estructura del documento

Siempre en este orden:

1. Fecha, alineada a la derecha. Formato: `Guatemala, 22 de septiembre de 2025`.
2. Destinatario en negrita, tres líneas: nombre, `Ciudad de Guatemala,`, `Guatemala`.
3. Título centrado en azul: **Propuesta de Honorarios**.
4. Saludo: `Estimado <Nombre>,` — o `Estimados,` si va a una entidad.
5. Párrafo de entrada (ver fórmulas abajo).
6. Secciones numeradas en romanos (I., II., III.), encabezado en azul y negrita.
   El orden canónico es **Trabajos a Desarrollar** → **Honorarios Profesionales**
   → **Gastos** (esta última solo si hay gastos de terceros).

   Cuando el encargo es complejo y el listado de trabajos se alarga, conviene
   abrirlo en secciones propias — **Trabajos a Desarrollar** → **Requisitos y
   Documentación Necesaria** → **Tiempos Estimados** → **Honorarios Profesionales**
   → **Gastos**. Es la estructura que JR usó en la propuesta de mandatos para Propi
   y hace el documento mucho más legible que meterlo todo bajo Trabajos.
7. Separador `-------------------------------------O-------------------------------------`
8. Cierre, `Atentamente,`, nombre y —opcionalmente— teléfono.

## Fórmulas de la casa

Estas frases se repiten en todas las propuestas. Reúsalas literalmente.

**Entrada, caso general:**
> De acuerdo a su requerimiento, a continuación, le presento la descripción de los
> trabajos a realizar, así como la **Propuesta Honorarios** que corresponden a dichos trabajos.

**Entrada cuando el encargo es un trámite concreto:**
> De acuerdo a su requerimiento, a continuación, nuestra **Propuesta Honorarios**
> para <el trámite> y su inscripción respectiva en <el registro>.

**Apertura del listado de trabajos:**
> Servicios Jurídicos que se extienden, pero no se limitan a:

**Plazo:**
> El trabajo antes descrito será de un plazo estimado de <N> mes(es).

**Gastos por cuenta del cliente (cuando no hay tabla):**
> Además de los honorarios, correrán por su cuenta todos los gastos en que se deba
> incurrir para la realización de los trabajos solicitados.

**Liquidación (cuando sí hay gastos que el despacho adelanta):**
> Al quedar finalizados los trámites, nosotros le presentaríamos la liquidación
> respectiva a efecto de determinar si existe un saldo acreedor o deudor con
> respecto a los gastos.

**Forma de pago (opcional, se usó en residencias):**
> Los honorarios se cancelan en un 50% al ser contratados y el saldo al momento de
> entregar las resoluciones correspondientes. Los gastos se pagan al momento que el
> procedimiento lo requiera y se comprueban con los recibos que emite la autoridad
> correspondiente.

**Cierre:**
> Quedo a su disposición para cualquier duda o comentario relacionado a lo anterior.

## Tono

Usted, formal, primera persona singular (`le presento`, `quedo a su disposición`) —
aunque los honorarios y gastos se enuncian en plural de despacho (`nuestros honorarios`,
`nosotros le presentaríamos`). No adornes: la propuesta describe y cotiza, no vende.
Sin adjetivos de valor, sin "nos complace", sin cierres cálidos.

Escribe limpio. Las propuestas viejas traen erratas (`serpa`, `ascientes`,
`De al Renovación`) — no las repliques.

## Convenciones tipográficas

- **Negrita** (con `**...**` en el spec) para montos, el término *Propuesta Honorarios*
  cuando aparece en el cuerpo, y los términos que el cliente debe fijar.
- Los montos en quetzales van `Q.5,000.00` o `Q5,000.00`; en dólares `US$ 500.00`.
- Siempre explicitar `+ IVA` o `más el Impuesto al Valor Agregado (IVA)`.
- Cuerpo justificado. Todo lo maneja el generador.

## El spec JSON

```json
{
  "plantilla": "membrete",
  "fecha": "Guatemala, 31 de agosto de 2026",
  "destinatario": ["Nombre del Cliente", "Ciudad de Guatemala,", "Guatemala"],
  "saludo": "Estimado Julio,",
  "intro": "De acuerdo a su requerimiento, ... la **Propuesta Honorarios** ...",
  "secciones": [
    {
      "titulo": "Trabajos a Desarrollar:",
      "bloques": [
        {"texto": "Servicios Jurídicos que se extienden, pero no se limitan a:"},
        {"lista": ["Primer trabajo.", "Segundo trabajo."], "tipo": "letra"},
        {"texto": "El trabajo antes descrito será de un plazo estimado de 1 mes."}
      ]
    },
    {
      "titulo": "Honorarios Profesionales:",
      "bloques": [{"p": "Los honorarios ascienden a **Q.1,250.00 + IVA**."}]
    },
    {
      "titulo": "Gastos:",
      "bloques": [
        {"p": "Los gastos ascienden aproximadamente a **Q.950.00**."},
        {"tabla": {
          "titulo": "Gastos para la constitución de S.A.",
          "columnas": ["Concepto", "Detalle", "Gastos"],
          "filas": [["Constitución de S.A.", "Edicto", "Q30.00"],
                    ["^", "Hojas de Protocolo", "Q110.00"]],
          "total": ["^", "TOTAL", "Q140.00"]
        }},
        {"p": "Al quedar finalizados los trámites, nosotros le presentaríamos la liquidación respectiva..."}
      ]
    }
  ],
  "telefono": "+502 5574-9748"
}
```

Claves y matices:

- `plantilla`: `"membrete"` (pie de página azul marino con el logo CAM y los datos
  de contacto) o `"simple"` (solo filetes azules arriba y abajo). Por defecto usa
  **membrete**; es la versión de marca. Usa `simple` solo si JR lo pide.
- Tipos de bloque dentro de `bloques`:
  - `{"p": "..."}` — párrafo con aire arriba y abajo (estilo `NormalWeb`). Es el
    default para prosa.
  - `{"texto": "..."}` — párrafo pegado al anterior, interlineado 1.15. Úsalo para
    la línea que introduce una lista y para el plazo.
  - `{"lista": [...], "tipo": "letra"|"numero"|"vineta"|"romano"}` — `letra` da
    `a) b) c)`, `numero` da `1. 2. 3.`. Cada lista reinicia su numeración.
  - Sublistas: en vez de una cadena, pasa
    `{"item": "Texto padre", "sub": ["hijo 1", "hijo 2"], "tipo": "letra"}`.
  - `{"tabla": {...}}` — el encabezado sale blanco sobre azul marino de marca.
    `"^"` en una celda la fusiona con la de arriba (para la columna *Concepto*
    que abarca varias filas). `total` es opcional y sale en negrita.
- `fecha`: escríbela completa, tal cual debe aparecer.
- `aire_superior`: número de líneas en blanco antes de la fecha (default 3).
- `firma`: default `José Roberto Castañeda Arriola`.
- `telefono`: omítelo si no lo quieres en la firma.

## Verificar antes de entregar

Renderiza y míralo — el formato importa tanto como el contenido. En esta Mac no hay
LibreOffice ni pandoc, y el `save as` de Word por AppleScript está roto.

**Propuesta de una página** — Quick Look basta y es instantáneo:

```bash
qlmanage -t -s 1400 -o /tmp/ "/ruta/Propuesta - X.docx"
```

**Propuesta de varias páginas** — Quick Look solo dibuja la primera. Exporta a PDF
con Pages y renderiza todas:

```bash
osascript -e 'tell application "Pages" to open POSIX file "/ruta/Propuesta - X.docx"' && sleep 7 && osascript -e 'tell application "Pages" to export document 1 to POSIX file "/tmp/p.pdf" as PDF' -e 'tell application "Pages" to close document 1 saving no' && pdftoppm -jpeg -r 65 /tmp/p.pdf /tmp/pg
```

Lee los PNG/JPG resultantes. Revisa que los encabezados salgan en azul, que la
numeración romana corra I. → II. → III., que las listas reinicien, que ningún
encabezado quede solo al pie de una página, y que la firma no quede huérfana en la
última. (Quick Look no dibuja el pie con el logo; el PDF de Pages sí.)

Para confirmar que el archivo abre sin pedir reparación y contar páginas:

```bash
osascript -e 'tell application "Microsoft Word" to open POSIX file "/ruta/Propuesta - X.docx"' -e 'delay 3' -e 'tell application "Microsoft Word" to compute statistics active document statistic statistic pages' -e 'tell application "Microsoft Word" to close active document saving no'
```

Borra el `~$…docx` que Word deja si quedó alguno.

## Historial de tarifas

Referencia de lo cotizado antes. Confirma con JR antes de reusar un monto: son
precedentes, no una lista de precios vigente.

| Servicio | Honorarios | Gastos |
|---|---|---|
| Constitución de S.A. + inscripción en RM | Q5,000.00 + IVA por sociedad | ~Q2,873.00 (capital autorizado hasta Q499,900.00) |
| Renovación y cancelación de nombramiento | Q1,250.00 + IVA | ~Q950.00 |
| Mandato (fungir como mandatario) | US$300.00/mes + IVA | por cuenta del cliente |
| Revisión de contrato y asesoría en negociación | US$80.00–100.00/hora + IVA | por cuenta del cliente |
| Acta notarial con visita técnica | por horas estimadas (US$550.00 por 6.5 h) | por cuenta del cliente |
| Residencia permanente | US$500.00 por persona | US$700.00 (IGM) |
| Permiso de trabajo | US$500.00 por persona | Q3,000.00 (MINTRAB) |

Sobre el capital autorizado en constituciones: el arancel registral es 8.5 por millar
sobre el capital autorizado, con tope de Q40,000.00. Hasta Q499,900.00 el desglose
completo ronda Q2,873.00.

## Detalle de gastos — constitución de S.A.

Desglose usado en la propuesta de junio 2024, útil como base:

| Detalle | Monto |
|---|---|
| Gastos registrales (8.5 por millar sobre capital autorizado, tope Q40,000.00) | variable |
| Edicto | Q30.00 |
| Pago publicación edicto | Q200.00 |
| Hojas de protocolo (11 hojas) | Q110.00 |
| Inscripción de nombramiento | Q150.00 |
| Inscripción de empresa | Q100.00 |
| Aviso de emisión de acciones | Q200.00 |
| Habilitación de libros en Registro Mercantil | Q170.00 |
| Elaboración de 3 libros (Asamblea, Órgano, Acciones) | Q750.00 |
| 4 timbres notariales de Q100 | Q400.00 |
| 5 timbres notariales de Q10 | Q50.00 |
| 6 timbres fiscales de Q100 | Q600.00 |
| 4 timbres fiscales de Q25 | Q100.00 |
| 26 timbres fiscales de Q0.50 | Q13.00 |
| **TOTAL** | **Q2,873.00** |

## Más contexto

`reference/ejemplo-spec.json` es un spec completo y funcional que puedes copiar como
punto de partida (incluye sublista y sección de gastos).

`reference/corpus.md` tiene el contenido íntegro de las siete propuestas analizadas
—incluidos los listados largos de requisitos migratorios— y las especificaciones
exactas de formato (colores, fuentes, márgenes, sangrías).
