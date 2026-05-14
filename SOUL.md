# SOUL.md — Great Vault boundary

This file is **not** an active agent persona.

The Great Vault may store many agent personas under `wiki/agentes/[agent-id]/`, but the Vault root must stay neutral so multiple OpenClaw agents do not all inherit the same identity.

## Rule

If an OpenClaw agent reads this file while trying to determine who it is, it must stop and load:

1. its configured runtime workspace under `/Users/jr/.openclaw/workspace-[agent-id]/`; and
2. its canonical package under `/Users/jr/documents/Great Vault/wiki/agentes/[agent-id]/`.

Current active Geoffrey runtime:

- Runtime workspace: `/Users/jr/.openclaw/workspace-geoffrey/`
- Canonical package: `/Users/jr/documents/Great Vault/wiki/agentes/geoffrey/`

## Related

- [[agentes/arquitectura]]
- [[geoffrey/SOUL]]
