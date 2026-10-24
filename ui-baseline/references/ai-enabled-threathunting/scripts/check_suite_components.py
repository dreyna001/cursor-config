"""Verify the released component sources and explicit native-control exceptions.

This source gate complements (and never replaces) Playwright visual/workflow checks.
"""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

VARIANTS = ('azure_notable_pipeline','llm_notable_analysis_onprem_systemd','s3_notable_pipeline','s3_notable_pipeline_commercial')
def frontends(root: Path) -> list[Path]:
    return [p for p in [root/'frontend',root/'portal',*(root/v/'frontend/analyst-portal' for v in VARIANTS)] if (p/'src/suite-workspace.css').is_file()]

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def native_controls(source: str):
    """Read JSX opening tags while respecting nested expressions and quoted > signs."""
    for match in re.finditer(r'<(button|input|textarea|select|dialog|div|section|aside)\b',source):
        i=match.end(); depth=0; quote=None; escaped=False
        while i<len(source):
            ch=source[i]
            if quote:
                if escaped: escaped=False
                elif ch=='\\': escaped=True
                elif ch==quote: quote=None
            elif ch in '\"\'`': quote=ch
            elif ch=='{': depth+=1
            elif ch=='}': depth-=1
            elif ch=='>' and depth==0:
                tag=source[match.start():i+1]
                if match[1] in ('div','section','aside'):
                    if not re.search(r'\brole=[\"\'](?:alertdialog|dialog)[\"\']',tag):break
                    kind='dialog-surface'
                else:kind=match[1]
                yield kind,hashlib.sha256(re.sub(r'\s+',' ',tag).encode()).hexdigest(),tag
                break
            i+=1

def inventory(root: Path):
    rows=[]
    shared=set(json.loads((root/'docs/suite-component-contract.json').read_text())['files'])
    for app in frontends(root):
        for path in sorted(p for p in (app/'src').rglob('*') if p.suffix in ('.tsx','.jsx')):
            if str(path.relative_to(app)) in shared or '.test.' in path.name or '.spec.' in path.name: continue
            for tag,sha,source in native_controls(path.read_text()):
                rows.append((str(path.relative_to(root)),tag,sha,source))
    return rows

def check_root(root: Path) -> None:
    contract=json.loads((root/'docs/suite-component-contract.json').read_text())
    doc=(root/'docs/suite-ui-standard.md').read_text()
    if f'Version: **{contract["version"]}**' not in doc:raise ValueError(f'{root}: component/baseline versions disagree')
    for app in frontends(root):
        for relative,sha in contract['files'].items():
            if digest(app/relative)!=sha:raise ValueError(f'{app/relative}: shared component drift; update canonical source and synchronize all six frontends')
        for css in (app/'src').rglob('*.css'):
            if css.name=='suite-components.css':continue
            if re.search(r'\.suite-(button|input|textarea|native-select|badge|dialog)\b|--suite-(control|field|dialog)-',css.read_text()):
                raise ValueError(f'{css}: app-local override of a shared component; use approved variants/layout props')
    actual=Counter((p,t,h) for p,t,h,_ in inventory(root))
    exceptions=json.loads((root/'docs/suite-component-exceptions.json').read_text())
    approved=Counter({(r['path'],r['tag'],r['sha256']):r['count'] for r in exceptions['nativeControls']})
    if actual!=approved:
        new=list((actual-approved).elements());stale=list((approved-actual).elements())
        raise ValueError(f'{root}: native-control inventory changed: {len(new)} new/changed, {len(stale)} stale. Use shared primitives or review an explicit preservation exception. New: {new[:3]}')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);parser.add_argument('--peer',type=Path,action='append',default=[])
    args=parser.parse_args();roots=[args.root,*args.peer]
    try:
        for root in roots:check_root(root)
        if len({(root/'docs/suite-component-contract.json').read_bytes() for root in roots})!=1:raise ValueError('Shared component manifests differ across repositories')
        print(f'Component source parity passed: {sum(len(frontends(r)) for r in roots)} frontends; native-control exceptions checked. Rendered/workflow validation is separate.')
        return 0
    except (OSError,ValueError,KeyError) as error:
        print(f'Component check failed: {error}');return 1

if __name__=='__main__':raise SystemExit(main())
