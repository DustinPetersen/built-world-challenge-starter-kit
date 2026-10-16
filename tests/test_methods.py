import json
from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'examples'))
from quantity_methods import slab, wall_layer, pitched_roof, volume_to_mass
from citation_check import verify

class MethodTests(unittest.TestCase):
    def test_opening_and_thickness_units(self):
        self.assertAlmostEqual(slab(10,8,100,[dict(id='one',area_m2=2)]),7.8)
        self.assertEqual(wall_layer(10,3,12,[dict(id='one',area_m2=2)]),dict(net_area_m2=28,volume_m3=0.336))
    def test_roof_slope(self):
        self.assertEqual(pitched_roof(80,0,12),80)
        self.assertAlmostEqual(pitched_roof(80,9,12),100)
    def test_duplicate_or_impossible_openings(self):
        for openings in ([dict(id='a',area_m2=1),dict(id='a',area_m2=1)], [dict(id='a',area_m2=81)]):
            with self.assertRaises(ValueError): slab(10,8,100,openings)
    def test_documented_mass_conversion(self):
        self.assertEqual(volume_to_mass(2,500,'fictional'),1000)
        with self.assertRaises(ValueError): volume_to_mass(2,500,'')
        with self.assertRaises(ValueError): slab(10,8,float('inf'))
    def test_wrong_edition_and_invented_reference(self):
        data=json.loads((Path(__file__).resolve().parents[1]/'examples/data/fictional-corpus.json').read_text())
        results=[verify(q,data['records']) for q in data['queries']]
        self.assertEqual(results[0]['status'],'reference_resolves_applicability_unverified')
        self.assertEqual([r['status'] for r in results[1:]],['unresolved','unresolved'])
    def test_duplicate_reference_is_ambiguous(self):
        data=json.loads((Path(__file__).resolve().parents[1]/'examples/data/fictional-corpus.json').read_text())
        self.assertEqual(verify(data['queries'][0],data['records']*2)['status'],'unresolved')

if __name__=='__main__': unittest.main()
