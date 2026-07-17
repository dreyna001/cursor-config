---
description: Use for repo structure, docs layout, runtime contracts, environment separation, deployment shape, and capability profiles
alwaysApply: false
---

# Architecture And Layout Rules

## Project Layout

Default new or reorganized Python projects to:

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

- Adapt to existing stable project structure when present.
- Python code belongs under `src/<package_name>/`.
- Tests belong under `tests/` and should import installed/package paths.
- Operator and architecture docs belong under `docs/`.
- Repeatable helper commands belong under `scripts/`.
- Small fixtures and sample payloads may live under `data/`; production data and secrets must not.
- Deployment assets belong under `deploy/` with subdirs such as `aws/`, `docker/`, `systemd/`, `k8s/`, or `terraform/`.
- Frontend code should live behind a clear app boundary such as `frontend/`, `web/`, or `apps/<ui-name>/`.

## Docs Layout

Default new projects and major subprojects to:

```text
docs/
  README.md
  delivery_package/
  architecture/
  technical_specs/
  prompts/
  planning/
  internal/
```

Default initial planning stack:

```text
docs/planning/domain_capability_map.md
docs/planning/implementation_tracker.md
docs/architecture/core_deployment_architecture.md
docs/technical_specs/core_technical_spec.md
```

- Use `docs/README.md` as the navigation index.
- Create missing directories and seed missing templates only.
- Never overwrite an existing docs stack just to match a template.

## Runtime Contracts

- Treat base URLs, ports, model IDs, data paths, index paths, feature flags, env vars, payload fields, entrypoints, and external schemas as runtime contracts.
- Keep contract values synchronized across code, tests, env examples, compose/systemd, install scripts, SDK defaults, README, and runbooks.
- Avoid drift between example config and production-oriented defaults.
- If adding a required setting, add examples, validation, and docs in the same change.

## Environment Separation

- Keep business logic independent from Lambda handlers, shell wrappers, cron glue, systemd units, or infrastructure callbacks.
- Isolate deployment-specific concerns near app edges.
- Be explicit about what is application logic versus deployment logic.
- Do not force universal adapter templates or portability theater.
- Portability should come from clean separation of concerns, not premature abstraction.

## Capability Profiles

- Treat product features as named capabilities with explicit flags.
- Risky capabilities must be off by default.
- Separate read-only, writeback, and action capabilities into different flags or gates.
- Validate flag dependencies and invalid combinations at startup; fail fast on unsupported config.
- Treat per-customer config as a documented capability profile, not a deployment hack.
- Keep capability flags, env examples, validation code, docs, and tests synchronized.
- New capabilities must define purpose, default state, dependencies, approval boundary, and rollback path.

## On-Prem Service Overlay

- Use `src/<project_package>/...` for service packages and helper packages.
- Keep host installers and operator commands under `scripts/`.
- Keep service units under `deploy/systemd/`.
- Document runtime host paths but do not treat them as repo folders: `/opt/...`, `/etc/...`, `/var/...`, SFTP/NFS drops, model weights, wheelhouses, logs, reports, generated manifests.
- Do not commit production notables, model weights, RAG SQLite/FAISS indexes, wheelhouses, secrets, or customer-specific manifests.