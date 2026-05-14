---
type: bootstrap
updated: 2026-05-14
---

# AI Bootstrap — entrada única

> **ESTE ES EL ÚNICO ARCHIVO QUE NECESITAS.** Contiene identidad, reglas, arquitectura completa y convenciones. Cualquier AI en cualquier plataforma puede operar el vault leyendo solo este archivo.

---

## Identidad

JR / José Roberto Castañeda Arriola, 30 años (n. 1995-10-26), abogado guatemalteco. Casado con [[monica]] (n. 1994-09-13). Padre de [[nicolas]] (n. 2026-03-06). Perro: [[niko]]. TZ: America/Guatemala (UTC-6). Idioma: español, mezcla inglés.

## Reglas de interacción (no negociables)

- **Optimizar tokens.** Bloques claros, no párrafos largos (TDAH).
- **Nunca inventar.** Un "no sé" honesto antes que datos inventados.
- **No opinar política/religión** salvo que pida.
- **No comprometerlo con terceros ni gastar dinero** sin consentimiento.
- Picky eater.
- Pronombres masculinos del español.

## Foco actual (verificar fecha)

| Proyecto | Estado | Próximo paso |
|---|---|---|
| [[crisol-tcg]] | activo | Definir fecha lanzamiento |
| [[understanding-kids]] | activo | Reparar checkout |
| [[propi]] | activo | Cerrar contratos brokers |
| [[tesis]] | activo | Cap. miércoles 6 PM |
| [[altezza]] | activo | Caso legal en curso |
| [[amc-legal]] | activo | Operación |
| [[diplomado-autismo-2026]] | activo | Campaña AUT26 |
| [[roamy]] | pausado | — |

Tarifa AMC Legal: USD $90/hr + IVA. Banco principal: G&T Continental. Inversiones: IBKR + cripto.

---

## Arquitectura del vault (3 capas)

```
Great Vault/
├── _AI_BOOTSTRAP.md     ← este archivo. Schema + entry point.
├── _CLAUDE.md           ← redirect a este archivo
├── _sensitive.md        ← NIT, DPI, dirección. NO cargar por defecto.
├── _templates/          ← plantillas: nota-diaria, proyecto, persona, research
│
├── raw/                 ← FUENTES. LLM solo LEE. Nunca edita.
│   ├── daily/           ← notas diarias crudas (captura del día)
│   ├── inbox/           ← capturas sueltas, recordatorios, mensajes
│   └── imports/         ← exports de Drive, Dropbox, Apple Notes, PDFs
│
└── wiki/                ← CONOCIMIENTO DESTILADO. LLM escribe y mantiene.
    ├── index.md         ← catálogo del vault
    ├── dashboard.md     ← eventos del día y próximos 14 días
    ├── IDENTITY.md      ← identidad completa: personalidad, valores, gustos, metas
    ├── log/             ← historial append-only mensual (log/YYYY-MM.md)
    ├── decisiones/      ← decisiones destiladas mensuales (decisiones/YYYY-MM.md)
    ├── proyectos/       ← activos/, pausados/, archivados/
    ├── personas/        ← contactos y personas relevantes
    ├── entidades/       ← empresas, sociedades, organizaciones
    ├── finanzas/        ← inversiones, propiedades, ingresos, egresos, patrimonio
    ├── ideas/           ← ideas en gestación
    ├── research/        ← libros, artículos, investigaciones procesadas
    └── resources/       ← agenda, suscripciones, identidad visual, mapas
```

**Regla fundamental:**
- `raw/` = inmutable. LLM lee para ingestar, nunca modifica.
- `wiki/` = LLM escribe, actualiza y mantiene. JR lee.
- `_templates/` = contratos de formato. LLM los usa para crear notas nuevas.

---

## Dónde va cada cosa

| Tipo de contenido | Capa | Carpeta |
|---|---|---|
| Nota diaria cruda (captura del día) | raw | `raw/daily/YYYY-MM-DD.md` |
| Captura rápida, recordatorio, mensaje | raw | `raw/inbox/` |
| Export de Drive / Dropbox / Apple Notes / PDF | raw | `raw/imports/` |
| Persona física procesada | wiki | `wiki/personas/` |
| Empresa / sociedad | wiki | `wiki/entidades/` |
| Proyecto activo | wiki | `wiki/proyectos/activos/` |
| Proyecto pausado / archivado | wiki | `wiki/proyectos/pausados/` o `archivados/` |
| Libro / artículo / research procesado | wiki | `wiki/research/` |
| Recurso / referencia | wiki | `wiki/resources/` |
| Finanzas | wiki | `wiki/finanzas/` |
| Idea en gestación | wiki | `wiki/ideas/` |
| Historial append-only de cambios al Vault | wiki | `wiki/log/YYYY-MM.md` |
| Decisiones destiladas de JR | wiki | `wiki/decisiones/YYYY-MM.md` |
| Plantilla | schema | `_templates/` |
| Datos sensibles | root | `_sensitive.md` |

---

## Templates

Templates live in `_templates/`. They are molds, not active memory.

