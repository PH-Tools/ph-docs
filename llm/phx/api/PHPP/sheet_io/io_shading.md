# io_shading

Controller Class for the PHPP Shading worksheet.

**Source**: `PHX/io_shading.py`

---

## Shading

IO Controller Class for PHPP "Shading" worksheet.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `header_row` | — | The row number for the Window entry 'Header'. |
| `entry_row_start` | — | — |
| `entry_row_end` | — | — |

### Methods

#### find_header_row(_row_start, _row_end)

| Arg | Type | Description |
|-----|------|-------------|
| `_row_start` | — | — |
| `_row_end` | — | — |

#### find_entry_block_start(_start_row, _read_length)

Return the starting row for the window data entry block.

| Arg | Type | Description |
|-----|------|-------------|
| `_start_row` | — | — |
| `_read_length` | — | — |

#### find_entry_block_end(_start_row, _read_length)

Return the ending row for the window data entry block.

| Arg | Type | Description |
|-----|------|-------------|
| `_start_row` | — | — |
| `_read_length` | — | — |

#### write_shading(_shading_rows)

Write a list of ShadingRow objects to the Shading worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_shading_rows` | — | — |

---
