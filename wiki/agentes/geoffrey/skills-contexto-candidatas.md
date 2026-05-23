---
type: reference
date: 2026-05-19
tags: [agente, geoffrey, skills, contexto, ob1]
---

# Skills de contexto candidatas — Geoffrey

Estas skills pueden construirse en paralelo con Fases 1–2 del roadmap OB1, pero deben respetar [[agentes/geoffrey/tool-authority-matrix]] y no comprometer a JR con terceros.

## Candidatas

| Skill | Propósito | Fuentes probables | Permisos iniciales | Estado |
|---|---|---|---|---|
| `/propi-brief` | Pull de contratos activos, corredores y estado de cumplimiento. | Vault, Drive/Docs indicados por JR, calendario si aplica. | Read-only; no enviar ni modificar contratos. | diseño pendiente |
| `/amc-status` | Horas, clientes, facturas pendientes. | Vault, hojas/Docs indicados, Gmail read-only para búsquedas puntuales. | Read-only; no facturar/enviar/cobrar sin aprobación. | diseño pendiente |
| `/tesis-avance` | Capítulo actual, próxima entrega y pendientes. | Vault, calendario, Docs indicados. | Read-only; no editar documento final sin aprobación. | diseño pendiente |

## Regla común

Cada skill de contexto debe producir primero un brief/checklist, no ejecutar acciones externas. Si propone memoria, va a [[agentes/geoffrey/memoria-sugerida]]. Si cambia `wiki/`, requiere log obligatorio.

## Próximo paso recomendado

Construir primero `/propi-brief`, porque está conectado a contratos activos/cumplimiento y puede producir valor operativo sin tocar terceros.

## Relacionado

- [[protocolo-operativo-agentes]]
- [[agentes/geoffrey/ob1-roadmap]]
- [[agentes/geoffrey/tool-authority-matrix]]
- [[agentes/geoffrey/importadores-seguros]]
