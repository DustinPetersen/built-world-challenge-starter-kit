"""Read-only public catalog discovery; prints metadata, never downloads datasets."""
import argparse
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen

def discover(query, rows=5):
    if not isinstance(rows, int) or not 1 <= rows <= 20:
        raise ValueError('rows must be 1..20')
    url = 'https://open.canada.ca/data/api/3/action/package_search?' + urlencode({'q':query,'rows':rows})
    request = Request(url, headers={'User-Agent':'built-world-starter-kit/2.0'})
    with urlopen(request, timeout=30) as response:
        data = json.load(response)
    if not data.get('success'):
        raise RuntimeError('catalog returned unsuccessful response')
    return [{'id':r['id'], 'title':r.get('title'), 'license':r.get('license_title'),
             'resources':[{'name':x.get('name'),'format':x.get('format'),'url':x.get('url')}
                          for x in r.get('resources',[])]}
            for r in data['result']['results']]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--query', default='housing')
    parser.add_argument('--rows', type=int, default=3)
    args = parser.parse_args()
    print(json.dumps(discover(args.query,args.rows),indent=2,ensure_ascii=False))
