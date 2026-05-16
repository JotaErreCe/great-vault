---
type: reference
date: 2026-05-15
tags: [understanding-kids, drive, fase-2, inventario, documentos]
---

# UK — Análisis semántico inicial de Drive

Inventario semántico para mejorar el índice operativo de [[understanding-kids]]. A diferencia del primer índice de carpetas, esta pasada clasifica qué tipos de documentos existen, qué función cumplen, cuáles parecen fuente de verdad y cuáles son sensibles o históricos.

No se copian datos personales, bancarios, clínicos ni expedientes crudos.

## Alcance revisado

| Root | Ítems inventariados | Observación |
|---|---:|---|
| Drive Z14 / `Administración zona 14` | 728 | Mapeo hasta 2 niveles. |
| Drive CAES / `Administración CAES` | 417 | Mapeo hasta 3 niveles. |
| Drive `Talleres` | 801 | Mapeo previamente usado para formación/talleres. |

## Distribución por tipo de archivo

| Root | Folders | Sheets | Docs | PDFs | XLSX | Imágenes/videos | Otros |
|---|---:|---:|---:|---:|---:|---:|---:|
| Z14 | 262 | 17 | 29 Google Docs + 27 DOCX | 266 | 4 | 110 aprox. | PostScript, forms, markdown, shortcuts, etc. |
| CAES | 198 | 7 | 17 Google Docs + 9 DOCX | 142 | 23 | 9 aprox. | Forms, shortcuts, video. |
| Talleres | 230 | 75 | 41 Google Docs + 31 DOCX | 327 | 1 | 51 aprox. | Forms, videos, images, shortcuts. |

## Distribución por función operativa

| Root | Funciones dominantes |
|---|---|
| Z14 | Staff/RRHH, contenido/marketing, formación, clínica/pacientes, finanzas, legal/admin. |
| CAES | Formación/talleres, clínica/pacientes, staff/RRHH, finanzas. |
| Talleres | Formación/talleres casi por completo; además formularios, comprobantes, materiales, grabaciones. |

Estimación de material sensible por ruta/nombre:

| Root | Ítems sensibles aproximados | Razón |
|---|---:|---|
| Z14 | 292 / 728 | Expedientes, informes, base de datos, facturas, estados de cuenta, formularios/respuestas. |
| CAES | 260 / 417 | Expedientes, informes, facturas, estados de cuenta, cierres, formularios. |
| Talleres | 50 / 801 | Principalmente respuestas de formularios, comprobantes y participantes. |

## Fuentes de verdad candidatas por área

### Finanzas

| Área | Fuente candidata | Qué contiene / para qué sirve | Estado |
|---|---|---|---|
| Z14 mensual | `Administración Pagos/Resumen fin de mes` | Resúmenes por año; incluye 2022–2026 y `Proyección 2025.xlsx`. | Fuente principal para consolidación Z14. |
| Z14 caja | `Administración Pagos/Cierres de caja zona 14` | Cierres por año 2022–2026. | Validación/caja, no resumen principal. |
| Z14 bancos | `Administración Pagos/Estados de cuenta zona 14` | Estados 2025–2026. | Sensible; solo para conciliación puntual. |
| Z14 impuestos | `Control pago impuestos` | Pestañas 2022, 2023, 2024. | Fuente fiscal histórica; no mezclar con egresos sin revisar. |
| Z14 histórico ventas | `Análisis ventas y empresa/2022 ventas` | Ventas 2022 por mes, clientes, categorías y canal. | Útil para tendencia histórica/comercial. |
| Z14 redes/web costo | `Manejo de Redes` | Comparativo/propuesta de redes, hosting, mantenimiento web, IVA. | Histórico/contratación, no tablero actual. |
| CAES mensual | `Resumen Fin de Mes` | Resúmenes 2025 y 2026; `Resumen mayo 2026 CAES` tiene pestañas: primera quincena, efectivo, facturas por cobrar, segunda quincena y gastos operación. | Fuente principal CAES. |
| CAES caja/bancos | `Administración Pagos/Cierre de Caja`, `Estado de Cuentas CAES` | Cierre de caja 2026 y estados de cuenta CAES. | Validación/conciliación; sensible. |
| Talleres | `Talleres` + `UK — Tabla histórica...` + `Formato - Finanzas` | Operación financiera de formación/talleres. | En espera de Magoo/Mónica para completar. |

### Staff / RRHH

| Área | Fuente candidata | Uso |
|---|---|---|
| Staff vigente/pagos | iCloud `Understanding Kids/Pagos/2026` | Corte vivo de pagos a terapeutas/secretarias. |
| Expedientes Z14 | `Administración zona 14/Expedientes` | Contratos, documentos, antecedentes, títulos. Alta sensibilidad. |
| Expedientes CAES | `Administración CAES/Expedientes` | Expedientes de CAES y terapeutas. Alta sensibilidad. |
| Facturas terapeutas CAES | `Administración CAES/Facturas/Terapeutas/Facturas 2026` | Validar servicios profesionales/facturas por mes. |
| Roles admin | `Responsabilidades recepcionista.docx` | Posible documento de rol/proceso administrativo. Pendiente lectura segura. |
| Checklists terapeutas | `Terapeutas/Checklist de observación...` | Estándares operativos clínicos. |

### Clínica / pacientes

| Fuente | Uso | Regla |
|---|---|---|
| `Informes de Seguimiento` Z14/CAES | Seguimiento clínico por terapeuta/paciente. | No indexar pacientes ni contenido clínico en Vault. |
| `Información clientes` / `Base de datos` | Base de clientes/pacientes. | No usar salvo instrucción específica. |
| `Inscripción y políticas de pago` | Formularios y políticas. | Útil para proceso; respuestas contienen PII. |

