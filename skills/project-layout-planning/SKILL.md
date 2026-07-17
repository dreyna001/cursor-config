---
name: project-layout-planning
description: Plan or reorganize project layout for Python services, docs, scripts, data, deployment assets, or frontend apps.
---

# Project Layout Planning

Use this skill when creating or reorganizing repository layout.

## Default Layout

Use this baseline and adapt to the project:

    project/
      README.md
      pyproject.toml
      src/<package_name>/
      tests/
      docs/
      scripts/
      data/
      deploy/

## Rules

- Keep `README.md` at the project root as the human entrypoint.
- Put importable Python under `src/<package_name>/`.
- Put tests under `tests/`; tests should import package paths.
- Put docs under `docs/`, grouped by purpose.
- Put repeatable helper commands under `scripts/`.
- Put small fixtures and sample payloads under `data/`.
- Never put secrets or production datasets under `data/`.
- Put deployment files under `deploy/<environment>/`.
- Put frontend code behind a clear boundary such as `frontend/`, `web/`, or `apps/<ui-name>/`.
- Do not create generic shared frameworks just to match a template.

## On-Prem Overlay

For on-prem Python services:

- Use `src/<project_package>/...` for all importable service code.
- Put host installers, smoke tests, offline/prestage helpers, and evidence helpers under `scripts/`.
- Put systemd units under `deploy/systemd/`.
- Keep `config.env.example` at the root when it is the operator-facing runtime contract.
- Document runtime host paths without creating repo folders for them.
- Do not commit production notables, model weights, wheelhouses, RAG indexes, generated reports, logs, secrets, or customer-specific manifests.
- When paths move, update systemd, installers, package data paths, config examples, docs, and tests together.

## Migration Checklist

1. Inventory files, imports, scripts, docs, tests, and deployment entrypoints.
2. Choose target package name and destination paths.
3. Move Python package code first and fix imports.
4. Update tests and run focused tests.
5. Move deployment assets and update path assumptions.
6. Move scripts, fixtures, and docs.
7. Update README, runbooks, examples, and commands.
8. Report remaining manual verification.

## Acceptance Criteria

Layout work is complete only when:
- imports resolve through the package
- tests run from project root
- deployment commands point at new paths
- docs and examples reference new layout
- no secrets, generated outputs, or production data are moved into tracked source