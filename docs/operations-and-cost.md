# Operations and cost planning

## Budget a case

Record pages processed, OCR calls, model input/output tokens, retries, embedding work, factor requests, storage and human correction minutes. Multiply each by the current provider price, then include recurring platform/database fees and support. Use measured low/typical/high cases rather than assuming every plan has the same complexity. This kit avoids fixed vendor prices because they change and vary by agreement.

## Document job state

Use queued → running → succeeded/failed/cancelled. Persist the provider operation id and poll it. Deduplicate retries using document hash plus pipeline configuration. Retry transient throttling with provider guidance; do not retry authorization errors indefinitely. Keep extraction completion separate from human-review completion.

## Revision management

Hash source documents; assign immutable revisions. Quantity changes invalidate downstream calculations. Factor updates create a new version while previous snapshots retain their original factor reference. A comparison should identify which geometry, product, factor or method changed.

## Sharing and access

Separate public examples from sponsor material. Define permissions for applicant, estimator, reviewer and administrator. Check document ownership on every endpoint. Review cloud retention and deletion requirements with the data owner before uploading. Store secrets outside Git, and avoid recording them in request logs.

## Accessibility and usability

Provide a table alternative for drawing overlays, keyboard navigation, readable focus states, labels that do not rely on colour, and error messages that identify the action needed. Reviewers should be able to open a source alongside a finding without losing their place.

## Release checklist

New teammate can run it; current dependencies are locked; synthetic and real data are distinguished; source permissions are documented; a domain reviewer has checked intended claims; failure states are demonstrated; job costs are bounded; exported snapshots include versions and exclusions; private files and secrets are absent from the public commit.
