---
type: audit
date: 2026-05-17
tags: [geoffrey, memoria, vault, auditoria]
---

# Auditoría de Vault con memory-writing-best-practices — 2026-05-17

Auditoría solicitada por JR usando [[agentes/geoffrey/memory-writing-best-practices]] y [[escribir-memoria]]. Enfoque: memoria que envejece mal, rutas hardcodeadas, datos sensibles fuera de `_sensitive.md`, transcripts/relleno, duplicación y punteros rotos.

## Alcance

- Archivos Markdown revisados: **156**.
- Excluidos deliberadamente: `_sensitive.md`, `.obsidian/`, `.stfolder/`, `.git/`.
- Herramientas: scripts read-only con `find`, `python3` y lectura directa.
- No se corrigieron hallazgos en esta pasada salvo crear este reporte y registrar el log.

## Resultado ejecutivo

El Vault está funcional y bastante ordenado, pero hay **4 focos de higiene**:

1. **Rutas absolutas y rutas de runtime dentro de memoria/wiki**: varias son históricas o justificadas, pero algunas contradicen la regla de no hardcodear rutas fuera de la fuente canónica.
2. **Contaminación de root por artefactos runtime/skills**: existen `skills/`, `.clawhub/` y `.openclaw/` dentro del root del Vault, fuera de la arquitectura declarada.
3. **Datos sensibles o semi-sensibles fuera de `_sensitive.md`**: principalmente chasis/placa, teléfono público de UK, carné UFM, contacto de servicio, y referencias a expedientes con DPI; no encontré contraseñas/API keys reales copiadas.
4. **Estado vivo en páginas canónicas y conversaciones**: en proyectos está bien si está fechado, pero algunas frases “hoy/mañana/actualmente” deben tener corte o moverse a dashboard/pendientes.

## Hallazgos por severidad

### Alta — revisar pronto

#### A1. Artefactos runtime/skills en root del Vault

El schema de [[_AI_BOOTSTRAP]] define el root como `_AI_BOOTSTRAP.md`, `_CLAUDE.md`, `_sensitive.md`, `_templates/`, `raw/` y `wiki/`. Sin embargo existen:

- `skills/` con `gmail` y `apple-mail-macos`.
- `.clawhub/lock.json`.
- `.openclaw/workspace-state.json`.

Riesgo: el Vault vuelve a absorber runtime/tooling, justo el antipatrón que JR ya corrigió antes. También puede hacer que agentes futuros crean que las skills viven dentro del Vault.

Recomendación: mover o eliminar estos artefactos del Vault después de confirmar si OpenClaw/ClawHub los sigue usando. Si se mueven, registrar en log y dejar el catálogo/auditoría solamente en `wiki/agentes/skills/`.

#### A2. `_AI_BOOTSTRAP.md` contiene una ruta hardcodeada problemática

Hallazgo:

- `_AI_BOOTSTRAP.md`: “Tienes acceso directo al filesystem (`~/Documents/Great Vault/`). Lee, edita y crea archivos directamente.”

Riesgo: contradice [[escribir-memoria]], que nació precisamente porque `~/Documents/Great Vault` es válido en Mac Mini pero falso en Mac Pro. Aunque `_AI_BOOTSTRAP` sea fuente canónica, esa frase debería expresar resolución por host, no una ruta única.

Recomendación: reemplazar por algo como: “Si tienes filesystem, resuelve la ruta del Vault según host; en Mac Mini suele ser `~/documents/Great Vault`, en Mac Pro `~/Great Vault`; si falla, consulta el bootstrap/routing local antes de crear archivos.”

#### A3. Datos de vehículo fuera de `_sensitive.md`

Hallazgo:

- `wiki/resources/outlander-2026.md`: chasis completo y placa.

Riesgo: placa/chasis son identificadores sensibles del vehículo. En memoria operativa puede bastar un puntero a `_sensitive.md` o últimos 4/característica parcial.

