# Integration recipes

These are implementation designs. The offline clients demonstrate public discovery; commercial service credentials and sponsor data are intentionally absent. Consult each provider's current official documentation in the [catalog](../resources/api-catalog.md).

## 1. EPD search and reviewed factor import

Input: material category, geography, target unit, module boundary, product constraints, assessment date. Query an authorized EPD service through a server-side adapter. Retain provider record id and version. Present candidates with product, unit, modules, geography, validity, source, and license. Require a human match decision before committing a factor.

Normalize to a factor record, not a bare floating-point value. Retain the original declared-unit description and GWP indicator name. Do not merge EN15804+A1 and +A2 results without an agreed methodology. Do not replace expired records silently. Cache only where the agreement permits it. A provider outage should leave existing licensed records usable only within their permitted terms and return an explicit unresolved state for new lookups.

Adapter contract: `search(query) -> candidates`; `fetch(id,version) -> record`; `normalize(record) -> FactorCandidate`. Authentication belongs in the server process. Respect provider retry guidance and stop on authorization failures. Store request metadata without secrets or document text.

## 2. Cloud document extraction

Input: an authorized PDF and extraction purpose. Record file hash, revision and page count. Confirm region and retention before upload. Select read/layout capability and poll the returned operation handle rather than resubmitting long jobs. Normalize page numbers, page dimensions, text spans and polygons into the same internal coordinate system.

Output: `Document -> Page -> Block -> SourceAnchor`. Extraction confidence helps triage; it does not validate the measured dimensions. Overlay extracted text on the original page. A user confirms conflicting dimensions and flags missing details. Add duplicate-hash detection and a per-job cost limit before batch processing.

## 3. Local vector PDF workflow

Extract text and lines with pdfplumber; render/overlay using PDF.js in a web implementation. Preserve crop box, page rotation and PDF point dimensions. Convert points to screen coordinates through a documented transform. Use written dimensions as evidence; use scaled geometry only after confirming calibration and view scale. Different views on the same sheet can use different scales.

Build a single slab or wall example before attempting an entire house. Sections determine thickness and assembly layers; plan geometry alone is insufficient. Keep inferred and assumed quantities visible. Deduplicate assemblies across plan, elevation and section views.

## 4. Government catalog discovery

Use CKAN `package_search` to locate datasets, then inspect `package_show` resources and the license. A catalog record is not necessarily the data itself. Validate publisher, update frequency, column definitions, geographic coverage and resource format before ingestion. Check CKAN's JSON `success` flag even with HTTP 200.

For Socrata, first discover the dataset id and column names. Query a small page with selected columns; use stable ordering for pagination. Do not infer engineering suitability, legal status or approval precedent from permit records. Market context is a separate feature from the two core challenge pipelines.

## 5. BIM extension

If later work accepts IFC, use IfcOpenShell for object identifiers, properties, units and geometry. Distinguish gross/net area, openings and quantity-set reliability. Reconcile IFC quantities with an independent reference. Autodesk APS and Speckle are possible interoperability paths when users already hold suitable accounts and authorized models. They do not replace the event's PDF input requirement.

## 6. Export and handoff

Generate a structured JSON/CSV record first, then a human-readable report. Include scope, revision, sources, assumptions, unresolved items and reviewer status. A carbon report must identify partial coverage. A code package must retain draft status and the selected form/edition. Treat export as a snapshot tied to calculation and source versions.
