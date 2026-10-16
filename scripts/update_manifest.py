"""Regenerate the release manifest after intentional repository changes."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {'.git', '__pycache__', '.venv', 'node_modules', 'private-data', 'local-outputs'}

def included(path):
    relative = path.relative_to(ROOT)
    return (path.is_file() and not any(part in EXCLUDED for part in relative.parts)
            and path.name != 'file-manifest.json'
            and not path.name.startswith('.env') and path.suffix != '.pyc')

if __name__ == '__main__':
    records = []
    for path in sorted(ROOT.rglob('*')):
        if included(path):
            data = path.read_bytes()
            records.append(dict(path=path.relative_to(ROOT).as_posix(), bytes=len(data),
                                sha256=hashlib.sha256(data).hexdigest()))
    (ROOT/'file-manifest.json').write_text(json.dumps(
        dict(release='expanded-2026-10-15', files=records), indent=2)+'\n', encoding='utf-8')
    print(f'Updated manifest: {len(records)} files')
