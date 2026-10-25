# Correctness And Testing

- Verify boundary conditions, malformed input handling, and empty or missing inputs.
- Check duplicate inputs, replay behavior, idempotency, and partial-failure behavior where relevant.
- Review timezone and date correctness anywhere timestamps or ranges matter.
- Check state transition validity, ordering assumptions, and uniqueness assumptions.
- Flag silent failure paths, swallowed exceptions, duplicate side effects, and invalid retry behavior.

# Testing

- Require happy-path, edge-case, negative-path, and regression coverage for non-trivial changes.
- Keep tests deterministic and behavior-focused.
- Avoid flaky assertions and tests tightly coupled to implementation details.
- Test names should describe behavior, not just function names.
- Behavior changes warrant tests for the happy path, representative failure modes, and regressions for parsers, validators, retries, and policy checks.
- Inject clocks, fake HTTP, stubs, or mock model calls instead of live network or real models in unit tests unless explicitly integration-scoped.
- When changing runtime contracts, update examples, operator docs, and runbooks in the same change.
- New features should include a clear verification path when non-obvious.
- Verify that required test, lint, and type checks actually run in the repository's automation when changing its delivery path. Distinguish a locally passing command from configured CI coverage; report missing production-specific validation rather than inferring it from test counts.

## Test selection and trustworthy evidence

- Start from the requirement, documented contract, or independently checked example. State the behavior a test must prove. Do not compute expected results with the same implementation/helper under test or accept generated snapshots solely because they match current output; exact snapshots and source/artifact checks remain useful for contracts that actually require them.
- Choose the smallest set of layers that exercises the changed failure boundary: unit/component tests for deterministic logic, application integration for routing/authentication/persistence/transactions, and real-browser journeys for important user-visible wiring. Do not prescribe a fixed test ratio, count, coverage percentage, or a browser test for every change.
- In integration tests, exercise the actual registered route or component and an isolated production-equivalent dependency when its semantics matter. Mock beyond the boundary being proved, not the behavior being tested. For database migrations, constraints, locking, and transaction isolation, use the production database engine; mocks or SQLite do not prove another engine's behavior. Report unavailable infrastructure and its unverified scope.
- Distinguish browser flows with mocked application APIs from journeys through the real application API and isolated persistent store. For material persistence or authorization journeys, verify the durable outcome through a fresh request/session or reload, and pair denied operations with valid authorized controls. A success message or HTTP status alone does not prove the stored result or absence of forbidden side effects. Stub paid or consequential external effects at their appropriate boundary and identify what that leaves untested.
- For defect regressions, establish failure without the correction and success with it when practical. Confirm that the failure reflects the intended behavior, not setup/collection errors. If the original state cannot safely run, state the limitation and use another meaningful control. Selective fault injection or mutation testing can probe important assertions when useful; use isolated disposable fixtures, inspect surviving/equivalent mutations, and avoid mandatory mutation infrastructure or score thresholds.
- Review changes to expectations, snapshots, skips/xfails, discovery filters, retries, and harness configuration as carefully as application changes. Do not weaken assertions, swallow failures, bypass collection, or suppress checks to obtain green results. A legitimate requirement/test correction needs an explicit reason and preserved independent controls; diagnose flaky tests instead of masking them with extra retries or sleeps.
- For consequential or unfamiliar changes, use independent requirement-based review, additional cases not copied from implementation examples, or expert review where judgment is needed. A second agent/model is useful assistance, not an independent correctness oracle by itself. Keep LLM schema/grounding/retention checks distinct from analytical quality and live-provider behavior; use the existing LLM regression guidance when applicable.
- Record the actual command, source/build or installed-artifact identity, test environment and real versus doubled dependencies, collected/executed tests, failures, skips/xfails, retries, and relevant result artifacts. Report collection errors, all-skipped runs, and unavailable checks explicitly; do not present them as successful verification. Follow the repository's local/CI policy rather than enabling automation or live services merely to satisfy a checklist.
- Keep tests that protect meaningful behavior. Consolidate or remove obsolete/redundant tests only after identifying the protected contract and showing where equivalent or stronger coverage remains. Do not remove a test solely because it is small, agent-written, or inconvenient; avoid accumulating trivial tests that mirror implementation details.
