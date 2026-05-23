---
type: reference
date: 2026-05-14
tags: [understanding-kids, auditoria, fase-1, geoffrey]
---

# UK — Auditoría fase 1 — 2026-05-14

Auditoría inicial para nutrir Understanding Kids antes de crear un agente especializado. No guarda transcripts ni datos sensibles crudos; solo hallazgos operativos.

## Fuentes revisadas

- Vault actual:
  - `wiki/proyectos/activos/understanding-kids.md`
  - `understanding-kids/finanzas.md`
  - `understanding-kids/operacion.md`
  - `understanding-kids/staff.md`
  - `uk-catalogo.md`
  - `diplomado-autismo-2026.md`
  - `integracion-sensorial.md`
- Drive / Google Workspace:
  - `UNDERSTANDING_KIDS_MAESTRO.md` (`2026-04-08`)
  - carpeta `Administración Pagos`
  - carpeta `Resumen fin de mes`
  - carpeta `Qpaypro`
  - hojas recientes 2026 de resumen mensual/quincenal
  - hoja `2026 diplomado`
- Gmail metadata/snippets recientes:
  - WordPress `kidsunderstanding.com`
  - Meta for Business / Publicidad Understanding Kids
  - OpenAI workspace Understanding Kids
- Web pública:
  - `kidsunderstanding.com`
  - tienda `kidsunderstanding.com/tienda1/`
  - carrito/checkout con producto de prueba en sesión temporal

## Hallazgos confiables

### Arquitectura de negocio

- UK está documentada como marca sombrilla con tres grandes mundos:
  - clínica;
  - formación;
  - línea B2B para colegios/instituciones en definición.
- Integración Sensorial opera como submarca temática/comercial, no como unidad operativa separada todavía.
- ToyLab y Muffin están pausadas.

### Operación y sistemas

- Drive sigue siendo la fuente operativa real más rica; Notion está declarado como objetivo/futuro hub, pero no se verificó acceso directo desde este runtime.
- `~/Documents/Understanding Kids/` aparece como fuente primaria en el Vault, pero no existe actualmente en la Mac revisada. Lo local accesible es principalmente el Vault y su backup.
- Sistemas identificados: WordPress + WooCommerce, QPayPro/Recurrente, FEL, Google Drive, Notion, Meta Ads.
- Hay carpetas Drive operativas clave: `Administración Pagos`, `Resumen fin de mes`, `Qpaypro`.

### Finanzas

- El Vault tiene febrero 2026 como último corte consolidado y confirmado.
- Drive contiene hojas recientes posteriores: marzo, abril y mayo 2026, con estructura por quincenas, efectivo, parqueo, facturas por cobrar y gastos de operación.
- La hoja de mayo existe y fue modificada el 2026-05-14.
- La lectura financiera mensual completa aún requiere consolidación; hay riesgo de datos mezclados por sede/unidad y por Integración Sensorial.

### Formación / diplomados

- `2026 diplomado` existe como hoja activa y contiene pestañas de cuentas, pagos realizados, temario/fechas y ponentes.
- El diplomado de Autismo 2026 está bien documentado en Vault para campaña, mensaje, fases, pauta y pendientes.
- También aparece la línea de Diplomado Internacional de Integración Sensorial 2026, vinculada a formularios/archivos en Drive.

### Web / e-commerce

- La tienda pública lista 90 productos.
- El carrito funciona para agregar un producto de prueba en sesión temporal.
- El checkout carga y muestra métodos: efectivo contra entrega y pago con tarjeta vía Recurrente.
- El producto agregado aparece sin nombre visible claro en el carrito/checkout (`“” se ha añadido...` / nombre vacío), lo cual es una señal de problema de catálogo/tema/plugin.
- No se completó compra ni se envió pedido.

### Gmail/señales recientes

- Hay actividad frecuente de WordPress: comentarios pendientes de moderación en blog.
- Hay actividad reciente de Meta Ads para Publicidad Understanding Kids, incluyendo aprobaciones de anuncios y recibos.
- Hay aviso de OpenAI: el plan/workspace de ChatGPT Business de Understanding Kids no renovará y quedaría disponible hasta 2026-06-08, según snippet revisado.

## Dudoso o desactualizado

- `last-touched` de varias páginas UK del Vault es 2026-05-02/04, pero Drive muestra actividad financiera y de campañas posterior.
- El estado “checkout roto” necesita redefinirse: la página de checkout sí carga con producto en sesión temporal, pero hay señales de configuración defectuosa: nombre de producto vacío, mezcla idioma, métodos de pago posiblemente incompletos y falta de prueba de pago real.
- Notion se menciona como hub objetivo y fuente activa de contenido, pero no fue auditado directamente.
- El directorio local `~/Documents/Understanding Kids/` indicado en el Vault no existe en esta Mac.

## Faltantes principales

