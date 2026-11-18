# Specialist: Import, Export and Data Portability

Provide data movement only when users or operations need it.

Define supported formats, schema/versioning, size limits, validation, preview, duplicate handling, partial failures, rollback, progress, cancellation and audit records. Treat uploaded files as untrusted. Protect against malicious files, formula injection, archive bombs and excessive resource use.

Exports must respect authorization and data minimization. Explain what is included, omit secrets, and provide appropriate expiry and access controls for generated files.

## Applied verification

Parse the downloaded artifact and compare its records, schema version, filters and authorization scope with the requested snapshot. Test formula-like text, interrupted import and duplicate rows; a download event alone proves neither content nor integrity.

## Format and transaction boundaries

For large imports, separate schema/encoding validation, preview and column mapping, resumable commit, error reporting and reversal. Preserve stable IDs and related records for round trips. CSV quoting alone does not neutralize spreadsheet formulas: choose an export policy for formula-significant cells and test the intended spreadsheet application. Bound rows, memory, file size and signed-download lifetime. Use NDJSON or a versioned archive manifest when streaming or multiple linked records justify it.

## Receipts and printable exports

When users request a receipt, produce a readable document in the requested format and keep raw data export explicit. Use a stable document number for the same underlying record, show it in the document and use it in the default download filename. Scope generated numbers to the record and environment; avoid putting private addresses or credentials in filenames. A changed status updates the record without inventing a new receipt identity. Preserve existing files when a CLI export repeats, and report the saved path.

Verify the actual document format and content, filename, repeated-export identity and distinct-record identity. A successful download or a renamed JSON file does not prove that a printable receipt was produced.
