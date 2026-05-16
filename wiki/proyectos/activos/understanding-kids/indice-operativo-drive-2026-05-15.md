---
type: reference
date: 2026-05-15
tags: [understanding-kids, drive, operacion, fase-2, z14, caes]
---

# UK — Índice operativo Drive Z14/CAES

Índice de fuentes de verdad para fase 2 del mapa operativo de [[understanding-kids]]. No copia datos de pacientes, clientes, bancos, DPI ni expedientes crudos; solo ubica fuentes y uso operativo.

## Resumen ejecutivo

| Sede / área | Root Drive identificado | Estado |
|---|---|---|
| Z14 / administración principal | `Administración zona 14` | Mapeado hasta 2 niveles; contiene administración, pagos, finanzas, RRHH, contenido, web y expedientes. |
| CAES / administración sede 2 | `Administración CAES` | Mapeado hasta 3 niveles; contiene pagos, cierres, estados de cuenta, expedientes, facturas, informes, inventario y talleres. |
| Talleres/formación | `Talleres` (`19XFN_MxgAklPxWg2wtIUQUrqAcY9JMi9`) | Ya tratado como fuente primaria de talleres/formación; en espera de respuesta Magoo/Mónica para datos faltantes. |

## Regla de uso

- **Drive manda** como fuente operativa principal.
- El Vault guarda solo índices, decisiones y resúmenes agregados.
- No copiar al Vault nombres de pacientes, expedientes, comprobantes, cuentas bancarias, DPI, direcciones, teléfonos ni datos clínicos.
- Para futuras consultas del agente UK, usar este índice para saber dónde buscar antes de leer contenido sensible.

---

## Z14 — fuentes principales

### 1. Administración / pagos / finanzas operativas

Root: `Administración zona 14/Administración Pagos`

| Subfuente | Uso operativo | Notas |
|---|---|---|
| `Resumen fin de mes` | Fuente primaria para ingresos/gastos mensuales Z14 | Contiene `Resumen 2022`, `Resumen 2023`, `Resumen 2024`, `Resumen 2025`, `Resumen 2026` y `Proyección 2025.xlsx`. |
| `Cierres de caja zona 14` | Caja diaria/mensual Z14 | Separado por años 2022–2026. Usar para validar efectivo/caja, no como resumen único. |
| `Estados de cuenta zona 14` | Conciliación bancaria | Contiene 2025 y 2026. Tratar como sensible. |
| `Control pago impuestos` | Impuestos | Útil para IVA/ISR/control fiscal; no mezclar con egresos operativos sin revisar. |
| `Horas trabajadas` | Horas por terapeuta | Histórico 2022–2023 detectado; revisar si hay fuente actual antes de usar. |
| `Parqueo` | Control de parqueo | Operativo auxiliar. |
| `Pago Taller de Dificultades en la alimentación` | Taller específico | Fuente histórica puntual, no sistema general. |
| `Curso pre universitarios` | Curso específico | Fuente histórica puntual. |
| `Control Horas Paola` | Control persona específica | Probablemente histórico o puntual. |

### 2. Análisis histórico / negocio

Root: `Administración zona 14/Análisis ventas y empresa`

| Archivo / carpeta | Uso |
|---|---|
| `2021 ventas .xlsx` | Histórico ventas 2021. |
| `2022 ventas` | Histórico ventas 2022. |
| `Flujo de Caja UK` | Flujo de caja / análisis financiero. |
| `Análisis empresa Mónica 3.xlsx` | Análisis antiguo de empresa. |

Uso recomendado: reconstrucción histórica y tendencias, no operación diaria.

### 3. Staff / expedientes / RRHH

| Fuente | Uso | Sensibilidad |
|---|---|---|
| `Expedientes` | Documentación de personal/contratistas Z14 | Alta: contratos, DPI, antecedentes, títulos, RENAS. No copiar detalles. |
| `Currículum recepcionistas` | Reclutamiento admin/recepción | Alta/media: CVs y datos personales. |
| `IGSS` | Constancias/gestión laboral | Alta. |
| `Cartas de Materiales` | Entrega/uso de materiales por personal | Media. |
| `Responsabilidades recepcionista.docx` | Rol administrativo | Útil para operación; revisar contenido antes de resumir. |
| `Terapeutas` | Checklists operativos para terapeutas | Útil para estándares internos. |

Nota: para pagos/staff vigente, iCloud `Understanding Kids/Pagos/2026` sigue siendo fuente crítica complementaria.

### 4. Clínica / pacientes / informes

| Fuente | Uso | Regla |
|---|---|---|
| `Informes de Seguimiento` | Informes clínicos y seguimiento por terapeuta/paciente | No indexar pacientes en Vault. Solo usar para confirmar existencia de sistema, no extraer contenido clínico. |
| `Información clientes` / `Base de datos` | Clientes/pacientes | Fuente sensible. No usar salvo instrucción específica y con minimización. |
| `Inscripción y políticas de pago` | Formularios/políticas | Útil para flujo operativo; formularios pueden contener PII. |

### 5. Contenido / marca / web

| Fuente | Uso |
|---|---|
| `Artes` | Artes 2026, campañas, UK/IS. |
| `Artes (JR)` | Artes históricas o gestionadas por JR, especialmente Integración Sensorial. |
| `Contenido redes sociales` | Material/redes; Notion sigue mandando para publicaciones actuales. |
| `Blog` | Contenido blog. |
| `Página web` | Datos y activos web; posible fuente para auditoría WooCommerce/checkout. |
| `Logo`, `Flyers`, `Trifoliares`, `Flashcards`, `Webinars` | Material de marca y contenido histórico. |
| `Manejo de Redes` | Posible control/plan de redes. Revisar antes de usar. |

