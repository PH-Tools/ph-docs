# results_map

Where the headline results live, per PHPP version — with the caption each value must sit beside.

**Source**: `PHX/results_map.py`

---

## ValueKind

How to interpret a result cell.

**Inherits from**: `enum.Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `NUMBER` | `'number'` | A numeric result; a '-' string means 'not applicable' in this workbook state. |
| `TEXT` | `'text'` | A selector string (ie: '10-Passive House'). |

---

## ResultCellSpec

One results-set item: value cell + the caption that must sit beside it.

---

## ResolvedMap

A results map picked for a version, with its provenance.

---
