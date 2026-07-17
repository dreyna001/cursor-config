---
description: Use for Docker, compose, GHCR, GitHub Actions, deployment images, and release workflow changes
globs: "Dockerfile,**/Dockerfile,**/docker-compose*.yml,**/compose*.yml,deploy/docker/**,.github/workflows/**"
alwaysApply: false
---

# Docker And Release Rules

## Release Artifacts

When a task touches a Docker deployment project, treat releases as two required artifacts:

1. Source code pushed to GitHub.
2. Built container image pushed to GHCR.

## Docker Standards

- Never hardcode credentials, tokens, or secrets in Dockerfiles, compose files, scripts, logs, or image layers.
- Use minimal runtime images where practical.
- Separate build and runtime stages when useful.
- Run containers as non-root where supported.
- Avoid unnecessary layers and copied files.
- Keep deployment/runtime contract values synchronized across code, compose/systemd, examples, and docs.

## Build Workflow

- Run relevant tests/lint checks before publishing images.
- Build location is host-aware:
  - Windows host: build from WSL.
  - Linux host: build directly on Linux.
- Use explicit target platform for deployment parity:

```bash
docker buildx build --platform linux/amd64 -t ghcr.io/<owner>/<image>:<tag> <context>
```

## Image Tags

- Push immutable tags using version or commit SHA.
- Moving tags such as `latest` are optional and must not be the only release reference.
- Verify pushed artifacts after publish:

```bash
docker pull ghcr.io/<owner>/<image>:<tag>
```

- Capture image digest for release notes or traceability.

## Deployment Validation

- Validate health checks.
- Validate startup behavior.
- Validate dependency connectivity.
- Validate rollback readiness.
- Fail deployment on critical validation errors.