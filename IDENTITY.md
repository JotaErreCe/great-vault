# IDENTITY.md — Great Vault identity boundary

This file is **not** an OpenClaw agent identity.

The Great Vault is JR's long-term knowledge base. It may contain agent packages, but it is not itself an agent runtime workspace.

## Rule for agents

Agent identities live in agent-specific packages under:

- `wiki/agentes/[agent-id]/`

OpenClaw runtime identity files live outside the Vault, in per-agent workspaces resolved from the current runtime/session, such as `workspace-geoffrey` or `workspace-[agent-id]`. Do not treat a host-specific absolute path as universal.

If an agent reads this file while looking for its own identity, it must stop and load its configured workspace plus its package under `wiki/agentes/[agent-id]/`.

## Current known agent packages

- `wiki/agentes/geoffrey/` — Geoffrey Barbara Butler / G, JR's principal digital butler.

## Related

- [[_AI_BOOTSTRAP]]
- [[agentes/arquitectura]]
- [[protocolo-operativo-agentes]]
- [[agentes/geoffrey/AGENT]]
