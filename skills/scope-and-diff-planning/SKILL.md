---
name: scope-and-diff-planning
description: Clarifies vague work into a bounded MVP block, defines acceptance criteria, identifies required integrations, and plans small testable diffs before implementation. Use before non-trivial coding, new projects, fuzzy requirements, or 2-week MVP planning.
---

# Scope And Diff Planning

Use this skill before non-trivial implementation or when scope is unclear.

## Workflow

1. Determine whether this is greenfield or a change to an existing repo.
2. Restate the use case in 1-2 sentences.
3. Identify the primary user or operator.
4. Define operational inputs and outputs.
5. Identify minimum deterministic logic.
6. Decide whether an LLM step is needed.
7. Identify required external integrations and classify each as:
   - required now
   - optional now
   - later phase
   - out of scope
8. Define in-scope, out-of-scope, assumptions, risks, and hard stops.
9. Ask only correctness-impacting questions.
10. Convert scope into functional and non-functional acceptance criteria.
11. Plan 3-6 small, independently testable diffs.
12. Stop after the plan unless the user explicitly asks to implement.

## Architecture Bias

- Keep the existing app shape unless change is necessary.
- Minimize new files.
- Extract logic only when it improves readability or testability now.
- Avoid shared cores, plugin systems, registries, profiles, bundles, or future-vendor abstractions unless there is a proven current need.
- Prefer direct solutions over generalized platforms.

## Integration Bias

- Add only integrations needed for the current block.
- Do not replace existing systems of record.
- Prefer CSV, local file input, or manual export/import as fallback when sufficient.
- Avoid deep bidirectional sync unless the workflow requires it now.

## Diff Plan Format

For each diff, include:
- objective
- files to touch
- tests to add or update
- commands to run
- acceptance criteria
- rollback or migration note

## Output

Return:
- goal
- in scope
- out of scope
- inputs
- outputs
- deterministic logic
- LLM use, if any
- required integrations
- risks and unknowns
- acceptance criteria
- 3-6 diff plan

## Preferred Outcome

High confidence before coding and small, testable, reviewable diffs.