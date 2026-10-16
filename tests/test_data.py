import csv
import hashlib
import json
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]

class DataTests(unittest.TestCase):
    def test_synthetic_geometry_and_diagrams(self):
        cases = json.loads((ROOT/'data/synthetic/slab-cases.json').read_text())
        self.assertEqual(len({x['id'] for x in cases}), 60)
        for x in cases:
            with self.subTest(case=x['id']):
                self.assertAlmostEqual(x['length_m']*x['width_m']*x['thickness_mm']/1000,x['expected_volume_m3'])
                p=ROOT/'data/synthetic'/x['source']
                self.assertIn('SYNTHETIC',p.read_text(encoding='utf-8'))
                ET.parse(p)
    def test_catalog_consistency(self):
        records=json.loads((ROOT/'resources/api-catalog.json').read_text(encoding='utf-8'))
        self.assertEqual(len(records),50)
        self.assertEqual(len({x['id'] for x in records}),len(records))
        with (ROOT/'resources/api-catalog.csv').open(encoding='utf-8',newline='') as f:
            self.assertEqual([x['id'] for x in csv.DictReader(f)],[x['id'] for x in records])
        for x in records:
            self.assertTrue(x['documentation_url'].startswith('https://'))
            self.assertTrue(x['access'] and x['caveat'])
    def test_upstream_integrity_and_table_shapes(self):
        folder=ROOT/'data/third-party/nrcan-housing-archetypes'
        for item in json.loads((folder/'provenance.json').read_text()):
            path=folder/Path(item['upstream_path']).name
            with self.subTest(path=path.name):
                self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(),item['sha256'])
                if path.suffix=='.csv':
                    with path.open(encoding='utf-8-sig',newline='') as f:
                        rows=list(csv.reader(f))
                    self.assertEqual(len(rows)-1,item['data_rows'])
                    self.assertEqual(len(rows[0]),item['columns'])
                    self.assertTrue(all(len(row)==len(rows[0]) for row in rows))

if __name__ == '__main__': unittest.main()
