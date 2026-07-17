---
name: requirements-shaping-and-diff-planning
description: Shape fuzzy requirements into scoped acceptance criteria and small testable implementation diffs.
---

# Requirements Shaping And Diff Planning

Use this skill before coding on non-trivial work.

## Quick Start

Follow this sequence:

1. Determine whether the work is **greenfield** or a **change to an existing repo**.
2. Collect only the environment pins that affect correctness and are still unknown.
3. Restate the use case in 1-2 sentences.
4. Produce a scope contract with:
   - in-scope
   - out-of-scope
   - assumptions
   - risks and unknowns
5. Ask targeted edge and corner questions before implementation.
6. Convert the answers into functional and non-functional acceptance criteria.
7. Maintain an unknowns or hard-stops list.
8. Plan 3-6 small, independently testable diffs.
9. Stop after the plan and wait for approval before coding diff 1.

## Architecture Level

When planning changes to an existing app, default to the current direct modular style:

- keep the existing app shape and workflow clear
- minimize the number of new files
- extract logic only when it improves readability or testability now
- keep `main.py` or the entrypoint focused on orchestration: config, loop startup, processing-step calls, shutdown, and top-level errors
- for frontend served by a backend, keep backend routes/controllers focused on request handling and response shaping; keep frontend routes/pages focused on UI orchestration, data loading, and passing state to simple components
- keep detailed work in simple helper modules or functions: input parsing, LLM calls, validation, rendering, file movement, external calls, and tests
- keep detailed frontend work in small components or helpers: form handling, display formatting, client API calls, validation, and focused tests
- add a new file only when an existing module would become harder to read; otherwise add a small function to the existing module
- avoid profiles, bundles, registries, shared cores, generic adapters, plugin systems, and future-vendor abstractions unless there is a proven current need

## Environment Pins

At minimum, collect what is not already inferable:

- target runtime environment
- language or runtime version
- OS, base image, or architecture when relevant
- constraints such as network, writable filesystem, timeouts, memory, and secrets handling

## Edge And Corner Questions

Focus questions on:

- inputs and outputs, including data contracts and sample payloads
- error taxonomy, retry, backoff, and idempotency
- concurrency model and timeout boundaries
- logging, observability, and redaction needs
- performance limits and expected volume
- security boundaries and least privilege
- backward compatibility expectations for existing code

Ask only what is needed to remove correctness-impacting ambiguity.

## Acceptance Criteria

Define:

- functional requirements with pass or fail checks
- non-functional requirements with pass or fail checks

Do not start implementation until success can be evaluated concretely.

## Hard Stops

Stop and ask before coding if:

- an unknown could change correctness
- an unknown could change compatibility
- an unknown could change security or safety posture
- the environment assumptions are still unclear

## Diff Plan Format

For each planned diff, include:

- objective
- exact files to touch
- tests to add or update
- commands to run
- acceptance criteria
- rollback or migration note if behavior or contracts change

## Execution Loop

- Do not code until the plan is approved.
- Implement one diff at a time.
- Touch only the listed files unless the user approves a plan change.
- Add or update deterministic tests for each diff.
- Run the planned verification commands.
- Report pass or fail results briefly.
- Ask permission before moving to the next diff.

## Default Dependency Posture

- Prefer the standard library and existing dependencies.
- Do not add new third-party packages without approval.

## Preferred Outcome

Aim for **high confidence before coding** and **small, testable, reviewable diffs** during implementation.
