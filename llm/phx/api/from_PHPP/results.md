# results

Read the headline results of a closed PHPP into a typed record, or refuse by name.

**Source**: `PHX/results.py`

---

## ValueStatus

What happened when one results cell was read.

**Inherits from**: `enum.Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `OK` | `'ok'` | Caption matched, value present and of the expected kind. |
| `NOT_APPLICABLE` | `'not_applicable'` | Caption matched; PHPP shows '-' (ie: cooling demand without mechanical cooling). |
| `EMPTY` | `'empty'` | Caption matched; the cell has no cached value. |
| `LABEL_MISMATCH` | `'label_mismatch'` | The caption beside the cell is not the one expected — value not trusted, not returned. |
| `SHEET_MISSING` | `'sheet_missing'` | The worksheet is not in this workbook. |
| `TYPE_MISMATCH` | `'type_mismatch'` | A number was expected and something else was cached. |

---

## ResultValue

One headline value with its provenance.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `source` | — | 'Sheet!cell' for display. |

---

## ResultsRecord

The headline results of one PHPP save, every value with its source cell.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `ok_keys` | — | Keys read with status OK. |

### Methods

#### get(key)

Return the value for a key, or None if it was not read OK.

| Arg | Type | Description |
|-----|------|-------------|
| `key` | — | — |

---

## ReadResult

What 'read_results()' returns: a record or a refusal, and always a report.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `ok` | — | True when a record was produced. |

---
