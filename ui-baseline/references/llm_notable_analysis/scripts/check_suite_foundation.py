"""Check local foundation parity and standalone deployment boundaries; peers are optional."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re

VARIANTS = ('azure_notable_pipeline', 'llm_notable_analysis_onprem_systemd', 's3_notable_pipeline', 's3_notable_pipeline_commercial')
def frontends(root):
    return [p for p in [root/'portal', root/'frontend', *(root/v/'frontend/analyst-portal' for v in VARIANTS)] if (p/'src/suite-workspace.css').is_file()]

def check_root(root):
    contract = json.loads((root/'docs/suite-foundation-contract.json').read_text())
    if f'Version: **{contract["version"]}**' not in (root/'docs/suite-ui-standard.md').read_text():
        raise ValueError(f'{root}: baseline and foundation release differ')
    count = 0
    for app in frontends(root):
        count += 1
        for relative, digest in contract['files'].items():
            if hashlib.sha256((app/relative).read_bytes()).hexdigest() != digest:
                raise ValueError(f'{app/relative}: shared foundation drift')
        package = json.loads((app/'package.json').read_text())
        for name, version in {**package.get('dependencies', {}), **package.get('devDependencies', {})}.items():
            if version.startswith(('file:', 'link:', 'workspace:')):
                raise ValueError(f'{app}: deployment dependency outside this frontend: {name}')
        optional_foundations = {'redux', '@reduxjs/toolkit', 'zustand', 'mobx', 'recoil', 'jotai', '@tanstack/react-query', 'axios', 'ky', 'react-hook-form', 'formik'}
        declared = set(package.get('dependencies', {})) | set(package.get('devDependencies', {}))
        unreviewed = (declared & optional_foundations) - set(contract.get('reviewedOptionalPackages', []))
        if unreviewed:
            raise ValueError(f'{app}: foundation packages need a baseline decision: {sorted(unreviewed)}')
        for dependency, pin in contract['dependencies'].items():
            if package.get('dependencies', {}).get(dependency) != pin:
                raise ValueError(f'{app}: {dependency} must be the released runtime pin {pin}')
        for path in (app/'src').rglob('*'):
            if path.suffix not in ('.ts', '.tsx', '.js', '.jsx') or '.test.' in path.name or '.spec.' in path.name:
                continue
            source = path.read_text()
            for target in re.findall(r'from\s+["\']([^"\']+)["\']', source):
                if target.startswith('.') and not (path.parent/target).resolve().is_relative_to(app.resolve()):
                    raise ValueError(f'{path}: cross-frontend import {target}')
            if path.is_relative_to(app/'src/lib/suite'):
                continue
            if re.search(r'\bfetch\s*\(', source):
                raise ValueError(f'{path}: use shared fetchResponse; keep credentials/protocols in the app adapter')
            if re.search(r'<form\b', source):
                raise ValueError(f'{path}: use SuiteForm to preserve common pending-submit behavior')
            if re.search(r'from\s+["\']react-router(?:/dom)?["\']', source):
                raise ValueError(f'{path}: use the shared routing entrypoint')
            if 'generated' not in path.parts and re.search(r'from\s+["\']zod["\']', source):
                raise ValueError(f'{path}: use the shared validation entrypoint')
    return count

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--peer', type=Path, action='append', default=[])
    args = parser.parse_args()
    try:
        roots = [args.root, *args.peer]
        count = sum(check_root(root) for root in roots)
        if len({(root/'docs/suite-foundation-contract.json').read_bytes() for root in roots}) != 1:
            raise ValueError('Foundation release manifests differ across repositories')
        print(f'Foundation parity passed: {count} standalone frontends; local sources and architecture boundaries checked.')
        return 0
    except (ValueError, OSError, KeyError) as error:
        print(f'Foundation check failed: {error}')
        return 1
if __name__ == '__main__':
    raise SystemExit(main())
