# Scoped guidance reorganization — 2026-11-04

## Published source layout

The four policy folders are global, ai-enabled-ato, ai-enabled-threathunting and
llm_notable_analysis. Existing shared packages were moved beneath global without
changing unrelated policy. Root tools and the offline UI baseline keep their own
locations. Cursor and Codex installers now select the new global source path.

Shared report/export parity, evidence-field assignment and independently deployable
frontend foundations are global. Generalizable analysis fixes reuse the existing
LLM evidence regression workflow. App runtime, field, report-display, revision,
approval and commercial/GovCloud boundaries remain project-only. Dated HTTP
observations were moved out of global references into matching app packages.

## WSL installation

Only task-owned changes were applied to the current WSL source checkout and
installed profile. The current checkout has unrelated uncommitted approved UI
changes, so this task did not repoint its global harness/skills to the isolated
publication worktree or overwrite those edits. The active checkout temporarily
retains its earlier source layout until its unrelated changes and this
reorganization are integrated through the normal Git workflow.

The existing agentic-security-workflows package was already available in WSL;
runtime discovery established that fact. The native Windows profile was not changed.
The two new managed global skills were installed, and both harnesses have the shared
security workflow available. Three app-only skills are installed locally with native
Codex project discovery links to the same Cursor package bodies.

Archived duplicate/obsolete material remains recoverable outside active discovery:
81 ATO skill package copies, 33 ATO rule copies, one obsolete notable Terraform
rule, and the old user-scoped threat-hunt-reporting package. App-specific content
was retained in the replacement local packages. Originals and hashes remain in
dated local backup directories; private backups and runtime catalog captures are
not included in this repository. Current app AGENTS files, customer/runtime data,
credentials and unrelated source changes were preserved.

Application source repositories were not committed or pushed by this task.
Their local guidance additions/removals can be reviewed separately from their
pre-existing implementation changes. This publication contains only the config
repository's guidance packages and packaging changes.

## Demonstrated verification

- 28 configuration/installer preservation tests passed.
- The scoped checker verified all four folders, 29 app package files, hashes,
  package entrypoint links, shared mirrors and absence of removed global app routes.
- Six shared/project skill entrypoints passed the official skill validator.
- An isolated fresh Codex profile installed and verified 60 managed global skills
  using the relocated source layout.
- WSL native Codex skills/list discovered all 60 managed global skills once from
  each of the three applications, with no discovery errors and no provider call.
- Each application discovered exactly its own one app-specific skill at repo scope;
  none of the other two app skills appeared in that context.
- The native Windows installer test passed in an isolated scratch destination:
  Linux-only learning was excluded, ordinary packages preserved, malformed sections
  rejected and conflicting existing work retained. No native profile was installed.
- The generated UI companion consistency check passed. No UI or baseline changes
  were made.

Broader application tests, UI exercises, live searches, model evaluations,
infrastructure mutations and production qualification remain deferred.
