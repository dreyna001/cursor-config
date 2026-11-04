# Operator runbook

Start at README Path A (current project-root `README.md#path-a--customer-default`) for configuration,
image builds and startup. This guide owns acceptance, recovery and rollback;
customer-default profile (current project-root `docs/customer-default-profile.md`) owns required settings.
New production hunts use `pydantic-ai-v1` and `direct`. LangGraph stays parked;
MCP cutover requires separate approval and qualification. Preserve saved engine,
backend and configuration bindings. API/worker startup never migrates schemas.

## Prepare and start

Follow Path A with immutable, matching images, protected secret files and a
customer-owned runtime YAML. The database URL must use Compose service `postgres`.
Generate `runtime/security.env` with the security exporter (current project-root `docs/production-security.md#configure-the-policy-source`);
pass it after `.env` in every production Compose command. Stop on placeholders,
invalid configuration or failed migrations. Ordinary startup excludes MCP.

```bash
docker compose --env-file .env --env-file runtime/security.env -f deploy/docker/compose.yml config
docker compose --env-file .env --env-file runtime/security.env -f deploy/docker/compose.yml build
docker compose --env-file .env --env-file runtime/security.env -f deploy/docker/compose.yml up -d
```

## Validate

```bash
curl --fail http://127.0.0.1:${THREAT_HUNTING_FRONTEND_PORT:-8080}/health/live
curl --fail http://127.0.0.1:${THREAT_HUNTING_FRONTEND_PORT:-8080}/health/ready
docker compose --env-file .env --env-file runtime/security.env -f deploy/docker/compose.yml ps
docker compose --env-file .env --env-file runtime/security.env -f deploy/docker/compose.yml logs --no-log-prefix --tail=100 migrate backend worker frontend
```

Require successful liveness/readiness, passing database/migration/storage/config
checks, a successful migration job, and the intended immutable release throughout.
Only the frontend publishes a browser port; keep PostgreSQL/API/worker private.
Verify approved HTTPS ingress, public origin and exact app/edge proxy ranges using
production security (current project-root `docs/production-security.md`). Liveness alone never admits work.

## Approved synthetic smoke

With written non-production pilot approval, use synthetic data only:

1. Confirm approved Splunk URL, namespace, indexes, time window, TLS chain and
   least-privilege account; verify the secret-mounted, qualified structured-output
   model. External providers require `model.data_boundary: external` and
   `execution.provider_data_handling_approval_ref`.
2. Sign in, create a hunt, discover scope, review and explicitly approve its exact
   plan, then execute. Confirm only approved bounded searches in the query ledger.
3. Exercise cancellation and explicit budget/timeout failures. Review cited
   findings and finalize the PDF.

```bash
.venv/bin/python scripts/run_known_answer_hunts.py --mode synthetic --json
```

This scorer checks deterministic contracts, not live model quality. Use the
isolated testing guide (current project-root `tests/README.md#isolated-real-service-qualification`)
for separately approved real-service qualification.

## Accept customer data

Record passing configuration/hard-stop review, deployment validation and synthetic
smoke; exact images, schema, runtime, provider/model, policy/prompt versions,
Splunk scope and run IDs; analyst acceptance of plan, queries, limits, evidence,
findings, PDF and audit trail; security acceptance of HTTPS, least privilege,
owner isolation, storage, backup, retention and provider handling; and compatible
rollback images/backups. Any safety failure blocks admission. Assistant review
never replaces independent analyst acceptance.

## Admission control, worker health, and recovery

Set `execution.admit_new_work: false` and restart **every API instance**, coordinating
ingress and draining discovery/planning. This stops discovery, rediscovery and new
execution admission; existing approved jobs may finish. Inspect queued, running,
expired, resumable and quarantined work before stopping writers, upgrading or
backing up; zero active leases is insufficient. Reopen only after API/worker
schema and configuration compatibility passes. Engine selection is separate.

