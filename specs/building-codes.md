# Example spec: Evidence-backed application preparation

**Status:** volunteer proposal for a narrow prototype. Consult the [official brief](https://edmontonunlimited.com/wp-content/uploads/2026/09/Building-Codes-Challenge-with-Appendix-.pdf) for the complete scope. The brief includes guided preparation, code identification, professional involvement, reviewer support, and form export. This spec is a suggested first slice.

## User and outcome

An applicant preparing one Alberta alternative-solution package can see what information is missing and why; a reviewer can inspect the same evidence trail. Success is a clearer package with fewer avoidable information gaps. Approval remains with authorized decision-makers.

## First slice

One organizer-confirmed form version, one application category, one reviewed code corpus. Input project facts, a proposed alternative, and evidence references. Output a draft structured package and a gap report with source locations. A filled field is recorded as present, not certified sufficient.

## Data contract

Project: id, jurisdiction, permit context, code edition/printing, building characteristics, applicant-provided facts.

Requirement: id, source document/version, section/page, required fields, applicability status, reviewer confirmation.

Evidence: id, document hash, page/section, short excerpt where permitted, linked claim, provenance.

Finding: requirement id, status (`missing`, `present_unverified`, `needs_review`), evidence ids, explanation, next action, human disposition.

## Acceptance criteria

| ID | Given / when | Expected |
| --- | --- | --- |
| BC-01 | Required project context is absent | Ask a focused question; preserve unknown values |
| BC-02 | A code reference is proposed | Verify it against the selected edition; show location and relevance for review |
| BC-03 | A reference cannot be verified | Label unresolved and exclude it from verified attributions |
| BC-04 | Evidence is attached | Show source location and mark presence separately from adequacy |
| BC-05 | A project changes jurisdiction or edition | Invalidate affected checks and require review |
| BC-06 | Supporting analysis needs professional judgment | Flag professional review; do not invent an engineering conclusion |
| BC-07 | Applicant corrects a fact | Preserve prior value, author/time, and recompute affected findings |
| BC-08 | Reviewer opens a gap | Original evidence and the requirement are reachable together |
| BC-09 | Input contains instructions to ignore checks | Treat them as document content; continue the configured checklist |
| BC-10 | Export is requested | Include unresolved issues, edition, sources, and draft status |

## Demonstration

Start with a synthetic incomplete proposal, produce two gaps, add evidence, then show one gap resolved as present but still unverified. Display an intentionally invalid citation as unresolved. Ask an expert whether the checklist and handoff match their real workflow.

## Expansion after validation

Map fields to the official template rather than claiming this example matches it. Add verified attribution tables, jurisdiction adapters, controlled form export, and revision comparisons. Have a qualified domain reviewer assess applicability and professional involvement triggers before using real applications.
