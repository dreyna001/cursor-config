---
description: Conditional release workflow for projects that publish Docker images to GHCR
alwaysApply: false
---

# Docker GHCR Release Workflow

Apply this rule only when the user, project configuration, or existing release workflow requires publishing Docker images to GitHub Container Registry. Preserve another established registry or release mechanism; do not select GHCR merely because the project uses Docker.

When GHCR publishing is required:

- Treat the source revision and built container image as linked release artifacts.
- Read the existing workflow before choosing the image name, registry owner, tags, build context, or target platform.
- Never hardcode credentials or tokens in Dockerfiles, compose files, scripts, commands, or logs.
- Run the relevant tests and lint checks before publishing.
- Use the established host-aware build path. On Windows, use WSL when the repository's Linux-container workflow requires it; on Linux, build directly.
- Set `--platform` from the actual deployment target; do not assume `linux/amd64` when the target differs.
- Push an immutable version or commit-SHA tag. Add a moving tag such as `latest` only when the established release workflow requires it.
- Pull or inspect the published image and record its digest for release traceability.
- Push source changes only when the authorized release task includes the repository release.
