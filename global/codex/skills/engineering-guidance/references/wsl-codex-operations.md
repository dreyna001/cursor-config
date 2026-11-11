# WSL Codex operations

Read only the section relevant to the task.

## Maintain WSL Codex configuration

The configuration repository packages separate instructions for Codex and Cursor. WSL Codex uses
global/codex/global-instructions.md through $CODEX_HOME/AGENTS.md (default ~/.codex/AGENTS.md).
Codex does not load Cursor's .mdc files. The managed Codex skills live under global/codex/skills
and install into ~/.agents/skills.

After changing WSL Codex guidance, run python3 codex/global_setup.py plan, then
python3 codex/global_setup.py sync --apply and python3 codex/global_setup.py verify --runtime.
Confirm the install plan preserves unrelated skills and instructions. Apply the WSL profile
only. Preserve the independently maintained non-Linux instructions.

## Local UI baseline

Use the app's release copy if the permanent WSL baseline is unavailable. For
installation or repair of the permanent copy, follow the versioned
[UI baseline and its Keeping one baseline procedure](../../../../../ui-baseline/README.md#keeping-one-baseline).
The local copy and app release copy are readable without GitHub sign-in.
Honor the authorized installation scope because the workstation can share the
same physical baseline between Windows and WSL.

## Codex model and subagent routing

- Use the user- or session-selected primary model and reasoning level. When no preference is set and model controls allow, prefer `gpt-6.1-sol` with `high` reasoning or `gpt-6-astra` with `high` reasoning. The primary may complete work directly, especially when the task is short or its steps depend on each other.
- Delegate concrete, independent, bounded work when parallelism, separate context, or independent review is likely to improve speed or quality. Prefer `gpt-6-luna` with `xhigh` reasoning for delegated execution when available and suitable, unless the user, session, or agent configuration selects otherwise. Coordinate shared-file edits, keep assignments bounded, and do not recursively delegate from an assigned subagent.
- After two distinct, evidence-based approaches fail, or the same blocker repeats, escalate to a capable available model or replacement worker. Include the objective, file ownership, current state, attempted approaches and errors, and useful next steps in the handoff.
- Respect the configured runtime and report model, reasoning, or subagent availability mismatches rather than silently changing the requested setup.

## AI COE checkout and cache hygiene

- Keep one checkout per product under ~/ai-coe-projects. Use worktrees only while a branch is active, then remove them.
- Put throwaway test/qualification output in a cache or tmp dir that you delete after the run, not next to the repo forever.
- Do not add a second clone under `C:\Users\Daniel.Reyna\ai-coe-projects` or `/mnt/c/Users/Daniel.Reyna/ai-coe-projects`.
- When a worktree's branch is no longer active, remove it only after the post-merge worktree cleanup checks pass.
- Keep reusable developer environments used for local testing before GPU-host work, including the on-prem CUDA/PyTorch `.venv`.

## Waiting for long-running commands

- For noninteractive commands expected to take a minute or longer, prefer blocking waits of 60-300 seconds, using 300000 ms for known multi-minute work when the tool supports it. Let completion return early.
- Respect the configured code-mode `default_exec_yield_time_ms`. Avoid overriding it with short yields for long-running work. Nested command tools have separate limits, so request their longest suitable supported wait as well.
- When a command returns a running session or cell ID, use its native wait/poll tool with a long wait. After an unchanged result, increase the wait toward 300 seconds. Avoid repeated one-second polling, short sleeps, or immediate status checks.
- Use shorter waits when interactive input, a concrete diagnostic need, a time-sensitive event, or the user's requested update cadence requires them. Honor tool limits and cancellation. A wait expiring while work remains active is a reason to continue waiting, not to restart or duplicate the command.
- During extended monitoring, report meaningful progress, completion, failures, or required user action. Avoid repetitive updates when the state is unchanged.
