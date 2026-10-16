# Built World Challenge · Starter Kit

Practical ideas, example specifications, data resources, and mentor tools for teams exploring building-code application preparation and residential embodied carbon.

**Independent volunteer resource · Edmonton, Alberta · October 2026.** This is not an official event publication or an endorsed solution. Original proposals here are starting points; the organizer's current challenge brief and supplied data package govern event requirements.

## Start here — 15 minutes

1. Pick a user and one workflow in [the idea bank](docs/idea-bank.md).
2. Copy the relevant [building codes spec](specs/building-codes.md) or [carbon spec](specs/embodied-carbon.md).
3. Choose a familiar stack from [stack options](docs/stacks.md).
4. Identify one authorized input and one human reviewer using [data resources](resources/data-sources.md).
5. Write three pass/fail cases before building. Use [evaluation guidance](docs/evaluation.md).

## Choose your path

| Your goal | Open this |
| --- | --- |
| Find an achievable project | [12 seed ideas](docs/idea-bank.md) |
| Help a team as a mentor | [Office-hours playbook](docs/mentor-playbook.md) |
| Scope the day and next eight weeks | [Build method](docs/build-method.md) |
| Build an application-preparation assistant | [Codes example spec](specs/building-codes.md) |
| Build a traceable takeoff-to-carbon tool | [Carbon example spec](specs/embodied-carbon.md) |
| Find official references and carbon data | [Resource directory](resources/data-sources.md) |
| Design dependable AI workflows | [Architecture and prompts](docs/ai-workflows.md) |
| Try something immediately | [Runnable examples](examples/README.md) |
| Prepare a pitch or handoff | [Demo template](templates/demo.md), [one-page spec](templates/project-spec.md) |

## Run the offline examples

Python 3.11+; no packages, API keys, or network calls required. From this folder:

```sh
python examples/carbon_calculator.py
python examples/application_check.py
python -m unittest discover -s tests -v
```

The carbon example demonstrates arithmetic, traceability, and rejected inputs. It does not read drawings. The application example checks a deliberately small illustrative checklist; it is not the official variance form. All example quantities, factors, and applications are synthetic. No real carbon factors or code clauses are bundled.

## Event context

The [organizer's program page](https://edmontonunlimited.com/programs/built-world-challenge/) lists an October 17 hackathon as part of an eight-week program. Follow its linked full briefs and the event team for authoritative details. This repository focuses on reusable technical help; private invitations and contact information are not reproduced.

## Contribute and reuse

Original repository content and code are MIT licensed; linked publications and third-party datasets retain their own terms. See [LICENSE](LICENSE) and [CONTRIBUTING](CONTRIBUTING.md). Source links were reviewed October 15, 2026; access, terms, and editions can change. Corrections and alternative approaches are welcome.

## Expanded reference library — 50 integration candidates

- [API/platform catalog](resources/api-catalog.md), also [JSON](resources/api-catalog.json) and [CSV](resources/api-catalog.csv)
- [Six integration recipes](docs/integration-recipes.md)
- [Domain primer and measurement traps](docs/domain-primer.md)
- [Product interviews, pilot design, and commercial hypotheses](docs/product-and-pilot.md)
- [Proposed records and endpoint contracts](contracts/README.md)
- [Data lab](data/README.md): real licensed housing tables, 60 synthetic slab cases/diagrams, and 20 failure scenarios
- [Repository split strategy](docs/repository-design.md)
- [Release scope and verification](RELEASE.md)

Optional live metadata discovery: `python examples/public_data_discovery.py --query housing --rows 3`. This performs a read-only network request to the Canadian public data catalog. Review resource licenses before downloading or reusing results.

Additional offline data exploration: `python examples/housing_summary.py` from the repository root. See [data provenance](data/README.md).

## Worked methods and more example specs

- [Drawing takeoff](docs/drawing-takeoff-method.md)
- [Code corpus and citation validation](docs/code-corpus-method.md)
- [Factor matching and substitutions](docs/factor-matching-method.md)
- [Reviewer workspace spec](specs/reviewer-workspace.md)
- [Carbon hotspot workspace spec](specs/carbon-hotspot-workspace.md)
- [Additional domain sources and acquisition priorities](resources/additional-domain-sources.md)
- [Operations and cost planning](docs/operations-and-cost.md)

Verify the complete local release: `python scripts/verify_release.py`.

## Additional runnable methods

From the repository root:

```sh
python examples/quantity_methods.py
python examples/citation_check.py
python scripts/profile_housing.py
```

The geometry helper covers slab openings, wall-layer thickness, roof slope and a documented volume-to-mass conversion. The citation lookup rejects an invented reference, wrong edition, or ambiguous match in a fictional corpus. These are small building blocks, not full extraction or compliance applications.

See [housing field profiles](data/profiles/README.md), [research datasets](resources/research-datasets.md), and [coverage map](docs/coverage-map.md).
