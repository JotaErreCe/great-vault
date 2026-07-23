---
type: plan-proyecto
proyecto: propi
materia: aml-adecuacion
norma-base: Decreto 15-2026
fuente: IVE PROPI Schedule.xlsx (Ena + Thelma)
date: 2026-07-23
tags:
  - proyecto/propi
  - tema/aml
  - tema/legal
  - cronograma
---

# Propi — Cronograma de adecuación al Decreto 15-2026 (proyecto Ena + Thelma)

Marco de trabajo que **Ena y Thelma** están ejecutando para adecuar Propi al Decreto 15-2026. Fuente: `IVE PROPI Schedule.xlsx`. Proyecto de **7 semanas: 14-jul → 30-ago-2026** (cierra ~2.5 semanas antes de la vigencia de la ley el 17-sep). El seguimiento post-cierre absorbe el nuevo reglamento SIB (~sept-dic).

> **Rol confirmado:** **Thelma = Oficial de Cumplimiento** de Propi. Ena = sponsor/dirección. "José" aparece como responsable de flujo/tecnología/piloto (confirmar si es José Mario Ávila Palomo u otro).

---

## 🔴 Discrepancias detectadas frente a la ley (corregir en el cronograma)

| Dónde | Dice el cronograma | Correcto (Dto. 15-2026) | Acción |
|---|---|---|---|
| Tareas #8, #17, #25 | Beneficiario final **20%** "fijado por ley" | **≥ 15 %** (Art. 2.b, texto literal) | **Cambiar a 15% antes de redactar la política de BF y el formulario KYC** (S3-S4). Ya decidido por JR. |
| Tarea #29 | Reportes "ROS/RTE" | Nueva ley usa **RTS** (Art. 30); ROS es nombre viejo | Alinear terminología (ya previsto en post-cierre #41) |
| Fuente Minfin | URL dice "decreto-16-2026" | Es **Decreto 15-2026** | Solo es typo del enlace; el título del cronograma sí dice 15-2026 |

---

## Fases y entregables (resumen)

| Sem | Fase | Entregables clave | Responsable |
|---|---|---|---|
| **S1** (14-18 jul) | Arranque + Diagnóstico | Acta kickoff · Nota técnica de encuadre normativo · Diagnóstico operativo · Flujo **as-is** · Informe de revisión documental (Manual, Reglamento Interno, Código de Ética, políticas) | Ena, Thelma, Comercial, Legal |
| **S2** (21-25 jul) | Diagnóstico + Matriz de riesgo | **Matriz de brechas** vs Dto. 15-2026 · Flujo **to-be** (puntos KYC/EDD, alertas, escalamiento) · Borradores de 4 matrices de riesgo (clientes, desarrolladores, corredores, empleados) | Thelma, Legal, Comercial |
| **S3** (28 jul-1 ago) | Flujo + BF | Flujo nuevo **aprobado** · Matrices por segmento afinadas · Borrador **política de beneficiario final** | José, Ena, Thelma, Legal |
| **S4** (4-8 ago) | Redacción final (semana pico) | **Matriz consolidada + acta de aprobación** · **Manual v2** · Reglamento Interno v2 · Código de Ética v2 · Políticas v2 (KYC/PEP/proveedores) · Manuales de procedimiento v2 · Política BF + formulario digital · Borrador **EDD** | Thelma, Ena, Admón, Legal, Tecnología |
| **S5** (11-15 ago) | EDD + Reportes | Política **EDD** + procedimiento · **Procedimiento de reportes** (ROS/RTE/RTS/IN-25) con umbrales de escalamiento · Tablero de monitoreo de alertas | Thelma, Ena, José, Tecnología |
| **S6** (18-22 ago) | Capacitación + Piloto | Capacitación a Comercial/Admón/Gerencia · Documentos publicados en repositorio · **Piloto** con 3-5 casos reales | Thelma, José, Admón |
| **S7** (25-30 ago) | Cierre | Ajustes de piloto · Aprobación formal final · **Verificar actualización de datos ante IVE** · Informe ejecutivo de cierre + checklist | Ena, Thelma |
| **Post** | Seguimiento | Ajustar reportes/terminología cuando salga el **Reglamento SIB** (~sept) · Monitoreo mensual de alertas | Thelma (OC) + Legal |

---

## Cómo lo que ya tenemos hecho alimenta el cronograma (evita duplicar trabajo)

| Tarea del cronograma | Ya lo tienes en el vault |
|---|---|
| #2/#9 Leer ley + nota técnica de encuadre normativo | [[decreto-15-2026-ley-integral-ldft-fpadm]] (verbatim) + [[index]] (resumen de qué cambia y clasificación de Propi) |
| #6 Revisión diagnóstica documental (Manual) | [[analisis-brechas-15-2026]] — ya hecho, artículo por artículo |
| #8 **Matriz de brechas** vs Dto. 15-2026 | [[analisis-brechas-15-2026]] — es exactamente esto (falta cruzar con flujo as-is/to-be) |
| #3/#5 Flujo as-is/to-be y puntos de control KYC/EDD | [[procedimiento-expediente-cliente]] §1 — ya mapeé el as-is de Ena y propuse la secuencia to-be (KYC antes de mover dinero) |
| #10-#13 Matrices de riesgo por segmento | Base: la matriz actual del manual (Tablas 3-5) revisada; el análisis ya distingue clientes/desarrolladores/corredores |
| #17/#25 Política de beneficiario final | [[analisis-brechas-15-2026]] B1 (≥15%) + matriz de respaldos de [[procedimiento-expediente-cliente]] (declaración jurada BF + libro de accionistas) |
| #20/#23/#24 Manual v2, políticas KYC/PEP/proveedores, procedimientos | [[analisis-brechas-15-2026]] (qué cambiar) + [[procedimiento-expediente-cliente]] (DDC híbrida + matriz de documentos) |
| #26/#28 Política EDD (debida diligencia reforzada) | [[procedimiento-expediente-cliente]] §3 — elevadores por perfil = criterios que activan EDD |
| #29 Procedimiento de reportes (RTS/IN-25) | [[formularios-ive]] — calendario y periodicidad de IN-25, MY-28, ONU, RTS |
| #39 Verificar inscripción/actualización ante IVE | [[formularios-ive]] (IVE-RPO-01) + Constancia IVE en expediente |
| Ruta de fondos / matriz desarrolladores | [[analisis-fondos-terceros-15-2026]] |

> En la práctica: el trabajo que hicimos cubre buena parte de S1-S4 (encuadre, brechas, flujo, DDC, BF, reportes). Se puede entregar a Thelma como insumo para acelerar.

---

## Notas
- El cronograma cierra el 30-ago; la ley entra en vigor el 17-sep → buen margen. El reglamento SIB (~dic) queda para post-cierre, bien planteado.
- La **matriz consolidada aprobada por dirección** (S4, #19) es obligación legal (Art. 8: el proceso de riesgo debe ser aprobado por el órgano de dirección superior y estar documentado). Bien contemplado.
- La segmentación de DDC decidida (**híbrida: valor + perfil**, ver [[procedimiento-expediente-cliente]] §3) debe alimentar las matrices de riesgo #10-#13 y la política EDD #26.

## Relacionado
- [[analisis-brechas-15-2026]] · [[procedimiento-expediente-cliente]] · [[analisis-fondos-terceros-15-2026]] · [[formularios-ive]]
- [[propi]] · [[propi/mapa-operativo]] · [[decreto-15-2026-ley-integral-ldft-fpadm]]
