---
type: analisis-legal
proyecto: propi
materia: aml-clasificacion-persona-obligada
norma-base: Decreto 15-2026
date: 2026-07-23
estado: v1-para-decision-jr
tags:
  - proyecto/propi
  - tema/aml
  - tema/legal
  - riesgo
---

# Propi — Análisis: modelo de fondos de terceros frente al Decreto 15-2026

**Pregunta:** ¿el hecho de que Propi reciba fondos de clientes en sus propias cuentas y los transfiera al desarrollador (cobro por cuenta ajena / cashback / "todo a través de Propi") la reclasifica, bajo el Decreto 15-2026, de **APNFD inmobiliaria** (Art. 3.c.1.i) a **actividad financiera** (Art. 3.b), con obligaciones más pesadas?

**Respuesta corta:** hoy Propi está bien clasificada como intermediación inmobiliaria, **pero el nuevo marco elevó el riesgo de reclasificación** porque eliminó el calificativo que muy probablemente sustentó el visto bueno anterior de la IVE. Conviene **documentar el flujo y reconfirmar el criterio con la IVE antes del 17-sep-2026**, y decidir el diseño operativo según cuánto quiera Propi apoyarse en este modelo.

---

## 1. El contexto de hecho

- Propi cobra por cuenta ajena: recibe fondos del comprador y los transfiere al desarrollador. Documentado en la **cláusula V.B del modelo de Alianza Estratégica** y en el modelo de **Cashback**.
- Ena (Country Manager) impulsó que "las personas puedan hacer **todo a través de Propi** y su página" — es decir, volverlo un canal estándar, no excepcional.
- En el vault consta que **la IVE ya avaló este flujo** bajo el régimen anterior: *"resuelto, no existe inconveniente regulatorio"* (planteado directamente a JR, [[propi]] act. 2026-06-15).

> ⚠️ Dato faltante para cerrar el análisis: **frecuencia, volumen y titularidad de cuentas reales**. ¿Es puntual o recurrente? ¿Los fondos entran a una cuenta operativa de Propi o a una cuenta espejo/escrow? ¿Qué % de las operaciones usa este flujo? La respuesta cambia el peso de la conclusión.

---

## 2. Por qué el nuevo marco cambia el análisis (el punto clave)

El régimen **anterior** (Dto. 67-2001, Art. 18.5.c) definía la actividad financiera relevante como:
> "Transferencias **sistemáticas o sustanciales** de fondos y/o movilización de capitales."

Ese calificativo — *"sistemáticas o sustanciales"* — es casi con certeza lo que permitió a la IVE concluir que el flujo de Propi, siendo accesorio y puntual, **no** la convertía en actividad financiera.

El **Decreto 15-2026 eliminó ese umbral**. Las categorías equivalentes ahora son, sin calificativo de "sistemático o sustancial":

| Categoría nueva | Texto (Art. 3.b.1) |
|---|---|
| iv | **"Custodia o movilización de capitales, fondos o valores."** |
| xi | **"Otras formas de inversión, administración o gestión, de fondos o de dinero en nombre de terceros."** |
| xii | **"Transferencia de fondos o transferencia de valores."** |

Y la definición de **transferencia de fondos** (Art. 2.p) es amplia: *"cualquier operación bancaria o no bancaria, llevada a cabo por un ordenante, por cualquier medio… con el objeto de hacer disponible una suma de dinero… a una persona denominada beneficiaria."*

**Conclusión jurídica:** al desaparecer el filtro de "sistemáticas o sustanciales", el margen que tenía la IVE para dejar el flujo fuera del bloque financiero **se estrechó**. El visto bueno anterior se dio bajo una norma que ya no existirá el 17-sep-2026.

---

## 3. Los dos escenarios y sus consecuencias

### Escenario A — El flujo es accesorio a la intermediación (posición conservadora defendible)
Propi actúa como **mandatario de cobro puntual** dentro de una compraventa que ella misma intermedió; el dinero se identifica con una operación inmobiliaria concreta y un beneficiario determinado (el desarrollador). Argumento: no es un "giro de negocio" de transferencias, sino un accesorio del Art. 3.c.1.i.
- **Se mantiene** como APNFD inmobiliaria.
- Obligaciones actuales (las del [[analisis-brechas-15-2026|análisis de brechas]]).

