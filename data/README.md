# Data lab

## Included

- `synthetic/slab-cases.json` and CSV: 60 original dimension/volume reference cases, with 60 self-authored SVG diagrams. Every file is clearly synthetic and not for construction.
- `synthetic/failure-cases.json`: 20 manual evaluation scenarios. These describe expected behavior; their existence does not prove an implementation handles them.
- `third-party/nrcan-housing-archetypes/`: original upstream CSV tables and license, accompanied by commit-pinned provenance and SHA-256 hashes.

The slab fixtures test annotation and arithmetic. SVG is an openly inspectable intermediate, not the vector PDF input required by the carbon challenge. For actual PDF extraction benchmarking, obtain permissioned sponsor vector PDFs or export your own fixture drawings to PDF and record the export tool/version.

The housing archetypes support Canadian housing-context and geometry exploration. They are energy-model inputs, not a bill of quantities, EPD database, or approved construction design. Read their upstream README and column definitions before analysis. No code-book corpus, sponsor plans or real applications are included.

## License boundary

Original synthetic fixtures: repository MIT license. NRCan files: Open Government Licence Canada, with attribution and original license retained. Each data family has separate provenance. External EPD sources remain links/integration candidates; no rights-restricted bulk carbon records are copied.
