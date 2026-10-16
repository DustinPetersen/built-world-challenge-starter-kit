# Data and reference directory

Reviewed October 15, 2026. These are links and access notes, not redistributed datasets. Public readability does not establish rights to copy, embed, scrape, train on, or republish material. Confirm exact terms for your intended use.

| Resource | Best use | Access / reuse / caveat |
| --- | --- | --- |
| [Organizer program and linked full scopes](https://edmontonunlimited.com/programs/built-world-challenge/) | Authoritative challenge direction and current briefs | Link to originals; confirm updates with event team |
| [Alberta codes and standards](https://www.alberta.ca/building-codes-and-standards) | Starting point for in-force code editions and official publication links | Record edition, printing, amendments, and project context; confirm applicability |
| [Alberta building STANDATA](https://www.alberta.ca/building-standata) | Locate provincial interpretations and notices | Check currency and relevance; not a replacement for the applicable code |
| [Safety Codes Council variances](https://www.safetycodes.ab.ca/permits-inspections/variances/) | Understand process and locate variance form | A useful process reference; verify form and jurisdiction requirements |
| [NRCan Material Carbon Emissions Estimator](https://prod-natural-resources.azure.cloud.nrcan-rncan.gc.ca/maps-tools-publications/tools-applications/material-carbon-emissions-estimator-mce2) | Canadian residential material/assembly reference and comparison workflow | Downloadable tool and guide; inspect terms and calculation basis before reusing factors |
| [NRC whole-building LCA guidelines](https://nrc-publications.canada.ca/eng/view/object/?id=f7bd265d-cc3d-4848-a666-8eeb1fbde910) | Methodology and comparability | Published guidance; check latest version and intended reporting scheme |
| [EC3](https://www.buildingtransparency.org/tools/ec3/) | Discover product EPDs and compare candidate materials | Tool access and API access have distinct terms |
| [EC3 API access](https://www.buildingtransparency.org/api-access-pricing/) | Assess integration feasibility | Check current rate limits, attribution, commercial-use terms and eligibility; do not assume unrestricted open data |
| [NRC construction LCA centre](https://cnrc.canada.ca/en/research-development/research-collaboration/programs/centre-excellence-construction-life-cycle-assessment) | Track Canadian data and methodology initiatives | A program description is not a ready-to-use downloadable factor dataset |
| Sponsor-provided plans, schedules, element lists, and reference takeoffs | Most relevant challenge inputs and evaluation baseline | Request through organizers; no public redistribution assumed |
| Manufacturer/program-operator EPDs | Product-specific factor evidence | Record verified declaration, unit, modules, geography, validity, and product match; rights differ by publisher |

## Data acquisition checklist

Ask organizers for: latest briefs; allowed inputs; approved code edition and printing; exact variance form; anonymized sample applications; expert-reviewed checklist and citations; vector drawing sets and revision ids; reference quantities; assembly definitions; factor source permissions; floor-area basis; expected exports; judging updates.

Keep sponsor data outside the public repository. This kit's `private-data/` ignore rule reduces accidental commits but is not access control. Inspect staged files before pushing.

## Source register template

For each resource record: source id, title, URL, publisher, version, retrieved date, allowed use, redistribution status, attribution, local hash if downloaded, reviewer, next review date. Store pointers publicly; retain restricted content privately.

## Synthetic data strategy

Start with self-authored geometry and fictional applications. For extraction testing, draw a simple plan with known dimensions and label it synthetic. Separate those results from performance on real sponsor drawings. The included quantity/factor records are solely arithmetic fixtures and must not become real-world benchmarks.
