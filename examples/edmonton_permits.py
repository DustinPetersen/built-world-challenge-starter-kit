"""Read-only Edmonton permit-record aggregation; no addresses or applicant details."""
import argparse
from datetime import datetime, timezone
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen

DATASET = '24uj-dj8v'
BASE = f'https://data.edmonton.ca/resource/{DATASET}.json'
LICENSE = 'https://data.edmonton.ca/stories/s/City-of-Edmonton-Open-Data-Terms-of-Use/msh8-if28'

def query_url(year):
    if isinstance(year,bool) or not isinstance(year,int) or not 2009 <= year <= 2100:
        raise ValueError('year must be an integer from 2009 to 2100')
    return BASE + '?' + urlencode({
        '$select':'building_type,count(*) as permit_rows',
        '$where':f"issue_date >= '{year}-01-01T00:00:00' AND issue_date < '{year+1}-01-01T00:00:00'",
        '$group':'building_type', '$order':'permit_rows DESC,building_type ASC', '$limit':'100'})

def normalize(rows):
    result=[]
    for row in rows:
        count=int(row['permit_rows'])
        if count < 0:
            raise ValueError('negative count from upstream')
        result.append(dict(building_type=row.get('building_type') or '(unclassified)',permit_rows=count))
    return result

def fetch(year):
    url=query_url(year)
    with urlopen(Request(url,headers={'User-Agent':'built-world-starter-kit/edmonton'}),timeout=30) as response:
        rows=json.load(response)
    return dict(source='City of Edmonton: General Building Permits',dataset_id=DATASET,
                dataset_url=f'https://data.edmonton.ca/d/{DATASET}',query_url=url,license_url=LICENSE,
                attribution='Contains information licensed under the Open Government Licence – City of Edmonton.',
                fetched_at_utc=datetime.now(timezone.utc).isoformat(),year=year,
                interpretation='Counts of issued-permit dataset rows by building type, filtered on issue_date; not homes, starts, completions, or alternative-solution approvals.',
                may_be_truncated=len(rows)>=100,rows=normalize(rows))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--year',type=int,default=2025)
    args=parser.parse_args()
    print(json.dumps(fetch(args.year),indent=2,ensure_ascii=False))
