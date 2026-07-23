---
type: procedimiento
proyecto: propi
materia: aml-ddc-expediente
norma-base: Decreto 15-2026
formulario-base: IVE-RE-23 (FEIC PORES)
date: 2026-07-23
estado: v1-borrador-para-discusion
tags:
  - proyecto/propi
  - tema/aml
  - tema/legal
  - procedimiento
---

# Propi — Procedimiento de expediente y debida diligencia del cliente (mapeado al flujo comercial)

Recomendaciones sobre **dónde, en el flujo comercial de Propi, pedir qué documentos** para la debida diligencia del cliente (DDC), distinguiendo **información declarada** vs **documento de respaldo**. Base: el flujo "as-is" de Ena (`Diagnostico y flujo comercial.xlsx`), el formulario oficial **IVE-RE-23 (FEIC)** y el [[decreto-15-2026-ley-integral-ldft-fpadm|Decreto 15-2026]] (Arts. 21-25), con las decisiones ya tomadas en el [[analisis-brechas-15-2026|análisis de brechas]] (beneficiario final ≥15%, PEP 1 año).

> **Estado:** borrador para discutir con JR/Ena/Thelma. No es el procedimiento final; es la base para redactarlo.

---

## 0. Principio rector: "no basta la info, hay que respaldarla"

Cada **dato declarado** por el cliente debe quedar **respaldado por un documento** de fuente confiable e independiente (Art. 21, num. 1: *"utilizando documentos, datos e información confiable de fuentes independientes"*). El FEIC recoge la información; los anexos la prueban. El FEIC por sí solo **es insuficiente** — pide un mínimo (DPI, recibo de servicios, escritura). Propi debe pedir **más**, escalando según el nivel de riesgo.

---

## 1. El problema de secuencia (a corregir en el rediseño) 🔴

En el flujo actual:
- **Subproceso 4.1 (Reserva):** formularios + "mini investigación" → habilita pago → el cliente **paga la reserva** (a la cuenta de la desarrolladora) → se bloquea la unidad.
- **Subproceso 4.2 (Expediente + DDC):** *después* de la reserva, el Proper solicita la papelería, el cliente llena el expediente y **entonces** se hace la debida diligencia, antes de la promesa.

**Riesgo:** el dinero se mueve (reserva) **antes** de completar la DDC. El Art. 21-22 exige aplicar DDC **al inicio de la relación de negocios y antes de ejecutar transacciones** sobre los umbrales. El Art. 22 permite completar la *verificación* hasta 3 meses después en casos justificados, **pero no** para riesgo alto, y obliga a **abstenerse** si la DDC es imposible.

**Recomendación de secuencia:**

| Momento en el flujo | Qué de DDC ocurre aquí |
|---|---|
| **Perfilamiento** (etapa 4) | Pre-screen ligero: nombre completo + screening contra listas (ONU/OFAC/Interpol/GAFI/PEP) vía Snap Compliance. Marca temprana de riesgo. |
| **Antes de habilitar el pago de la reserva** (4.1) | **Abrir expediente + identificación y verificación mínimas**: FEIC + DPI/pasaporte + recibo de servicios + NIT/RTU + **identificar beneficiario final** + asignar **nivel de riesgo** (define la intensidad de DDC). Sin esto, no se habilita el pago. |
| **Entre reserva y promesa** (4.2) | **Completar el expediente**: respaldos de origen de fondos e ingresos, documentos societarios (si PJ), y **aprobación del Oficial de Cumplimiento** antes de firmar la promesa. Aquí se cierra la DDC estándar/intensificada. |
| **Escrituración** (etapa 10) | Verificación final y archivo del expediente completo (conservación 15 años, ver [[analisis-brechas-15-2026]] B3). |

> Regla simple: **identidad + beneficiario final + screening de listas ANTES de que el dinero se mueva**; respaldos financieros y de origen de fondos ANTES de la promesa.

---

## 2. Matriz: dato declarado → documento de respaldo (el núcleo)

Esto es lo que JR pidió: no pedir solo la información, sino el documento que la prueba.

### 2.1 Persona individual

| Dato (FEIC) | Documento de respaldo a exigir | Vigencia / nota |
|---|---|---|
| Identidad (4.1-4.5) | **DPI** (ambos lados) o **pasaporte** vigente | Extranjero: + documento de **condición migratoria** (visa, tarjeta de residencia, pase especial) |
| Dirección particular (4.6) | **Recibo de servicios** (agua, luz o teléfono **fijo** — no celular) que registre la dirección | **≤ 3 meses**. Si no está a su nombre: declaración + prueba del vínculo (contrato de arrendamiento, etc.) |
| NIT (4.7) | **RTU actualizado** (SAT), reimpresión reciente | Confirma NIT, nombre, actividad económica y régimen |
| Profesión/actividad (4.4) | RTU + (según riesgo) constancia laboral o patente si es comerciante individual | |
| Ingresos/egresos (4.14-4.15) | Según nivel de DDC: **constancia laboral / recibo de sueldo**, **estados de cuenta bancarios**, **declaraciones de ISR/IVA** | Escala con el riesgo (ver §3) |
| **Origen de los fondos** (4.16) | Según monto: constancia de ingresos, estados de cuenta, **escritura/contrato de venta** de otro bien, **carta de aprobación de crédito** bancario, etc. | Campo crítico en inmuebles. Debe ser **coherente** con el perfil declarado |
| Trabajo (4.11-4.12) | Constancia laboral / patente | |
| Referencias (8) | Referencias **bancarias** y **comerciales** con teléfonos | Verificables |

