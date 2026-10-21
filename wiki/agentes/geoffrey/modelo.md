
## Modelo de Geoffrey (20-oct-2026)
- OpenClaw usa la cuenta de ChatGPT (backend codex), no una clave de API de OpenAI. Configuración real: `~/.openclaw/openclaw.json` (no `gateway/config.yaml`).
- `gpt-5.6-sol` da «Bad Request» en ChatGPT. Desde el 20-oct-2026 el primario es `openai/gpt-6.1-sol`, con respaldo `anthropic/claude-sonnet-5-5` (lo hizo Claude a pedido de JR; respaldo en `openclaw.json.bak-claude-gpt61-20261020`).
- El chat de Telegram de JR con Geoffrey estaba fijado a `ollama/nemotron-3-super:cloud` (override de sesión en `~/.openclaw/agents/main/sessions/sessions.json`, respaldo `.bak-claude-20261020`). Se quitó. Si JR usa `/model` en ese chat, se vuelve a fijar; `/model default` lo regresa.
- Diagnóstico: `openclaw status` (sección «Model selection») y `/tmp/openclaw/openclaw-AAAA-MM-DD.log` (eventos `model_fallback_decision`).