### 6. Legal / administración corporativa

| Fuente | Uso |
|---|---|
| `Sociedad Anónima` | Documentos corporativos de Inversiones Multidisciplinarias, S.A. |
| `Contador` / `Reunión Contador` | Documentación contable/administrativa. |
| `Facturas` | Facturas por años/categorías. Sensible. |
| `Inventario General` | Inventario Z14. |

---

## CAES — fuentes principales

Root: `Administración CAES`

### 1. Administración / pagos / finanzas operativas

| Subfuente | Uso operativo | Notas |
|---|---|---|
| `Administración Pagos / Cierre de Caja` | Caja CAES | Contiene `Cierre de Caja 2026`, incluyendo carpeta de mayo. |
| `Administración Pagos / Estado de Cuentas CAES` | Conciliación bancaria CAES | Contiene 2026, abril detectado. Sensible. |
| `Resumen Fin de Mes` | Fuente principal para resumen mensual CAES | Contiene `Resumen 2025` y estructura mensual; ya fue usada para datos CAES 2025/2026. |

### 2. Staff / expedientes / facturas

| Fuente | Uso | Sensibilidad |
|---|---|---|
| `Expedientes` | Expedientes de personal CAES y algunos terapeutas | Alta: DPI, contratos, antecedentes, RENAS, títulos. No copiar detalles. |
| `Facturas / Terapeutas / Facturas 2026` | Facturas de terapeutas por mes | Alta/media; útil para validar pagos por servicios profesionales. |

### 3. Clínica / pacientes / informes

| Fuente | Uso | Regla |
|---|---|---|
| `Informes de seguimiento` | Informes por terapeuta/paciente CAES | No indexar pacientes ni datos clínicos en Vault. |

### 4. Inventario y talleres CAES

| Fuente | Uso |
|---|---|
| `Inventario Material / INVENTARIO CAES.xlsx` | Inventario sede CAES. |
| `Talleres` | Talleres específicos de CAES, inscripciones, participantes y materiales. |

---

## Talleres/formación — fuente separada

Root confirmado por JR: `Talleres` (`19XFN_MxgAklPxWg2wtIUQUrqAcY9JMi9`).

Estatus:

- Tabla histórica y formato financiero ya creados.
- Pendiente de respuesta Magoo/Mónica para completar datos faltantes.
- Esta carpeta no debe mezclarse con `Formación continua` de Z14: `Formación continua` es más académica/material; `Talleres` es la fuente operativa/financiera de talleres.

## Mapa por tipo de pregunta

| Pregunta futura | Buscar primero | Validar con |
|---|---|---|
| ¿Cuánto vendió Z14 en un mes? | Z14 → `Administración Pagos/Resumen fin de mes` | Cierres de caja / estados de cuenta si hace falta. |
| ¿Cuánto vendió CAES en un mes? | CAES → `Resumen Fin de Mes` | Cierres de caja / estados de cuenta CAES. |
| ¿Qué pagos de staff están pendientes? | iCloud `Understanding Kids/Pagos/2026` | Facturas terapeutas / expedientes solo si hace falta. |
| ¿Quién trabaja en UK y en qué rol? | `staff.md` + iCloud pagos | Expedientes solo para confirmar documentación, no para publicar datos. |
| ¿Qué talleres/diplomados existen y cuánto dejaron? | Drive `Talleres` + Sheet histórica | Formato Finanzas / respuesta Magoo/Mónica. |
| ¿Qué contenido publicar? | Notion actual | Drive `Artes`, `Contenido redes`, Canva. |
| ¿Cómo está checkout/web? | WordPress/WooCommerce + Drive `Página web` | Prueba controlada read-only/checkout sin pago. |
| ¿Qué documentos legales/contables existen? | Z14 → `Sociedad Anónima`, `Contador`, `Facturas` | No copiar datos sensibles. |

## Riesgos detectados en Fase 2

1. **Duplicidad de fuentes**: Z14 tiene `Resumen fin de mes`; CAES tiene `Resumen Fin de Mes`; talleres tiene otra carpeta separada.
2. **PII abundante** en expedientes, informes, formularios y comprobantes.
3. **Nombres similares**: `Formación continua` no equivale a `Talleres`.
4. **Finanzas dispersas**: caja, resumen mensual, estados de cuenta, impuestos y facturas no son intercambiables.
5. **Contenido disperso**: Notion manda para publicaciones actuales, pero Drive contiene artes/material histórico.

## Próximas acciones de Fase 2

- [ ] Crear tabla de fuentes por sede/unidad para consolidación financiera marzo–mayo 2026.
- [ ] Confirmar si `Resumen Fin de Mes` CAES es suficiente como fuente mensual o si hay que cruzar con caja/estados.
- [ ] Revisar si ya aparecieron pagos de mayo en iCloud antes de actualizar staff.
- [ ] Indexar, sin PII, qué carpetas de expedientes corresponden a personal activo vs inactivo.
- [ ] Separar en Vault: `finanzas-2026-z14-caes.md` cuando JR autorice consolidación.

## Relacionado

- [[understanding-kids/mapa-operativo]] · [[understanding-kids/pendientes-operativos-2026-05-15]] · [[understanding-kids/operacion]] · [[understanding-kids/finanzas]] · [[understanding-kids/staff]] · [[understanding-kids/comercial-formacion]]
