---
type: reference
date: 2026-05-21
tags: [agente, geoffrey, auditoria, superpowers]
---

# Auditoría Superpowers Extended CC → adaptación OpenClaw/Codex

Fecha: 2026-05-21  
Objeto: `superpowers-extended-cc` instalado en Claude Code, versión 5.5.0.  
Fuente local: `/Users/jr/.claude/plugins/marketplaces/superpowers-extended-cc-marketplace/`

## Estado verificado

- Plugin Claude Code instalado y habilitado: `superpowers-extended-cc@superpowers-extended-cc-marketplace`, versión 5.5.0.
- Inventario Claude Code: 21 skills, 0 agents, 1 hook SessionStart.
- Costo always-on estimado en Claude Code: ~1,059 tokens/sesión.
- Hooks agresivos adicionales existen como ejemplos, pero no están activados: gates de usuario, bloqueo de commits, orden `blockedBy`, validación de dispatch de subagentes, evidencia de retorno de subagentes y stop-deflection guard.
- El repo incluye `.codex-plugin/plugin.json` y script `scripts/sync-to-codex-plugin.sh`, pero ese script está orientado a sincronizar el plugin hacia `prime-radiant-inc/openai-codex-plugins`, no a instalarlo localmente en este Mac.
- En este entorno no hay binario `codex` en PATH (`codex: command not found`). OpenClaw actualmente usa modelo `openai-codex/gpt-5.5`, pero la config muestra `agentRuntime.id: claude-cli`, no runtime nativo `codex`.

## Mapa de skills y portabilidad

| Skill | Valor práctico | Portabilidad a OpenClaw/Codex | Adaptación recomendada |
|---|---|---:|---|
| `brainstorming` | Evita empezar a implementar sin entender intención, alcance, tradeoffs y aprobación. | Alta | Convertir en protocolo Geoffrey: diseño breve antes de features/proyectos; guardar spec en Vault o repo, no necesariamente `docs/superpowers`. |
| `writing-plans` | Convierte spec aprobado en tareas pequeñas con archivos, AC y verificación. | Alta | Mapear a `update_plan` + plan markdown; incluir `Goal / Files / Acceptance Criteria / Verify`. |
| `executing-plans` | Ejecuta planes por lotes con checkpoints. | Alta | Usar `update_plan`, subagentes OpenClaw y work logs/checkpoints OB1. |
| `subagent-driven-development` | Implementador + review de spec + review de calidad por tarea. | Alta | Mapear a `sessions_spawn`; cada subagente recibe contexto mínimo y devuelve evidencia. |
| `dispatching-parallel-agents` | Paraleliza investigaciones independientes. | Alta | Ya encaja con `sessions_spawn`; añadir regla de no compartir contexto salvo necesidad. |
| `test-driven-development` | Red/green/refactor; evita código sin test real. | Media-Alta | Aplicar en repos con test suite. No forzar en tareas no testeables o exploratorias. |
| `systematic-debugging` | Root cause antes de parches. | Alta | Adoptar como regla obligatoria ante bugs/fallos de comandos; documentar hipótesis, prueba, evidencia. |
| `verification-before-completion` | No declarar listo sin prueba. | Muy alta | Ya coincide con Geoffrey; convertir en gate general para final answers. |
| `requesting-code-review` | Revisión antes de merge/fin de feature. | Alta | Subagente reviewer o Claude Code reviewer; severidad y bloqueo de críticos. |
| `receiving-code-review` | No aceptar feedback a ciegas; verificar técnicamente. | Alta | Adoptar para PRs/reviews externos. |
| `using-git-worktrees` | Aísla trabajo de feature. | Media-Alta | En OpenClaw preferir worktree nativo si existe; si no, `git worktree`. Requiere confirmar repo/branch. |
| `finishing-a-development-branch` | Cierre ordenado: tests, merge/PR/descartar, limpieza. | Alta | Convertir en checklist de cierre por repo/proyecto. |
| `checking-gates` / `specifying-gates` | Cuando el usuario pide “verifica”, obliga a definir cómo probar. | Alta conceptualmente, media técnicamente | Reproducir en OpenClaw con metadata en plan + preguntas mínimas si el “cómo” es ambiguo. Hooks automáticos quedan pendientes. |
| `writing-skills` | TDD aplicado a crear skills: prueba de fallo, skill, prueba de cumplimiento. | Alta | Útil para crear `geoffrey-superpowers` o adaptar skills a OpenClaw. |
| comandos `brainstorm`, `write-plan`, `execute-plan`, `gate-check`, `specify-gate` | Atajos Claude Code. | Baja como comandos | Reemplazarlos por invocaciones naturales / skills OpenClaw. |

