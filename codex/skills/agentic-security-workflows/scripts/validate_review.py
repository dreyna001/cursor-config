#!/usr/bin/env python3
"""Check review structure and local evidence references; no model/network calls."""

from __future__ import annotations

import argparse
from datetime import date
import json
from pathlib import Path
import re


def validate(review: object, repo: Path) -> list[str]:
    errors: list[str] = []
    repo = repo.resolve()
    if not isinstance(review, dict):
        return ["review must be an object"]

    def require(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    def nonblank(value: object) -> bool:
        return isinstance(value, str) and bool(value.strip())

    def strings(value: object) -> bool:
        return isinstance(value, list) and bool(value) and all(nonblank(v) for v in value)

    def records(key: str) -> dict[str, dict]:
        rows = review.get(key)
        if not isinstance(rows, list) or not rows:
            errors.append(f"{key} must be a nonempty array")
            return {}
        result: dict[str, dict] = {}
        for row in rows:
            if not isinstance(row, dict) or not nonblank(row.get("id")):
                errors.append(f"{key} entries need an id")
                continue
            require(row["id"] not in result, f"duplicate {key} id: {row['id']}")
            result[row["id"]] = row
        return result

    def local_path(value: object, label: str) -> Path | None:
        if not nonblank(value) or Path(value).is_absolute():
            errors.append(f"{label} must be repository-relative")
            return None
        path = (repo / value).resolve()
        if not path.is_relative_to(repo):
            errors.append(f"{label} escapes repository")
            return None
        return path

    def choice(value: object, options: set[str]) -> bool:
        return isinstance(value, str) and value in options

    require(type(review.get("schema_version")) is int and review["schema_version"] == 1, "unsupported schema_version")
    require(choice(review.get("use_case"), {"threat_hunting", "incident_response", "ssp_authoring"}), "invalid use_case")
    require(choice(review.get("review_level"), {"source_only", "synthetic", "live"}), "invalid review_level")
    require(bool(re.fullmatch(r"[0-9a-f]{40}", str(review.get("source_revision", "")))), "source_revision must be a full Git SHA")
    require(nonblank(review.get("objective")), "objective is required")
    try:
        date.fromisoformat(review.get("review_date", ""))
    except (ValueError, TypeError):
        errors.append("review_date must be an ISO date")
    for key in ("boundaries", "limits"):
        require(strings(review.get(key)), f"{key} must contain nonempty strings")

    variants = records("variants")
    roots = {key: local_path(row.get("root"), f"variant {key} root") for key, row in variants.items()}
    for key, root in roots.items():
        require(root is not None and root.is_dir(), f"variant {key} root does not exist")

    evidence = records("evidence")
    for key, row in evidence.items():
        require(choice(row.get("kind"), {"source", "recorded_evaluation"}), f"{key}: invalid evidence kind")
        variant = row.get("variant") if isinstance(row.get("variant"), str) else ""
        require(variant in variants, f"{key}: unknown variant")
        path = local_path(row.get("path"), f"{key} path")
        require(nonblank(row.get("anchor")), f"{key}: source anchor is required")
        if path is None:
            continue
        root = roots.get(variant)
        require(root is not None and path.is_relative_to(root), f"{key}: source outside variant")
        if not path.is_file():
            errors.append(f"{key}: missing source file")
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            errors.append(f"{key}: source is not readable UTF-8")
            continue
        require(nonblank(row.get("anchor")) and row["anchor"] in content, f"{key}: anchor not found")

    def references(row: dict, label: str) -> None:
        refs = row.get("evidence_ids")
        require(strings(refs), f"{label}: evidence_ids are required")
        if isinstance(refs, list):
            for ref in refs:
                require(isinstance(ref, str) and ref in evidence, f"{label}: unknown evidence {ref!r}")

    capabilities = records("capabilities")
    for key, row in capabilities.items():
        require(choice(row.get("status"), {"implemented", "partial", "configuration_gated", "parked", "intentional_boundary", "not_found", "unknown"}), f"{key}: invalid capability status")
        require(nonblank(row.get("assessment")), f"{key}: assessment is required")
        references(row, key)

    items = records("work_items")
    graph: dict[str, list[str]] = {}
    for key, row in items.items():
        require(choice(row.get("priority"), {"P1", "P2", "P3"}), f"{key}: invalid priority")
        require(choice(row.get("type"), {"defect", "ux", "capability", "verification"}), f"{key}: invalid work type")
        require(choice(row.get("status"), {"proposed", "requires_scope_decision", "verification_required"}), f"{key}: invalid work status")
        require(isinstance(row.get("capability_id"), str) and row["capability_id"] in capabilities, f"{key}: unknown capability")
        for field in ("problem", "recommendation"):
            require(nonblank(row.get(field)), f"{key}: {field} is required")
        require(strings(row.get("acceptance")), f"{key}: observable acceptance criteria required")
        references(row, key)
        deps = row.get("depends_on")
        require(isinstance(deps, list) and all(isinstance(d, str) and d in items for d in deps), f"{key}: invalid dependencies")
        graph[key] = [d for d in deps if isinstance(d, str) and d in items] if isinstance(deps, list) else []

    visited: set[str] = set()
    active: set[str] = set()

    def visit(key: str) -> None:
        if key in active:
            errors.append(f"dependency cycle at {key}")
            return
        if key in visited:
            return
        active.add(key)
        for dep in graph[key]:
            visit(dep)
        active.remove(key)
        visited.add(key)

    for key in graph:
        visit(key)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("review", type=Path)
    parser.add_argument("--repo", type=Path, required=True)
    args = parser.parse_args()
    try:
        review = json.loads(args.review.read_text(encoding="utf-8"))
        errors = validate(review, args.repo)
    except (OSError, ValueError) as exc:
        errors = [str(exc)]
    print(json.dumps({"valid": not errors, "errors": errors, "scope": "structure_and_local_source_references"}))
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
