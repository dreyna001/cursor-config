---
name: scope-and-diff-planning
description: "Plan a bounded 2-week MVP implementation block with acceptance criteria, required integrations, and small testable diffs; not for unresolved correctness/security choices or greenfield use-case framing."
---

# Scope And Diff Planning

Use this skill to plan a 2-week MVP implementation block. For unresolved correctness, compatibility, security, or safety choices, use [requirements shaping](../requirements-shaping-and-diff-planning/SKILL.md). For a greenfield use-case review that must not impose a shared architecture, use [use-case scope review](../use-case-scope-review/SKILL.md).

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
8. Define in-scope, out-of-scope, assumptions, risks, and unknowns, noting which work depends on each unresolved item.
9. Ask only correctness-impacting questions.
10. Convert scope into functional and non-functional acceptance criteria.
11. Plan the smallest independently testable diffs proportional to the task.
12. Return only the plan when the user requested planning only. Otherwise proceed once scope is clear, and continue work that does not depend on an unresolved consequential choice.

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
- proposed diffs

## Preferred Outcome

High confidence before coding and small, testable, reviewable diffs.