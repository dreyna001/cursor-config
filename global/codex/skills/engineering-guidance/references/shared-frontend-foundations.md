# Shared Frontend Foundations

Apply when multiple applications share frontend foundations, not to unrelated
projects merely using the same framework. Read each app's current contracts and
the suite's maintained baseline where one exists.

- Share stable primitives, tokens and semantic contracts when useful; keep domain
  workflows, approval/review gates, terminology exceptions and data adapters local.
- Every app must build and deploy independently. Do not require another app's
  checkout, runtime, credentials or live services to build the affected product.
- Treat the current foundation as a reviewed default, not proof of optimality.
  Compare alternatives against the actual requirements, maintenance and deployment
  costs; record evidence and intentional domain differences.
- Preserve newer approved behavior and styling, accessible primitives, editing
  guards and export contracts. A shared refactor does not authorize a redesign or
  a rollout outside the requested apps.
- Verify affected builds and rendered workflows within scope. Source parity alone
  does not establish interaction, accessibility or live-deployment correctness.
  Follow a suite's established synchronization procedure for approved shared changes.
