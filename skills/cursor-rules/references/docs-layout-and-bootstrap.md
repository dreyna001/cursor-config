---
description: Standard docs stack and bootstrap convention
alwaysApply: false
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
- Match the purpose-based layout established in `vulnerability_management/docs` unless the user explicitly asks for a different structure.
