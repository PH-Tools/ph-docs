# ground_data

Model class for the PHPP 'Ground' worksheet: one PHX foundation as building-section-1 inputs.

**Source**: `PHX/ground_data.py`

---

## GroundExportError

Raised when a PHX foundation cannot be written to the PHPP 'Ground' worksheet.

**Inherits from**: `Exception`

---

## GroundFoundationBlock

One PHX foundation, plus the site's soil, as the inputs of PHPP 'Ground' building section 1.

### Methods

#### create_xl_items(_sheet_name, _header_row)

Return the XlItems for the foundation, located relative to the 'Floor slab type' header row.

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | The name of the worksheet to write to. |
| `_header_row` | — | The worksheet row of the located 'Floor slab type' header. |

---
