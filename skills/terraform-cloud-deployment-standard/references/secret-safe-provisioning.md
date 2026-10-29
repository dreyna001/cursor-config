# Secret-safe Terraform and guided setup

Apply when cloud infrastructure creates, reads, imports, rotates or consumes a
secret/private key. Preserve the application's purpose, existing services,
resource ownership and the user's execution permissions.

## Secret flow

- Draw the actual path from protected input or approved cloud secret store through
  every provider/API to its destination. Use the target cloud's native store
  (for example Key Vault or Secrets Manager), with least-privilege identities and
  the established private networking. Independently choose existing/create for
  stores, keys, secret objects and consuming resources where their lifecycles differ.
- `sensitive` is display redaction, not a storage guarantee. Ordinary secret data
  sources, resource arguments, generated passwords, local values, outputs and
  provisioner triggers can persist bytes. Encrypted state does not satisfy a
  requirement that the key never enter state.
- Inspect the actual locked provider schema and versioned implementation. Use
  ephemeral input/reads into a genuine write-only destination, or a service-native
  secret reference whose value Terraform never reads. An ephemeral source cannot
  safely feed an ordinary persisted argument. A normal Key Vault/Secrets Manager
  read does not become safe just because the original value lives in a vault.
- Trace refresh/readback as well as writes: a second resource or data source must
  not read the secret back into state. Check provider-private payloads, default API
  exports, imported state, error responses and debug logs. Restrict exports to
  explicit nonsecret fields, disable secret-bearing diagnostics, and capture or
  sanitize provider/subprocess errors before recording or displaying them.
- Use documented nonsecret revision controls for intentional secret updates when
  needed. Verify whether the provider stores secret-derived private hashes;
  select version-based handling when zero secret-derived state is required.
  Do not use an ephemeral value to derive an ordinary revision or persisted output.
- Protect source files, stdin/environment and temporary files. No raw key/password
  in collected configuration, tfvars, argv, images, review artifacts, receipts or
  checkpoints. Use protected file references and in-memory transfer where practical;
  remove owned temporary secret copies on success/failure, preserve customer-owned
  originals and durable store values. Treat environment variables as secret-bearing
  input, not as proof of nonpersistence.
- Before declaring creation unsupported, check authoritative pinned-provider
  capabilities and appropriate native Terraform alternatives. Adding a focused
  provider for a missing secure API can be justified; qualify its Government
  endpoints, authentication, API version and lifecycle. Do not broadly upgrade
  providers, add unrelated services or bypass Terraform with scripts/provisioners.
  If no qualified path exists, block unsafe creation and document the limitation.

## Ordering, ownership and recovery

- Collect ownership choices and protected references once. Derive service IDs,
  secret URIs and backend settings; do not ask the customer to re-enter generated
  values. Automate the supported cloud steps through the documented Terraform
  roots, while keeping identity consent, agency-side networking, PKI issuance and
  other external approvals with their actual owners. Certificate import/storage
  is distinct from certificate issuance, trust and renewal.
- Order foundational storage/network/roles before secret publication and consumers.
  A new private dependency must be reachable from the approved deployment runner;
  do not introduce public access as a bootstrap shortcut.
- Persist a generated/issued key to its approved store before retryable consumers
  depend on it. Read the exact persisted version on recovery. Do not regenerate a
  password on retry when the store already contains the prior successful value.
- Reference existing objects read-only; create mode must not silently overwrite
  an occupied secret/certificate name or adopt a shared resource/policy. Keep one
  Terraform owner per resource. Existing state/address/identity transitions and
  historical key-bearing snapshots need an explicitly reviewed migration.
- Default to plan; apply the exact reviewed saved plan, bound to configuration,
  state target, source material and artifact identities. If secret material affects
  a review, use protected keyed bindings where appropriate, not public password
  hashes. Rebind a changed file/version to a fresh review.
- Separate durable recovery metadata from disposable review files. Unknown write
  outcomes stop for inspection; retry only with evidence of the actual store/state
  outcome and safe replay. Reuse an already completed matching version rather than
  overwrite it or duplicate the operation. Never clear state/checkpoints to get
  past a failure. Do not add redundant approval gates for a choice already collected
  and approved in the same authorized setup session.

## Qualification and handoff

- Exercise existing/create and mixed ownership, compatible references, collisions,
  invalid scope, stale inputs, no-op refresh, deliberate rotation and partial failure
  followed by recovery. Preserve neighboring supported behavior and execution guards.
- For a new secret-handling bridge, use the actual pinned provider against a local
  service double when feasible. Verify the service received the synthetic canary
  key and inspect binary saved-plan archives and decoded members, plan JSON,
  current/backup state including decoded provider-private state, generated files,
  outputs and logs for raw/escaped/encoded secret material. Schema assertions,
  mocked providers and UI redaction alone do not establish the boundary. Include
  error responses that echo the canary and confirm the supported runner suppresses
  or sanitizes them without losing failure/recovery status.
- Run relevant formatting, backend-disabled initialization, validation, contract
  tests and the established pinned security scanner. Reuse installed tools/caches,
  serialize shared provider-cache initialization and retain lockfile validation.
  Respect local-only/no-GitHub-Actions constraints; never manufacture cloud or CI
  success. Local doubles cannot prove subscription/region availability, private
  routing, RBAC propagation, peer-device settings or a live tunnel.
- Keep one README-first operator journey, field references and recovery/rotation
  guidance aligned. Record what is automated, what remains external, exact checks,
  scanner exceptions and unverified live acceptance. Passing local tests grants
  no deployment or migration permission.
