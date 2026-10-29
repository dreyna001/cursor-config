Work in: <PROJECT_PATH>

Audit and implement the existing Terraform deployment so a customer can complete
one guided setup with independently selected existing/new dependencies. Apply
engineering-guidance, terraform-cloud-deployment-standard and its secret-safe
provisioning reference, plus operator-documentation-journey. Preserve this app's
purpose, existing cloud stack, security boundaries and supported features.

- Use the documented Terraform root(s) for all infrastructure. No provisioning
  scripts, provisioners, alternate IaC or console-only setup paths.
- Inventory required dependencies and support explicit create/reference choices
  independently wherever their lifecycles differ, including secret stores, keys,
  secret objects and consuming services. Test mixed choices. Never silently adopt,
  overwrite, replace or take over an existing resource or shared policy.
- Collect nonsecret settings and protected secret references once; derive generated
  IDs/URIs and pass them between ordered foundation, permission, artifact, secret
  and application stages. Keep external identity/PKI/agency approvals with their
  owners, clearly distinguished from cloud steps Terraform can automate.
- Keep keys/passwords in the appropriate cloud secret store and out of Terraform
  plans, current/backup/provider-private state, outputs and logs. Sensitive is only
  redaction. Verify actual pinned ephemeral/write-only or service-reference support,
  including refresh/readback, API exports and error handling. Qualify a focused
  native Terraform provider alternative before declaring secure creation unsupported;
  block unsafe paths when no qualified solution exists.
- Protect original input files; avoid persistent secret copies or secret argv.
  Use exact secret versions and deliberate nonsecret rotation revisions. Recovery
  must reuse completed matching values, not regenerate or overwrite them.
- Default to plan and apply only the reviewed saved plan bound to the exact
  customer/configuration/state/source. Preserve durable receipts, idempotency and
  evidence-backed recovery after partial or uncertain writes. Changed inputs need
  fresh review; never clear checkpoints or weaken guards to continue.
- Reuse installed pinned tools/provider caches and lockfiles; serialize shared-cache
  initialization. Run local format/validate/contracts/security checks and meaningful
  existing/create/mixed/failure/refresh/rotation/recovery regressions. For new secret
  bridges, exercise the actual provider against local synthetic APIs and inspect
  saved plan archives, state including private payloads, files and logs for canary
  secrets. Include API errors that echo the canary. Distinguish simulated results
  from live regional availability, networking, identity and tunnel acceptance.
- Consolidate docs into one README-first journey with a field reference and clear
  recovery/renewal guidance. List exactly what is automated, what remains external,
  and any supported-platform exceptions. Update the existing TODO in place.

No GitHub Actions work or customer deployment. Do not change existing deployed
resources or historical state without a separately scoped migration. Run local
checks, commit and merge the authorized implementation to remote main, then verify
main is synced and the checkout is clean; clean up only eligible task worktrees.
Report the material changes, actual checks and remaining limitations.
