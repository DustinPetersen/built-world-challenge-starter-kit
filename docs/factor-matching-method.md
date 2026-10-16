# Worked method: factor matching and substitution

## Candidate eligibility comes before ranking

Filter by material/product category, declared function, declared unit, lifecycle modules, indicator/method, geography, validity and source quality. Then present suitable candidates. A low GWP value is not sufficient to establish a suitable substitution.

## Unit reconciliation examples

| Quantity | Factor basis | Required step |
| --- | --- | --- |
| 8 m3 concrete | kgCO2e/m3 | Multiply directly after product/scope review |
| 8 m3 material | kgCO2e/kg | Require documented product density in kg/m3 |
| 100 m2 board | kgCO2e/m2 at a specified thickness | Confirm identical specification or justify a supported conversion |
| Count of windows | per complete declared window | Match dimensions, glazing/frame and declaration basis |
| Insulation volume | per m2 at a declared R-value | Reconcile thermal performance and declared geometry; do not guess |

Example with fictional values: 2 m3 × 500 kg/m3 × 0.4 kgCO2e/kg = 400 kgCO2e. Density is part of the evidence chain. This is arithmetic only; no real product claim is implied.

## Preserve comparability

Keep the indicator and method intact. Do not sum totals that mix A1-A3 with A1-A5. Preserve biogenic treatment and distinguish components when reported. An assessment's reporting period, excluded components and area basis belong in the result, not only in a tooltip.

## Human match record

Store candidate set, chosen factor id/version, match rationale, reviewer, date, conversion inputs and alternatives rejected. Distinguish product-specific and industry-average data. A user should be able to explain why the factor was chosen without rerunning a model.

## Substitution experiment

Hold geometry, scope, method and function constant where justified. Change one product/factor at a time. Show absolute change, percentage change when the baseline is nonzero, and assumptions. If a substitution changes required thickness or mass, recalculate quantities too. Rank only compatible alternatives and retain baseline snapshots.

## Data sources and permissions

[EC3](https://docs.buildingtransparency.org/ec3/api-and-integrations) provides an integration path subject to account permissions and terms. [EPD International's downstream API](https://www.environdec.com/services/api) requires a formal request and approval. [CLF North American baselines](https://carbonleadershipforum.org/clf-north-american-material-baselines/) are useful industry-average references with a stated CC BY-SA license; read the dataset's geography and methodology. [ÖKOBAUDAT](https://www.oekobaudat.de/en/service/downloads.html) is another structured research source whose geography and indicator conventions require explicit review.

This kit does not invent live endpoints or bundle an unreviewed normalized factor table. Authorized ingestion should preserve the original source and expose all compatibility decisions.
