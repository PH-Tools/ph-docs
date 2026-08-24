# xl_openpyxl

The closed-file Excel backend: openpyxl, read-only, cached values only.

**Source**: `PHX/xl_openpyxl.py`

---

## NoSuchSheetError

Raised when a worksheet name is not in the workbook (case-insensitive).

**Inherits from**: `KeyError`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `msg` | — | — |

---

## OpenpyxlWorkbook

A closed .xlsx/.xlsm opened read-only through openpyxl, exposing the 'XLReadable' surface.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `path` | `Path` | The workbook on disk. Never written to. |
| `data_only` | — | True (default) reads cached values; False reads formulas. |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `properties` | — | The openpyxl 'DocumentProperties' (creator, lastModifiedBy, modified, ...). |
| `sheetnames` | — | Worksheet names in workbook order, as written. |
| `worksheet_names` | — | Set of the workbook's worksheet names, upper-cased. |

### Methods

#### close()

Release the underlying zip handle.

#### get_data(_sheet_name, _range)

Return a value (single cell) or nested lists (range) from the workbook.

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
| `_row_end` | — | (int | None) Last row (default: the sheet's last row). |

#### get_single_row_data(_sheet_name, _row_number)

Return all the values of one row, from column A to the sheet's last used column.

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | (str) The worksheet name (case-insensitive). |
| `_row_number` | — | (int) The row number. |

---
