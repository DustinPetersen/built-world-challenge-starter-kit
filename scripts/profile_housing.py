"""Rebuild descriptive profiles from the bundled unmodified NRCan tables."""
import csv
import json
import math
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def profile(path):
    with path.open(encoding='utf-8-sig',newline='') as stream:
        reader=csv.DictReader(stream)
        counts={name:Counter() for name in reader.fieldnames}
        count=0
        for row in reader:
            count+=1
            for key,value in row.items(): counts[key][value]+=1
    fields=[]
    for name,values in counts.items():
        nonblank={v:n for v,n in values.items() if v.strip()}
        numeric=[]
        all_numeric=bool(nonblank)
        for value,n in nonblank.items():
            try:
                number=float(value)
                if not math.isfinite(number): all_numeric=False;break
                numeric.append((number,n))
            except ValueError:
                all_numeric=False;break
        result=dict(field=name,rows=count,blank_count=sum(n for v,n in values.items() if not v.strip()),
                    distinct_nonblank=len(nonblank),observed_type='finite_numeric_text' if all_numeric else 'text_or_mixed',
                    common_values=[dict(value=v,count=n) for v,n in values.most_common(3)],
                    unit='not inferred; consult upstream schema/model documentation')
        if all_numeric:
            result.update(min=min(v for v,n in numeric),max=max(v for v,n in numeric),
                          mean=sum(v*n for v,n in numeric)/sum(n for v,n in numeric))
        fields.append(result)
    return dict(source=path.name,row_count=count,column_count=len(fields),fields=fields)

if __name__=='__main__':
    out=ROOT/'data/profiles';out.mkdir(exist_ok=True)
    for path in sorted((ROOT/'data/third-party/nrcan-housing-archetypes').glob('*.csv')):
        data=profile(path)
        (out/(path.stem+'.profile.json')).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
        print(f"{path.name}: {data['row_count']} rows, {data['column_count']} fields")
