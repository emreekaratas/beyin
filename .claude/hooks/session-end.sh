#!/bin/bash
VAULT_DIR="$(dirname "$(dirname "$(dirname "$0")")")"
STATE_DIR="$VAULT_DIR/.claude/hooks/.state"
LOG_DIR="$VAULT_DIR/daily"
TODAY=$(date +%Y-%m-%d)
mkdir -p "$LOG_DIR"

{
  echo ""
  echo "### Oturum Kapanışı: $(date '+%Y-%m-%d %H:%M:%S')"
  echo "- Durum: Oturum sonlandırıldı."
} >> "$LOG_DIR/$TODAY.md"

rm -f "$STATE_DIR/session_start_time" "$STATE_DIR/prompt_count"
exit 0
