---
name: pr-readiness
description: "Prepare an existing PR for merge by addressing actionable feedback, conflicts, or authorized CI failures."
---
# Pull Request Readiness

Use this workflow when asked to make a pull request ready for review or merge. Inspect the current branch, base and open review feedback. Use local verification by default. Inspect or troubleshoot GitHub Actions only when the user explicitly requests GitHub Actions work, as required by the global instructions. Do not assume a particular Git host, command, agent mode, or review bot.

1. **Conflicts:** inspect the conflict and both sides' intent. Resolve only when the intended behavior is clear; otherwise leave the conflict intact and report the decision needed. Do not merge or rebase another branch without authorization.
2. **Review feedback:** read unresolved actionable comments and the smallest necessary surrounding context. Check the reported behavior against the code and tests before changing anything. If a GitHub integration or CLI is unavailable, ask the user to provide the relevant comment or report that limitation.
3. **CI:** for authorized CI work, fix failures caused by this branch and within its scope. Do not weaken checks or make unrelated changes to turn a red run green. For unrelated failures, report evidence and whether the branch is behind its base.
4. **Verification:** run the relevant tests and checks; distinguish what passed, failed, was skipped, or could not be inspected.
5. **Handoff:** summarize remaining comments, conflicts, CI state, and changes made. Do not post comments, mark threads resolved, push, or merge unless the user explicitly authorized that action.
