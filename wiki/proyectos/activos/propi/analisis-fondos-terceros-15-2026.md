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