### Escenario B — El flujo es un canal estándar de pago ("todo a través de Propi")
Si los compradores pagan **rutinariamente hacia cuentas de Propi** como característica central de la plataforma (la visión de Ena), Propi está, en los hechos, **moviendo y administrando fondos de terceros de forma habitual** → cae en Art. 3.b.1.iv/xi/xii.
- **Reclasificación al bloque financiero**, que activa:
  - **Art. 39** — obligaciones de transferencias de fondos/valores (regla de viaje: información de ordenante y beneficiario a lo largo de la cadena de pagos; registro de agentes/subagentes).
  - **Art. 34** — conservación digital adicional de **10 años** (solo aplica a bloques a y b).
  - Mayor intensidad de DDC y de supervisión.
  - Posible necesidad de **actualizar/reclasificar la inscripción** ante la IVE.

---

## 3-bis. Consecuencias detalladas de ofrecer el cobro por cuenta ajena como servicio constante

Si Propi decide **institucionalizar** el cobro por cuenta ajena (que los fondos transiten habitualmente por sus cuentas como parte del producto), las consecuencias no se limitan a "más papeleo AML". Se abren **siete frentes de riesgo**:

**1. Reclasificación regulatoria (Art. 3.b.1.iv/xi/xii + Arts. 4 y 6).**
Deja de ser accesorio y se vuelve **giro de negocio** → encuadra en actividad financiera. La IVE puede **reclasificar a Propi de oficio** (Art. 6) o incorporarla formalmente (Art. 4). Cambia su naturaleza: de APNFD inmobiliaria a **Persona Obligada financiera**, con un régimen mucho más exigente.

**2. Obligaciones AML más gravosas que se activan de inmediato.**
- **Art. 39 — "regla de viaje":** asegurar que la información de ordenante y beneficiario viaje con cada transferencia por toda la cadena de pagos; políticas para ejecutar/rechazar/suspender transferencias sin información completa; **registro de agentes y subagentes**; reporte de las transferencias a la IVE.
- **Art. 34 — conservación digital adicional de 10 años** (además de los 5), exclusiva de los bloques a) y b).
- **Art. 25.m — DDC intensificada** en transferencias sobre el umbral que fije el reglamento.
- **Arts. 63-64 — supervisión más intensa** de la SIB, con enfoque basado en riesgo reforzado.
- Sistemas de **monitoreo transaccional** más robustos (mayor volumen y velocidad de fondos).

**3. Riesgo prudencial / de actividad reservada (Ley de Bancos y Grupos Financieros, Dto. 19-2002).**
Movilizar fondos de terceros de forma habitual puede **rozar actividades reservadas** a entidades financieras autorizadas (captación/intermediación/servicios de pago). Guatemala **no tiene aún un marco claro de servicios de pago para no bancos**, por lo que operar un "canal de pago" de facto genera **incertidumbre regulatoria** y expone a Propi a que la SIB cuestione la actividad. En el peor caso, señalamiento por realizar actividad financiera sin autorización.

**4. Riesgo tributario (SAT).**
Los fondos que **entran a cuentas de Propi** pueden ser interpretados por la SAT como **ingreso propio** de la Sociedad, generando exposición de **ISR e IVA** sobre montos que no son de Propi. Mitigarlo exige un **mandato de cobro por cuenta ajena** impecable y **contabilidad segregada** (cuentas de orden / cuentas puente), con trazabilidad de que el dinero es de terceros. Un error contable convierte un pass-through en base imponible.

**5. Riesgo civil y contractual.**
Al recibir y custodiar dinero ajeno, Propi asume la calidad de **depositario/mandatario** → responde por la **guarda, exactitud, oportunidad y correcta transferencia** de los fondos. Se expone a **reclamos** de compradores y desarrolladores por demoras, errores o pérdidas, y al riesgo de **confusión patrimonial** (commingling) si no segrega cuentas. Un embargo a Propi podría alcanzar fondos de clientes si no están claramente separados.

