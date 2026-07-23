---
type: referencia-operativa
tema: formularios-reportes-ive
jurisdiccion: guatemala
date: 2026-07-23
tags:
  - legal
  - aml
  - ive
  - formularios
  - reference
---

# Catálogo de formularios y reportes de la IVE — Guatemala

Referencia operativa de los formularios y reportes de la **Intendencia de Verificación Especial (IVE)** de la SIB, mapeados a las obligaciones del [[decreto-15-2026-ley-integral-ldft-fpadm|Decreto 15-2026]]. Sirve para saber **qué formulario/reporte usar para qué**, con qué periodicidad y cuál aplica a Propi.

> ⚠️ **Transición:** los formularios e instructivos vigentes citan como base los Dtos. 67-2001 / 58-2005 y sus reglamentos (AG 118-2002 / 86-2006), **derogados el 17-sep-2026**. Las **obligaciones de reporte persisten** bajo el Dto. 15-2026, pero los **códigos y formatos pueden reemitirse** con el nuevo reglamento (≈dic-2026). Vigilar publicaciones de la IVE en el Portal PPO.

---

## Portal y canal

- **Portal Personas Obligadas (PPO)** — `https://portalpo.sib2.gob.gt` (registro: `/registropo/login`). Es el canal único para inscripción, envío de reportes (Validador Web) y el Reporte Listas ONU.
- Los reportes electrónicos se suben como **archivo de texto plano empaquetado en ZIP**, con delimitador de campos **`&&`** (ASCII 38 doble).
- Manual de referencia: *Manual del Portal de Personas Obligadas IVE* (versión ago-2020).

---

## A. Registro / inscripción

| Form / Instructivo | Qué es | Quién / cómo | Base nueva ley |
|---|---|---|---|
| **IVE-RPO-01** | Instructivo para el **Registro de Persona Obligada** | Solo el **representante legal** (o mandatario con plenos poderes). Vía Portal PPO. | Art. 5 (inscripción); Art. 117 (POs ya inscritas solo **actualizan datos**, no re-registran) |

> Propi **ya está inscrita** (ver Constancia IVE en su expediente). Bajo el Dto. 15-2026 solo deberá **actualizar información** cuando el nuevo reglamento lo indique.

---

## B. Expediente del cliente (KYC / DDC)

| Form | Qué es | Aplica a Propi | Base nueva ley |
|---|---|---|---|
| **IVE-RE-23 (FEIC)** | **Formulario para la creación del expediente del cliente** — Personas Obligadas **Régimen Especial (PORES)**, actividades de promoción inmobiliaria/compraventa de inmuebles y vehículos | ✅ **Sí — es el de Propi** | Arts. 21-22 (DDC). Ver matriz de respaldos en [[procedimiento-expediente-cliente]] |
| IVE-AF-01 | Formulario de inicio de relaciones / expediente — **persona individual** (sector financiero) | Referencia (Propi usa el RE-23) | Arts. 21-22 |
| IVE-AF-02 | Ídem — **persona jurídica** | Referencia | Arts. 21-22 |
| IVE-AF-03 | Ídem — **efectivo** (bancos / fianzas) | Referencia | Arts. 21-22 |
| IVE-NF-30 | Formulario de expediente del cliente (formato pleno con datos de la PO y del cliente) | Referencia | Arts. 21-22 |
| IVE-IR-01, IVE-OC-22, IVE-RE-TE, Anexos A.I-A.IV | Otros del expediente / oficial de cumplimiento (en el iCloud de Propi) | Revisar en su carpeta `Formularios IVE/` | — |

> Propi, por ser **régimen especial**, usa el **IVE-RE-23**; los AF/NF son el formato pleno del sector financiero, útiles como referencia de campos.

---

## C. Reportes periódicos — el calendario de cumplimiento de Propi 📅

| Reporte | Qué reporta | Periodicidad y plazo | Aplica a Propi | Base nueva ley |
|---|---|---|---|---|
| **IVE-IN-25** | Transacciones de **promoción inmobiliaria / compraventa de inmuebles** (código `BI`). Campos: fecha, sucursal, tipo (P/C/V), factura, monto total, **monto en efectivo**, tipo/doc/nacionalidad del comprador, etc. | **Mensual** — primeros **10 días hábiles** del mes siguiente | ✅ **Sí — reporte sectorial central de Propi** | Arts. 32/35 (otros reportes) |
| **IVE-MY-28** | Transacciones **en efectivo mayores a US$10,000** (código `MY`) | **Mensual** — primeros **5 días hábiles** del mes siguiente | ✅ **Sí** | **Art. 31** (registro/reporte de efectivo ≥US$10k) |
| **IVE-ONU-Mensual** (Reporte Periódico Listas ONU) | Informar **SI/NO** se detectaron coincidencias con personas designadas por el **Consejo de Seguridad de la ONU**; y las inmovilizaciones ordenadas por el MP | **Mensual** — **5 días hábiles** del mes siguiente. Aun si NO hubo coincidencias, hay que informarlo | ✅ **Sí** | **Art. 43** (listas ONU / congelamiento sin demora). Base actual: Oficio IVE 107-2019 |
| **IVE-VE-26** | Transacciones de **compraventa de vehículos** (código `VA`) | Mensual — 10 días hábiles | ❌ No (salvo que Propi comercialice vehículos) | — |
| **RTS** (Reporte de Transacción Sospechosa) | Transacciones sospechosas detectadas | **Eventual — "con prontitud"** | ✅ **Sí** (antes "ROS") | **Art. 30** |

> **Obligación importante para el manual de Propi:** el IVE-IN-25 y el IVE-MY-28 exigen **conservar los archivos y la documentación de respaldo de cada transacción, incluida la forma de pago**, por si la IVE pide información adicional. Esto refuerza la política de conservación (15 años, [[analisis-brechas-15-2026]] B3) y la matriz de respaldos ([[procedimiento-expediente-cliente]]).

---

## D. Documentos propios de Propi (no genéricos)

Están en el expediente de Propi, no en esta biblioteca: **Constancia de inscripción IVE**, `13052024 IVE - Propi Tech, S.A.` (inscripción), `PROPI FOUNDERS - MEMO IVE`, y el `Formulario_IVE-IN-25_Con_Datos` (ejemplo llenado). Ubicación: iCloud `AMC Legal/Clientes/Propi/IVE/` y `Formularios IVE/` (ver [[propi/mapa-operativo]] §3.2).

---

## Mapa rápido: obligación → reporte

- Inscribirse / actualizarse como PO → **IVE-RPO-01** (Portal PPO).
- Abrir expediente de un cliente → **IVE-RE-23 (FEIC)** + respaldos.
- Reportar ventas/promoción de inmuebles del mes → **IVE-IN-25** (10 días hábiles).
- Reportar efectivo ≥US$10k del mes → **IVE-MY-28** (5 días hábiles).
- Informar screening de listas ONU del mes (haya o no coincidencias) → **IVE-ONU-Mensual** (5 días hábiles).
- Detecté una operación sospechosa → **RTS**, con prontitud.

---

## Relacionado
- [[procedimiento-expediente-cliente]] — matriz de documentos de respaldo (usa el IVE-RE-23).
- [[analisis-brechas-15-2026]] · [[decreto-15-2026-ley-integral-ldft-fpadm]] · [[index|Biblioteca AML]]
