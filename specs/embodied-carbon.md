# Example spec: Reviewable takeoff to carbon

**Status:** volunteer proposal. The [official brief](https://edmontonunlimited.com/wp-content/uploads/2026/09/BWT_EmbodiedCarbon_Challenge_Scope-Draft-V2-August-19-2026.docx-1.pdf) calls for vector PDF input, a traceable takeoff, A1–A3 assessment, corrections, and substitutions. The first slice below deliberately covers one assembly; it is not a complete challenge submission.

## User and outcome

A residential estimator confirms a quantity from drawings, selects a compatible factor, and sees how a reviewed substitution changes a clearly bounded estimate.

## First slice

One slab with explicit length, width, and thickness. Record where each dimension came from; have a person confirm it. Calculate volume, match a factor declared per cubic metre, and report subtotal. Do not infer scale from a screenshot without calibration. Add foundations, walls, roof, and schedules only after independently validating the first slice.

## Data contract

Quantity: id, assembly/material, value, unit, drawing id/revision, sheet/detail/coordinates, basis (`measured`, `inferred`, `assumed`), assumptions, human review status.

Factor: id/version, material/product, declared unit, value in kgCO2e per declared unit, module boundary, geography, source URL/document, validity dates, data type, access/reuse terms.

Result: quantity and factor ids, conversion basis, emissions, coverage, excluded assemblies, floor-area definition, assumptions, calculation version.

## Calculation rules

For compatible units: emissions = quantity × factor. If units differ, require an explicit dimensionally valid conversion, including density or thickness where needed; otherwise stop the line. Never match by material name alone.

Sum compatible A1–A3 records only. Report operational emissions, other modules, and biogenic-carbon treatment separately when relevant; do not silently net unlike indicators. Intensity = scoped kgCO2e / explicitly defined positive floor area. A partial subtotal divided by area remains a partial intensity.

## Acceptance criteria

| ID | Given / when | Expected |
| --- | --- | --- |
| EC-01 | Vector plan is supplied | Inventory readable sheets; report missing details |
| EC-02 | A dimension is extracted | Retain source and basis; allow correction |
| EC-03 | A 10 m × 8 m × 0.1 m synthetic slab is reviewed | Volume is 8 m3 |
| EC-04 | Quantity unit differs from factor unit | Block without a documented conversion |
| EC-05 | Factor has incompatible modules or expired validity | Block or require explicit reviewed replacement; disclose choice |
| EC-06 | Factor is unavailable | Keep the line unresolved; never use zero as a substitute |
| EC-07 | Only slab is included | Label output as partial and list exclusions |
| EC-08 | User changes slab thickness | Update quantity, subtotal, contributions, and intensity |
| EC-09 | A substitution is requested | Compare compatible function and scope, preserve baseline |
| EC-10 | New revision is uploaded | Mark old quantities stale and prevent duplicate counting |

## Demo and validation

Show source dimensions → reviewed volume → chosen factor → subtotal → correction → substitution. Compare quantities against an estimator's reference before judging carbon outputs. Report extraction coverage and errors separately; a plausible total cannot validate a takeoff.

The offline example uses fictional factors to exercise arithmetic. Replace them only with authorized, traceable data and add material suitability, validity, and conversion checks before any real estimate.
