---
name: requirements-shaping-and-diff-planning
description: "Shape fuzzy requirements into scoped acceptance criteria and small testable implementation diffs."
---
# Requirements Shaping And Diff Planning

Use this skill when requirements are fuzzy, the user requests a plan, or unresolved choices could materially affect correctness, compatibility, security, or safety. Do not invoke it merely because a well-scoped task is non-trivial.

## Quick Start

Shape only the parts of the task that remain unclear:

1. Determine whether the work is **greenfield** or a **change to an existing repo**.
2. Collect only the environment pins that affect correctness and are still unknown.
3. Restate the use case in 1-2 sentences.
4. Produce a scope contract with:
   - in-scope
   - out-of-scope
   - assumptions
   - risks and unknowns
5. Ask targeted questions only for unresolved decisions that could materially change the result.
6. Convert the answers into functional and non-functional acceptance criteria.
7. Maintain an unknowns and decisions list, noting which work depends on each unresolved item.
8. Plan the smallest independently testable diff or sequence of diffs proportional to the task.

## Use-Case Boundaries

- Identify the primary user or operator and the operational inputs and outputs.
- Define the minimum deterministic logic and decide whether an LLM step is needed.
- Classify integrations as required now, optional now, later, or out of scope.
- Prefer file-based or manual import/export when it meets the current need; avoid deep bidirectional sync without a present requirement.
- Keep the existing system of record unless changing it is required for the current block.

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

Define pass/fail criteria for correctness-impacting behavior before implementing that behavior. Surface unresolved decisions and continue work that does not depend on them.

## Diff Plan

For each necessary diff, identify:

- objective
- exact files to touch
- tests to add or update
- commands to run
- acceptance criteria
- rollback or migration note if behavior or contracts change

When returning a plan, summarize the goal and scope, user or operator, inputs and outputs, deterministic and LLM responsibilities, integration priority, risks and unknowns, acceptance criteria, and proposed diffs.

## Planning Boundary

- Return only the plan when the user requested planning only. Otherwise, proceed with the authorized task once its scope is clear.
- If a consequential choice blocks part of the work, ask about that choice and continue independent work.
- Do not request approval between ordinary implementation increments.
- Ask only when a scope expansion or consequential external change is not already authorized, or when a materially different product, architecture, security, or compatibility outcome remains undecided.
- Keep implementation aligned with the plan, but adjust locally when evidence shows a smaller correct path.

## Default Dependency Posture

- Prefer the standard library and existing dependencies.
- Add a third-party package only when the current task requires it and existing mechanisms are insufficient; explain the need.

## Preferred Outcome

Aim for **high confidence before coding** and **small, testable, reviewable diffs** during implementation.