| Runtime contract | Operator meaning |
| --- | --- |
| Worker heartbeat ≤45 seconds old, tied to process identity | Proves liveness, not analytical or provider progress; readiness also checks dependencies/application head and, for graph, checkpoint schema |
| Five DB connections per process, no overflow | One API + two workers use at most 15; reserve administrative/health headroom. API readiness reuses its pool |
| Lock timeout 10 s; statement timeout 30 s, including saver connections | Preserve these bounds; after client death, wait for database abort and verify rollback |
| SIGTERM stops claims, cancels active lease token and drains with renewals/liveness | Interrupted handlers cannot complete successfully; forced death leaves durable actions for recovery, not proof of no external submission |
| Shutdown grace = largest model/search/transport timeout +30 s | Match `THREAT_HUNTING_WORKER_SHUTDOWN_GRACE_SECONDS` and Compose `stop_grace_period`; shipped default 330 s |

`GET /api/hunts/{hunt_id}/recovery` is owner-authorized, sanitized and audited;
ordinary polling is read-only. Owner/CSRF-protected
`POST /api/hunts/{hunt_id}/recovery/resume` revalidates plan, approval and immutable
binding. It preserves job identity, generations, original deadline, artifacts and
usage. Three infrastructure lease expiries stop automatic requeue; eligible resume
resets that counter, not the lifetime audit. It never replenishes budgets, resolves
unknown provider responses or replaces expired SIDs with a new population.

| Recovery case | Required handling |
| --- | --- |
| New graph submit loses SID acknowledgement | Read-only lookup of deterministic job ID; adopt only matching SPL, time bounds, authenticated owner/app and atomic current-generation fence. Missing/inaccessible/mismatched/incomplete metadata stays unknown with its grant held; never resubmit. Historical unknowns without the contract remain held |
| Graph submit time lost | Retain unknown timestamp/latency; use immutable admission time as conservative timeout anchor. Expiration may be early and does not prove Splunk stopped |
| Non-graph known SID | Validate saved bounded submission contract before reads. Historical SID/time-only records resume that SID without inventing sentinel SPL/caps; `eventIsTruncated` still reports incomplete storage. Partial/malformed/query-mismatched contracts fail before connector access |
| Legacy pre-acknowledgement crash | Lookup deterministic ID, reuse visible job, create same ID on miss; miss behavior is **not qualified exactly-once**. Lost submit time starts per-query timeout at recovery, capped by original hunt deadline; saved times stay intact. Do not replay historical unknown model outcomes |
| `execution_configuration_incompatible` | No model/search/graph dispatch. Stop incompatible workers, retain approved pinned runtime, inspect/resume through current API, then start only compatible workers. Resume requeues without certifying compatibility; incompatible claimants quarantine again. Before rolling back to an API lacking this disposition, resume through current API first |
| Pre-initialization failure, including missing checkpoint schema/invalid approval | `graph_initialization_failure` is terminal while the captured lease/state/artifact revision owns the active hunt. Preserve cancellation, newer artifacts and draft/final reports. No in-place resume; repair future admission and reconcile unknown outcomes before any separately approved replacement hunt |
| Unexpected graph interrupt | No analyst-pause feature exists. Quarantine with checkpoint/action history; generic resume is unavailable. Inspect, cancel or apply compatible forward repair |
| Finalized report in infrastructure quarantine | Recover only with verified exact accepted durable report origin; preserve analyst edits, version and PDF. Tampered origin blocks recovery |

Never edit job markers, approvals, checkpoints, artifact revisions, usage or actions
to force recovery. Quarantine/resume history survives marker clearing. Queue events
(enqueue, claim/wait, capacity deferral/retry, lease recovery, quarantine, resume,
completion, cancellation) commit atomically to `audit_records`; audit failure rolls
back transitions. Do not invent missing historical timings. Public views omit worker
identities/arbitrary metadata; retain protected records with the recovery set.

Graph composition policy `accepted_answer_report_projection_v7` changes action
identity/request hashes: older in-flight work must finish/reconcile on its original
runtime. Never refresh a stale checkpoint CAS cursor to admit a different request.
Execution metrics include planning in total charged calls/tokens; phase totals are
included breakdowns. Query counts describe native ledger entries, not unique queries
or every attempt. Missing/unknown legacy or graph failed/deferred/pending totals stay
null; preserve ledgers when reconciling accounting.

