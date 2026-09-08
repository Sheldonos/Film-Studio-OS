import json,sys
try: payload=json.load(sys.stdin)
except Exception: payload={}
print("Film Studio OS v0.4.0: read AGENTS.md; run python scripts/bootstrap_bob.py in a fresh clone; diagnose every new source before development. External/paid actions, rights, consent, safety and approvals fail closed.")
