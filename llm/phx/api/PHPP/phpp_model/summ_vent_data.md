# summ_vent_data

Model class for the PHPP 'SummVent' summer heat-recovery mode.

**Source**: `PHX/summ_vent_data.py`

---

## SummVentExportError

Raised when a summer heat-recovery mode cannot be mapped to PHPP.

**Inherits from**: `ValueError`

---

## SummerHrvMode

A PHX summer heat-recovery mode mapped to the PHPP 'SummVent' checkbox group.

### Methods

#### create_xl_items(_sheet_name, _header_row)

Return the four checkbox XlItems located relative to the section header row.

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | — |
| `_header_row` | — | — |

---
