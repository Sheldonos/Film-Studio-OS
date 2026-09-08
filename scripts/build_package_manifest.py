#!/usr/bin/env python3
"""Build the deterministic self-excluding package checksum manifest."""
from __future__ import annotations
from datetime import date
from hashlib import sha256
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUTPUT=ROOT/"docs/validation/package_manifest.json"
EXCLUDED_PARTS={".git",".venv","__pycache__",".pytest_cache","build","film_studio_os.egg-info"}

def main():
    rows=[]
    for path in sorted(x for x in ROOT.rglob("*") if x.is_file()):
        rel=path.relative_to(ROOT)
        if path==OUTPUT or any(part in EXCLUDED_PARTS for part in rel.parts) or path.suffix==".pyc":
            continue
        data=path.read_bytes()
        rows.append({"path":rel.as_posix(),"bytes":len(data),"sha256":sha256(data).hexdigest()})
    payload={"schema_version":"2.0","version":"0.4.0","generated_at":date.today().isoformat(),"file_count":len(rows),"self_excluded":True,"files":rows}
    OUTPUT.write_text(json.dumps(payload,indent=2)+"\n")
    print(json.dumps({"path":str(OUTPUT),"file_count":len(rows)}))

if __name__=="__main__": main()
