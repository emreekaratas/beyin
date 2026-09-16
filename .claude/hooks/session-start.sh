#!/bin/bash
VAULT_DIR="$(dirname "$(dirname "$(dirname "$0")")")"
MEM_DIR="$VAULT_DIR/🔮 850-Companion"
STATE_DIR="$VAULT_DIR/.claude/hooks/.state"
mkdir -p "$STATE_DIR"
date +%s > "$STATE_DIR/session_start_time"
echo "0" > "$STATE_DIR/prompt_count"

json_escape() {
  local s="$1"
  s="${s//\\/\\\\}"
  s="${s//\"/\\\"}"
  s="${s//$'\t'/\\t}"
  s="${s//$'\r'/}"
  s="${s//$'\n'/\\n}"
  printf '%s' "$s"
}

LAST_SESSION=""
[ -f "$MEM_DIR/Last-Session.md" ] && LAST_SESSION=$(head -40 "$MEM_DIR/Last-Session.md" 2>/dev/null)

THREADS=""
[ -f "$MEM_DIR/Threads.md" ] && THREADS=$(grep -E "^### |^\*\*Status:\*\*" "$MEM_DIR/Threads.md" 2>/dev/null | head -10)

KURALLAR=""
[ -f "$MEM_DIR/Kurallar.md" ] && KURALLAR=$(head -40 "$MEM_DIR/Kurallar.md" 2>/dev/null)

CTX=""
[ -n "$LAST_SESSION" ] && CTX="${CTX}[Hafıza: Son Oturum]
${LAST_SESSION}

"
[ -n "$THREADS" ] && CTX="${CTX}[Hafıza: Aktif Threadler]
${THREADS}

"
[ -n "$KURALLAR" ] && CTX="${CTX}[Hafıza: Kurallar]
${KURALLAR}

"
CTX="${CTX}[Sistem]: beyin aktif. CLAUDE.md yönergelerine harfiyen uy."

if [ -n "$CTX" ]; then
  ESC=$(json_escape "$CTX")
  echo "{\"hookSpecificOutput\":{\"hookEventName\":\"SessionStart\",\"additionalContext\":\"${ESC}\"}}"
fi
exit 0
