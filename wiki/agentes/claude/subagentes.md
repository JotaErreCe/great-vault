---
type: reference
date: 2026-10-19
tags: [agente, claude, subagentes]
---

# Subagentes de Claude

Agentes que Claude lanza como coordinador ([[agentes/claude/rol-coordinador]]). Trabajan para Claude, no hablan con JR; Claude revisa todo antes de mostrarlo. Sus definiciones viven fuera del Vault, en `~/Claude/.claude/agents/<nombre>.md` (estado de runtime); aquí se documenta qué hace cada uno.

## Definidos en `~/Claude/.claude/agents/`

| Agente | Para qué | Entrega en | Reglas clave |
|---|---|---|---|
| `compras` | Asesor de compras para la casa nueva: qué distingue un producto bueno, modelos que de verdad se venden en Guatemala, dentro del presupuesto | `~/Claude/pendiente-vault/compras/<tema>/` | Nunca inventar precios, medidas, modelos ni disponibilidad; cada dato con URL y fecha; verificar que quepa (con la holgura de ventilación del fabricante); voltaje, garantía local, tarifa EEGSA, dureza del agua; sin rayas largas |
| `interiores` | Diseñador de interiores de la casa nueva: planos a escala, distribución, propuestas visuales | `~/Claude/pendiente-vault/interiores/<ambiente>/` | Nunca inventar una medida (supuesto marcado + pregunta); recomendaciones de medidas con fuente citada; planos a escala con cotas en metros, orientación, puertas, arcos y chimenea; seguridad para Nico y el perro |
| `pendientes-magoo` | Revisa correos de Magoo a jcastaneda@ sin respuesta desde el 1-ago-2026 y pendientes con ella en Notion; arma la checklist «✅ Pendientes con Magoo» en Notion y redacta respuestas | Página de Notion + reporte | **Ningún correo sale**; solo lectura en Gmail (`gws`); borradores de tú, cortos, con «cachetes de conejo», sin rayas largas; no cambia `Status` ni toca Drive; dudas como opción múltiple (máx. 4, la recomendada primero) |
| `legal` | Redactor de contratos y documentos legales (UK y AMC Legal), derecho guatemalteco; versiones nuevas sobre formatos existentes | `~/Claude/pendiente-vault/legal/<tema>/` | Nunca inventar datos ([PENDIENTE]); solo cambios decididos por JR; nunca sobrescribir originales (V2, V3…); sin vocabulario laboral en contratos civiles; verificar el DOCX como texto; sin rayas largas |
| `auditor-vault` | Auditoría del Great Vault: enlaces rotos, duplicados, desactualizado, contradicciones, huérfanas, huecos, forma; ideas de segundo cerebro | `~/Claude/pendiente-vault/auditoria-vault/<AAAA-MM-DD>/` | Solo lectura sobre el Vault; no abre `_sensitive.md` ni copia secretos; cada hallazgo con ruta y evidencia; sin rayas largas |
| `precios-uk` | Análisis de precios y paquetes de UK: escenarios con precio a la familia, costo de terapeuta, comisión de cobro y margen | `~/Claude/pendiente-vault/precios-uk/<tema>/` | Nunca inventar precios ni costos (fuente por cada número, supuestos marcados); solo propone; sin rayas largas |
| `finanzas-uk` | Analista financiero experto de UK: cierres por sede, costo real por sesión, reparto de gastos compartidos, impuestos; fuente de números de otros agentes | `~/Claude/pendiente-vault/finanzas-uk/<tema>/` (+ `criterios.md`) | Cero supuestos (pregunta lo que falta); cada número con fuente; cuadre contra contador; reglas de JR: reparto por % de clientes por sede, margen mínimo 20% = (P−C)/P, vehículo aparte |
| `buscador-drive` | Bibliotecario del Drive (jcastaneda@ y joserca95@): índice completo + mapa legible; los demás agentes le piden archivos | Índice `~/Claude/state/drive-index/`, mapa [[mapa-drive]] | Solo lectura; sin contenido ni nombres de pacientes en el Vault; nunca elige entre candidatos; actualización semanal (launchd `com.jr.drive-mapa`, domingo 4:00, `~/Claude/bin/drive-mapa-semanal.sh`) |

Los agentes `compras` e `interiores` leen la nota de la casa en `~/Claude/pendiente-vault/casa-nueva-canada-de-elgin.md`. Desde el 19-oct-2026 la versión canónica está en el Vault: [[casa-canada-de-elgin]] (la copia local se conserva; **pendiente** actualizar la ruta en sus definiciones).

## Correcciones de artes a demanda

«El agente que hace arte» es la tarea programada `uk-artes-semanales`. Sus corridas son desatendidas: **no se les puede mandar mensajes** (falla con «session is unattended»). Para corregir artes fuera del domingo se lanza un subagente que lee `~/.claude/scheduled-tasks/uk-artes-semanales/SKILL.md` y la [[guia-maestra-estilo]], y trabaja con el sistema de plantillas: script nuevo `Sistema/armar_correccion_<fecha>_<tema>.py`, render en `Pendientes de Revision/<pieza> (v2)/`, nunca se modifican ni se corren scripts viejos.

**Cómo se cierra una corrección (decisión de JR, 19-oct-2026, resuelve la contradicción anterior): no se le escribe correo a Magoo.** Magoo pide los cambios por Notion (comentarios en la página o en cada lámina + Status «Cambios pedidos»), y los procesa la corrida `uk-cambios` (lunes, miércoles y viernes 20:00). Una corrección a demanda por Telegram tampoco dispara el cierre: no se sube a Drive, no se cambia a Aprobado/Publicado y no se escribe a Magoo (`~/Claude/CLAUDE.md`); el cierre lo hace `uk-cierre` cuando Magoo pone «Aprobado», sin correo.

> Histórico, **superado** en este punto: el 21-sep-2026 JR había pedido cerrar cada corrección respondiendo el correo original de Magoo («De ahora en adelante voy a necesitar que respondas a los correos que ella me mandó…»), con Status → Done. Ni ese correo ni el estado «Done» se usan ya.

Preferencias de arte que salieron de la sesión del 21-sep: ver [[artes-decisiones-y-lecciones]] § Correcciones del 21-sep.

## Relacionado

- [[agentes/claude/AGENT|Claude]] · [[agentes/claude/rol-coordinador]]
- [[casa-canada-de-elgin]] · [[sistema-artes-redes]] · [[artes-decisiones-y-lecciones]]
- [[agentes/claude/correo]] · [[monica]]
