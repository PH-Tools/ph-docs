# xl_readable

Read-side Protocol for the Excel-interop layer.

**Source**: `PHX/xl_readable.py`

---

## XLReadable

The minimal read-only surface shared by the xlwings and openpyxl backends.

**Inherits from**: `Protocol`

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `worksheet_names` | — | Cached set of the Workbook's worksheet names, upper-cased. |

### Methods

#### get_data(_sheet_name, _range)

Return a value (single cell) or nested lists (multi-cell range).

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | (str) The worksheet name (case-insensitive). |
| `_range` | — | (str) A cell ("A1") or range ("A1:B4") address. |

#### get_single_data_item(_sheet_name, _range)

Return the value of a single cell.

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | (str) The worksheet name (case-insensitive). |
| `_range` | — | (str) A single-cell address ("A1"). |

#### get_single_column_data(_sheet_name, _col, _row_start, _row_end)

Return the values of one column between two rows (inclusive).

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | (str) The worksheet name (case-insensitive). |
| `_col` | — | (str) The column letter. |
| `_row_start` | — | (int | None) First row (default 1). |
| `_row_end` | — | (int | None) Last row (default: last used row). |

#### get_single_row_data(_sheet_name, _row_number)

Return all the values of one row, from column A to the last used column.

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | (str) The worksheet name (case-insensitive). |
| `_row_number` | — | (int) The row number. |

---
