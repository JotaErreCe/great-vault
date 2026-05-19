---
type: reference
date: 2026-05-07
tags: [index, navigation, ai-helper]
---

# Vault Map — índice de búsqueda rápida

> **Para AIs sin filesystem (ChatGPT, Gemini, etc.):** usa este índice para saber qué archivo pedir. Busca por nombre, keyword o categoría. **Para agentes con filesystem:** lee primero [[_AI_BOOTSTRAP]] y luego usa este mapa solo para navegación rápida.

---

## Agentes y auto-ubicación

Regla general: si eres un agente especializado, tu paquete canónico vive en `wiki/agentes/[slug]/`, donde `[slug]` es tu nombre operativo en minúsculas y con guiones.

| Agente | Carpeta canónica | Estado | Qué debe cargar |
|---|---|---|---|
| Geoffrey | `wiki/agentes/geoffrey/` | Activo | `SOUL.md`, `AGENT.md`, `memoria.md`, `skills-permitidas.md` |
| Understanding Kids | `wiki/agentes/understanding-kids/` | Previsto | Crear desde `_templates/openclaw-agent/` cuando Master JR lo apruebe |
| Finanzas | `wiki/agentes/finanzas/` | Previsto | Crear desde `_templates/openclaw-agent/` cuando Master JR lo apruebe |
| Legal | `wiki/agentes/legal/` | Previsto | Crear desde `_templates/openclaw-agent/` cuando Master JR lo apruebe |
| Meta Ads | `wiki/agentes/meta-ads/` | Previsto | Crear desde `_templates/openclaw-agent/` cuando Master JR lo apruebe |
| Marketing / Imágenes | `wiki/agentes/marketing-imagenes/` | Previsto | Crear desde `_templates/openclaw-agent/` cuando Master JR lo apruebe |

Si tu carpeta no existe, **no inventes identidad ni reglas**. Lee [[arquitectura|Arquitectura de agentes]], revisa `_templates/openclaw-agent/` y pide aprobación antes de crear una nueva instancia.

## Proyectos activos

| Nombre | Archivo | Keywords |
|---|---|---|
| [[crisol-tcg]] | `wiki/proyectos/activos/crisol-tcg.md` | Trading card game, lanzamiento, estrategia |
| [[understanding-kids]] | `wiki/proyectos/activos/understanding-kids.md` | UK, educación, staff, finanzas, formaciones, tienda; subcarpeta `understanding-kids/` contiene plan de nutrición completa, auditorías, mapa operativo y fuentes |
| [[understanding-kids/plan-nutricion-completa]] | `wiki/proyectos/activos/understanding-kids/plan-nutricion-completa.md` | Proyecto Geoffrey/JR para nutrir UK antes de README-AI/agente especializado |
| [[diplomado-autismo-2026]] | `wiki/proyectos/activos/diplomado-autismo-2026.md` | AUT26, autismo, dream team, pauta, campañas, formularios |
| [[propi]] | `wiki/proyectos/activos/propi.md` | Propi, real estate, brokers, contratos, alianzas |
| [[tesis]] | `wiki/proyectos/activos/tesis.md` | Jurídica, capítulos, deadline miércoles 6 PM |
| [[disegno-casa-cliente]] | `wiki/proyectos/activos/disegno-casa-cliente.md` | Cliente/proyecto AMC Legal; casos bajo relación Disegno Casa |
| [[altezza]] | `wiki/proyectos/activos/altezza.md` | Caso legal, demanda |
| [[amc-legal]] | `wiki/proyectos/activos/amc-legal.md` | Despacho legal, clientes, tarifa USD $90/hr |
| [[uk-catalogo]] | `wiki/proyectos/activos/uk-catalogo.md` | Catálogo UK, servicios, tienda, formación |
| [[integracion-sensorial]] | `wiki/proyectos/activos/integracion-sensorial.md` | IS, formación, terapia, UK |

## Proyectos pausados / archivados

| Nombre | Archivo | Estado |
|---|---|---|
| [[roamy]] | `wiki/proyectos/pausados/roamy.md` | Pausado |
| [[is-avanzada-padres-2025]] | `wiki/proyectos/archivados/is-avanzada-padres-2025.md` | Archivado jul-sep 2025 |

## Personas

