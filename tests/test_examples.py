import copy
import json
from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'examples'))
from carbon_calculator import calculate
from application_check import check

class ExampleTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((Path(__file__).resolve().parents[1] / 'examples/data/carbon.json').read_text())
    def test_known_total_and_intensity(self):
        result = calculate(self.data)
        self.assertEqual(result['total_kgCO2e'], 2000)
        self.assertEqual(result['partial_kgCO2e_per_m2'], 20)
    def test_correction_recalculates(self):
        self.data['quantities'][0]['quantity'] = 10
        self.assertEqual(calculate(self.data)['total_kgCO2e'], 2500)
    def test_substitution(self):
        self.data['factors'][0]['value'] = 180
        self.assertEqual(calculate(self.data)['total_kgCO2e'], 1440)
    def test_invalid_inputs(self):
        mutations = [lambda d: d.update(floor_area_m2=0),
                     lambda d: d['quantities'][0].update(unit='kg'),
                     lambda d: d['quantities'][0].update(quantity=-1),
                     lambda d: d['quantities'][0].update(quantity=float('nan')),
                     lambda d: d['quantities'][0].update(factor_id='missing'),
                     lambda d: d['factors'][0].update(modules='A1-A5'),
                     lambda d: d['quantities'].append(copy.deepcopy(d['quantities'][0]))]
        for mutation in mutations:
            with self.subTest(mutation=mutation):
                data = copy.deepcopy(self.data)
                mutation(data)
                with self.assertRaises(ValueError): calculate(data)
    def test_presence_does_not_mean_approved(self):
        findings = check({'jurisdiction':'example'})
        self.assertEqual(findings[0]['status'], 'present_unverified')
        self.assertEqual(findings[1]['status'], 'missing')

if __name__ == '__main__': unittest.main()