Recomendación: mover chasis/placa completa a `_sensitive.md`; en `outlander-2026.md` dejar “identificadores completos en `_sensitive.md`” y datos de mantenimiento no sensibles.

### Media — corregir en lote controlado

#### M1. Rutas absolutas de runtime en archivos duraderos

Ejemplos representativos:

- `SOUL.md`, `TOOLS.md`, `IDENTITY.md` en root: rutas `/Users/jr/.openclaw/...` y `/Users/jr/documents/Great Vault/...`.
- `wiki/agentes/arquitectura.md`: rutas absolutas de workspace neutral y Geoffrey.
- `wiki/agentes/skills/*.md`: rutas absolutas a skills, binarios y configs.
- `wiki/agentes/geoffrey/brief-mananero.md`: rutas absolutas a scripts de validación/scan.

Riesgo: muchas rutas son útiles como documentación técnica, pero deben distinguirse entre “ejemplo local actual” y “fuente universal”. Si no, agentes en otra máquina fallan.

Recomendación: normalizar redacción:

- Para reglas duraderas: “resolver desde workspace activo / skill permitida”.
- Para documentación técnica: marcar “Ruta observada en Mac Mini al YYYY-MM-DD”.
- Para rutas necesarias de scripts runtime: considerar un índice `wiki/agentes/geoffrey/runtime-local.md` o mantenerlas en workspace, no en memoria general.

#### M2. Estado vivo con frases “hoy/mañana/actualmente”

Ejemplos:

- `wiki/proyectos/activos/understanding-kids/staff.md`: “Pagos de mayo pendientes de hacerse hoy/mañana.”
- `wiki/proyectos/activos/understanding-kids/staff-auditoria-2026-05-14.md`: frase similar.
- `wiki/proyectos/activos/uk-catalogo.md`: “Checkout actualmente roto.”
- `wiki/proyectos/activos/propi.md`, `tesis.md`: secciones “Estado actual”.

Riesgo: no todo es malo; en páginas de proyecto puede haber estado, pero debe estar fechado y apuntar a la fuente viva. “Hoy/mañana” caduca inmediatamente.

Recomendación: convertir a cortes fechados:

- “Al 2026-05-14, pagos de mayo pendientes según JR; verificar Reminders/Drive antes de actuar.”
- “Checkout no confiable/no probado al corte X; verificar antes de afirmar que está roto.”

#### M3. Slug typo: `disengo-casa` vs Disegno Casa

Hallazgo:

- Archivo y wikilinks usan `disengo-casa`, pero el nombre correcto es **Disegno Casa**.

Riesgo: aunque los wikilinks funcionan, el slug mal escrito se vuelve memoria duradera incorrecta y puede propagarse.

Recomendación: renombrar `wiki/proyectos/activos/disengo-casa.md` → `disegno-casa.md` y actualizar wikilinks. Hacerlo como cambio controlado con búsqueda y log.

#### M4. Wikilinks rotos / falsos positivos

Hallazgos reales o revisables:

- `raw/Why Google Just Gave Away Gemma 4 for Free.md`: mención a `Ali H. Salem` sin página canónica.
- `raw/Post by @danpeguine on X.md`: mención a `@danpeguine` sin página canónica.

Falsos positivos aceptables:

- `wiki/agentes/geoffrey/memory-writing-best-practices.md`: el placeholder de ejemplo fue convertido a texto plano en la auditoría de enlaces del 2026-05-22.
- `wiki/log/2026-05.md`: `[[JR]]` aparece como parte de una entrada histórica de normalización.

Recomendación: en `raw/` no urge corregir; si esos autores importan, crear páginas/personas o convertir a texto plano para evitar nodos huérfanos.

### Baja — monitorear

#### B1. Duplicación menor aceptable

Se detectaron duplicados de líneas largas entre manuales/skills, por ejemplo comandos de dump de Reminders y frases de “evitar guardar mensajes crudos”. No es grave: son reglas transversales repetidas por seguridad.

