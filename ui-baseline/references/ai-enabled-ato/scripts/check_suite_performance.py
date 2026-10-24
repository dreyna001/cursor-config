"""Check production eager/total JS budgets and schema-only codegen; no peer checkout required."""
import argparse
import gzip
import json
from pathlib import Path

def measure(app):
    dist = app / 'dist'
    manifest = json.loads((dist / '.vite/manifest.json').read_text())
    visited = set()
    def visit(key):
        if key in visited: return
        visited.add(key)
        for dependency in manifest[key].get('imports', []): visit(dependency)
    for key, value in manifest.items():
        if value.get('isEntry'): visit(key)
    eager = sorted({manifest[key]['file'] for key in visited if manifest[key]['file'].endswith('.js')})
    all_js = sorted(dist.rglob('*.js'))
    return {'eagerJavaScriptBytes': sum((dist/f).stat().st_size for f in eager),
            'eagerGzipCalculated': sum(len(gzip.compress((dist/f).read_bytes(), compresslevel=9, mtime=0)) for f in eager),
            'totalJavaScriptBytes': sum(f.stat().st_size for f in all_js), 'eagerAssets': eager}

def check(root):
    contract = json.loads((root/'docs/suite-performance-contract.json').read_text())
    results = []
    # A checkout directory may have any name (including CI's generic workspace path).
    matches = [frontends for frontends in contract['frontends'].values()
               if all((root / relative / 'package.json').is_file() for relative in frontends)]
    if len(matches) != 1:
        raise ValueError('Cannot uniquely match this checkout to the reviewed frontend paths')
    for relative, budgets in matches[0].items():
        app = root/relative
        package = json.loads((app/'package.json').read_text())
        if 'openapi-zod-client' in package['scripts'].get('generate:api', ''):
            if '--template openapi/schemas-only.hbs' not in package['scripts']['generate:api']:
                raise ValueError(f'{app}: use the reviewed schema-only generator template')
            if '@zodios/core' in (app/'src/api/generated/portalSchemas.ts').read_text():
                raise ValueError(f'{app}: generated runtime schemas include an unused HTTP client')
        observed = measure(app)
        for key in ['eagerJavaScriptBytes', 'totalJavaScriptBytes']:
            if observed[key] > budgets[key]:
                raise ValueError(f'{app}: {key} {observed[key]} exceeds reviewed budget {budgets[key]}')
        results.append({'frontend': relative, **observed})
    return results

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    print(json.dumps({'passed': True, 'results': check(args.root)}, indent=2))
