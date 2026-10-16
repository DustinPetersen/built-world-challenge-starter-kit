# Edmonton project and submission context

## Establish jurisdiction first

Record municipality, responsible authority, permit/project reference if available, building type, proposal and selected source versions. Edmonton metro includes multiple municipalities; a project in another municipality should not inherit City of Edmonton forms or workflows automatically.

## Keep the decision paths distinct

| Question | Starting source | Product behavior |
| --- | --- | --- |
| What is proposed on the site? | [Edmonton Zoning Bylaw](https://zoningbylaw.edmonton.ca/) and current City development process | Record the development context; route zoning questions for the appropriate review |
| What construction information must be submitted? | [House application requirements](https://www.edmonton.ca/residential_neighbourhoods/application-requirements-house-permits) or [commercial building guidance](https://www.edmonton.ca/business_economy/new-commercial-building) | Choose the applicable project pathway and checklist |
| Which technical code source applies? | [Alberta codes and standards](https://www.alberta.ca/building-codes-and-standards) and [STANDATA](https://www.alberta.ca/building-standata) | Store edition, printing, amendment and project applicability confirmation |
| Is an alternative solution being proposed? | [Safety Codes Council variance process](https://www.safetycodes.ab.ca/permits-inspections/variances/) and City project requirements | Organize benchmark, claimed performance, evidence and unresolved review questions |
| Is the issue energy efficiency? | [City energy-code guidance](https://www.edmonton.ca/residential_neighbourhoods/energy-code-requirements) | Keep energy-code information distinct from the embodied-carbon calculation |

Development-permit or zoning variances and building-code alternative solutions are different processes. Do not label a zoning check as a safety-code decision. An applicant-facing assistant should explain the next information need and direct unresolved applicability to an appropriate reviewer.

## Alberta code snapshot

At this review, [Alberta's official hub](https://www.alberta.ca/building-codes-and-standards) lists National Building Code – 2023 Alberta Edition, second printing, and NECB 2020, second printing, under codes in force. Store that review date and confirm the edition applicable to the specific project. A generic NBC or a code from another province is not a substitute for the selected Alberta source.

## A useful Edmonton intake record

```json
{
  "municipality": "Edmonton",
  "authority_confirmed_by": null,
  "project_type": null,
  "development_context": "unconfirmed",
  "building_permit_reference": null,
  "code_edition": "candidate: NBC 2023 Alberta Edition",
  "code_printing": "candidate: second printing",
  "applicable_edition_confirmed": false,
  "local_requirements_source": null,
  "alternative_solution_description": null,
  "benchmark_reference": null,
  "professional_review_questions": [],
  "status": "draft"
}
```

This is a proposed software record, not the City's form. Do not invent clause identifiers, professional involvement determinations or official approval outcomes to populate it.
