#!/usr/bin/env python3
"""Fresh-clone bootstrap/check utility. Uses stdlib until package installation begins."""
from __future__ import annotations
import argparse, importlib.util, json, shutil, subprocess, sys, venv
from pathlib import Path

CORE=("pydantic","yaml","jsonschema")
OPTIONAL=("pytest","pypdf","mcp")

def readiness(root:Path)->dict:
    skills=list((root/".bob/skills").glob("*/SKILL.md")); workflows=list((root/"workflows/v2").glob("*.json"))+list((root/"workflows/pilots").glob("*.json"))
    modules={name:bool(importlib.util.find_spec(name)) for name in CORE+OPTIONAL}
    files={name:(root/name).exists() for name in ("AGENTS.md","pyproject.toml",".bob/settings.json",".bob/custom_modes.yaml","capabilities/registry_v2.json")}
    actions=[]
    if sys.version_info < (3,10): actions.append("Install Python 3.10 or newer.")
    if not all(files.values()): actions.append("Open the command at the Film Studio OS repository root.")
    if not all(modules[n] for n in CORE): actions.append("Run: python scripts/bootstrap_bob.py --install")
    if not modules["pytest"]: actions.append("Install the dev extra before validation: python -m pip install -e '.[dev]'")
    if not modules["mcp"]: actions.append("Install the mcp extra before starting the Bob MCP server: python -m pip install -e '.[mcp]'")
    if not shutil.which("ffmpeg") or not shutil.which("ffprobe"): actions.append("Install ffmpeg/ffprobe for media QC; creative planning remains available without them.")
    if not shutil.which("higgsfield"): actions.append("Optional only: install the Higgsfield CLI after the studio approves that provider; do not authenticate or submit from bootstrap.")
    return {"schema_version":"1.0","python":sys.version.split()[0],"root":str(root),"repository_files":files,"bob":{"skills":len(skills),"workflows":len(workflows)},"python_modules":modules,"commands":{"ffmpeg":bool(shutil.which("ffmpeg")),"ffprobe":bool(shutil.which("ffprobe")),"higgsfield":bool(shutil.which("higgsfield"))},"ready_core":sys.version_info >= (3,10) and all(files.values()) and all(modules[n] for n in CORE),"actions":actions}

def install(root:Path)->int:
    env=root/".venv"
    if not env.exists(): venv.EnvBuilder(with_pip=True).create(env)
    py=env/("Scripts/python.exe" if sys.platform=="win32" else "bin/python")
    subprocess.run([str(py),"-m","pip","install","-e",str(root)+"[dev,mcp,ingest]"],cwd=root,check=True)
    subprocess.run([str(py),"-m","film_studio_os","validate-bob","--root",str(root)],cwd=root,check=True)
    subprocess.run([str(py),"-m","film_studio_os","validate-package","--root",str(root)],cwd=root,check=True)
    print(json.dumps({"installed":True,"venv":str(env),"next":"Select a Bob skill-capable mode, verify project skills, then run diagnose-project."},indent=2))
    return 0

def main(argv=None):
    ap=argparse.ArgumentParser(); ap.add_argument("--root",default=Path(__file__).resolve().parents[1]); ap.add_argument("--check",action="store_true",help="explicit alias for the default read-only check"); ap.add_argument("--install",action="store_true"); args=ap.parse_args(argv); root=Path(args.root).resolve()
    if args.install: return install(root)
    report=readiness(root); print(json.dumps(report,indent=2,sort_keys=True)); return 0 if report["ready_core"] else 2

if __name__=="__main__": raise SystemExit(main())
