# Example spec: carbon hotspot and substitution workspace

User: an estimator or sustainability lead choosing what to investigate before locking a material specification. First slice: three reviewed assemblies and one compatible alternative per assembly.

## Interaction

Show a quantity table, factor provenance, subtotal by assembly, coverage and assumptions. Select a row to open its source. Edit a dimension or factor match and create a new result snapshot. Compare a baseline with the alternative while showing exactly what changed.

## Acceptance cases

- Every contribution traces to reviewed quantity and factor versions.
- Unknown factors stay unresolved and do not become zero emissions.
- A mixed module boundary is blocked from the A1-A3 subtotal.
- A substitution changing thickness triggers quantity recalculation.
- Partial coverage remains prominent in totals and intensity.
- Baseline and alternative can be exported with a change log.

## Implementation

Keep geometry, factor matching and calculation separate. Use an editable table UI first; source highlighting follows when stable anchors exist. A bar chart can reveal hotspots, but the table must remain accessible and sufficient to inspect the calculation.

## Validation

Reconcile quantities with an estimator and factor matches with an LCA-informed reviewer. Observe whether the interface helps them identify the next useful action. A lower fictional total in a demo does not establish a real building improvement.
