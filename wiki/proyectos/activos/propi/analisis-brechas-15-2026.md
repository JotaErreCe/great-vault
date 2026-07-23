---
type: analisis-legal
proyecto: propi
materia: aml-ldft-fpadm
norma-base: Decreto 15-2026
documento-evaluado: Compliance Manual 2026 (Propi Tech, S.A.)
date: 2026-07-23
estado: v1-revision
tags:
  - proyecto/propi
  - tema/aml
  - tema/legal
  - compliance
  - analisis-brechas
---

# Propi — Análisis de brechas: Manual de Cumplimiento vs. Decreto 15-2026

Revisión del **Manual de Cumplimiento del Sistema Integral de Prevención LDA/FT/FPADM de Propi Tech, S.A.** (versión evaluada: `Compliance Manual 2026.pdf`, 37 pp.) frente a la nueva **[[decreto-15-2026-ley-integral-ldft-fpadm|Ley Integral, Decreto 15-2026]]**, que entra en vigor el **17-sep-2026** y deroga el Dto. 67-2001 y el Dto. 58-2005.

> **Biblioteca legal de respaldo:** [[index|AML Guatemala]] · [[decreto-15-2026-ley-integral-ldft-fpadm|Dto. 15-2026]] · [[decreto-67-2001-ley-lavado|Dto. 67-2001 (derogado)]] · [[ag-118-2002-reglamento|AG 118-2002 (transitorio)]].

---

## Veredicto general

El manual **NO requiere reescritura**. Su estructura ya es moderna: enfoque por riesgo, DDC simplificada/estándar/intensificada, PEP, beneficiario final, matriz de riesgo, monitoreo/RTS, conocimiento de empleados y proveedores. El trabajo es de **alineación** en tres capas:

1. **Citas y terminología** — reemplazar las leyes derogadas y ajustar nombres (ROS→RTS, etc.).
2. **Parámetros numéricos** — beneficiario final, período PEP, plazos de conservación, umbrales.
3. **Brechas sustantivas nuevas** — congelamiento sin demora (listas ONU), metodología de riesgo documentada, screening de personal contra listas ONU, y revisión del modelo de fondos de terceros.

⚠️ **Importante:** varios parámetros concretos (umbrales de DDC por actividad, montos de efectivo/transferencias, contenido mínimo del manual, plazos de RTS, procedimiento sancionador) la ley los remite al **nuevo reglamento**, que la SIB/IVE debe emitir a más tardar ≈**17-dic-2026** (Art. 127). Recomendación: hacer ahora la alineación de lo que ya es firme, y dejar señalados los puntos "pendientes de reglamento" para una segunda pasada cuando salga.

---

## A. Brechas CRÍTICAS (citar ley derogada = incumplimiento a partir del 17-sep-2026)

| # | Sección del manual | Qué dice hoy | Qué exige el Dto. 15-2026 | Acción |
|---|---|---|---|---|
| A1 | **IV. Normativa aplicable** (p.6) | Cita Dto. **67-2011** (sic, es 67-2001), AG 118-2002, Dto. 58-2005, AG 86-2006 | Todas derogadas/sustituidas | Reemplazar por **Decreto 15-2026** + (cuando exista) su reglamento. Corregir el typo "67-2011". |
| A2 | **I. Introducción** (p.5) | Clasifica a Propi bajo "Art. 5, inciso m) subinciso i) del **Reglamento**" (Grupo B) | Base nueva: **Art. 3, literal c) numeral 1, romano i** (promoción e intermediación inmobiliaria) del Dto. 15-2026 | Actualizar la cita. La taxonomía Grupo A/B desaparece de la ley (era reglamentaria); esperar el nuevo reglamento para cualquier re-agrupación. |
| A3 | Todo el manual | Referencias a "Ley contra el Lavado de Dinero y Activos, su Reglamento e Instructivo" | Instrumento único: Dto. 15-2026 | Barrido global de citas. Nota del Art. 125 Dto. 15-2026: toda referencia a las leyes viejas se entiende hecha a la nueva — pero conviene actualizarlas expresamente en el manual. |

---

## B. Brechas de PARÁMETROS (números que ya no coinciden con la ley)