### Comercial / marketing / contenido

| Fuente | Qué hay | Estado |
|---|---|---|
| Notion | Calendario actual de publicaciones. | Fuente principal actual para publicaciones según JR. |
| `Artes` / `Artes (JR)` | Campañas, UK, IS, assets. | Fuente de activos visuales/históricos. |
| `Contenido redes sociales` | Material de redes. | Histórico/soporte. |
| `Blog/2025` | Artículos/documentos de blog. | Útil para inventario editorial. |
| `Página web` | Datos/accesos/listados web. | Sensible; usar para auditoría web con cuidado. |
| `Manejo de Redes` | Costos/propuesta redes-hosting-mantenimiento. | Histórico, no necesariamente vigente. |
| `Logo`, `Flyers`, `Trifoliares`, `Flashcards`, `Webinars` | Material de marca y recursos. | Banco de activos. |

### Formación / cursos / talleres

| Fuente | Qué contiene | Nota |
|---|---|---|
| `Talleres` | Carpetas por taller/diplomado, formularios, participantes, materiales, grabaciones, presupuestos. | Fuente operativa principal de formación. |
| `Formación continua` Z14 | Material académico, manuales, PDFs, carpetas temáticas. | No confundir con fuente financiera de talleres. |
| `Planificación 2025` | Pestañas: Hoja 1, Curso para niñeras, Circuito, Terapia Grupal de lenguaje, Curso pre-universitarios, Club de lecto-escritura. | Fuente de calendario/planificación formación 2025. |
| `Curso de vacaciones / Cursos de vacaciones` | Texto comercial con cursos por edades, fechas, horarios y precios. | Útil para histórico de oferta. |

## Documentos leídos o muestreados sin copiar PII

### `FODA`

Contenido útil:

- Define misión y alcance de UK.
- Enumera servicios actuales: talleres para padres, talleres para profesionales, capacitaciones, diplomados, eventos con expositoras, terapias, tutorías, estimulación temprana, material de formación/aprendizaje, blogs.
- Segmenta audiencias: profesionales, padres, niños/familias, público general.
- Diferenciadores: no solo centro de terapia; enfoque multidisciplinar; formación continua; involucramiento familiar; informes y trabajo con padres/colegios.

Valor operativo: **documento estratégico** para misión, posicionamiento y futuro agente UK.

### `Reunión Contador`

Contenido útil:

- Notas fiscales/contables sobre nueva clínica, IVA, facturas de pequeño contribuyente, viajes, facturas especiales, préstamos e intereses.

Valor operativo: **referencia fiscal/contable**, no fuente de números operativos.

### `Curso de vacaciones / Cursos de vacaciones`

Contenido útil:

- Mensajes comerciales por curso, edades, fechas, horarios, ubicación Z14 y precios históricos.
- Ejemplos: cursos de 7 semanas, precios Q1,200, Q1,300 y Q1,000 según grupo/curso.

Valor operativo: **histórico de oferta comercial** y copy para cursos.

### `Manejo de Redes`

Contenido útil:

- Comparativo/propuesta con costos de redes, posts, hosting, mantenimiento web, diseño administrativo e IVA.

Valor operativo: **histórico de proveedores/costos de marketing/web**, no calendario vigente.

### `2022 ventas`

Contenido útil:

- Ventas mensuales 2022 por categorías: clientes nuevos, clientes totales, terapias, tutorías, estimulación, alimentación, lenguaje, evaluación, psicología, clases grupales, productos, etc.
- Segunda tabla por canal: referencia familiar/personal, redes sociales, flashcards, clases grupales, talleres, curso de vacaciones.

Valor operativo: **histórico comercial/financiero** para tendencias y mix de servicios.

## Lectura semántica: qué hay realmente en Drive

1. UK no tiene solo “finanzas” y “staff”; tiene cuatro sistemas documentales mezclados:
   - operación administrativa;
   - clínica/pacientes;
   - formación/comercial;
   - contenido/marca/web.
2. La carpeta Z14 es el hub histórico y administrativo más amplio.
3. La carpeta CAES está más orientada a operación de sede: pagos, expedientes, informes, inventario, talleres y resúmenes mensuales.
4. La carpeta Talleres funciona como línea de negocio separada con su propio mini-Drive operativo.
5. Hay mucho material que sirve para construir el futuro agente, pero debe etiquetarse por permiso:
   - lectura libre resumida: FODA, planificación, materiales públicos, índices;
   - lectura con cuidado: finanzas, facturas, estados, formularios;
   - no resumir salvo instrucción: expedientes, informes clínicos, bases de clientes, comprobantes.

## Mejoras necesarias al índice operativo

- Crear una tabla de **documentos clave**, no solo carpetas.
- Marcar cada fuente con:
  - área;
  - sede;
  - sensibilidad;
  - vigencia;
  - si sirve para números, proceso, estrategia, contenido o cumplimiento.
- Separar `fuente de verdad` de `archivo histórico/de apoyo`.
- Para documentos sensibles, indexar existencia y función, no contenido.

## Próxima acción recomendada

Crear `catalogo-fuentes-drive.md` con filas tipo:

| Fuente | Sede/área | Tipo | Sensibilidad | Vigencia | Sirve para | Cómo usar |
|---|---|---|---|---|---|---|

Ese catálogo será mejor base para el futuro agente UK que el índice de carpetas actual.

## Relacionado

- [[understanding-kids/indice-operativo-drive-2026-05-15]] · [[understanding-kids/mapa-operativo]] · [[understanding-kids/pendientes-operativos-2026-05-15]] · [[understanding-kids/finanzas]] · [[understanding-kids/staff]] · [[understanding-kids/formacion]]
