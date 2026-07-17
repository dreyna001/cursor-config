---
description: Adaptive project layout standards for Python, deployment, docs, scripts, data, and UI assets
alwaysApply: false
---

# Project Layout Standards

Default new or reorganized Python projects to a professional `src/` layout unless the existing project has a deliberate, stable alternative.

Preferred baseline:

```text
project/
  README.md
  pyproject.toml
  src/<package_name>/
  tests/
  docs/
  scripts/
  data/
  deploy/
```

Adapt the baseline to the actual project shape:

- Python code lives under `src/<package_name>/`; use package imports, not root-relative module imports.
- Tests live under `tests/` and should import the installed/package path.
- Operator and architecture docs live under `docs/`, organized by purpose.
- Repeatable helper commands live under `scripts/`; one-off/generated outputs do not.
- Small fixtures and sample payloads live under `data/`; production data and secrets do not.
- Deployment assets live under `deploy/` with environment subdirs such as `deploy/aws/`, `deploy/docker/`, `deploy/systemd/`, `deploy/k8s/`, or `deploy/terraform/`.
- Frontend code, when present, should live in a clear app boundary such as `frontend/`, `web/`, or `apps/<ui-name>/`, not mixed into backend package internals.
- Keep runtime contracts synchronized across code, tests, docs, examples, and deployment files when paths or entrypoints move.

On-prem Python service overlay:

- Use `src/<project_package>/...` for service packages and integration helper packages; prefer the project package name over generic package names like `onprem_service`.
- Keep host installers and operator helper commands under `scripts/`; keep service units under `deploy/systemd/`.
- Keep runtime host paths documented but not treated as repo folders: `/opt/...`, `/etc/...`, `/var/...`, SFTP/NFS drop paths, model-weight paths, wheelhouses, logs, reports, and generated dependency manifests.
- Keep local model runtime, RAG index paths, SFTP/NFS ingest paths, config examples, systemd units, and docs synchronized when entrypoints or package data paths move.
- Do not commit production notables, model weights, RAG SQLite/FAISS indexes, wheelhouses, secrets, or customer-specific manifests; use `data/` only for small fixtures and sample payloads.

For migrations, move in small verifiable diffs: package imports/tests first, deployment paths second, scripts/data/docs last.
