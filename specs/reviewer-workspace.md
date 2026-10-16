# Example spec: reviewer evidence workspace

User: a reviewer assessing whether an application package contains the information needed for review. First slice: one package with ten domain-reviewed checklist items.

## Interaction

Left pane: original application and attachments. Right pane: requirement, finding, linked evidence and applicant response. A reviewer can confirm evidence presence, request clarification or mark an applicability question. No model output becomes an official decision.

## Acceptance cases

- Open a finding and see the cited page and exact relevant region.
- Distinguish missing evidence, present evidence and unresolved adequacy.
- Record a reviewer correction without overwriting the original extraction.
- Change source revision and mark affected findings stale.
- Export a concise information-request list with stable item ids.
- Prevent a user without document permission from loading the source.

## Implementation

Use PDF.js for viewing and a typed backend record for each finding. Anchor coordinates to a source revision. Start with a manually reviewed checklist. Evaluate time to locate evidence, missed gaps, false alarms and reviewer correction count on unseen cases.

## Failure demonstration

Attach an irrelevant document with a plausible filename. The tool must not mark the technical case adequate simply because an attachment exists. Show where the reviewer records the remaining question.
