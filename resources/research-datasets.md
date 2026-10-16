# Further research datasets and acquisition paths

These sources extend the practical data directory. Their presence here does not mean their contents are bundled or their use is permitted in every project. Review the linked primary source and its exact version before downloading.

| Resource | Useful experiment | Format / access | Key limitation |
| --- | --- | --- | --- |
| [CubiCasa5K](https://github.com/CubiCasa/CubiCasa5k) | Floor-plan semantic recognition and annotation research | Dataset download linked from the project | [Project license](https://github.com/CubiCasa/CubiCasa5k/blob/master/LICENSE) states CC BY-NC 4.0; do not assume a commercial-use right |
| [FloorPlanCAD](https://floorplancad.github.io/) | CAD symbol recognition and vector drawing research | Follow official dataset instructions | Verify the distribution agreement and annotations; CAD symbols are not complete material takeoff ground truth |
| [buildingSMART certification datasets](https://github.com/buildingSMART/Certification-datasets) | IFC import and schema/interoperability testing | Versioned example files | Repository formerly linked as Sample-Test-Files redirects here; review file-level rights and purpose. IFC is an extension beyond the event's PDF input |
| [ecoinvent access and licensing](https://support.ecoinvent.org/licensing) | Background inventory for an advanced LCA workflow | Licensed database access | Access, integration and redistribution rights are agreement-specific; no database records are included |
| [CLF North American baselines](https://carbonleadershipforum.org/clf-north-american-material-baselines/) | Industry-average factor selection and comparison research | Official workbook download route | Preserve indicator, declared unit, geography, version, attribution and share-alike terms |

## How to choose a dataset

For immediate event work, permissioned sponsor plans and reference quantities are more directly relevant than a large generic plan-image corpus. Use generic corpora to test a specific perception component, then separately validate on the actual PDF drawings and assembly requirements. Keep training, tuning and final evaluation splits distinct, including at the plan-family level.

Do not train on the same plan variants later used as an unseen benchmark. Preserve the source dataset's license alongside derived annotations and model-training records. A public repository URL does not itself establish a dataset license or a right to commercialize its contents.