### 2.2 Persona jurídica

| Dato (FEIC) | Documento de respaldo a exigir | Vigencia / nota |
|---|---|---|
| Existencia legal (5.1-5.3) | **Testimonio de la escritura de constitución, inscrita** + **Patente de Sociedad** + **Patente de Empresa** | Fundaciones/iglesias/ONG: acuerdo gubernativo o documento de autorización |
| NIT / actividad (5.4) | **RTU actualizado** de la persona jurídica | Confirma NIT, objeto y régimen |
| Dirección (5.8) | Recibo de servicios de la sede / o dirección en patente y RTU | ≤ 3 meses cuando aplique |
| **Representante legal** (6) | **Acta de nombramiento del representante legal, INSCRITA en el Registro Mercantil y VIGENTE** + DPI/pasaporte del representante | ⚠️ Verificar que el **plazo** del nombramiento no esté vencido (justo el punto que remarcó JR) |
| Cargo del firmante dentro de la PJ | **Nombramiento inscrito y vigente** que acredite el cargo y las **facultades** para el acto | Si firma un apoderado: mandato/poder inscrito |
| **Beneficiario final** (7) — ≥15% | **Declaración jurada de beneficiario final** + **nómina/libro de accionistas** que identifique a quienes tengan **≥15%** | Cadenas de propiedad: desglosar hasta llegar a **persona natural** (Art. 2.b) |
| Estructura accionaria | Libro de registro de accionistas / certificación del secretario | Conecta con la reforma al Art. 125 Cód. Comercio ([[analisis-brechas-15-2026]] §F) |
| Ingresos/egresos (5.9-5.10) | Según riesgo: **estados financieros**, **declaraciones ISR/IVA**, dictamen de auditor | Escala con el riesgo |
| Origen de fondos | Estados financieros, estados de cuenta, contratos que expliquen la fuente | |
| Si el cliente es a su vez Persona Obligada | **Constancia de inscripción ante la IVE** | |

### 2.3 Transversal (todo cliente)
- **Screening de listas** (ONU 1267/1988/1989/2253, 1718/1737/2231, 1373; OFAC; Interpol; países alto riesgo GAFI) + **declaración jurada PEP** → si hay match en listas ONU, activar **congelamiento sin demora** (24 h → MP), ver [[analisis-brechas-15-2026]] C1.
- **FEIC IVE-RE-23** firmado por el cliente/representante y por el empleado responsable.
- **Datos del bien/servicio** (FEIC §3): tipo de inmueble, moneda de la operación.

---

## 3. Escalonamiento por nivel de DDC — modelo HÍBRIDO (valor + perfil)

✅ **DECIDIDO (JR, 23-jul-2026):** el nivel de DDC se asigna combinando el **valor de la operación** con el **perfil de riesgo del cliente**, no por ingreso mensual (que encaja mal con compras de inmueble y es difícil de sostener ante la IVE). Es lo más alineado al enfoque basado en riesgo (Arts. 8-11).

**Regla de asignación:** `nivel final = el MÁS ALTO entre (nivel por valor) y (nivel por perfil)`. El perfil **solo sube** el nivel, nunca lo baja. La **simplificada** solo procede si el valor es bajo **Y** el perfil está limpio (Art. 23: nunca para transacción inusual ni riesgo alto).

### Paso 1 — Nivel base por valor/tipo de operación *(umbrales a calibrar con el nuevo reglamento)*
| Tipo/monto de operación | Nivel base |
|---|---|
| Arrendamientos y operaciones menores de bajo monto | Simplificada (si perfil limpio) |
| Compraventa de inmueble (rango ordinario) | **Estándar** (piso para compraventa) |
| Operaciones de alto monto (sobre umbral a definir) | Intensificada |

### Paso 2 — Elevadores por perfil (suben el nivel aunque el monto sea bajo)
- **PEP** o asociado cercano/pariente → **intensificada**.
- Cliente, fondos o contraparte de **país/jurisdicción de alto riesgo GAFI** o del extranjero → intensificada.
- **Estructura societaria opaca**, beneficiario final no claro, sospecha de testaferro → intensificada.
- **Efectivo significativo** o indicios de **fraccionamiento** → intensificada + evaluar RTS.
- **Incoherencia** entre perfil declarado e ingresos/origen de fondos → intensificada.
- **Match en listas ONU/sanciones** → no vincular; congelamiento sin demora (Art. 43).

