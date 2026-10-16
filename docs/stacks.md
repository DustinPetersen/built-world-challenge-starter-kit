# Stack options

Recommendations are volunteer judgments. Choose existing team skills. Install supported versions, consult current documentation, and commit a lockfile in your implementation.

| Team | Suggested stack | Why / tradeoff |
| --- | --- | --- |
| Python/data beginners | Streamlit + Python + SQLite + JSON files | Quick forms and editable tables; custom drawing interactions require more work |
| Web developers | React/TypeScript + PDF.js + FastAPI + SQLite | Strong source highlighting and review UI; more integration work |
| Document/ML specialists | Python extraction pipeline + FastAPI + thin review UI | Clear separation of parsing, validation, and user corrections; avoid pipeline complexity before one case works |
| Product/design team | Clickable prototype + manually prepared reference outputs | Tests usability and value immediately; explicitly disclose manual processing |

## Building blocks

- [Streamlit](https://streamlit.io/): Python data app UI.
- [FastAPI](https://fastapi.tiangolo.com/): API boundary for extraction jobs and validated responses.
- [PDF.js](https://mozilla.github.io/pdf.js/): browser PDF rendering and coordinates.
- [pdfplumber](https://github.com/jsvine/pdfplumber): PDF text, tables, lines, and coordinates. Evaluate on actual vector plans; text extraction alone is not takeoff.
- [Pydantic](https://docs.pydantic.dev/latest/): typed validation for structured pipeline records.
- SQLite or JSON: sufficient for a single-user prototype; add a shared database when collaboration requires it.

## AI and hosting choices

Use an approved model endpoint already available to the team. Compare candidate models on the same small evaluation set: evidence accuracy, extraction quality, latency, and cost per document. Keep provider-specific calls behind a small adapter. Never put API secrets in browser code or the repository.

Start with local processing and synthetic inputs. Before cloud upload of sponsor plans, confirm authorization, retention, and model-provider terms. Add a page limit, timeout, and spending cap. Cache permitted extraction results by document hash and pipeline version.

## Architecture boundaries

UI → document intake → extraction → validated records → human review → deterministic checks/calculations → export.

For codes, use searchable source passages and exact attribution lookup tables before adding a vector database. For carbon, keep factors in versioned records; calculations consume approved quantities and compatible factors. Queue long jobs only when synchronous processing becomes a measured problem.
