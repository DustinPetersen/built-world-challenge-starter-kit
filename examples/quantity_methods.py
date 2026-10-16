"""Small, explicit geometry helpers. Synthetic examples; no drawing extraction."""
import json
import math

def nonnegative(value, label):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
        raise ValueError(f'{label} must be finite and nonnegative')
    return value

def net_area(gross, openings):
    gross = nonnegative(gross, 'gross area')
    seen = set()
    deduction = 0
    for opening in openings:
        if not opening.get('id') or opening['id'] in seen:
            raise ValueError('opening ids must be nonempty and unique')
        seen.add(opening['id'])
        deduction += nonnegative(opening['area_m2'], 'opening area')
    if deduction > gross:
        raise ValueError('openings exceed gross area')
    return gross - deduction

def slab(length_m, width_m, thickness_mm, openings=()):
    area = net_area(nonnegative(length_m, 'length') * nonnegative(width_m, 'width'), openings)
    return area * nonnegative(thickness_mm, 'thickness') / 1000

def wall_layer(length_m, height_m, thickness_mm, openings=()):
    area = net_area(nonnegative(length_m, 'length') * nonnegative(height_m, 'height'), openings)
    return dict(net_area_m2=area, volume_m3=area * nonnegative(thickness_mm, 'thickness') / 1000)

def pitched_roof(projected_area_m2, rise, run):
    rise = nonnegative(rise, 'rise')
    run = nonnegative(run, 'run')
    if run == 0:
        raise ValueError('run must be positive')
    return nonnegative(projected_area_m2, 'projected area') * math.hypot(run, rise) / run

def volume_to_mass(volume_m3, density_kg_per_m3, density_source):
    if not density_source or not str(density_source).strip():
        raise ValueError('documented density source required')
    return nonnegative(volume_m3, 'volume') * nonnegative(density_kg_per_m3, 'density')

if __name__ == '__main__':
    print(json.dumps(dict(label='SYNTHETIC GEOMETRY ONLY',
        slab_m3=slab(10,8,100,[dict(id='opening-1',area_m2=2)]),
        wall=wall_layer(10,3,12,[dict(id='window-1',area_m2=2)]),
        roof_m2=pitched_roof(80,6,12),
        mass_kg=volume_to_mass(2,500,'FICTIONAL density fixture')),indent=2))
