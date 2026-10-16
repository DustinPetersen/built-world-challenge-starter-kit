# API, platform, and integration catalog

50 curated candidates across 10 categories. These include live APIs, local libraries, downloadable tools and reference hubs; interface types and access requirements are explicit. Core identifies candidates relevant to an initial implementation; Extension is optional. Documentation was reviewed October 15, 2026. No authenticated vendor integration was executed. Pricing and entitlement details must be reconfirmed with providers.

Machine-readable versions: [JSON](api-catalog.json), [CSV](api-catalog.csv).

## Carbon

| Candidate | Interface / access | Useful for | Limitation |
| --- | --- | --- | --- |
| [EC3 API](https://docs.buildingtransparency.org/ec3/api-and-integrations) | Authenticated REST; Account and current API agreement | EPD discovery and factors | Confirm current entitlements; pricing page and older docs can differ. No EC3 records bundled. |
| [EC3 API terms and pricing](https://www.buildingtransparency.org/api-access-pricing/) | Access policy; Provider agreement | Plan integration and caching rights | Do not assume website access includes API, caching or production rights. |
| [openEPD example client](https://github.com/cchangelabs/python-openepd-sample) | Schema / REST client example; Provider account for live access | Study structured EPD exchange | Schema openness does not license underlying data. |
| [ÖKOBAUDAT developer interface](https://www.oekobaudat.de/anleitungen/softwareentwickler.html) | soda4LCA / ILCD+EPD; Read current service terms | Explore structured construction LCA records | German geography; preserve EN15804 version and indicator definitions. |
| [ÖKOBAUDAT downloads](https://www.oekobaudat.de/en/service/downloads.html) | CSV / ILCD+EPD archive; Download and dataset terms | Bulk research candidate | Check dataset-specific rights and system boundary before importing. |
| [International EPD System library](https://www.environdec.com/library) | Search / published declarations; Library access; integration rights to confirm | Find original product declarations | No general unrestricted API entitlement is asserted. |
| [Federal LCA Commons](https://www.lcacommons.gov/) | Dataset repositories; Per-dataset metadata and terms | US background inventory research | Inventory flows are not automatically ready-made Canadian A1-A3 factors. |
| [openLCA](https://www.openlca.org/) | Desktop LCA software; Software and database licenses differ | Independent calculation workflow | Installing software does not grant access to licensed databases. |
| [NRCan MCE2](https://prod-natural-resources.azure.cloud.nrcan-rncan.gc.ca/maps-tools-publications/tools-applications/material-carbon-emissions-estimator-mce2) | Downloadable workbook; Review download terms | Canadian residential comparisons | Not documented here as an HTTP calculation API. |
| [Brightway](https://docs.brightway.dev/) | Python LCA framework; Software and inventory licenses differ | Advanced LCA experimentation | Requires methodology expertise; not a quick factor lookup substitute. |
| [Athena Impact Estimator](https://www.athenasmi.org/our-software-data/impact-estimator/) | Desktop tool; Review software/data terms | Independent North American assessment comparison | Not asserted to expose a public calculation API. |

## Method

| Candidate | Interface / access | Useful for | Limitation |
| --- | --- | --- | --- |
| [NRC whole-building LCA guidelines](https://nrc-publications.canada.ca/eng/view/object/?id=f7bd265d-cc3d-4848-a666-8eeb1fbde910) | Publication; Publisher terms | Method and reporting basis | Use latest applicable guidance; partial prototype is not certified wbLCA. |
| [EPA greener products resources](https://www.epa.gov/greenerproducts) | Reference portal; Publication-specific terms | US procurement context | US policy references are not Alberta legal requirements. |

## Data

| Candidate | Interface / access | Useful for | Limitation |
| --- | --- | --- | --- |
| [NRCan housing archetypes](https://github.com/canmet-energy/housing-archetypes) | CSV / HOT2000 models; Open Government Licence Canada | Housing geometry/context research | Energy archetypes are not material quantity ground truth. |
| [Edmonton Open Data](https://data.edmonton.ca/) | Socrata portal; Dataset-specific metadata and city terms | Permit and city context | Permits do not supply code approval precedent or full plan drawings. |
| [Socrata developer API](https://dev.socrata.com/) | REST / SoQL; Dataset and platform terms; app token optional by service | Query public municipal tables | Verify dataset id, schema and limits before use. |
| [CKAN Action API](https://docs.ckan.org/en/2.11/api/) | JSON RPC-style HTTP; Public reads vary by portal | Discover government datasets | HTTP 200 can contain success=false; check both. |
| [Statistics Canada WDS](https://www.statcan.gc.ca/en/developers/wds) | Web data service; Statistics Canada terms | Market/context statistics | Statistics are not project-specific quantities. |
| [ArcGIS feature query](https://developers.arcgis.com/rest/services-reference/enterprise/query-feature-service-layer/) | REST feature service; Service permissions and dataset terms | Spatial context | Handle pagination and spatial reference explicitly. |

## Codes

| Candidate | Interface / access | Useful for | Limitation |
| --- | --- | --- | --- |
| [Alberta codes and standards](https://www.alberta.ca/building-codes-and-standards) | Official reference hub; Publication-specific terms | Edition and printing selection | Applicability requires project-specific confirmation. |
| [Alberta building STANDATA](https://www.alberta.ca/building-standata) | Reference notices; Government publication terms | Find relevant interpretation and notices | Track supersession and effective dates. |
| [Safety Codes Council variances](https://www.safetycodes.ab.ca/permits-inspections/variances/) | Process and form; Council terms | Workflow and form discovery | Public form access is not an approval API. |

## Documents

| Candidate | Interface / access | Useful for | Limitation |
| --- | --- | --- | --- |
| [Azure Document Intelligence](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/) | Cloud REST / SDK; Azure identity/resource; metered | OCR and layout extraction | Text/layout output does not establish drawing geometry accuracy. |
| [Google Document AI](https://docs.cloud.google.com/document-ai/docs) | Cloud REST / SDK; Cloud project, IAM, processor; metered | OCR and structured extraction | Check processor location, retention and supported files. |
| [Amazon Textract](https://docs.aws.amazon.com/textract/) | Cloud API / SDK; AWS IAM; metered | Text, forms and tables | Compare synchronous and asynchronous limits before design. |
| [PDF.js](https://mozilla.github.io/pdf.js/) | Browser library; Open-source library terms | PDF viewing and overlays | Define page rotation and coordinate transforms. |
| [pdfplumber](https://github.com/jsvine/pdfplumber) | Python library; Open-source library terms | Vector text, lines and tables | Not automatic semantic quantity extraction. |
| [Docling](https://docling-project.github.io/docling/) | Local document conversion toolkit; Code and model licenses | Structured document conversion | General document parsing is not validated drawing takeoff. |
| [Unstructured](https://docs.unstructured.io/) | API / document processing; Service credentials; deployment-specific terms | Partition documents into elements | Preserve source positions and evaluate plan-specific behavior. |
| [PyMuPDF](https://pymupdf.readthedocs.io/) | Python PDF library; Review AGPL/commercial licensing options | PDF rendering and extraction | Choose a compatible license before redistribution in an app. |
| [Tesseract OCR](https://tesseract-ocr.github.io/) | Local OCR engine; Open-source engine/model terms | Raster text recognition | OCR cannot recover missing drawing geometry or validate scale. |

## BIM

| Candidate | Interface / access | Useful for | Limitation |
| --- | --- | --- | --- |
| [IfcOpenShell](https://docs.ifcopenshell.org/) | Python / native library; Open-source project terms | IFC properties and geometry | Official carbon challenge uses PDF; BIM is an extension path. |
| [Autodesk Model Derivative](https://aps.autodesk.com/developer/overview/model-derivative-api) | Cloud REST; APS app/OAuth and service entitlement | Translate/view design models | Not required for the PDF-first event workflow. |
| [Speckle](https://docs.speckle.systems/) | Platform / connectors; Deployment and access-token terms | Interoperability and model collaboration | Verify connector compatibility and project permissions. |
| [IfcTester](https://docs.ifcopenshell.org/ifctester.html) | IFC validation toolkit; Project license | Check model information requirements | IFC information checks do not establish building-code compliance. |

## Build

| Candidate | Interface / access | Useful for | Limitation |
| --- | --- | --- | --- |
| [FastAPI](https://fastapi.tiangolo.com/) | Python framework; Open-source project terms | Typed backend endpoints | Application auth and document protection remain your responsibility. |
| [Streamlit](https://streamlit.io/) | Python UI; Framework vs hosting terms differ | Rapid review UI | Do not upload restricted sponsor plans to a public app. |
| [Pydantic](https://docs.pydantic.dev/latest/) | Python validation; Open-source project terms | Validate extraction contracts | Valid shape does not mean factually correct. |

## AI

| Candidate | Interface / access | Useful for | Limitation |
| --- | --- | --- | --- |
| [OpenAI Responses API](https://developers.openai.com/api/reference/responses/overview) | Cloud REST / SDK; Provider account and API key; metered | Structured extraction and evidence-linked drafting | Evaluate models on authorized inputs; API access and ChatGPT subscriptions differ. |
| [Claude API](https://platform.claude.com/docs/en/api/overview) | Cloud REST / SDK; Provider account and credentials; metered | Document reasoning and structured candidate extraction | Verify current model capabilities, limits and data terms. |
| [Gemini API](https://ai.google.dev/gemini-api/docs) | Cloud REST / SDK; Project credentials and applicable tier | Multimodal extraction experiments | Validate page grounding; do not infer dimensional accuracy from vision capability. |
| [Microsoft Foundry model inference](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview) | Cloud inference service; Azure project, deployment and identity | Use existing cloud governance | Model availability and terms vary by deployment. |
| [Ollama](https://docs.ollama.com/) | Local runtime / API; Local compute and model license | Offline/private model experimentation | Hardware capacity and model-specific terms still apply. |
| [Cohere](https://docs.cohere.com/) | Cloud REST / SDK; Provider account and credentials | Embedding/reranking candidates | Evaluate retrieval quality separately from generation. |
| [Mistral AI](https://docs.mistral.ai/) | Cloud REST / SDK; Provider account and credentials | OCR and model alternatives | Confirm OCR output anchors and accepted file limits. |

## Retrieval

| Candidate | Interface / access | Useful for | Limitation |
| --- | --- | --- | --- |
| [pgvector](https://github.com/pgvector/pgvector) | Postgres extension; Database deployment and project license | Filtered vector retrieval | Filter edition/jurisdiction before presenting source candidates. |
| [Qdrant](https://qdrant.tech/documentation/) | Vector database / API; Local deployment or cloud account | Metadata-filtered evidence search | A nearest-neighbour result is not proof of code applicability. |
| [Chroma](https://docs.trychroma.com/) | Vector database / client; Deployment-specific terms | Prototype retrieval | Keep source manifest and deletion/version propagation. |

## Workflow

| Candidate | Interface / access | Useful for | Limitation |
| --- | --- | --- | --- |
| [Microsoft Graph](https://learn.microsoft.com/en-us/graph/overview) | REST / SDK; Entra app, delegated/application permissions | Approved document-storage integration | Use least privilege; tenant consent and data access are separate from E5 licensing. |
| [Procore developer platform](https://developers.procore.com/) | Construction platform APIs; Developer app/OAuth and customer authorization | Later construction-workflow integration | Do not make integration a dependency for the event demo. |
