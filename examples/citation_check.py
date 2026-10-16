"""Exact source-version lookup using a fictional corpus; no real code text."""
import json
from pathlib import Path

def verify(citation, corpus):
    required = ('source_id', 'edition', 'printing', 'article')
    if any(not citation.get(key) for key in required):
        return dict(status='unresolved', reason='Missing source/version/article context')
    matches = [row for row in corpus if all(row.get(k) == citation[k] for k in required)]
    if len(matches) != 1:
        return dict(status='unresolved', reason='Reference absent or ambiguous in selected source version')
    row = matches[0]
    return dict(status='reference_resolves_applicability_unverified',
                source_anchor=row['source_anchor'], text=row['text'],
                attributions=row['attributions'])

if __name__ == '__main__':
    data = json.loads((Path(__file__).parent/'data/fictional-corpus.json').read_text())
    for citation in data['queries']:
        print(json.dumps(dict(citation=citation, result=verify(citation,data['records'])),indent=2))
