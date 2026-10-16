"""Illustrative presence check, not an official form or code assessment."""
import json
from pathlib import Path

FIELDS = ('jurisdiction', 'code_edition', 'proposal', 'benchmark_reference', 'evidence')

def check(application):
    return [dict(field=field, status='present_unverified' if application.get(field)
                 else 'missing', next_action='Review content with domain expert'
                 if application.get(field) else 'Provide ' + field)
            for field in FIELDS]

if __name__ == '__main__':
    data = json.loads((Path(__file__).parent / 'data/application.json').read_text())
    print('SYNTHETIC ILLUSTRATIVE CHECKLIST - NOT OFFICIAL FORM VALIDATION')
    print(json.dumps(check(data), indent=2))
