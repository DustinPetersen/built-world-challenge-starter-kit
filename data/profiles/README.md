# Housing table profiles

These are descriptive profiles derived from the bundled NRCan CSV snapshots using `python scripts/profile_housing.py`.

Each source field has row count, blank count, distinct nonblank values, three common values, and an observed text/numeric classification. Finite numeric text also receives a minimum, maximum and frequency-weighted mean. All three original tables have 6,794 rows; together they expose 540 field positions. Repeated field names across tables are not necessarily independent concepts.

The profiler treats only whitespace/empty strings as blank. Zero, sentinel codes and values such as `NA` retain their literal meanings; the tool does not decide whether they mean missing in the upstream schema. Numeric parsing does not establish a physical unit or make a column meaningful to average. Review the upstream documentation before analysis, especially for categorical codes stored as numbers.

Profiles describe this dated source snapshot. They do not establish representativeness, statistical independence, construction quantities, or embodied-carbon factors.

Source: Natural Resources Canada, canmet-energy/housing-archetypes. Contains information licensed under the [Open Government Licence – Canada](https://open.canada.ca/en/open-government-licence-canada). These profiles are derived summaries; original source tables remain unmodified. See [source provenance](../third-party/nrcan-housing-archetypes/provenance.json) and [attribution](../third-party/nrcan-housing-archetypes/ATTRIBUTION.md).
