# Repository organization

Keep one repository initially so participants can find the full kit through one link. The directories form separable modules:

| Module | Content | Split when |
| --- | --- | --- |
| Resource hub | docs, specs, resources, templates | Remains the public entry point |
| Data lab | data, provenance, synthetic benchmark | Dataset release cadence or size needs independent versioning |
| Starter implementations | examples, contracts, tests | Teams maintain deployable applications with their own dependencies |

If splitting later, use `built-world-resources`, `built-world-data-lab`, and separate team implementation repos. Keep a versioned manifest in the hub linking compatible releases. Never create a public data repository for sponsor material unless authorized. Large licensed datasets can be acquired through documented scripts rather than duplicated.

This release is a ZIP of a single coherent repository. It contains no Git history, account details or credentials. `PUBLISH.md` explains publication. The additional materials expand the original kit without removing its beginner entry points.