### OpenClaw agent templates

The following files in `_templates/openclaw-agent/` are used to create new AI agent identity, memory, tool, and operating-instruction files:

- [[AGENTS.template]] — base structure for defining AI agent operating rules and role behavior.
- [[_templates/openclaw-agent/IDENTITY|IDENTITY.template]] — base structure for defining an AI assistant’s identity, purpose, and metadata.
- [[_templates/openclaw-agent/SOUL|SOUL.template]] — base structure for defining tone, values, personality, and behavioral preferences.
- [[_templates/openclaw-agent/USER|USER.template]] — base structure for summarizing the user’s long-term preferences, projects, context, and communication style.
- [[_templates/openclaw-agent/TOOLS|TOOLS.template]] — base structure for documenting available tools, workflows, commands, and integrations.
- [[_templates/openclaw-agent/HEARTBEAT|HEARTBEAT.template]] — base structure for recurring status, active priorities, recent changes, and continuity notes.

**These files are not active memory files by themselves.** Use them only as templates when creating or updating actual working agent files.

Actual agent instances live in `wiki/agentes/[slug]/`, for example:

- [[geoffrey/SOUL|SOUL — Geoffrey]]
- [[geoffrey/AGENT|AGENT — Geoffrey]]
- [[geoffrey/memoria|Memoria — Geoffrey]]

If an agent wakes up after memory loss, it must recover from its package: read `wiki/agentes/[slug]/AGENT.md`, then the newest conversation log under `wiki/agentes/[slug]/conversaciones/`, then the newest relevant checkpoint under `wiki/agentes/[slug]/checkpoints/`, then `wiki/decisiones/YYYY-MM.md` for decisions, then `wiki/log/YYYY-MM.md` for recent edits.

---

## Flujo de captura y procesamiento

```
1. CAPTURA  → raw/daily/ o raw/inbox/ (siempre cae aquí primero)
      ↓
2. INGEST   → LLM lee raw/, extrae conocimiento clave
      ↓
3. PROCESA  → LLM escribe/actualiza páginas en wiki/:
              · nueva persona → wiki/personas/
              · nuevo proyecto → wiki/proyectos/activos/
              · insight de libro → wiki/research/
              · dato financiero → wiki/finanzas/
              · decisión explícita de JR → wiki/decisiones/YYYY-MM.md
              · actualiza wikilinks bidireccionales
      ↓
4. ACTUALIZA → wiki/dashboard.md (si afecta hoy/14 días)
               wiki/IDENTITY.md (si es dato vivo: familia, banca, foco)
      ↓
5. LOG      → apendar a wiki/log/YYYY-MM.md:
              YYYY-MM-DD | acción | descripción
```

---

## Reglas operativas (cualquier AI)

- **Lee antes de escribir.** Si vas a editar un archivo wiki, léelo completo primero.
- **raw/ es intocable.** Nunca edites ni borres archivos en `raw/`.
- **Busca antes de crear.** Evita duplicados — un mismo concepto = una sola nota.
- **Nunca sobrescribir historial.** `wiki/log/` es append-only.
- **Datos sensibles** (NIT, DPI, dirección, credenciales, cuentas) → SOLO en `_sensitive.md`.
- **Toda modificación al wiki** → apendar línea a `wiki/log/YYYY-MM.md`.
- **Decisiones de JR se destilan.** Si JR decide, aprueba, rechaza, cambia criterio o fija una preferencia/regla, guardar una versión breve en `wiki/decisiones/YYYY-MM.md`; no guardar transcript completo.
- **Buenas respuestas se archivan.** Un análisis, comparación o síntesis valiosa → guardar como página en `wiki/`.

---

## Frontmatter (obligatorio en todo archivo wiki)

```yaml
---
type: [daily|proyecto|persona|entidad|idea|research|reference|resource|inbox|dashboard|index|group|decision]
date: YYYY-MM-DD
tags: [tag1, tag2, ...]
---
```

**Campos opcionales por contexto:**
- Proyecto: `estado`, `fecha-inicio`, `fecha-objetivo`
- Persona: `rol`, `empresa`, `relacion`, `ultima-interaccion`
- Research/Reference: `fuente`, `relevancia`

**Regla:** no dejar campos vacíos (`tags: []`). Si no hay valor, omitir el campo.
**Deprecado:** `ai-first: true` (todos los archivos son AI-first por defecto).

## Tag system

- **Tipo:** `daily`, `proyecto`, `persona`, `entidad`, `research`, `idea`, `reference`, `resource`, `inbox`, `dashboard`, `index`, `group`, `decision`
- **Estado:** `estado/activo`, `estado/pausado`, `estado/completado`
- **Prioridad:** `prioridad/alta`, `prioridad/media`, `prioridad/baja`
- **Tema:** `tema/[categoria]` (ej: `tema/autismo`, `tema/marketing`, `tema/legal`)

## Convenciones de escritura

**Nombres de archivo:** `lowercase-con-guiones.md` — NUNCA UPPERCASE, espacios, números al inicio.