**6. Riesgo penal sustantivo (Arts. 73 y 76).**
Interponerse en el flujo del dinero **coloca a Propi dentro de la cadena de pago** de cada operación. Si un comprador paga con **fondos de origen ilícito**, Propi los "invierte, convierte o transfiere" (Art. 73.a) o los "administra/tiene/utiliza" (Art. 73.b), y la cláusula de **"permita o facilite"** (Art. 73, párr. 2) amplía la exposición. La **responsabilidad penal de la persona jurídica** (Art. 76) se vuelve mucho más tangible: multa hasta US$625,000 y, en reincidencia, cancelación de la personalidad jurídica. En un esquema de intermediación pura (sin tocar el dinero), esta superficie es mínima; con pass-through, se dispara.

**7. Riesgo bancario y reputacional (de-risking).**
Cuentas con **alto flujo de fondos de terceros** hacen que Propi **parezca un transmisor de dinero** a los ojos de sus bancos. Riesgo real de **cierre de cuentas** (de-risking) por parte de la banca, que es reacia a clientes con perfil de "money service business". Perder la cuenta operativa paralizaría el negocio.

> **Síntesis:** ofrecerlo como servicio constante convierte un riesgo AML acotado en un riesgo **regulatorio + tributario + civil + penal + bancario** simultáneo. La forma de tener la comodidad de "todo por la plataforma" **sin** cargar estos riesgos es sacar los fondos del balance de Propi (escrow, fideicomiso o convenio de recaudo a nombre de la desarrolladora), o canalizarlos por un tercero licenciado.

---

## 4. Recomendaciones (para decisión de JR)

1. **Levantar los hechos** con Propi (Ena/Thelma): frecuencia, volumen, titularidad de cuentas, y si el pago-a-Propi será opcional o el canal por defecto. Sin esto, cualquier opinión es preliminar.
2. **Definir el diseño operativo**, tres caminos:
   - **(a) Mantener accesorio:** dejar el cobro por cuenta ajena como excepción documentada (mandato puntual por operación), evitando que se vuelva el canal por defecto. Bajo riesgo de reclasificación.
   - **(b) Sacar los fondos del balance de Propi:** que el dinero fluya por un **tercero licenciado** (escrow/fiducia bancaria o un proveedor de pagos regulado), de modo que Propi nunca "movilice" fondos de terceros. Habilita la visión "todo por la plataforma" sin cargar a Propi con el régimen financiero.
   - **(c) Asumir el bloque financiero:** si Propi quiere que el pass-through sea núcleo del producto, prepararse para clasificar bajo Art. 3.b y adoptar el programa reforzado (Art. 39 + conservación 10 años). Es la opción más costosa en compliance.
3. **Reconfirmar con la IVE por escrito** el criterio bajo el Decreto 15-2026 **antes del 17-sep-2026**, dado que el visto bueno previo se apoyó en una norma derogada y en el calificativo eliminado. Idealmente obtener respuesta escrita (no verbal como la anterior) para tener respaldo.
4. **No** anclar el manual a la clasificación actual sin resolver esto: la sección de clasificación (Introducción / Art. 3) y el alcance de obligaciones dependen del resultado.

**Recomendación de fondo:** salvo que Propi quiera entrar deliberadamente al régimen financiero, la vía más limpia para habilitar la visión de Ena es la **opción (b)** — que los fondos pasen por un escrow/fiducia o pasarela regulada, no por las cuentas propias de Propi. Eso concilia el producto con el riesgo regulatorio.

---

## 5. Nota de método
Este análisis parte del texto de la ley ([[decreto-15-2026-ley-integral-ldft-fpadm|Dto. 15-2026]], Arts. 2.p, 3.b, 34, 39) y del anterior ([[decreto-67-2001-ley-lavado|Dto. 67-2001]] Art. 18) para aislar el cambio normativo. **No sustituye** una consulta formal a la IVE ni una opinión firmada; es insumo interno para decidir el diseño operativo y la estrategia de consulta.

---

## Relacionado
- [[analisis-brechas-15-2026]] — brechas del manual (este flag es la sección G de ese documento).
- [[propi]] · [[propi/mapa-operativo]] · [[decreto-15-2026-ley-integral-ldft-fpadm]] · [[index|Biblioteca AML]]