### Paso 3 — Documentos por nivel resultante
| Nivel | Documentos mínimos (además del FEIC) |
|---|---|
| **Simplificada** | Identidad (DPI/pasaporte) + recibo de servicios + NIT/RTU |
| **Estándar** | Lo anterior + actividad económica respaldada + ingresos (constancia/estados de cuenta) + origen de fondos básico + referencias + (PJ) documentos societarios y beneficiario final ≥15% |
| **Intensificada** | Lo anterior + **estados financieros / declaraciones ISR-IVA** + origen de fondos reforzado + **aprobación del órgano de dirección superior** para vincular + monitoreo más frecuente |

---

## 4. Recomendaciones sobre el flujo de Ena

1. **Adelantar el KYC** antes del pago de la reserva (ver §1). Es el cambio estructural más importante.
2. **Consolidar la captación multicanal** (Zoko/Rumi/HubSpot) en un CRM con trazabilidad única — no solo por eficiencia comercial, sino porque la DDC exige un **expediente único y trazable** por cliente (Art. 34, conservación).
3. **Rumi (agente IA):** definir en qué momento el bot deja de capturar lead y entra la **identificación formal**. Un bot no puede "verificar identidad de fuente confiable"; la verificación debe recaer en un humano/proceso controlado antes de habilitar pago.
4. **Ruta del dinero:** en el flujo actual la reserva se paga **directo a la cuenta de la desarrolladora** (modelo más seguro en AML). Si se migra a "todo a través de Propi" (visión de Ena), aplica el [[analisis-fondos-terceros-15-2026|análisis de fondos de terceros]] — recomendación: usar escrow/pasarela regulada para no cargar a Propi con el régimen financiero.
5. **"Cliente apto" (perfilamiento):** el checklist comercial de "apto" debería incluir ya las **banderas AML** (screening de listas, PEP, país de riesgo) para no avanzar a un cliente que luego habrá que rechazar.
6. **Cierre perdido por causa AML:** cuando el desistimiento/rechazo sea por DDC (no se pudo verificar, match en listas, origen de fondos no justificado), registrarlo diferenciado y evaluar **RTS** (no basta marcar "cierre perdido").

---

## 5. Nota de transición normativa

El FEIC IVE-RE-23 cita como base legal el **Art. 18 de la Ley FT (58-2005), Art. 14 de su reglamento y Art. 28 de la Ley LD (67-2001)** — **todo derogado** el 17-sep-2026. Es muy probable que la IVE emita **formularios actualizados** con el nuevo reglamento (≈dic-2026). Diseñar el procedimiento de modo que el **contenido** (identificación, verificación, beneficiario final ≥15%, origen de fondos, screening) sobreviva al cambio de formulario; el formulario es el envase, no el fondo.

---

## 6. Apéndice — estructura del FEIC IVE-RE-23 (para referencia)

Formulario **PORES** (Personas Obligadas Régimen Especial) — "Actividades de promoción inmobiliaria o compraventa de inmuebles y vehículos automotores". Secciones: (1) tipo de cliente; (2) lugar/fecha de creación; (3) datos del bien/servicio y moneda; (4) datos persona individual; (5) datos persona jurídica; (6) representante legal; (7) beneficiario final/adquirente real; (8) referencias comerciales y bancarias. Documentos que exige anexar (mínimo): individual → DPI/pasaporte, migratoria si extranjero, recibo de servicios; jurídica → testimonio de constitución inscrito, patente de sociedad, patente de empresa, acuerdo gubernativo si aplica.

---

## Decisiones de diseño (JR, 23-jul-2026)
1. ✅ **Segmentación de DDC:** modelo **híbrido** (valor de operación + perfil) — ver §3.
2. ✅ **Ruta del dinero:** el procedimiento contempla **ambas**:
   - **Directo a la desarrolladora** (as-is; modelo más seguro, mantiene a Propi como APNFD).
   - **Cobro por cuenta ajena** cuando aplique, usando una de tres modalidades que mantienen los fondos **fuera del balance de Propi**: (a) **escrow** (bancario o notarial), (b) **fideicomiso bancario de pagos**, o (c) **convenio de recaudo/cobranza a nombre de la desarrolladora** (cuenta recaudadora del banco a nombre del desarrollador; el cliente paga ahí y Propi solo concilia). Evitar que los fondos pasen por cuentas propias de Propi (reclasificaría a actividad financiera — ver [[analisis-fondos-terceros-15-2026]]).
3. ✅ **Formularios IVE ingeridos** → [[formularios-ive]].

**Pendiente (próximo entregable):** redactar el **Procedimiento de Debida Diligencia y Expediente del Cliente** formal (con el modelo híbrido y las dos rutas) y las **modificaciones al manual** con las decisiones ya tomadas.

---

## Relacionado
- [[analisis-brechas-15-2026]] · [[analisis-fondos-terceros-15-2026]] · [[propi]] · [[propi/mapa-operativo]]
- [[decreto-15-2026-ley-integral-ldft-fpadm]] · [[index|Biblioteca AML]]
