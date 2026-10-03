---
name: security-best-practices
description: "Apply version-aware security guidance for Python, JavaScript, TypeScript, and Go; use focused review skills for audits."
---
# Security Best Practices

Identify the languages, frameworks, installed versions, and security-sensitive boundaries in the requested scope. Read only the matching general and framework references from `references/`.

This entrypoint controls scope and version handling when a copied reference uses broader or version-pinned wording.

## Version And Source Discipline

- Treat reference version labels as snapshots, not project requirements.
- Check manifests, lockfiles, and installed versions before applying framework-specific advice.
- Verify version-sensitive APIs and defaults in authoritative documentation or source for the installed version.
- Follow valid repository patterns and explicit project requirements; do not upgrade, replace, or add dependencies merely to match a reference.
- If the reference conflicts with current authoritative guidance, follow the authoritative source and state the difference when material.

## Application

- For implementation, apply secure defaults only to the code and configuration in scope.
- For ordinary work, flag only clear, high-impact issues in touched or directly adjacent code; do not turn the task into an unsolicited audit.
- For a requested audit, use the focused [security review](../review-security/SKILL.md) or [Python security review](../python-security-review/SKILL.md) skill and use these references as framework-specific support.
- Findings must cite concrete evidence and distinguish confirmed vulnerabilities from controls that may exist outside the inspected boundary.
- Fix root causes with the smallest correct change. Do not disable protections, broaden trust, or add speculative security infrastructure.
- Preserve behavior unless a security requirement explicitly requires a breaking change; verify the relevant regression and security behavior.

## Reference Routing

- Go backend: [golang-general-backend-security.md](references/golang-general-backend-security.md)
- General browser JavaScript or TypeScript: [javascript-general-web-frontend-security.md](references/javascript-general-web-frontend-security.md)
- Express: [javascript-express-web-server-security.md](references/javascript-express-web-server-security.md)
- React: [javascript-typescript-react-web-frontend-security.md](references/javascript-typescript-react-web-frontend-security.md)
- Next.js: [javascript-typescript-nextjs-web-server-security.md](references/javascript-typescript-nextjs-web-server-security.md)
- Vue: [javascript-typescript-vue-web-frontend-security.md](references/javascript-typescript-vue-web-frontend-security.md)
- jQuery: [javascript-jquery-web-frontend-security.md](references/javascript-jquery-web-frontend-security.md)
- FastAPI: [python-fastapi-web-server-security.md](references/python-fastapi-web-server-security.md)
- Django: [python-django-web-server-security.md](references/python-django-web-server-security.md)
- Flask: [python-flask-web-server-security.md](references/python-flask-web-server-security.md)

For frontend-plus-backend applications, read the relevant reference for each side. If no matching reference exists, rely on the installed framework's authoritative security guidance rather than inventing version-specific behavior.