Recomendación: no tocar salvo que crezca. Si se vuelve ruidoso, centralizar en `wiki/resources/` y enlazar.

#### B2. Conversaciones diarias contienen rutas y estados históricos

`wiki/agentes/geoffrey/conversaciones/*.md` contiene muchas rutas absolutas y estados ya superados. Esto es esperable porque son bitácoras operativas, no memoria canónica.

Recomendación: no reescribir historial. Solo asegurarse de que decisiones/reglas vigentes estén destiladas en `wiki/decisiones/` y páginas canónicas.

## Datos sensibles: evaluación específica

No encontré contraseñas, tokens, API keys reales ni dumps crudos de credenciales en el wiki revisado.

Sí encontré datos que conviene clasificar:

| Hallazgo | Archivo | Recomendación |
|---|---|---|
| Chasis y placa de vehículo | `wiki/resources/outlander-2026.md` | Mover completo a `_sensitive.md`; dejar puntero. |
| Carné UFM | `wiki/proyectos/activos/tesis.md` | Evaluar si es necesario; si no, mover/quitar. |
| Teléfono público UK | `wiki/proyectos/activos/understanding-kids.md`, `uk-catalogo.md` | Puede quedarse si es público/operativo. |
| Contacto IDC Valores | `wiki/finanzas/inversiones.md` | Puede quedarse si es contacto de servicio, sin cuentas/token. |
| Referencias a expedientes con DPI | `understanding-kids/expedientes-staff-2026-05-14.md` | La matriz no copia números; aceptable, pero mantener como “alto cuidado”. |
| WhatsApp JID | `conversaciones/2026-05-14.md` | Histórico; no usar como fuente viva. Considerar redacción menos identificable si JR quiere limpieza de privacidad. |

## Recomendación de plan de corrección

### Lote 1 — seguridad/higiene root

1. Confirmar si `skills/`, `.clawhub/` y `.openclaw/` en root son residuos.
2. Si son residuos, moverlos fuera del Vault o eliminarlos según corresponda.
3. Registrar log.

### Lote 2 — rutas y bootstrap

1. Corregir frase `~/Documents/Great Vault/` en `_AI_BOOTSTRAP.md`.
2. Revisar root `SOUL.md`, `TOOLS.md`, `IDENTITY.md` para que no fijen rutas absolutas como universales.
3. Marcar rutas técnicas como “observadas en Mac Mini” o moverlas a docs runtime.

### Lote 3 — sensibles livianos

1. Mover chasis/placa completa de Outlander a `_sensitive.md` o reemplazar por puntero.
2. Revisar si el carné UFM debe seguir en `tesis.md`.
3. Mantener teléfonos/correos públicos de UK si JR los aprueba como operativos.

### Lote 4 — estado vivo

1. Reemplazar “hoy/mañana/actualmente” por cortes fechados en páginas de proyecto.
2. Mover pendientes vivos a `wiki/dashboard.md` o a Reminders cuando corresponda.
3. No tocar conversaciones históricas salvo por privacidad explícita.

### Lote 5 — slug y wikilinks

1. Renombrar `disengo-casa.md` a `disegno-casa.md`.
2. Actualizar wikilinks.
3. Resolver o aceptar nodos raw de autores externos.

## Conclusión

La memoria estructural está bien encaminada: no hay transcripts crudos relevantes ni credenciales copiadas. El mayor riesgo no es contenido sensible masivo, sino **deriva de arquitectura**: rutas/runtime dentro del Vault y pequeños estados vivos que podrían volverse falsos. La corrección debe hacerse en lotes pequeños y verificables, no con refactor masivo.

## Relacionado

- [[agentes/geoffrey/memory-writing-best-practices]]
- [[escribir-memoria]]
- [[_AI_BOOTSTRAP]]
- [[agentes/geoffrey/memoria]]
- [[agentes/geoffrey/AGENT]]
