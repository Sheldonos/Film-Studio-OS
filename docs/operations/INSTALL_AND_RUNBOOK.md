# Install & Operator Runbook

## Local install
```bash
python scripts/bootstrap_bob.py
python scripts/bootstrap_bob.py --install
source .venv/bin/activate
python -m film_studio_os validate-bob
python -m film_studio_os validate-package
pytest -q
```

The installer creates `.venv` and installs `.[dev,mcp,ingest]`. It does not install or authenticate Higgsfield. See `AGENTS.md` for Bob Advanced/skill-mode discovery and setup recovery.

## Validate workflow definitions
```bash
python -m film_studio_os validate-workflow workflows/v2/intake_rights_v2.json
```

## Diagnose a new project
```bash
film-studio diagnose-project --project demo --source-type script --project-type feature --production-route hybrid
```
Resolve blocking questions before downstream development.

## Run safe pilots
```bash
python -m film_studio_os pilot animated-short
python -m film_studio_os pilot dialogue-scene
python -m film_studio_os pilot action-sequence
python -m film_studio_os pilot documentary-segment
python -m film_studio_os pilot episodic-linked-scenes
```
All pilots are fixture-only and use `mock-generation`; they do not authorize external side effects.

## IBM Bob
Open the repository as a trusted workspace only after reviewing `AGENTS.md` and `.bob/`. Use IBM Bob Advanced mode or a project mode with the Skill tool, then confirm project discovery in Bob Settings → Skills. Bob should discover modes, skills and personas from `.bob/custom_modes.yaml`, `.bob/skills`, and `.bob/agents`. The optional local MCP server is configured in `.bob/mcp.json`; install the `[mcp]` extra before enabling it.

## Recovery
Workflow state is stored in the SQLite path passed to CLI/runtime. Re-run the same workflow/project to resume. Never delete the database to resolve a production failure unless the project is disposable; inspect work orders/events first.

## Live providers
Live provider execution is disabled by default in v0.4.0. The Higgsfield adapter supports governed discovery/dry-run and a separately authorized live boundary; do not reinterpret installation, provider manifests or a successful dry-run as authorization.
