---
name: apple-mail-access
description: "How to read/search/send email via Apple Mail on this Mac using osascript — verified working patterns, account scope, and gotchas"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 58eeb36b-d815-482e-aed7-7c3149c7fdf0
  modified: 2026-08-13T16:23:05.880Z
---

Apple Mail (Mail.app) on this Mac (jotaerre) is scriptable via `osascript`/AppleScript, and terminal automation permission is **already granted** — no setup needed, just use it. Confirmed working 2026-07-13.

**Read/search scope (confirmed with JR):** Google (joserca95@gmail.com), iCloud, jcastaneda@kidsunderstanding.com, ufm.edu. Hotmail account exists but has no mailboxes/is unused.

**Send scope:** JR wants to be asked which account to send from **every time** — no default identity. Never send without picking the account explicitly in that turn and getting explicit confirmation of recipient/subject/body first (this is also a hard rule regardless of setup — see global send-permission policy).

**EXCEPCIÓN por tarea (JR 2026-08-13) — el ÚNICO correo que se manda sin preguntar nada:** el de la tarea semanal de artes de UK/IS ([[uk-template-system]]). Remitente **siempre `jcastaneda@kidsunderstanding.com`**, destinatario **siempre Magoo (`msamayoa@kidsunderstanding.com`)**, y **el cuerpo tampoco se confirma**. JR lo pidió expresamente (dos veces, escalando): cada confirmación frena un ciclo que quiere desatendido, y si él no está frente a la compu no sale nada. No volver a pedirle que apruebe este correo.

Dos cosas que igual se hacen: **pegar el cuerpo enviado en el reporte** (visibilidad sin bloquearlo), y **preguntar solo si el correo se sale de la rutina** — otro destinatario, o contenido que no sea el traspaso normal de artes.

**La regla general de arriba sigue vigente para TODO lo demás** (Propi, AMC Legal, personal): ahí se pregunta cuenta, destinatario y cuerpo. Esta excepción no se generaliza a otras tareas ni a otros correos de UK.

## Working AppleScript patterns

**Gotcha:** Gmail's special folders (Todos/Enviados/Importantes/Destacados/Papelera/Spam = All Mail/Sent/Important/Starred/Trash/Spam) live nested under a `[Gmail]` container per account. They CANNOT be addressed as `mailbox "Enviados" of account "Google"` directly (throws error -1728). You must iterate `every mailbox of account` and match by name. Top-level mailboxes like `INBOX`, `Sent Messages`, `Drafts` on Google are separate/legacy Apple-created ones with very different (much smaller/stale) content than the real Gmail folders — don't confuse them. E.g. on Google account: real "Enviados" (Sent) = 1351 msgs, real "Todos" (All Mail) = 28988 msgs, but the decoy "Sent Messages" = only 28 msgs.

List accounts + all mailboxes (flattened, correct way):
```bash
osascript <<'EOF'
tell application "Mail"
  set acct to account "Google"
  repeat with mb in every mailbox of acct
    log (name of mb) & " -> " & (count of messages of mb)
  end repeat
end tell
EOF
```

Search a specific mailbox by name (resolve object first, then filter — `whose` works reliably once the mailbox is correctly resolved, tested up to ~17,700 messages in INBOX):
```bash
osascript <<'EOF'
tell application "Mail"
  set acct to account "Google"
  repeat with mb in every mailbox of acct
    if name of mb is "Enviados" then
      set targetMb to mb
      exit repeat
    end if
  end repeat
  set matches to (messages of targetMb whose subject contains "Brera")
  repeat with m in matches
    log (date sent of m) & " | " & (subject of m)
  end repeat
end tell
EOF
```

For iCloud/other accounts, top-level `mailbox "INBOX" of account "iCloud"` works fine directly (no Gmail-style nesting issue) — the nesting gotcha is specific to Gmail-provider accounts.

There's a "Proyectos-AMCLegal" folder mirrored in both Google and iCloud accounts (alongside Proyectos-Propi, Proyectos-UK, Finanzas-*, Personal-Familia) — looks like an intended filing scheme from another tool/rule, but as of 2026-07-13 it's **empty (0 messages)** on both accounts. Don't rely on it — search INBOX/Enviados/Todos directly instead.

## Related
- [[brera_arredamenti]] and other AMC Legal client work will likely be the main use case for this (client correspondence lives in the Google account's INBOX/Enviados).
- There's a third-party "apple-mail-macos" clawhub skill installed in the Great Vault (`~/Great Vault/skills/apple-mail-macos/`) — that's tooling for a *different* agent runtime (openclaw/clawdbot) the user also runs, not for Claude Code. Don't try to invoke it as a Skill; the osascript patterns above are what Claude Code should use directly via Bash.
