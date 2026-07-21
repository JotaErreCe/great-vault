#!/bin/bash
# ============================================================
# Setup del sistema de artes UK/IS en una Mac nueva (ej. Mac Mini siempre encendida)
# Correr UNA VEZ en la máquina destino:  bash setup_mac_nueva.sh
# Requisitos previos: iCloud Drive con "Escritorio y Documentos" activado y
# sincronizado (para que esta carpeta Sistema ya exista), y sesión de la misma
# cuenta de iCloud que la MacBook de JR.
# ============================================================
set -e
echo "▶ Setup del sistema de artes UK/IS"

SIS="$HOME/Documents/Understanding Kids/Artes/Sistema"
if [ ! -d "$SIS" ]; then
  echo "✗ No existe $SIS — esperá a que iCloud sincronice la carpeta 'Understanding Kids/Artes' o copiala manualmente antes de seguir."
  exit 1
fi
echo "✓ Carpeta Sistema encontrada en iCloud"

# 1. Claude Code (instalador oficial firmado — NO npm)
if ! command -v claude >/dev/null 2>&1; then
  echo "▶ Instalando Claude Code..."
  curl -fsSL https://claude.ai/install.sh | bash
else
  echo "✓ Claude Code ya instalado"
fi

# 2. Python 3 + Playwright + Chromium
echo "▶ Verificando Python/Playwright..."
python3 -m pip install --user --quiet playwright 2>/dev/null || pip3 install --user --quiet playwright
python3 -m playwright install chromium
echo "✓ Playwright + Chromium listos"

# 3. Prueba de humo del motor
echo "▶ Prueba de render..."
cd "$SIS"
python3 -c "import build_portada; build_portada.render({'icon':'✅','headline_main':'Setup completo en esta Mac','headline_keyword':'listo'}, '_smoke.png')" \
  && rm -f "$SIS/_smoke.png" && echo "✓ El motor renderiza correctamente" \
  || { echo "✗ Falló el render — revisá Playwright/Chromium"; exit 1; }

echo ""
echo "═══════════════════════════════════════════════════════════"
echo "PASOS MANUALES QUE FALTAN (no se pueden automatizar):"
echo "  1. Instalar 'Google Drive para escritorio' con la cuenta"
echo "     jcastaneda@kidsunderstanding.com y esperar que sincronice."
echo "     Verificá: ls ~/Library/CloudStorage/GoogleDrive-jcastaneda@kidsunderstanding.com/My\\ Drive/Administración/Artes/"
echo "  2. Abrir Claude Code y conectar los MCP: Notion, Canva, tareas programadas."
echo "     (Apple Mail y osascript ya funcionan sin setup.)"
echo "  3. Recrear las 2 tareas programadas — pedile a Claude en esta Mac:"
echo "     'Recreá las tareas uk-artes-semanales (domingos 18:00) y"
echo "      uk-tendencias-virales (jueves 18:00) desde los SKILL.md en"
echo "      Documents/Understanding Kids/Artes/Sistema/scheduled-tasks-backup/'"
echo "  4. En la MacBook vieja: DESACTIVAR ambas tareas (que no corran dos veces)."
echo "  5. Dejar Claude Code ABIERTO en esta Mac (las tareas corren con la app abierta)."
echo "═══════════════════════════════════════════════════════════"