1. Confirmar fuente de verdad actual por área: Drive, Notion, web, Canva, WhatsApp, Gmail.
2. Consolidar finanzas marzo–mayo 2026 sin exponer datos sensibles de pacientes/clientes.
3. Separar vistas financieras: UK sin IS / solo IS / con IS.
4. Verificar flujo real del checkout hasta antes de pago y revisar QPayPro/Recurrente con credenciales aprobadas por JR.
5. Confirmar precios vigentes de clínica y evaluación.
6. Completar historial de diplomados/formación y resultados comerciales.
7. Confirmar estructura actual de staff, roles y apellidos completos sin publicar datos personales innecesarios.
8. Definir línea UK en el Aula / colegios.
9. Revisar calendario comercial y contenido orgánico/campañas.
10. Decidir si WordPress comentarios/blog son canal vivo o ruido operativo.

## Preguntas agrupadas para JR/Mónica

### A. Fuente de verdad

1. ¿Notion ya debe tratarse como fuente principal, o todavía Drive manda y Notion es aspiracional?
2. ¿Dónde vive hoy el calendario de contenido real: Notion, Canva, Drive, Meta Planner u otro?
3. ¿El folder local `~/Documents/Understanding Kids/` debería existir o ya fue reemplazado por Drive/Vault?

### B. Prioridad inmediata

4. De estos frentes, ¿cuál quiere atacar primero: checkout/web, finanzas, formación/diplomados, contenido/Meta Ads, staff/operación, o colegios?
5. ¿El problema del checkout sigue siendo “no se puede comprar”, o ahora es más bien “checkout mal configurado / no confiable / no probado”?

### C. Finanzas

6. ¿Quiere que consolide marzo, abril y mayo 2026 en el Vault con totales por sede/unidad, evitando nombres de pacientes/clientes?
7. ¿Cómo quiere manejar Integración Sensorial financieramente: centro de costo separado desde ya, etiqueta dentro de UK, o solo vista analítica?
8. ¿Cuál es la métrica principal para UK: utilidad total, ingresos por sede, margen por línea, ocupación de terapeutas, leads/ventas de formación, u otra?

### D. Formación y campañas

9. ¿El Diplomado de Autismo 2026 y el Diplomado de Integración Sensorial 2026 son campañas separadas con prioridades distintas?
10. ¿Quién es responsable hoy de responder leads/WhatsApp de diplomados y cerrar ventas?
11. ¿Hay meta de ventas/cupos para cada diplomado?

### E. Web / tienda

12. ¿Puedo auditar WordPress/WooCommerce con acceso cuando usted lo apruebe, sin cambiar nada?
13. ¿QPayPro sigue siendo el procesador real, o Recurrente reemplazó/absorbe ese flujo?
14. ¿Los 90 productos de tienda siguen vigentes o hay que depurar catálogo?

### F. Futuro agente UK

15. Por ahora, el mejor agente UK parece necesitar foco en `operación + finanzas + comercial`, no solo marketing. ¿Está de acuerdo?
16. ¿Quiere que ese agente, cuando exista, lea WhatsApp/Gmail/Drive solo para detectar señales y preparar reportes, sin responder ni publicar?

## Recomendación de Geoffrey

Antes de crear el agente UK, completar tres bloques en Vault:

1. `mapa-operativo.md`: fuentes, responsables, procesos, sistemas, permisos.
2. `finanzas-2026.md`: totales mensuales limpios por sede/unidad, sin datos personales crudos.
3. `comercial-formacion.md`: diplomados, campañas, leads, WhatsApp, pauta, metas y pendientes.

Luego sí diseñar el agente especializado con responsabilidades claras.

## Relacionado

- [[understanding-kids]] · [[proyectos/activos/understanding-kids/finanzas]] · [[proyectos/activos/understanding-kids/operacion]] · [[uk-catalogo]] · [[diplomado-autismo-2026]] · [[integracion-sensorial]] · [[agentes/arquitectura]]

## Respuestas de JR — 2026-05-14

- Drive sigue mandando como fuente principal operativa.
- Notion únicamente manda por ahora para publicaciones de redes.
- Prioridad siguiente: staff y operación.
- Recurrente reemplazó por completo a QPayPro.
- JR pidió explicar antes qué se consolidaría financieramente.
- JR preguntó dónde se encontró el catálogo de 90 productos.

## Respuestas adicionales de JR — 2026-05-14 14:38

- Catálogos actuales desactualizados; no tomarlos en cuenta por ahora.
- Finanzas requieren análisis más profundo porque los Excel/Sheets no tienen formato unificado.
- Proseguir con staff y operación.

## Staff/operación — fuente iCloud agregada

JR indicó que para staff/operación no debe auditarse solo Drive/Vault: también usar iCloud `Understanding Kids/Pagos`, especialmente pagos quincenales de terapeutas y secretarias.

Se creó auditoría específica: `wiki/proyectos/activos/understanding-kids/staff-auditoria-2026-05-14.md`.
