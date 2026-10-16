# Offline starter examples

Run from the repository root with Python 3.11+:

```sh
python examples/carbon_calculator.py
python examples/application_check.py
python -m unittest discover -s tests -v
```

No dependencies or external requests. Both programs read local synthetic JSON. Paths resolve relative to the scripts, so they also work from another directory.

Carbon: matches explicitly identical units and A1-A3 scope; rejects unknown factors, negative/nonfinite values, zero area, and unit mismatch. Deliberately does not implement PDF extraction, real factor suitability checks, or unit conversion. It labels the subtotal partial.

Application: a tiny illustrative presence check. It does not encode official form requirements, code applicability, or technical sufficiency. A present value stays `present_unverified`.

Edit copies of the fixtures to experiment. Never substitute private data into a public commit. Fictional factors cannot be used for real assessments.

Additional offline data exploration: `python examples/housing_summary.py` from the repository root. See [data provenance](../data/README.md).

## Additional runnable methods

From the repository root:

```sh
python examples/quantity_methods.py
python examples/citation_check.py
python scripts/profile_housing.py
```

The geometry helper covers slab openings, wall-layer thickness, roof slope and a documented volume-to-mass conversion. The citation lookup rejects an invented reference, wrong edition, or ambiguous match in a fictional corpus. These are small building blocks, not full extraction or compliance applications.

See [housing field profiles](../data/profiles/README.md), [research datasets](../resources/research-datasets.md), and [coverage map](../docs/coverage-map.md).
