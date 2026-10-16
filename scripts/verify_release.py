"""Verify local documentation, JSON, synthetic data and bundled-source integrity."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from update_manifest import included

ROOT = Path(__file__).resolve().parents[1]

def main():
    errors = []
    docs = 0
    for path in ROOT.rglob('*.md'):
        if 'third-party' in path.parts:
            continue  # Upstream README links retain their upstream meaning.
        docs += 1
        for target in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
            if target.startswith(('https://', 'http://', '#')):
                continue
            if not (path.parent / target.split('#')[0]).exists():
                errors.append(f'{path.relative_to(ROOT)}: {target}')
    for path in ROOT.rglob('*.json'):
        json.loads(path.read_text(encoding='utf-8'))
    if errors:
        raise ValueError('Broken local links: ' + repr(errors))
    manifest = json.loads((ROOT/'file-manifest.json').read_text(encoding='utf-8'))
    expected = {item['path'] for item in manifest['files']}
    actual = {path.relative_to(ROOT).as_posix() for path in ROOT.rglob('*') if included(path)}
    if expected != actual:
        raise ValueError(f'Manifest file-set mismatch: missing={expected-actual}, extra={actual-expected}')
    for item in manifest['files']:
        data = (ROOT/item['path']).read_bytes()
        if len(data) != item['bytes'] or hashlib.sha256(data).hexdigest() != item['sha256']:
            raise ValueError('Manifest content mismatch: ' + item['path'])
    subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-v'],
                   cwd=ROOT, check=True)
    print(f'Verified {docs} original Markdown documents and all JSON files.')
    print(f'Verified manifest content for {len(expected)} files.')
    print('External link reachability, vendor authentication and domain accuracy are separate checks.')

if __name__ == '__main__':
    main()
