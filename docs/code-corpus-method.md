# Worked method: build a source-grounded code corpus

This is a proposed retrieval design, not regulatory interpretation. Establish applicability with qualified reviewers and the responsible authority. Use [Alberta's official hub](https://www.alberta.ca/building-codes-and-standards), [STANDATA](https://www.alberta.ca/building-standata), and the organizer-provided package.

## Source manifest

For each document: publisher, title, edition, printing, amendment date, retrieval date, source URL, hash, permitted use, and domain-review status. Keep source rights explicit. Public reading access is not automatically permission to publish an extracted code corpus.

## Structure-aware ingestion

Extract headings, article identifiers, tables, notes and cross-references while preserving their hierarchy. A table detached from its heading may lose the condition that makes it applicable. Keep parent context and page references. Detect repeated headers and broken OCR. Represent missing or ambiguous identifiers as ingestion errors.

Suggested record: `source_id`, `edition`, `printing`, `division`, `part`, `section`, `article`, `paragraph`, `text`, `page_start`, `page_end`, `parent_id`, `cross_references`, `rights`.

## Candidate retrieval and deterministic attribution

Filter to the confirmed corpus version, then search keywords or embeddings. Keep candidate selection separate from the verified lookup of objective/function/intent relationships. Store those relationships as reviewed data. Have the UI show the exact provision and its context, proposed relevance, and unconfirmed applicability.

## Citation verification

Resolve every cited identifier against the corpus; reject missing identifiers; open the cited location; confirm the excerpt exists in the selected source version. A working URL alone is insufficient: it must point to the supporting provision. Preserve reviewer corrections as explicit data rather than relying on a prompt to remember them.

## Product evidence

The [CCMC registry guidance](https://www.cnrc.canada.ca/en/certifications-evaluations-standards/canadian-construction-materials-centre/about-ccmc-registry-product-assessments) explains how product assessments include conditions and limitations. Use the exact product and current assessment context; a matching product name alone cannot establish applicability. Registry access and reproduction restrictions must be reviewed before ingestion. No CCMC assessments are redistributed in this kit.

## Evaluation set

Include a valid reference, real but irrelevant reference, obsolete edition, altered article number, nearby table with a different applicability condition, missing attribution, and a proposal requiring professional analysis. Ask a reviewer to assess citation correctness and applicability separately. Measure whether users can locate evidence and correct errors quickly.
