"""Fail-closed guard for commands that can spend money or create external assets."""
import json, os, re, sys

try:
    payload = json.load(sys.stdin)
except Exception:
    # Bob hooks must not break harmless tools because of an unrelated event shape.
    sys.exit(0)

raw = json.dumps(payload.get("input", {}), sort_keys=True)
side_effect_patterns = (
    r"\bfilm-studio\b[^\n]*(?:provider-submit|--live)\b",
    r"\b(?:higgsfield|higgs|hf)\b\s+generate\s+(?:create|workflow)\b",
    r"\b(?:higgsfield|higgs|hf)\b\s+(?:upload|soul-id\s+create)\b",
)
is_external_action = any(re.search(pattern, raw, re.IGNORECASE) for pattern in side_effect_patterns)
if is_external_action and os.environ.get("FILM_STUDIO_EXTERNAL_AUTHORIZED") != "1":
    print(
        "Blocked: external provider action requires FILM_STUDIO_EXTERNAL_AUTHORIZED=1 "
        "plus a matching approval record and cost preflight.",
        file=sys.stderr,
    )
    sys.exit(2)
sys.exit(0)
