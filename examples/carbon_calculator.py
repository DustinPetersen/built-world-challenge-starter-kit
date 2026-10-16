"""Synthetic arithmetic example; not an LCA engine or drawing reader."""
import json
import math
from pathlib import Path

def number(value, label, positive=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{label}: numeric value required")
    if not math.isfinite(value) or value < 0 or (positive and value == 0):
        raise ValueError(f"{label}: invalid number")
    return value

def calculate(data):
    area = number(data['floor_area_m2'], 'floor area', positive=True)
    factors = {}
    for factor in data['factors']:
        if factor['id'] in factors:
            raise ValueError('duplicate factor id')
        factors[factor['id']] = factor
    results, seen = [], set()
    for row in data['quantities']:
        if row['id'] in seen:
            raise ValueError('duplicate quantity id')
        seen.add(row['id'])
        if row['factor_id'] not in factors:
            raise ValueError('unknown factor: ' + row['factor_id'])
        factor = factors[row['factor_id']]
        if row['unit'] != factor['declared_unit']:
            raise ValueError('unit mismatch: ' + row['id'])
        if factor['modules'] != 'A1-A3':
            raise ValueError('incompatible module scope')
        if not row.get('source') or not factor.get('source'):
            raise ValueError('source required')
        emissions = number(row['quantity'], 'quantity') * number(factor['value'], 'factor')
        number(emissions, 'line emissions')
        results.append(dict(id=row['id'], kgCO2e=emissions,
                            quantity_source=row['source'], factor_id=factor['id'],
                            factor_source=factor['source'], basis=row['basis']))
    total = sum(row['kgCO2e'] for row in results)
    number(total, 'total')
    intensity = total / area
    number(intensity, 'intensity')
    return dict(label='SYNTHETIC PARTIAL A1-A3 ESTIMATE', lines=results,
                total_kgCO2e=total, partial_kgCO2e_per_m2=intensity,
                exclusions=data['exclusions'])

if __name__ == '__main__':
    data = json.loads((Path(__file__).parent / 'data/carbon.json').read_text())
    print(json.dumps(calculate(data), indent=2))
