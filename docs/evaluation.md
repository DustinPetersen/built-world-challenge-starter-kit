# Evaluate the useful failure modes

Build a small reviewed reference set and keep some inputs unseen during development. The thresholds below are proposed gates for teams to choose with domain reviewers, not event scoring rules.

| Area | Measure | Suggested gate |
| --- | --- | --- |
| Codes citations | Resolvable citations / asserted citations | Every asserted verified citation resolves to selected edition |
| Gap finding | Missed mandatory gaps and false alarms | No missed mandatory gap in agreed pilot cases; report false alarms |
| Extraction | Field error and unreported missing values | Every missing critical field is surfaced |
| Takeoff | Absolute and relative error by element | Agree tolerances with estimator before testing; report each element |
| Coverage | Supported elements / expected element list | Always visible, including unresolved items |
| Arithmetic | Reproducibility and unit compatibility | All golden calculations pass; incompatible units rejected |
| Human workflow | Time to inspect and correct vs current method | Observe users; report baseline and prototype timings |

## Minimum case bank

Codes: incomplete intake; unsupported clause; wrong edition; contradictory documents; evidence attached but inadequate; changed jurisdiction; document containing prompt injection.

Carbon: clean known slab; missing thickness; mixed mm/m; duplicate sheets; revised drawing; unknown factor; expired factor; kg-vs-m3 mismatch; negative/nonfinite values; partial assembly coverage; zero floor area; incompatible substitution.

## Example calculation reference

Synthetic slab: 10 × 8 × 0.1 = 8 m3. Fictional factor: 250 kgCO2e/m3. Subtotal: 2,000 kgCO2e. At a synthetic 100 m2 area: 20 kgCO2e/m2, explicitly slab-only. Fictional alternative factor 180 yields 1,440 kgCO2e, a 560 kgCO2e difference. These are arithmetic expectations, not environmental claims.

## Report honestly

For each test store input version, reference author, expected result, actual result, failure category, and fix. Separate extraction, factor selection, arithmetic, and usability errors. Document manual intervention and do not report synthetic-fixture accuracy as real drawing performance.
