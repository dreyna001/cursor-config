# ai-enabled-ato project-only guidance

This folder contains only guidance for `ai-enabled-ato`. It is a versioned distribution
package, not a global installation and not an application checkout. Current
instructions and normative documents in the matching app repository take
precedence over the packaged snapshots. Check source revisions and hashes in
`source-manifest.json` before using historical detail.

## Install into the matching project

Review a diff against that project's existing `.cursor/` files, then copy this
folder's `rules/` to `<ai-enabled-ato>/.cursor/rules/` and its `skills/` to
`<ai-enabled-ato>/.cursor/skills/`. Copy complete skill directories, including references.
Preserve unrelated project instructions and newer approved safeguards. Never
install this package into a user-wide Cursor/Codex skill root or another app.
Installation is manual; the global installer does not deploy app packages.

These project rules and skills route reusable behavior to the installed global
guidance rather than carrying copies of ordinary engineering, security, ML,
Terraform, model routing or review skills. Global guidance lives under `global/`
in this configuration repository. Install the relevant global harness before
using these project routes. App safeguards and deployment boundaries stay local.

`skills/ato-ssp-workflow/references/repository-agents.md` is the full source
`AGENTS.md` snapshot for comparison. Do not install that snapshot over the app's
current `AGENTS.md`; its relative links resolve in the original app repository.
Other packaged references retain product-specific contracts or explicitly dated
source reviews. They do not grant execution, deployment, publication, model-call
or additional verification authority.
