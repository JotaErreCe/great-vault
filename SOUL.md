# SOUL.md — Great Vault boundary

This file is **not** an active agent persona.

The Great Vault may store many agent personas under `wiki/agentes/[agent-id]/`, but the Vault root must stay neutral so multiple OpenClaw agents do not all inherit the same identity.

## Rule

If an OpenClaw agent reads this file while trying to determine who it is, it must stop and load:

1. its configured runtime workspace under the active OpenClaw workspace for `[agent-id]`; and
2. its canonical package under `wiki/agentes/[agent-id]/` in the resolved Great Vault.

Current active Geoffrey references:

- Runtime workspace: resolve from OpenClaw session/workspace context, normally `workspace-geoffrey`.
- Canonical package: `wiki/agentes/geoffrey/`.
- Common protocol: `wiki/resources/protocolo-operativo-agentes.md`.

## Related

- [[agentes/arquitectura]]
- [[protocolo-operativo-agentes]]
- [[geoffrey/SOUL]]