| # | Sección | Valor en el manual | Valor Dto. 15-2026 | Acción / decisión |
|---|---|---|---|---|
| B1 | **Beneficiario final** (Glosario p.8; Tabla 1 p.15; Tabla 2 proveedores; DDC; clientes no aceptados) | **"10% o más"** / "más del 10%" | **≥ 15 %** (Art. 2.b) | Cambiar a **15 %** en TODAS las apariciones. *Decisión JR:* la ley fija piso del 15%; Propi puede mantener 10% como política interna más estricta, pero entonces debe decirlo explícitamente ("Propi aplica un umbral más riguroso del 10% respecto del 15% legal"). Recomiendo alinear a 15% salvo que quieras el estándar más estricto. |
| B2 | **Período PEP tras cesar** (p.8 "igual al ejercicio"; **p.17 "5 años"**; **p.18 "3 años"**) | Inconsistente: 5 años y 3 años | **1 año** posterior al cese, sin trámite (Art. 2.g y Art. 25.a) | Unificar a **1 año** en las tres apariciones. Hoy el manual se contradice a sí mismo y ninguna cifra coincide con la ley. |
| B3 | **Conservación de documentos** (XIII p.33) | **15 años** | **5 años** mínimo (Art. 34). Los 10 años digitales adicionales aplican SOLO a POs de los bloques a) y b); Propi es bloque c) → no le aplican | Re-anclar la base legal a Art. 34 y corregir cita. *Decisión JR:* 15 años es más estricto que la ley (no es infracción). Mantener 15 o bajar a 5 es decisión de negocio; recomiendo al menos re-fundamentar la cita. |
| B4 | **Umbral "otro medio"** (X.e p.27) | Reporte de operaciones en "otro medio" > **US$25,000** | El Dto. 15-2026 solo fija efectivo **≥US$10k** (Art. 31); el umbral de "otros medios/transferencias" queda "según reglamentación" (Art. 25.l/m) | Mantener interino y marcar **"pendiente de reglamento"**. No inventar base legal para los 25k. |
| B5 | **Beneficiario final % (screening listas)** p.16-19 | "accionistas con más del 10%" | ≥15% (Art. 2.b) | Igual que B1. |

---

## C. Brechas SUSTANTIVAS (obligaciones nuevas o reforzadas)

### C1. Congelamiento sin demora / listas ONU — **la brecha más importante** 🔴
- **Hoy:** el manual hace *screening* contra OFAC, Interpol, ONU y GAFI vía Snap Compliance al vincular al cliente (bien). Pero **no describe el procedimiento de congelamiento/inmovilización "sin demora"**.
- **Ley (Arts. 43-44):** ante coincidencia con listas del Consejo de Seguridad ONU (1267/1988/1989/2253 terrorismo; 1718/1737/2231 FPADM; 1373), la PO debe **limitar con efecto preventivo los fondos/activos del cliente** y **comunicar por escrito al Ministerio Público en ≤24 horas**; el MP solicita ratificación judicial en ≤72 h; prohibición de avisar al cliente; y hay exención de responsabilidad para la PO que aplique la medida.
- **Acción:** agregar una sección específica: monitoreo continuo contra listas ONU, procedimiento de congelamiento sin demora (24 h → MP), no revelación, levantamiento de la medida (Art. 44), y exención de responsabilidad (Art. 43). Esto conecta directamente con el trámite **"Firma con Certeza"/CBR** que Astrid gestiona (screening PEP/sanciones).

### C2. Metodología de riesgo documentada (EBR) 🟠
- **Hoy:** hay matriz de riesgo (Tablas 3-5, líneas de negocio Rents/Presales/Secondary) — buena base.
- **Ley (Arts. 8-11):** exige metodología **documentada** que defina factores de riesgo cubriendo como mínimo: **(i) base de clientes, (ii) ubicación geográfica, (iii) canales de distribución, (iv) bienes/productos/servicios**; autoevaluación periódica (Art. 10); mitigación (Art. 11); aprobación por el **órgano de dirección superior**; y evaluación de riesgo **previa al lanzamiento de nuevos productos, servicios o tecnologías** (Art. 11).
- **Acción:** mapear explícitamente los 4 factores del Art. 9 en la sección XI, y añadir la obligación de evaluar riesgo **antes** de lanzar nuevos productos/tecnología (relevante para una proptech que itera su plataforma).