Rejected structured responses retain protected hash/type diagnostics capped at
12 KiB, bound to native request/response attempts. They distinguish validator
candidates from diagnostic serialized data, use canonical ASCII JSON and mark
truncation/omissions; no raw claims/responses enter logs or model context. Predictable
hashes remain guessable. Diagnostics establish neither truth nor replay authority.
`observed_value` accepts a complete typed scalar from a literal row/parsed `_raw`
field (dots are literal); nested/array/serialized-member extraction is invalid.
Whole serialized strings/counts do not establish event relationships. Obtain
approved source-bound evidence or state the limitation. One repair retains original
context/response and labeled mismatches; identical validators apply, with a second
rejection explicit. These rules do not change reasoning or allowances.

## Database baseline and upgrades

The baseline is `0037_saved_hunt_qa`, followed by unchanged additive
`0038_mcp_discovery_grants`. Fresh installations run the explicit migration job;
existing `0037` applies only `0038`; current databases are unchanged.
For older revisions, close admission, drain/reconcile and back up. Using release
`8b06c668fd4eef974ee2daef9bbbed2e7f759fbc` and protected database configuration,
run `python -m alembic upgrade 0037_saved_hunt_qa`, then the new release's migration
job to `head`. Older/nonempty unversioned schemas fail closed: never stamp,
reset or drop data. The baseline cannot downgrade; MCP retains its live-grant
rollback guard. Source integration does not migrate a running installation.

Graph checkpoint setup is separate administrative DDL, only after matching app
migrations and while graph writers are stopped. Its protected
`THREAT_HUNTING_DATABASE_URL_FILE` input is never printed; output is bounded JSON.
`check` is read-only. Run check/setup/check before any approved graph activation:

```bash
docker compose --env-file .env --env-file runtime/security.env -f deploy/docker/compose.yml run --rm --no-deps backend \
  python -m threat_hunting.checkpoint_admin check
docker compose --env-file .env --env-file runtime/security.env -f deploy/docker/compose.yml run --rm --no-deps backend \
  python -m threat_hunting.checkpoint_admin setup
docker compose --env-file .env --env-file runtime/security.env -f deploy/docker/compose.yml run --rm --no-deps backend \
  python -m threat_hunting.checkpoint_admin check
```

Equivalent entry point: `threat-hunting-checkpoint-db {check|setup}`. Optional
`--schema NAME` must match the application schema.

## Local account administrator role

After migrations, use audited account commands with an explicit operator ID:

```bash
docker compose --env-file .env --env-file runtime/security.env -f deploy/docker/compose.yml run --rm --no-deps backend \
  threat-hunting-account analyst --create-admin --operator-id 'approved-operator-id'
```

For existing accounts substitute `--grant-admin` or `--revoke-admin`.
`--create-admin` prompts for the password; never supply passwords as arguments.
The stored role gates runtime hunt-limit settings on every request, including
existing sessions. Headers/bodies cannot grant it; login and `/api/auth/me` only
expose `is_admin`. Scheduling stays disabled unless explicitly configured;
direct Entra collection is removed.

## Optional app-owned MCP

Default remains `direct`; source integration is not cutover approval. Official
Splunk MCP requires an approved package download, compatible installed app and
qualification of version, schemas, permissions, durable submit/SID, paging,
cancellation and recovery. Until then it is unavailable with no silent fallback.
A local Splunk lab can host it; app-owned MCP needs no vendor app.

1. Review matching immutable API/worker/MCP images, backups and schema compatibility;
   apply `0038` only through the separately approved migration job. The local app
   database was not migrated by source integration.
2. In the operator runtime copy, preserve model/reasoning/budgets/engine/approvals.
   Set `execution.mode: mcp`, `mcp_backend: app_owned`, stable `mcp_connection_id`,
   exact Splunk principal `mcp_upstream_identity`, approved HTTPS `mcp_url`, and
   exact certificate CN `mcp_service_subject`. Set absolute `mcp_ca_bundle_path`,
   `mcp_client_cert_path`, `mcp_client_key_path`, `mcp_server_cert_path` and
   `mcp_server_key_path` references; never put secret bytes in configuration/logs.
