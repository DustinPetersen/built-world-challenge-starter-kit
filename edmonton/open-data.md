# Edmonton municipal data: practical recipes

## Start with the primary dataset

[General Building Permits, `24uj-dj8v`](https://data.edmonton.ca/d/24uj-dj8v) exposes a [Socrata endpoint](https://data.edmonton.ca/resource/24uj-dj8v.json) and [schema metadata](https://data.edmonton.ca/api/views/24uj-dj8v.json). Both metadata and a live aggregate query were tested on October 15, 2026.

Use these exact API fields: `issue_date`, `building_type`, `work_type`, `job_category`, `units_added`, `construction_value`, `neighbourhood`, and `zoning`. Display labels are not necessarily API field names: PERMIT_DATE maps to `issue_date`, whereas REPORT_PERMIT_DATE maps to `permit_date`. The neighbourhood-number field is spelled `neighbourhood_numberr` in the checked schema. Revalidate fields before building an integration.

## Run the local example

```sh
python examples/edmonton_permits.py --year 2025
```

It performs one read-only aggregate query, selecting building type and counts. It returns source, query, retrieval time and attribution. No addresses, applicant information or API key are requested. Network access is required; the unit tests cover URL construction and result handling without making network calls.

The bundled [2025 snapshot](data/permit-counts-2025.json) is a dated example of that live response. It can change as records are revised. Read its query and interpretation before quoting a number.

## Useful query patterns

| Question | Suggested aggregation | Decision supported |
| --- | --- | --- |
| Which building categories appear frequently? | Count permit rows by `building_type` within an explicit `issue_date` window | Choose interview segments |
| Which work categories matter for a prototype? | Count by `work_type` or `job_category` after checking values | Focus intake examples |
| How does activity vary by neighbourhood? | Aggregate by `neighbourhood`; preserve null values | Explore geography without presenting individual properties |
| How does a category change over time? | Consistent date-window and category filters | Establish context, with caveats about data definitions |

Inspect categories before writing filters. An infill/new-construction classification needs an explicit method; do not infer it from neighbourhood name alone. For large raw-row retrieval, use stable ordering/pagination and respect current platform limits; this example deliberately asks for a bounded aggregate.

## Interpretation limits

- A permit record is not a unique home, household or building. Multiple permits can relate to a project.
- Issued permits are not housing starts or completions; units added is a separate field requiring its own interpretation.
- Permit records do not expose the material takeoff, supporting engineering case, or alternative-solution approval rationale.
- Zoning recorded on a historical permit is not proof of today's applicable zoning.
- Dataset metadata describes occupancy-date coverage limitations and says it is for trends rather than legal confirmation of occupancy. Preserve those limitations if using that field.
- Missing classifications should stay visible. The example flags potential truncation at its result limit.

Dataset metadata uses `SEE_TERMS_OF_USE`. Follow the [City's licence page](https://data.edmonton.ca/stories/s/City-of-Edmonton-Open-Data-Terms-of-Use/msh8-if28) and retain attribution when sharing derived results. The snapshot is City-derived data, separate from the repository's MIT-licensed original code and prose.