**Excepciones documentadas:** archivos bootstrap/runtime de agentes pueden usar nombres esperados por OpenClaw (`AGENT.md`, `SOUL.md`, `IDENTITY.md`, `README.md`, `HEARTBEAT.md`, `TOOLS.md`, `USER.md`, `AGENTS.template.md`) cuando el runtime o la plantilla lo requiere. Logs mensuales, conversaciones y checkpoints pueden iniciar con fecha ISO (`2026-05.md`, `2026-05-13.md`, `checkpoint-YYYY-MM-DD-...`). No crear nuevas excepciones sin documentarlas.

**Wikilinks:** usar doble corchete para referencias internas reales, por ejemplo `[[index]]` o `[[vault-map|Vault Map]]`. Nunca `[texto](ruta)` para archivos internos.

**Sección Relacionado:** obligatoria al final de todo archivo wiki, excepto daily notes, logs append-only, conversaciones/checkpoints de agente y bootstrap.

**Estructura de nota wiki (típica):**
```markdown
---
type: [tipo]
date: YYYY-MM-DD
tags: [tags]
---

# Título

2-3 oraciones explicando qué es esto y por qué importa.

## Secciones con contenido estructurado

## Relacionado

- [[index]] · [[dashboard]]
```

---

## Reglas de seguridad

- Datos sensibles (NIT, DPI, dirección exacta, cuentas completas, identificadores financieros de cliente, credenciales, tokens): SOLO en `_sensitive.md`.
- Contactos operativos de negocio (correos/teléfonos públicos o de clientes/proveedores) pueden vivir en wiki si sirven para operación; datos personales íntimos, residencia precisa, documentos de identidad, números completos de cuenta/tarjeta y secretos van en `_sensitive.md` o se reemplazan por `ver _sensitive.md`.
- NUNCA crear archivos con API keys, contraseñas o PII sensible fuera de `_sensitive.md`.
- Si detectas datos sensibles en wiki/ o raw/, es un bug — reportar al usuario sin imprimir el valor.

---

## Mantenimiento periódico

**Mensual:**
- Revisar `wiki/decisiones/YYYY-MM.md` — consolidar duplicados y enlazar a proyectos/personas/agentes relevantes
- Procesar `raw/inbox/` — items resueltos → log
- Revisar `raw/daily/` — insights → wiki
- Actualizar `wiki/IDENTITY.md` si cambió familia, banca, foco
- Crear `wiki/log/YYYY-MM.md` para el mes nuevo
- Limpiar wikilinks rotos

**Trimestral:**
- Revisar estado de proyectos en `wiki/proyectos/activos/`
- Consolidar research duplicado en `wiki/research/`
- Revisar personas con `ultima-interaccion` hace >6 meses

---

## Carga progresiva

| Nivel | Archivos | Uso |
|---|---|---|
| **L0** | `_AI_BOOTSTRAP.md` | Contexto base — cualquier AI, cualquier sesión |
| **L1** | + `wiki/IDENTITY.md`, `wiki/dashboard.md`, `wiki/index.md` | Contexto completo para trabajo diario |
| **L2** | + archivos wiki específicos (proyecto, persona, finanza) | Trabajo profundo en un tema |
| **L3** | + sub-archivos (staff.md, finanzas.md) + raw/ si se ingesta | Detalles operativos máximos |
| **Sensitive** | `_sensitive.md` | Solo cuando usuario pide trámite específico |

---

## Si eres Claude Code

Slash commands disponibles (`~/.claude/skills/obsidian-*`):

| Comando | Para qué |
|---|---|
| `/obsidian-exobrain` | Activa contexto completo del vault |
| `/obsidian-find [query]` | Busca en el vault |
| `/obsidian-save` | Guarda la conversación actual al wiki |
| `/obsidian-ingest [fuente]` | Procesa raw/ o fuente externa → wiki |
| `/obsidian-health` | Audita salud del vault |
| `/obsidian-daily` | Crea/abre nota del día en raw/daily/ |
| `/obsidian-world [L0-L3]` | Carga contexto por niveles |

Tienes acceso directo al filesystem (`~/Documents/Great Vault/`). Lee, edita y crea archivos directamente.

## Si eres ChatGPT / Gemini / cualquier otra AI

No tienes acceso al filesystem. Tu workflow:

1. El usuario te pegará archivos (empieza por este bootstrap).
2. Devuelve **archivos completos modificados** en bloque de código, listos para copiar.
3. Si necesitas un archivo que no has visto, pídelo. Nunca inventes su contenido.
4. Para encontrar qué archivo pedir: consulta [[vault-map|Vault Map]] (`wiki/resources/vault-map.md`).
5. Respeta: naming conventions, frontmatter, sección Relacionado, raw/ intocable, sensitive aislado.

---

## Relacionado

- [[IDENTITY]] — identidad completa, valores, gustos, metas
- [[dashboard]] — eventos del día, próximos 14 días
- [[index]] — catálogo completo del wiki
- [[vault-map|Vault Map]] — índice searchable para AIs sin filesystem
