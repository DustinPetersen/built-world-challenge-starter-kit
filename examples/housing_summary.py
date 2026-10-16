"""Summarize bundled NRCan housing-archetype rows without third-party packages."""
import csv
import json
from collections import Counter
from pathlib import Path

def summarize(path):
    with Path(path).open(encoding='utf-8-sig', newline='') as stream:
        reader = csv.DictReader(stream)
        provinces, house_types, count = Counter(), Counter(), 0
        columns = len(reader.fieldnames)
        for row in reader:
            count += 1
            provinces[row['province']] += 1
            house_types[row['houseType']] += 1
    return dict(rows=count, columns=columns, provinces=dict(provinces), house_types=dict(house_types))

if __name__ == '__main__':
    path = Path(__file__).resolve().parents[1] / 'data/third-party/nrcan-housing-archetypes/base_archetype_description.csv'
    print(json.dumps(summarize(path),indent=2))
    print('Housing energy archetypes, not material takeoffs or carbon factors.')
