# Implementation contracts

These are proposed records and endpoint boundaries, not an externally hosted API. Use them to keep team work parallel and to preserve provenance.

## Records

`SourceAnchor`: document_id, revision, page (1-based), region coordinate system, bbox, source_text, hash.

`Quantity`: id, assembly_id, material_category, numeric value, unit, basis, source_anchors, assumptions, review_status, revision.

`FactorCandidate`: id, provider, provider_version, product, declared_unit, indicator, modules, geography, valid_from, valid_until, source_url, rights, value, match_status.

`Finding`: requirement_id, status, evidence_ids, source_requirement_id, explanation, next_action, reviewer_id, reviewed_at.

`CalculationSnapshot`: id, input revisions, quantity ids, factor versions, conversions, totals, intensity basis, exclusions, unresolved items, algorithm version.

## Suggested endpoints

| Method / route | Purpose | Result |
| --- | --- | --- |
| POST /documents | Register authorized upload | document id + job id |
| GET /jobs/{id} | Poll extraction status | queued/running/succeeded/failed + diagnostics |
| GET /documents/{id}/anchors | Read source locations | versioned anchors |
| PATCH /quantities/{id} | Human correction with expected revision | new revision or 409 conflict |
| POST /factor-search | Query authorized providers | candidate records with access provenance |
| POST /factor-matches | Confirm reviewed match | versioned selection |
| POST /calculations | Compute compatible reviewed records | snapshot or explicit validation errors |
| POST /applications/check | Apply reviewed checklist | findings with unresolved states |
| GET /exports/{snapshot_id} | Export immutable result | structured/human-readable files |

Validate input types, finite numbers, nonempty source references, known units and scope. Require expected revision for updates. Associate access checks with every document id; knowing an id must not grant access. Error responses should carry a stable code, field path, user action and correlation id; do not leak private source content.
