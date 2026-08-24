# report

Typed refusals and the per-file read report.

**Source**: `PHX/report.py`

---

## RefusalReason

Why a workbook was refused outright (as opposed to read with gaps).

**Inherits from**: `enum.Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `NOT_A_FILE` | `'not_a_file'` | The path does not exist or is not a regular file. |
| `NOT_A_WORKBOOK` | `'not_a_workbook'` | openpyxl could not open it as an .xlsx/.xlsm zip package. |
| `NOT_A_PHPP` | `'not_a_phpp'` | No 'Data' + 'Verification' + 'PER' worksheets; not a PHPP. |
| `VERSION_UNREADABLE` | `'version_unreadable'` | A PHPP by its sheets, but the version cell could not be parsed. |
| `VERSION_UNSUPPORTED` | `'version_unsupported'` | A PHPP whose version/language has no results map (named in the detail). |
| `BLANK_TEMPLATE` | `'blank_template'` | A PHPP with no project content (TFA 0, no building name) — identity is known, results are not read. |
| `RESULTS_REGION_EMPTY` | `'results_region_empty'` | Sniffed as a project PHPP, but every results cell is empty (no cached values). |
| `READ_ERROR` | `'read_error'` | openpyxl raised while reading a bounded cell (malformed sheet XML, ...); named, not propagated. |

---

## Refusal

A typed, loud refusal to read a workbook.

---

## UnreadItem

One thing the reader wanted and did not get.

---

## ReadReport

What one read of one file did: read, not read, and why.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `ok` | — | True when the file was not refused. |

### Methods

#### summary()

Return a one-paragraph plain-text summary of the report.

---
