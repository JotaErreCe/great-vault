# AGENTS.md — Great Vault operating schema

This is **not** an OpenClaw agent runtime identity file. The Vault root is neutral for multi-agent safety.

This Vault follows the LLM Wiki pattern. Before doing substantive work here, read [[_AI_BOOTSTRAP]] and follow it.

Any agent operating in this Vault must also follow `wiki/resources/protocolo-operativo-agentes.md`, which connects OB1-style work logs/checkpoints/memory review/import safety with the Vault memory rules.

Core rules:

- `raw/` = immutable sources. Read, cite, and ingest; do not rewrite source files.
- `wiki/` = LLM-maintained compiled knowledge. Create/update pages here when integrating sources or answering durable questions.
- `_templates/` = reusable page shapes only. Do not put source material or finished wiki pages here.
- Root files are schema/control files only. Do not clutter the root with agent runtime memory, generic defaults, or temporary artifacts.
- Tool-managed root exceptions may exist (`skills/`, `.clawhub/`, `.openclaw/`) because OpenClaw/ClawHub created or tracks them. Treat them as tooling/config, not Vault knowledge; do not move or delete them without explicit approval because that may affect installed skills.
- Ask before broad reorganizations, destructive moves, or anything that changes Obsidian/Syncthing behavior.
- If something is runtime state for an agent rather than Vault knowledge, keep it outside this Vault.

If unsure, stop and ask Master JR.
