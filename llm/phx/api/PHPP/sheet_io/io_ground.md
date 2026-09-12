# io_ground

Controller Class for the PHPP "Ground" worksheet.

**Source**: `PHX/io_ground.py`

---

## Ground

IO Controller for the PHPP "Ground" worksheet.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |

### Methods

#### find_section_header_row(_row_start, _row_end)

Return the row number of the 'Floor slab type' header, which every input row is offset from.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_start` | — | — |
| `_row_end` | — | — |

#### write_foundation(_foundation_block)

Write one foundation into building section 1.

| Arg | Type | Description |
|-----|------|-------------|
| `_foundation_block` | — | — |

---
