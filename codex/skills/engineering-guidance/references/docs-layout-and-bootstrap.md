---
description: Standard docs stack and bootstrap convention
alwaysApply: false
globs: "**/README.md,**/docs/**/*.md"
---

# Docs Stack Convention

- Default new projects and major subprojects to a `docs/` tree organized by purpose:
  - `delivery_package/`
  - `architecture/`
  - `technical_specs/`
  - `prompts/`
  - `planning/`
  - `internal/`
- Use `docs/README.md` as the navigation index for that tree.
- Default the first planning stack to:
  - `planning/domain_capability_map.md`
  - `planning/implementation_tracker.md`
  - `architecture/core_deployment_architecture.md`
  - `technical_specs/core_technical_spec.md`
- When bootstrapping a docs stack, create missing directories and seed missing template files only.
- Never overwrite an existing docs stack just to match the template.
- Preserve an established repository documentation structure. Use this purpose-based layout only when no valid structure exists or the task explicitly requests it.

# Operator journey (deployable products)

- Root `README.md` owns the full Path A/B/C deploy order, approval gate, validation terminus, and rollback vs teardown.
- `docs/README.md` is a topic index only; do not duplicate path tables or long warnings from the root README.
- Each runbook: one responsibility, 1-2 sentence purpose at the top, concise `## Next` when it belongs to a path.
- One canonical owner per topic; link elsewhere instead of repeating commands or checklists.
- For a full documentation pass, use skill `operator-documentation-journey`.
