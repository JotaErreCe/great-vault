---
type: audit
date: 2026-05-19
tags: [geoffrey, vault, ob1, memoria, auditoria, estructura]
---

# Auditoría estructural — OB1 + memoria del Vault — 2026-05-19

## Alcance

Auditoría solicitada por JR para verificar que la estructura OB1 adaptada y la estructura de memoria del Vault se complementen y estén disponibles para Geoffrey y futuros agentes.

Revisión ejecutada sobre:

- `_AI_BOOTSTRAP.md`.
- `wiki/agentes/arquitectura.md` y `wiki/agentes.md`.
- `wiki/resources/escribir-memoria.md`.
- `wiki/resources/protocolo-continuidad-proyectos.md`.
- `wiki/agentes/geoffrey/AGENT.md`, `memoria.md`, `memoria-sugerida.md`, `ob1-roadmap.md`, `tool-authority-matrix.md`, `importadores-seguros.md`, `work-log.md`.
- `_templates/openclaw-agent/`.
- Índices de navegación: `wiki/index.md`, `wiki/resources/vault-map.md`, work-logs index.
- Escaneo automático de Markdown del wiki.

No se abrió `_sensitive.md` ni secretos. Los hallazgos de “sensible” del script son detecciones por palabras clave, no impresión ni lectura de valores sensibles.

## Resultado ejecutivo

La estructura general sí existía, pero estaba repartida en varias páginas. El hueco era que no había un **contrato común único** que obligara a todos los agentes y templates a aplicar juntos:

1. memoria segura;
2. recuperación de proyectos/subproyectos;
3. matriz de autoridad;
4. work logs;
5. memoria sugerida;
6. importadores seguros;
7. checkpoints.

Se corrigió creando [[protocolo-operativo-agentes]] y enlazándolo desde las capas de entrada y creación de agentes.

## Hallazgos

### H1 — OB1 y memoria estaban bien diseñados, pero no completamente integrados

Existían piezas correctas:

- [[escribir-memoria]] — reglas globales de memoria.
- [[geoffrey/tool-authority-matrix]] — autoridad por fuente/superficie.
- [[geoffrey/work-log]] — estándar de work logs.
- [[geoffrey/memoria-sugerida]] — staging de memoria.
- [[geoffrey/importadores-seguros]] — dry-run/fingerprints/dedup.
- [[geoffrey/checkpoints/index]] — continuidad ante pérdida de contexto.
- [[protocolo-continuidad-proyectos]] — recuperación de proyectos.

Pero faltaba una página que dijera: “estas piezas son un solo contrato común para cualquier agente”.

### H2 — Templates de agentes no heredaban la estructura

Escaneo inicial: `_templates/openclaw-agent/` no referenciaba explícitamente:

- [[protocolo-operativo-agentes]];
- [[escribir-memoria]];
- [[protocolo-continuidad-proyectos]].

Riesgo: un agente futuro podía nacer desde template sin las reglas que ya aprendimos con Geoffrey.

Corrección: templates actualizados para heredar protocolo común, memoria segura, continuidad y OB1.

### H3 — `_AI_BOOTSTRAP.md` tenía una ruta problemática

La auditoría previa de memoria ya había detectado una frase hardcodeada: `~/Documents/Great Vault/` como ruta universal.

Corrección: se reemplazó por instrucción de resolver la ruta del Vault según host/runtime antes de leer o escribir.

### H4 — `ob1-roadmap.md` tenía estado inconsistente

La tabla decía Fase 3 y Fase 4 “pendiente”, aunque más abajo constaba que estaban implementadas base.

Corrección: estados actualizados a `implementada base`.

### H5 — `memoria-sugerida.md` decía “no hay propuestas pendientes” aunque sí había

Riesgo: confundir revisión de memoria y promover/ignorar mal.

Corrección: encabezado ajustado para indicar que hay propuestas pendientes listadas abajo.

### H6 — índice de work logs no listaba todos los work logs existentes

Corrección: actualizado `work-logs/index.md` con logs faltantes.

### H7 — slug `disengo-casa` era incorrecto y podía propagar error

Corrección: el proyecto se renombró de `disengo-casa.md` a `disegno-casa-cliente.md` para evitar typo y evitar choque con la entidad `entidades/disegno-casa.md`. Se actualizaron links en dashboard, Altezza, índice y vault-map.

### H8 — frases vivas “hoy/mañana/actualmente” en páginas de proyecto

Corrección aplicada en páginas UK relevantes para convertirlas a cortes fechados/verificables.

## Cobertura posterior al ajuste

Escaneo de 137 archivos Markdown en `wiki/`:

| Control | Archivos que lo referencian |
|---|---:|
| [[escribir-memoria]] | 10 |
| [[protocolo-continuidad-proyectos]] | 7 |
| [[geoffrey/tool-authority-matrix]] | 11 |
| [[geoffrey/importadores-seguros]] | 9 |
| [[geoffrey/work-log]] / work logs | 12 |
| [[geoffrey/memoria-sugerida]] | 11 |
| `obsidian-import-safe` | 4 |

Cobertura cualitativa después del ajuste:

- Entrada fría: `_AI_BOOTSTRAP.md` apunta al protocolo común.
- Raíz Vault: `AGENTS.md` apunta al protocolo común.
- Arquitectura de agentes: `wiki/agentes/arquitectura.md` apunta al protocolo común.
- Índice de agentes: `wiki/agentes.md` apunta al protocolo común.
- Navegación rápida: `vault-map.md` apunta al protocolo común.
- Geoffrey: `geoffrey/AGENT.md` apunta al protocolo común.
- Templates de agentes: `AGENTS.template`, `SOUL`, `TOOLS`, `USER`, `IDENTITY`, `HEARTBEAT` apuntan al protocolo común.

## Interpretación de “sin excepción”

No conviene copiar todo el protocolo en cada página del Vault. Eso crearía duplicación y memoria que envejece mal. La forma correcta de “sin excepción” es:

1. **Entrada única**: `_AI_BOOTSTRAP.md`.
2. **Contrato común**: [[protocolo-operativo-agentes]].
3. **Herencia por arquitectura**: [[arquitectura]] y [[agentes]].
4. **Herencia por templates**: `_templates/openclaw-agent/`.
5. **Punteros en índices**: [[vault-map]] e [[index]].
6. **Aplicación por agente**: cada `AGENT.md` específico debe enlazarlo.

Así evitamos repetir texto y mantenemos una sola fuente de verdad.

## Pendientes no ejecutados deliberadamente

Estos puntos no se resolvieron en esta pasada porque requieren decisión o lote separado:

1. Artefactos root `.clawhub/`, `.openclaw/`, `skills/`: parecen tooling creado por OpenClaw/ClawHub. No mover sin aprobación porque puede romper skills.
2. Datos semi-sensibles detectados por auditoría previa: vehículo, carné UFM, teléfonos/contactos. Requieren criterio de JR para mover/redactar.
3. Conversaciones/checkpoints/logs históricos con rutas absolutas: no se reescriben porque son historial; las reglas vigentes ya fueron corregidas en bootstrap/protocolo.
4. Promoción de memoria sugerida a `geoffrey/memoria.md`: pendiente de confirmación explícita de JR.

## Cambios aplicados

- Creado [[protocolo-operativo-agentes]].
- Actualizado `_AI_BOOTSTRAP.md`.
- Actualizado Vault root `AGENTS.md`, `SOUL.md`, `TOOLS.md`, `IDENTITY.md`, `USER.md`.
- Actualizado [[arquitectura]], [[agentes]] y [[vault-map]].
- Actualizado [[geoffrey/AGENT]].
- Actualizados `_templates/openclaw-agent/` y `_templates/README.md`.
- Actualizados [[geoffrey/ob1-roadmap]], [[geoffrey/memoria-sugerida]], [[geoffrey/work-logs/index]].
- Renombrado proyecto de cliente Disegno Casa a `disegno-casa-cliente.md` para evitar typo/choque.
- Convertidas frases vivas de UK a cortes fechados.

## Conclusión

Después de esta auditoría, la estructura OB1 y la estructura de memoria ya no viven como piezas separadas: quedan integradas por [[protocolo-operativo-agentes]] y heredadas por bootstrap, arquitectura, índices, Geoffrey y templates de agentes futuros.

El riesgo residual principal no es estructural sino operativo: cada agente debe obedecer el protocolo. Para mejorar cumplimiento, el siguiente paso sería crear una prueba/checklist automática de healthcheck del Vault que revise enlaces mínimos, frontmatter, duplicados de slugs, estados vivos y referencias obligatorias.

## Relacionado

- [[protocolo-operativo-agentes]]
- [[protocolo-continuidad-proyectos]]
- [[escribir-memoria]]
- [[geoffrey/tool-authority-matrix]]
- [[geoffrey/work-log]]
- [[geoffrey/memoria-sugerida]]
- [[geoffrey/importadores-seguros]]
- [[geoffrey/auditoria-recuperacion-uk-2026-05-19]]
- [[geoffrey/auditoria-vault-memoria-2026-05-17]]
