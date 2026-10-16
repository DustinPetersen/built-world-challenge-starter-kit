# Worked method: drawing geometry to a reviewed quantity

## Use a narrow reference case

Start with a rectangular slab, then add one opening, then one revision. Each additional feature introduces a separately testable geometry rule. Keep scope visible in the UI; drawing recognition and arithmetic are different capabilities.

## 1. Inspect the file

Record hash, revision, page size, crop box, rotation, text presence and layer information if available. Identify floor plans, sections and schedules. A PDF can contain vector text over a raster image; text presence alone does not mean usable vector geometry. Flag encrypted, corrupt or unsupported documents explicitly.

## 2. Define source anchors

Use page number and bounding boxes with a declared coordinate basis. PDF points, normalized coordinates and screen pixels must not be mixed. Save the original transform and page dimensions so overlays survive resizing. Test rotations of 0/90/180/270 degrees and crop offsets.

## 3. Establish dimensions

Prefer explicit written dimensions linked to the relevant geometry. If measuring from vectors, confirm scale for that specific view with a known dimension; do not use the title-block scale for every detail on a mixed-scale sheet. Store measurement origin, scale basis, and reviewer confirmation. OCR can confuse 8 and 3 or omit a decimal; display the evidence.

## 4. Compute a known slab

Synthetic inputs: length 10 m, width 8 m, thickness 100 mm. Convert thickness: 100/1000 = 0.1 m. Gross area = 80 m2. Gross volume = 8 m3. If a fully penetrating 1 m × 2 m opening is included, net area = 78 m2 and net volume = 7.8 m3. Keep an explicit openings policy. Footings and foundation walls remain separate assemblies.

Store each input dimension and formula. The derived volume should not be editable without deciding whether the user is overriding a dimension or the final quantity. Preserve both the extracted and accepted records.

## 5. Expand assemblies

For a wall, establish length, height, openings and assembly layers from appropriate details. Area-based layers use net area under a declared policy. Volume-based layers also require thickness. Framing needs a defensible framing/spacing method and openings treatment; do not assume area alone establishes lumber volume. Roof slope and overhangs require separate geometry. Windows are commonly schedule-driven and need type/count reconciliation.

## 6. Validate against an independent reference

Compare each quantity with a reference prepared by an estimator, not with another pass through the same extraction algorithm. Report absolute error, relative error where the reference is nonzero, source coverage, and correction count. Separately score assembly classification, dimensions and quantity calculations.

## 7. Handle revisions

Link quantities to the exact document revision. A changed section thickness can affect many plan instances. Mark affected results stale and require revalidation. Mirrored geometry may preserve area while changing openings or elevations; reuse only reviewed invariants.