## Hooks opcionales y recomendación

No activar todavía de forma global. Evaluación:

1. `pre-commit-check-tasks.sh` — útil en repos de código, pero puede bloquear commits legítimos si el plan/task state se desincroniza. Activar solo por proyecto.
2. `post-task-complete-revalidate.sh` y `stop-revalidate-user-gates.sh` — muy alineados con “evidencia antes de afirmar”; buenos candidatos, pero primero probar en sandbox Claude Code.
3. `pre-task-blockedby-enforce.sh` — útil si usamos tareas nativas Claude Code con dependencias; no portable directo a OpenClaw porque OpenClaw usa `update_plan`, no TaskUpdate nativo.
4. `pre-agent-task-dispatch-validate.sh` y `post-agent-return-validate.sh` — útiles para subagentes, pero dependen de herramientas/metadata Claude Code. Adaptar conceptualmente a instrucciones de `sessions_spawn`.
5. `stop-deflection-guard.sh` — coincide con la frustración de “dejémoslo para otra sesión” sin razón real; no activar sin revisar frases/umbral para evitar falsos positivos.

## Adaptación recomendada para OpenClaw/Codex

Crear una skill local, provisionalmente `geoffrey-superpowers`, que no copie ciegamente el plugin sino que traduzca la metodología a nuestras herramientas:

- `brainstorming` → conversación de diseño + opciones + aprobación.
- `writing-plans` → `update_plan` + archivo de plan cuando sea trabajo largo.
- `executing-plans` → ejecución con gates, subagentes y evidencia.
- `subagent-driven-development` → `sessions_spawn` aislado, con implementador/revisor.
- `verification-before-completion` → gate obligatorio antes de final.
- `systematic-debugging` → protocolo de root cause antes de fixes.
- `finishing-a-development-branch` → checklist de cierre.
- `checking/specifying gates` → si el criterio de verificación es ambiguo, preguntar solo lo mínimo antes de cerrar.

Integración con OB1/Vault:

- Specs y planes importantes deben ir al repo del proyecto cuando sean código; si son operativos/personales, al Vault.
- Work logs y checkpoints de Geoffrey siguen siendo la continuidad duradera.
- No duplicar `protocolo-captura-diaria`; Superpowers lo complementa en ejecución, no reemplaza memoria/continuidad.

## Pasos sugeridos

1. **No tocar hooks globales todavía.** Mantener Claude Code Superpowers habilitado solo con el hook SessionStart instalado por defecto.
2. **Hacer una prueba controlada en Claude Code** con un repo pequeño: brainstorming → plan → ejecución → verification-before-completion.
3. **Crear `geoffrey-superpowers` para OpenClaw** usando `skill-creator`/`writing-skills`: presión de prueba primero, luego skill, luego prueba con subagente.
4. **Diseñar formato de task metadata portable**:
   - `Goal`
   - `Files`
   - `Acceptance Criteria`
   - `Verify`
   - `Evidence Required`
   - `Blocked By`
   - `Vault/Work-log target` si aplica.
5. **Mapear subagentes**:
   - implementador,
   - spec reviewer,
   - quality reviewer,
   - optional research/debugger.
6. **Agregar reglas ligeras a Geoffrey/AGENT.md solo después de probar** para no inflar el prompt con metodología que aún no validamos.
7. **Si Master JR quiere runtime Codex nativo**, auditar aparte la config OpenClaw: hoy no hay `codex` CLI en PATH y `agentRuntime.id` apunta a `claude-cli`; esto es distinto de usar modelo `openai-codex/gpt-5.5`.

## Recomendación ejecutiva

Adoptar Superpowers como **metodología de ejecución**, no como nueva fuente de verdad. Para Geoffrey, el mejor beneficio inmediato es endurecer tres hábitos:

1. diseño antes de implementación,
2. tareas con verificación explícita,
3. evidencia antes de decir “listo”.

La adaptación a OpenClaw/Codex es viable porque las piezas centrales son instrucciones y estructura de trabajo; lo que no es portable directamente son los hooks Claude Code y la task API nativa.

## Relacionado

- [[agentes/geoffrey/AGENT]]
- [[agentes/geoffrey/ob1-roadmap]]
- [[agentes/geoffrey/work-log]]
- [[protocolo-operativo-agentes]]