| Nombre | Archivo | Relación |
|---|---|---|
| [[jr]] | `wiki/personas/jr.md` | Master JR / usuario principal |
| [[monica]] | `wiki/personas/monica.md` | Esposa |
| [[nicolas]] | `wiki/personas/nicolas.md` | Hijo |
| [[niko]] | `wiki/personas/niko.md` | Perro importante de Master JR |
| [[jacky-chang]] | `wiki/personas/jacky-chang.md` | Mejor amigo |
| [[danilo-perez]] | `wiki/personas/danilo-perez.md` | Mejor amigo |
| [[chirizosos]] | `wiki/personas/chirizosos.md` | Grupo: Rafa, Sebastián, Óscar, Diego, André |
| [[julio-cruz]] | `wiki/personas/julio-cruz.md` | Cliente AMC, PM Proyecto Arlés |
| [[pablo-cruz]] | `wiki/personas/pablo-cruz.md` | Cliente físico |
| [[javier-hegel]] | `wiki/personas/javier-hegel.md` | Cliente físico |
| [[aracely-hernandez]] | `wiki/personas/aracely-hernandez.md` | Cliente físico |
| [[andres-wer]] | `wiki/personas/andres-wer.md` | Amigo cercano / apoyo legal ocasional |
| [[rafa-galvez]] | `wiki/personas/rafa-galvez.md` | Amigo, alias Shafaga |
| [[sebastian-martinez]] | `wiki/personas/sebastian-martinez.md` | Mejor amigo, Chirizosos |
| [[oscar-batres]] | `wiki/personas/oscar-batres.md` | Amigo |
| [[diego-escobar]] | `wiki/personas/diego-escobar.md` | Amigo, alias Chiriz/Chorizo |
| [[andre-suchini]] | `wiki/personas/andre-suchini.md` | Amigo |

## Entidades

| Nombre | Archivo | Tipo |
|---|---|---|
| [[propi-tech]] | `wiki/entidades/propi-tech.md` | Startup real estate |
| [[brera-arredamenti]] | `wiki/entidades/brera-arredamenti.md` | Empresa de muebles |
| [[disegno-casa]] | `wiki/entidades/disegno-casa.md` | Nombre comercial de Brera |
| [[inversiones-multidisciplinarias]] | `wiki/entidades/inversiones-multidisciplinarias.md` | Vehículo de inversión |
| [[healing-hands]] | `wiki/entidades/healing-hands.md` | Empresa / proyecto |
| [[intensegroup-gt]] | `wiki/entidades/intensegroup-gt.md` | Broker cliente Propi |
| [[milesimo]] | `wiki/entidades/milesimo.md` | Broker cliente Propi |
| [[corp-victoria]] | `wiki/entidades/corp-victoria.md` | Broker cliente Propi |

## Finanzas

| Concepto | Archivo | Descripción |
|---|---|---|
| Índice financiero | `wiki/finanzas/index.md` | Entrada al sistema financiero del Vault |
| Portafolio / inversiones | `wiki/finanzas/inversiones.md` | IBKR, holdings, cripto cuando aplique |
| Propiedades | `wiki/finanzas/propiedades.md` | Z13 alquilada, Museo San Mateo Z7 |
| Ingresos | `wiki/finanzas/ingresos.md` | AMC, UK, Propi, consultoría |
| Egresos | `wiki/finanzas/egresos.md` | Gastos operativos |
| Patrimonio | `wiki/finanzas/patrimonio.md` | Net worth, assets |

## Recursos y plantillas

| Item | Archivo | Para qué |
|---|---|---|
| Plantillas base | `_templates/` | Moldes para proyecto, persona, research, daily, agentes |
| Plantillas OpenClaw agent | `_templates/openclaw-agent/` | Crear paquetes de agentes nuevos |
| Visual Identity | `wiki/resources/visual-identity.md` | Paletas, estilos, marcas |
| Agenda | `wiki/resources/agenda.md` | Eventos recurrentes, próximos eventos |
| Correos y contactos | `wiki/resources/correos-y-contactos.md` | Mapa de cuentas y roles de correo |
| Suscripciones | `wiki/resources/suscripciones.md` | Servicios y cobros recurrentes |
| Outlander 2026 | `wiki/resources/outlander-2026.md` | Vehículo y mantenimientos |
| Information hierarchy | `wiki/resources/information-hierarchy.md` | Niveles de carga/contexto del Vault |
| Protocolo operativo agentes | `wiki/resources/protocolo-operativo-agentes.md` | Contrato común OB1 + memoria + continuidad + autoridad para Geoffrey y agentes especializados |
| Protocolo continuidad proyectos | `wiki/resources/protocolo-continuidad-proyectos.md` | Búsqueda obligatoria para proyectos/subproyectos: canónica, subcarpeta, log, decisiones, conversaciones y fuentes autorizadas |

## Cómo usar Vault Map

1. Busca por palabra clave: `autismo`, `broker`, `monica`, `finanzas`, `agente`, etc.
2. Encuentra el archivo en la tabla.
3. Si no tienes filesystem, pide el contenido exacto de la ruta.
4. Si sí tienes filesystem, lee antes de editar y registra cambios en `wiki/log/YYYY-MM.md`.
5. Nunca edites `raw/`; solo ingesta hacia `wiki/`.

---

## Relacionado

- [[_AI_BOOTSTRAP]] — entrada única del Vault
- [[index]] — catálogo denso con descripciones largas
- [[arquitectura|Arquitectura de agentes]] — paquetes, reglas y agentes previstos