### C3. Selección de personal contra listas ONU + veto por condena (Art. 12.a) 🟠
- **Hoy:** conocimiento de empleados con antecedentes penales/policiales (p.21) — bien.
- **Ley (Art. 12.a):** además exige verificar que personal, directores, agentes e intermediarios **no figuren en listas del Consejo de Seguridad ONU**, y **prohíbe contratar/nombrar** a condenados por LD/FT hasta **5 años después de cumplida la pena**.
- **Acción:** añadir el screening de personal/directores/agentes contra listas ONU y la barrera de 5 años post-condena.

### C4. Guardarraíl de DDC simplificada (Art. 23) 🟡
- **Hoy:** DDC simplificada se dispara solo por ingreso ≤US$600/mes (p.15).
- **Ley (Art. 23):** la DDC simplificada solo procede si el riesgo es **menor** y **nunca** para transacción inusual ni cliente de riesgo alto, sin importar el monto.
- **Acción:** añadir el candado: "la DDC simplificada no aplica ante transacción inusual o riesgo alto, aunque el monto sea bajo".

### C5. Abstención cuando la DDC es imposible (Art. 22 §3) 🟡
- **Ley:** si no se puede completar la DDC, la PO debe **abstenerse/terminar** la relación **y evaluar reportar RTS**.
- **Acción:** el manual cubre "clientes no aceptados" y terminación; añadir expresamente el deber de abstención y de considerar RTS ante imposibilidad de DDC.

---

## D. Alineación de TERMINOLOGÍA

| # | Manual | Dto. 15-2026 | Acción |
|---|---|---|---|
| D1 | **ROS** (Reporte de Operación Sospechosa) | **RTS** (Reporte de Transacción Sospechosa) — Art. 30 | Renombrar ROS→RTS en todo el manual (X.c/d). |
| D2 | "Operaciones Reguladas" | "Reportes de transacciones en efectivo" — Art. 31 | Ajustar nombre; el fondo (efectivo ≥US$10k) se mantiene. |
| D3 | Glosario: "Asociados Comerciales", "Compañeros de Vida", "Persona Relacionada" | **"Asociados cercanos"** definido en Art. 2.a | Añadir/alinear la definición legal de asociados cercanos. |
| D4 | Glosario: IVE "creada para la **persecución del delito**" (p.9) | La IVE es administrativa / inteligencia financiera; la persecución penal es del MP (Arts. 51-52) | Corregir: la IVE **no** persigue delitos; recibe/analiza/difunde inteligencia financiera. |
| D5 | Plazos internos de análisis: 15 días hábiles + envío 10 días (del AG 118-2002 Art. 16) | La ley dice reportar "con prontitud"; plazos concretos → reglamento (Art. 30) | Mantener interino y marcar "pendiente de reglamento". |
| D6 | Glosario faltante | Definiciones nuevas: **estructura jurídica** (2.f), **relación de negocios** (2.j), **Riesgo LD/FT/FPADM** (2.k), **debida diligencia del cliente** (2.e), y mención de **proveedor de servicios de activos virtuales** (2.i) | Incorporar al glosario (aunque activos virtuales no sea giro de Propi, conviene dejar constancia de que no lo es). |

---

## E. Puntos a AJUSTAR / confirmar (menor o decisión de negocio)

- **E1. Auditoría (XV, Art. 15):** el manual exige auditoría interna **y externa** anual. Para Propi (bloque c) la ley obliga a la revisión anual **interna o por auditores especializados**; el **informe de aseguramiento externo** solo es obligatorio para entidades supervisadas por la SIB (bloque a). *Decisión JR:* mantener la externa como estándar propio o relajarla a lo que exige la ley. Recomiendo aclararlo para no auto-imponer una carga que la ley no pide.
- **E2. Oficial de Cumplimiento (VI, Arts. 16-20):** re-anclar a los Arts. 16-20 (hoy cita Arts. 21-22 del AG 118-2002). Sustancia compatible (independencia, suplente, gerencial, único enlace). El **Art. 18** permite que una PO individual/pequeña ejerza ella misma la función — útil dado el tamaño de Propi. Confirmar la cadena de nombramiento real ("Secretario Junta Directiva Único" en el manual vs. la estructura societaria vigente — ver [[propi/mapa-operativo]] §6: nombramiento es por cargo).
- **E3. Verificación diferida (Art. 22):** opción nueva de completar verificación hasta **3 meses** después del inicio de la relación en casos justificados. Se puede incorporar si conviene operativamente (onboarding ágil que Ena pidió).
- **E4. Umbrales de DDC por ingreso mensual** (≤600 / 600–10k / >10k): son diseño propio de Propi. La ley remite umbrales por actividad al reglamento (Art. 21.b). Mantener, marcando "sujeto a ajuste según reglamento".

