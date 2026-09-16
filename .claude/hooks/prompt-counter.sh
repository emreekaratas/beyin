#!/bin/bash
VAULT_DIR="$(dirname "$(dirname "$(dirname "$0")")")"
STATE_DIR="$VAULT_DIR/.claude/hooks/.state"
mkdir -p "$STATE_DIR"
COUNT=0
[ -f "$STATE_DIR/prompt_count" ] && COUNT=$(cat "$STATE_DIR/prompt_count" 2>/dev/null || echo 0)
COUNT=$((COUNT + 1))
echo "$COUNT" > "$STATE_DIR/prompt_count"

json_escape() {
  local s="$1"
  s="${s//\\/\\\\}"
  s="${s//\"/\\\"}"
  s="${s//$'\t'/\\t}"
  s="${s//$'\r'/}"
  s="${s//$'\n'/\\n}"
  printf '%s' "$s"
}

if [ $((COUNT % 15)) -eq 0 ]; then
  MSG="[Hafıza Uyarısı]: $COUNT. istemdesin. Context şişmesini önlemek için oturum çıktısını Last-Session.md dosyasına özetleyip oturumu yenile."
  ESC=$(json_escape "$MSG")
  echo "{\"hookSpecificOutput\":{\"hookEventName\":\"UserPromptSubmit\",\"additionalContext\":\"${ESC}\"}}"
fi
exit 0
