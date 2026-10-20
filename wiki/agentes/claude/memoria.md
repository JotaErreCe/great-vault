---
type: reference
date: 2026-10-19
tags: [agente, claude, memoria, index]
---

# Memoria de Claude → páginas del Vault

Desde el 2026-10-19 (fase F4 de [[vault-cerebro]], decisión D4) cada memoria de Claude en `~/.claude/projects/-Users-jr-Claude/memory/` es una **regla corta con enlace** a su página aquí. Si algo cambia, se corrige primero la página del Vault y después la regla corta. Respaldo de las memorias completas antes del cambio: `~/Claude/respaldos/2026-10-vault-cerebro/memory.tar.gz` y `memory-pre-f4.tar.gz`.

| Memoria | Página del Vault | Forma |
|---|---|---|
| `feedback_style` | [[como-trabajar-con-jr]] | corta |
| `great_vault` | [[great-vault]] | corta |
| `rol_coordinador_agentes` | [[agentes/claude/rol-coordinador]] | corta |
| `telegram_persona_iroh` | [[agentes/claude/persona-tio-iroh]] | corta |
| `telegram_watchdog` | [[agentes/claude/telegram-puente]] | **completa** (operativa) |
| `avisos_tareas_programadas` | [[agentes/claude/avisos-tareas-programadas]] | **completa** (operativa) |
| `claude_sin_autoupdate` | [[agentes/claude/actualizaciones]] | **completa** (operativa) |
| `vault_centralizacion` | [[vault-cerebro]] | **completa** |
| `notas_de_voz_telegram` | [[agentes/claude/notas-de-voz]] | corta |
| `gws_dos_cuentas` | [[agentes/claude/correo]] | corta |
| `apple_mail_access` | [[agentes/claude/correo]] | corta |
| `drive_montaje_vacio` | [[agentes/claude/drive]] | corta |
| `apify_mcp_setup` | [[agentes/claude/tareas-programadas]] § Apify | corta |
| `skills_finanzas_solo_lectura` | [[agentes/claude/skills-finanzas]] | corta |
| `project_understanding_kids` | [[understanding-kids]] § Para agentes | corta |
| `uk_template_system` | [[sistema-artes-redes]] · [[plantillas-artes]] · [[artes-decisiones-y-lecciones]] | corta (F6, 19-oct-2026; detalle técnico que faltaba pasado a [[plantillas-artes]] § Detalles técnicos) |
| `uk_copy_style` | [[artes-decisiones-y-lecciones]] § Copy · [[guia-maestra-estilo]] §3 | corta (F6, 19-oct-2026) |
| `uk_reglas_revision_2026-08-17` | [[artes-decisiones-y-lecciones]] § Revisión 17-ago | corta |
| `uk_correcciones_flujo` | [[agentes/claude/subagentes]] (cierre sin correo, decisión del 19-oct) | corta |
| `uk_campanas_fuente_notion` | [[artes-decisiones-y-lecciones]] § Campañas · [[campana-eda26]] | corta |
| `uk_notion_fotos_limitacion` | [[artes-decisiones-y-lecciones]] § Notion | corta |
| `eda26_inscripciones_whatsapp` | [[campana-eda26]] § Estado | corta |
| `propi_handoff` | [[propi/handoff-2026-08-24\|handoff TORONJA]] | corta |

**`uk_template_system` y `uk_copy_style` (acortadas en F6, 19-oct-2026):** se conservaron completas hasta que el `SKILL.md` de `uk-artes-semanales` dejó de leerlas; desde F6 la corrida lee las páginas del Vault. La versión completa anterior quedó en `~/Claude/respaldos/2026-10-vault-cerebro/f6/`.

## Pendientes y contradicciones (para JR)

- ~~Correcciones a demanda: ¿correo a Magoo o no?~~ Resuelto el 19-oct-2026: sin correo; Magoo pide cambios por Notion ([[agentes/claude/subagentes]]).
- `ibkr.env` no existe (ver [[agentes/claude/skills-finanzas]]).
- Las definiciones de los subagentes `compras`, `interiores` y `pendientes-magoo` apuntan a rutas locales (`~/Claude/pendiente-vault/…`, memorias): actualizarlas al Vault en F6.

## Relacionado

- [[agentes/claude/AGENT|Claude]] · [[escribir-memoria]] · [[vault-cerebro]]