---

## F. Acciones SOCIETARIAS de Propi Tech, S.A. (fuera del manual, pero mismo paquete) 🔴

El Dto. 15-2026 reforma el **Código de Comercio** y obliga a la sociedad, no solo al programa de compliance:

| Obligación | Base | Plazo | Estado / enlace |
|---|---|---|---|
| **Registro de Acciones** actualizado al nuevo contenido del Art. 125 Cód. Comercio (incluye país, estructuras jurídicas, dirección y correo de cada accionista, y remisión al Registro Mercantil) | Art. 113 + **Art. 120** transitorio | **1 año** desde vigencia → ≈**17-sep-2027** | Cotejar con el "Libro de registro de accionistas" existente ([[propi/mapa-operativo]] §3.1). |
| **Inscribir en el Registro Mercantil** a los miembros del órgano de administración con representación legal | Art. 112 + **Art. 121** transitorio | **6 meses** desde vigencia → ≈**17-mar-2027** | Conecta con nombramientos en curso (José Mario PCA, Ena). Vencido el plazo, la sociedad **no podrá operar** en el Registro Mercantil. |

---

## G. FLAG estratégico — modelo de fondos de terceros ⚠️🔴

**El punto más delicado, y que recomiendo elevar/consultar antes de reescribir el manual.**

Propi cobra por cuenta ajena / cashback: recibe fondos de clientes y los transfiere al desarrollador (cláusula V.B del modelo de Alianza Estratégica). En el vault consta que la **IVE ya avaló este flujo bajo el régimen anterior** ("sin inconveniente regulatorio", [[propi]] act. 2026-06-15).

**Bajo el Dto. 15-2026 conviene revisar ese criterio**, porque recibir/movilizar/transferir fondos por cuenta de terceros de forma habitual encaja en actividades del **bloque financiero (Art. 3.b.1)**:
- 3.b.1.iv — custodia o movilización de capitales, fondos o valores;
- 3.b.1.xi — administración o gestión de fondos de terceros;
- 3.b.1.xii — transferencia de fondos o valores.

Si la IVE llegara a considerar que Propi realiza una de esas actividades, subiría de categoría (de APNFD inmobiliaria a **actividad financiera**), lo que activa obligaciones **más pesadas**: Art. 39 (obligaciones de transferencias de fondos/valores), conservación digital adicional de **10 años** (Art. 34), y mayor escrutinio de supervisión.

**Recomendación:** documentar por qué el flujo es accesorio a la intermediación inmobiliaria (mandato de cobro puntual, no giro de transferencias), y valorar reconfirmarlo con la IVE bajo el nuevo marco antes del 17-sep-2026. Decisión de JR.

---

## H. Plan sugerido (orden de trabajo)

1. **Barrido de citas** (A1-A3) y terminología (D1-D6) — mecánico, hacer ya.
2. **Parámetros firmes** (B1 beneficiario final 15%, B2 PEP 1 año) — decisión rápida de JR y aplicar.
3. **Brechas sustantivas** (C1 congelamiento ONU, C2 metodología riesgo, C3 screening personal) — redacción nueva.
4. **Marcar "pendiente de reglamento"** (B3-B4, D5, E4) — segunda pasada cuando salga el reglamento (≈dic-2026).
5. **Acciones societarias** (F) y **flag de fondos de terceros** (G) — abrir como líneas de trabajo separadas con sus plazos.
6. Aprobar el manual actualizado por el **órgano de dirección superior** (Art. 12) y comunicar cambios a la IVE según corresponda.

> Cuando digas, en otra sesión pasamos de este análisis a **redactar** las secciones (paso 3 de tu decisión de hoy). El manual fuente está en `AMC Legal/Clientes/Propi/IVE/` (V3) y en `Downloads/Compliance Manual 2026.pdf`.

---

## Relacionado
- [[propi]] · [[propi/mapa-operativo]] · [[amc-legal]]
- [[decreto-15-2026-ley-integral-ldft-fpadm]] · [[index|Biblioteca AML]]
