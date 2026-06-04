---
type: reference
date: 2026-06-04
tags: [agentes, marketing, agencia, canva, notion, meta-ads, understanding-kids]
---

# Arquitectura — Marketing Agency Agents

Diseño inicial aprobado por JR para crear una agencia digital operada por agentes separados de Geoffrey. Primer piloto: [[agentes/marketing-agency/clientes/understanding-kids/piloto-30-dias|Understanding Kids]].

## Decisiones base

- Los agentes deben ser **totalmente separados** de Geoffrey, con workspaces propios y posibilidad de hablarles directamente.
- Primer cliente piloto: **Understanding Kids**.
- Clientes previstos: Understanding Kids, Integración Sensorial, ToyLab, Crisol y práctica legal de JR.
- Estructura multi-cliente: los agentes son funcionales; el cliente vive como paquete/contexto compartido. No crear un equipo completo por cliente al inicio.
- Autonomía media: pueden investigar, planificar, crear, organizar y preparar; la versión final requiere revisión humana.
- Prohibido gastar pauta o activar campañas sin aprobación explícita de JR.
- Cambiar manuales de marca requiere aprobación explícita.
- Debe existir bitácora permanente de qué hicieron, cuándo, por qué y dónde quedó.

## Agentes propuestos

### 1. Agency Strategist

**Agent ID sugerido:** `agency-strategist`

Responsable de estrategia, diagnóstico, campañas, calendario editorial, investigación de mercado, análisis de empresa, métricas y coordinación entre agentes.

Puede:

- analizar profundamente empresa, competencia, público y oferta;
- proponer estrategia mensual/trimestral;
- decidir pilares de contenido y objetivos por canal;
- pedir producción a Brand Studio / Content Producer;
- revisar reportes y convertir métricas en aprendizajes;
- hablar directamente con JR.

No puede:

- publicar;
- gastar pauta;
- cambiar manuales aprobados sin autorización.

### 2. Agency Brand Studio

**Agent ID sugerido:** `agency-brand-studio`

Responsable de identidad visual, manuales de marca, templates, sistema visual premium y consistencia por cliente.

Puede:

- leer manuales de marca existentes;
- crear borradores de manual cuando no exista;
- definir templates por formato y campaña;
- usar Canva, imagen generativa y herramientas creativas autorizadas;
- proponer cambios al Brand OS.

Debe pedir aprobación para:

- modificar manuales oficiales;
- cambiar logo, paleta, tipografía, tono o reglas visuales base.

### 3. Agency Content Producer

**Agent ID sugerido:** `agency-content-producer`

Responsable de producción concreta de piezas: copy, captions, texto en imagen, carruseles, stories, reels covers, ads, emails y variaciones.

Puede:

- producir artes y borradores en Canva;
- generar imágenes con modelos autorizados cuando Canva no alcance;
- crear variantes por formato/canal;
- subir links al sistema operativo del cliente;
- marcar piezas como listas para revisión.

No puede:

- dar por final una pieza sin revisión humana;
- publicar por su cuenta.

### 4. Hormozi

**Agent ID:** `agency-publishing-operator`

Responsable de performance marketing, ofertas, programación, publicación y Meta Ads en modo controlado. Nombre inspirado en Alex Hormozi por su enfoque en ofertas y conversión; no representa ni suplanta a la persona real.

Puede:

- preparar publicación o campaña;
- crear campañas/anuncios en borrador o pausados cuando la integración lo permita;
- preparar UTMs, naming conventions y checklist de publicación;
- registrar bitácora operativa.

No puede:

- publicar contenido sin aprobación humana;
- activar campaña o gastar pauta sin aprobación explícita de JR;
- compartir archivos externamente sin autorización.

## Workspaces OpenClaw propuestos

```text
~/.openclaw/workspace-agency-strategist/
~/.openclaw/workspace-agency-brand-studio/
~/.openclaw/workspace-agency-content-producer/
~/.openclaw/workspace-agency-publishing-operator/
```

Cada workspace debe tener al menos:

```text
AGENTS.md
IDENTITY.md
SOUL.md
USER.md
TOOLS.md
HEARTBEAT.md
```

Geoffrey puede ayudar a diseñarlos, pero los agentes deben tener identidad, memoria operativa y permisos separados.

## Integraciones por fases

### Fase 0 — Gobernanza

- Crear agentes separados y reglas de aprobación.
- Definir paquete cliente para UK.
- Definir bitácora y rutas de Drive/Notion.

### Fase 1 — Operación segura

- Google Drive y Notion.
- Crear briefs, calendarios, docs, reportes, links y estados.
- No publicación automática todavía.

### Fase 2 — Producción creativa

- Canva MCP/Canva Connector como primera opción.
- Imagen generativa como fallback para assets.
- Exportar/guardar piezas en Drive y/o Canva.

### Fase 3 — Meta Ads controlado

- Primero lectura/reporting.
- Luego creación de campañas en borrador/pausadas.
- Activación/pauta solo con aprobación expresa de JR.

### Fase 4 — Affinity / arte avanzado

- Evaluar solo si Canva + generación de imagen no bastan.
- Requiere app instalada y skill/automatización auditada.

## Herramientas y estado de factibilidad

| Herramienta | Estado inicial | Nota |
|---|---|---|
| Canva | Factible; preferir MCP/Connector | Usar cuenta Canva Pro de JR; browser como fallback. |
| Google Drive/Docs/Sheets | Alta factibilidad | Google Workspace MCP ya es ruta natural para docs/reportes. |
| Notion | Factible; falta autenticación | Requiere integración/token y compartir bases/páginas. |
| Meta Ads | Factible medio; requiere setup serio | Business Manager de Mónica; usar system user/token si procede. |
| Imagen generativa | Factible | Usar para assets cuando Canva no alcance; revisión humana obligatoria. |
| Video AI | Posible, selectivo | Clips cortos 4–8s; no base diaria por costo/control. |
| Affinity | Fase posterior | Automatización menos estable; no fase 1. |

## Guardrails no negociables

- No gastar dinero ni activar pauta sin aprobación explícita.
- No publicar sin aprobación humana.
- No borrar ni reorganizar carpetas sin plan aprobado.
- No cambiar manuales de marca sin aprobación.
- No compartir Drive/Canva/Notion con terceros sin aprobación.
- Mantener separación por cliente y bitácora de acciones.
- Para UK: evitar promesas clínicas absolutas, diagnósticos por redes o claims sensibles sin revisión humana.

## Estructura cliente recomendada

```text
Agency OS/
├── 00_Admin/
├── 01_Templates/
├── 02_Agents/
└── Clients/
    └── Understanding Kids/
        ├── 00_Brand OS/
        ├── 01_Content Calendar/
        ├── 02_Campaigns/
        ├── 03_Creative Assets/
        ├── 04_Copy Bank/
        ├── 05_Reports/
        └── 06_Learnings/
```

## Próximo paso recomendado

Ejecutar piloto UK sin automatizar publicación ni pauta todavía:

1. crear paquete cliente UK;
2. localizar manual de marca;
3. auditar Notion actual;
4. definir Brand OS y Content OS;
5. producir primera semana de piezas en modo revisión humana;
6. medir fricción y ajustar SOP.
