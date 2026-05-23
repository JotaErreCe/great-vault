---
type: reference
date: 2026-05-04
tags: [structure, visualization]
---

# Jerarquía de información — Piramide visual

> Mapa de cómo está organizada la información sobre ti, de lo más general a lo más específico.

---

## Diagrama de árbol (texto ASCII)

```
┌─────────────────────────────────────────────────────────┐
│ L0: ENTRADA ÚNICA — _AI_BOOTSTRAP.md                    │
│ Quién eres: José Roberto Castañeda Arriola, 30 años     │
│ Reglas: tokens, honestidad, sin política/religión       │
│ Foco: 7 proyectos activos + 1 pausado                   │
│ Banco: G&T Continental | Inversiones: IBKR              │
└───────────┬──────────────────────────────────┬──────────┘
            │                                  │
    ┌───────▼─────────┐        ┌───────────────▼──────────┐
    │ L1: IDENTIDAD   │        │ L1: OPERATIVA DIARIA     │
    │ IDENTITY.md     │        ├──────────────────────────┤
    │ (~800 tokens)   │        │ dashboard.md — hoy/14d   │
    ├─────────────────┤        │ index.md — catálogo      │
    │ • Personalidad  │        │ wiki/log/ — historial    │
    │ • Valores       │        │ _CLAUDE.md → redirect    │
    │ • Gustos        │        │ vault-map — búsqueda     │
    │ • Metas         │        └──────────────────────────┘
    │ • Familia       │
    │ • Conocidos     │
    └───────┬─────────┘
            │
    ┌───────▼────────────────────────────────────────────────┐
    │ L2: DOMINIO ESPECÍFICO — datos categorizados          │
    ├────────────┬───────────────┬──────────┬──────────────┤
    │ PROYECTOS  │ PERSONAS      │ EMPRESAS │ FINANZAS     │
    ├────────────┼───────────────┼──────────┼──────────────┤
    │ • Crisol   │ • Monica      │ • UK     │ • Inversiones│
    │ • UK       │ • Nicolas     │ • Propi  │ • Propiedades│
    │ • Propi    │ • Clientes    │ • Brera  │ • Ingresos   │
    │ • Tesis    │ • Amigos      │ • Brokers│ • Egresos    │
    │ • Altezza  │ • Team        │          │ • Patrimonio │
    │ • AMC      │               │          │              │
    │ • Diplom.  │               │          │              │
    └────────────┴───────────────┴──────────┴──────────────┘
            │
    ┌───────▼──────────────────────────────────────────────┐
    │ L3: DETALLE OPERATIVO — sub-archivos + tablas       │
    ├──────────────────────────────────────────────────────┤
    │ understanding-kids/                                  │
    │  ├─ staff.md (16 personas tabla)                     │
    │  ├─ finanzas.md (ingresos feb 2026)                  │
    │  └─ operacion.md (Drive, sistemas, políticas)        │
    │                                                      │
    │ diplomado-autismo-2026.md (dream team, pauta)        │
    │ finanzas/inversiones.md (11 holdings IBKR)           │
    │ personas/*.md (fichas detalladas de contactos)       │
    └──────────────────────────────────────────────────────┘
            │
    ┌───────▼──────────────────────────────────────────────┐
    │ L4: MÁXIMO DETALLE — fuentes externas                │
    ├──────────────────────────────────────────────────────┤
    │ • _sensitive.md (NIT, DPI, dirección, credenciales)  │
    │ • Google Drive (UK docs, contratos, formularios)     │
    │ • Notion (bases de datos, trackers)                  │
    │ • Apple Notes (capturas rápidas sin procesar)        │
    │ • Correos, Slack (comunicaciones vivas)              │
    └──────────────────────────────────────────────────────┘
```

---

## Tabla de qué hay en cada nivel

| Nivel   | Nombre         | Archivo(s)                                                     | Tokens   | Uso                                                 | Carga automática         |
| ------- | -------------- | -------------------------------------------------------------- | -------- | --------------------------------------------------- | ------------------------ |
| **L0**  | Bootstrap      | `_AI_BOOTSTRAP.md`                                             | ~200     | Contexto frío en cualquier AI, cualquier plataforma | ✅ Siempre                |
| **L1a** | Identidad      | `wiki/IDENTITY.md`                                             | variable | Personalidad, valores, gustos, metas completos      | ✅ L1                     |
| **L1b** | Operativa      | `wiki/dashboard.md`, `wiki/index.md`, `wiki/log/`, `wiki/resources/vault-map.md` | variable | Eventos hoy, catálogo completo, historial | ✅ L1                     |
| **L2**  | Categorías     | `wiki/proyectos/`, `wiki/personas/`, `wiki/entidades/`, `wiki/finanzas/` | variable | Organización por dominio                            | ❌ Bajo demanda           |
| **L3**  | Detalle        | `wiki/proyectos/activos/understanding-kids/staff.md`, `wiki/finanzas/inversiones.md`, etc. | variable | Tablas, listas, detalles operativos | ❌ Bajo demanda           |
| **L4**  | Máximo detalle | `_sensitive.md`, Drive, Notion, Apple Notes                    | variable | Datos legales, comunicaciones, fuentes externas     | ❌ Solo demanda explícita |

---

## Lectura por caso de uso

### "Necesito contexto rápido de JR"
Lee: **L0** (`_AI_BOOTSTRAP.md`) — 5 minutos, ~200 tokens

### "Necesito contexto completo para trabajar hoy"
Lee: **L0** + **L1** (bootstrap + IDENTITY + dashboard + index) — 15 minutos, ~2,500 tokens

### "Necesito info sobre [proyecto específico]"
1. Busca en **Vault Map** (`wiki/resources/vault-map.md`)
2. Lee el archivo **L2** correspondiente
3. Carga **L3** sub-archivos si necesitas profundidad

### "Necesito datos sensibles / info bancaria"
1. Usuario pide explícitamente
2. Carga **L4** (`_sensitive.md`)
3. AI lo respeta y no lo carga automáticamente en futuras sesiones

---

## Dónde está la info sobre TI específicamente

```
TÚ (José Roberto Castañeda Arriola)
│
├─ L0: _AI_BOOTSTRAP.md
│   └─ Línea rápida (nombre, edad, familia, TZ, reglas, foco)
│
├─ L1: wiki/IDENTITY.md
│   └─ Identidad completa (personalidad, valores, gustos, metas)
│
├─ L2: wiki/personas/jr.md
│   └─ Ficha canónica con aliases, familia, datos vitales
│
├─ L2: wiki/finanzas/
│   ├─ inversiones.md (portafolio IBKR)
│   ├─ propiedades.md (Z13, Z7)
│   └─ patrimonio.md (net worth)
│
├─ L2: Proyectos (todos te tienen como protagonista)
│   ├─ wiki/proyectos/activos/understanding-kids.md
│   ├─ wiki/proyectos/activos/propi.md
│   └─ ... (7 activos + 1 pausado)
│
├─ L3: raw/daily/YYYY-MM-DD.md
│   └─ Capturas diarias crudas; insights duraderos se procesan hacia wiki/
│
└─ L4: _sensitive.md
    └─ NIT, DPI, dirección Z13
```

---

## Relacionado

- [[_AI_BOOTSTRAP]] — entrada única
- [[wiki/IDENTITY]] — identidad completa
- [[vault-map|Vault Map]] — búsqueda rápida
- [[dashboard]] — eventos hoy