3. Use separate client/server private keys. MCP mounts server key/cert, CA, subject
   and Splunk token; API/worker mount client key/cert and CA. Verify server hostname
   and reject absent, untrusted or wrong-subject clients.
4. Close admission and drain/reconcile direct jobs. Compose ≥2.24.4 is required
   for the override that replaces API/worker mounts and removes direct tokens:

   ```bash
   docker compose --env-file .env --env-file runtime/security.env -f deploy/docker/compose.yml -f deploy/docker/compose.mcp.yml --profile mcp config --quiet
   ```

5. Use the same files/profile for deployment and validation. Test private reachability,
   tool schemas, certificate denials, owner/connection/lease checks, complete paging,
   uncertain-submit recovery and approved synthetic hunt/export. Monitoring only
   checks protocol/upstream identity, not search readiness. Paid model calls require
   separate authorization. Verify network denial of direct API/worker-to-Splunk access
   while preserving MCP/model access; the override alone does not prove this.

Endpoint, identity, namespace, protocol or CA changes invalidate fingerprints and
require reapproval. Never redirect approved/in-flight jobs. Retain their backend
through rollback and hold unresolved work. Unavailable deployment checks remain open.

Local integration uses scripted models, synthetic Splunk and a disposable database
named with suffix `_test`; provide protected restricted-user session/DB files:

```bash
THREAT_HUNTING_LOCAL_SPLUNK_MCP=1 \
THREAT_HUNTING_TEST_DATABASE_URL_FILE=/protected/disposable-database-url \
THREAT_HUNTING_SPLUNK_TOKEN_FILE=/protected/restricted-test-session \
.venv/bin/python -m pytest -q tests/integration/test_local_splunk_mcp.py
```

Remove test DB/session/keys afterward; retain sanitized results. Never target the
application DB or replace its credential. For missing WSL Docker integration,
refresh Ubuntu off/apply/on/apply (may interrupt services), then check `docker version`
and `docker ps -a` in a fresh terminal. Inspect existing stopped containers/volumes;
never reset Docker, prune volumes or reinitialize Splunk. Splunkbase needs login;
blocked Azure downloads need approved proxy/firewall access including auth/download
redirects, or an approved package transfer.

## Monitor, backup and rollback

Monitor readiness/restarts/migration exit, DB connectivity/free space, leases,
queued/failed jobs, retention cleanup, hunt/query/model counts, budgets, timeouts,
retries and cancellations. Review login/SPL rejection, approval, execution,
cancellation and finalization audits. Exclude secrets, cookies, CSRF, authorization,
upload contents and unnecessary event payloads from logs.

With admission closed and writers stopped, back up the **whole database** consistently:
workflow/jobs/audits, model usage accounts/attempts/decisions/seeds, graph
executions/actions/artifacts, checkpoints/blobs/writes/migrations; include external
artifacts and exact image/config references. Restore cannot prove later remote work
never happened. Reconcile uncertain provider calls/SIDs before reopening admission.

Rollback preserves volumes and accounting; use a schema-compatible qualified image
or repair forward, then validate again. Fencing, recovery, deletion or admission
history can prohibit downgrade. Never erase paid/reserved attempts or rewrite
approvals for compatibility. An image requiring `0013` cannot recover a `0014`
usage-ledger database; post-backup dispatches also require reconciliation. Every
schema-changing release needs its own compatibility/recovery path. Synthetic
qualification tools are not production restore commands.

## Stop versus teardown

```bash
docker compose --env-file .env --env-file runtime/security.env -f deploy/docker/compose.yml down
```

This preserves named volumes. `docker compose down -v` destroys persistent data:
it is teardown, not rollback, and requires explicit destructive-data approval.

## Next

Continue monitoring the accepted release. Use isolated qualification (current project-root `tests/README.md#isolated-real-service-qualification`)
only on separately approved lab stacks.
