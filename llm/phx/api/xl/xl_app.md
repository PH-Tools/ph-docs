# xl_app

Class for managing the Excel Application Connection and common read/write operations.

**Source**: `PHX/xl_app.py`

---

## ReadRowsError

Raised when the row_start value exceeds row_end in an Excel range read.

**Inherits from**: `Exception`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `msg` | — | — |

---

## NoActiveExcelRunningError

Raised when no active instance of Excel is found running.

**Inherits from**: `Exception`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `msg` | `str` | — |

---

## ReadMultipleColumnsError

Raised when read_multiple_columns is called with identical start and end columns.

**Inherits from**: `Exception`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `msg` | — | — |

---

## WriteValueError

Raised when writing a value to an Excel cell fails.

**Inherits from**: `Exception`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `msg` | — | — |

---

## XlReadException

Raised when get_single_data_item is called with a multi-cell range.

**Inherits from**: `Exception`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `msg` | — | — |

---

## NoSuchFileError

Raised when the specified Excel file cannot be found on disk.

**Inherits from**: `Exception`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `msg` | — | — |

---

## XLConnection

An Excel connection Facade / Interface.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `worksheet_names` | — | Cached set of the Workbook's worksheet names, upper-cased. |
| `excel_running` | — | Returns True if Excel is currently running, False if not |
| `apps` | — | Return the xl framework 'apps' object. |
| `books` | — | Return the xl framework 'books' object. |
| `os_is_windows` | — | Return True if the current OS is Windows. False if it is Mac/Linux |
| `wb` | — | Returns the Workbook of the active Excel Instance. |

### Methods

#### activate_new_workbook()

Create a new blank workbook and set as the 'Active' book. Returns the new book.

#### start_excel_app()

Starts Excel Application, if it is not currently running.

#### get_workbook()

Return the right Workbook, depending on the App state and user inputs.

#### autofit_columns(_sheet_name)

Runs autofit on all the columns in a sheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | — |

#### autofit_rows(_sheet_name)

Runs autofit on the rows in a sheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | — |

#### clear_range_data(_sheet_name, _range)

Sets the specified excel sheet's range to 'None'

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | (str) The name of the worksheet |
| `_range` | — | (str) The cell range to write to (ie: "A1") or a set of ranges (ie: "A1:B4") |

#### clear_sheet_contents(_sheet_name)

Clears the content of the whole sheet but leaves the formatting.

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | — |

#### clear_sheet_formats(_sheet_name)

Clears the format of the whole sheet but leaves the content.

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | — |

#### clear_sheet_all(_sheet_name)

Clears the content and formatting of the whole sheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | — |

#### create_new_worksheet(_sheet_name, before, after)

Try and add a new Worksheet to the Workbook.

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | — |
| `before` | — | — |
| `after` | — | — |

#### find_row(_search_item, _data, _start)

| Arg | Type | Description |
|-----|------|-------------|
| `_search_item` | — | — |
| `_data` | — | — |
| `_start` | — | — |

#### get_row_num_of_value_in_column(sheet_name, row_start, row_end, col, find)

Returns the row number of the first instance of a specific value

| Arg | Type | Description |
|-----|------|-------------|
| `sheet_name` | — | (str) The name of the sheet to be looking in |
| `row_start` | — | (int) The row number to begin looking from |
| `row_end` | — | (int) The row number to stop looking on |
| `col` | — | (str) The column to look in |
| `find` | — | (Optional[str]) The string to search for (or 'None' for blank cell) |

#### get_upper_case_worksheet_names()

Return a set of all the worksheet names in the workbook, upper-cased.

#### get_sheet_by_name(_sheet_name)

Returns an Excel Sheet with the specified name, or KeyError if not found.

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | (str): The excel sheet name or index num. to locate. |

#### get_last_sheet()

Return the last Worksheet in the Workbook.

#### get_last_used_row_num_in_column(_sheet_name, _col)

Return the row number of the last cell in a column with a value in it.

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | The name of the Worksheet to read from. |
| `_col` | — | The Alpha character of the column to read. |

#### get_single_column_data(_sheet_name, _col, _row_start, _row_end)

Return a list with the values read from a single column of the excel document.

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | (str) The Excel Worksheet to read from. |
| `_col` | — | (str) The Column letter to read. |
| `_row_start` | — | (Optional[int]) default=None |
| `_row_end` | — | (Optional[int]) default=None |

#### get_last_used_column_in_row(_sheet_name, _row)

Return the column letter of the last cell in a column with a value in it.

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | The name of the Worksheet to read from. |
| `_row` | — | — |

#### get_single_row_data(_sheet_name, _row_number)

Return all the data from a single Row in the Excel Workbook.

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | The name of the sheet to read |
| `_row_number` | — | The row number to read |

#### get_multiple_column_data(_sheet_name, _col_start, _col_end, _row_start, _row_end)

Return a list of lists with the values read from a specified block of the xl document.

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | (str) The Worksheet to read from. |
| `_col_start` | — | (str) The Column letter to read from. |
| `_col_end` | — | (str) The Column letter to read to. |
| `_row_start` | — | (int) default=1 |
| `_row_end` | — | (int) default=100 |

#### get_data(_sheet_name, _range)

Return a value or values from the Excel document.

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | (str) The name of the worksheet to read from. |
| `_range` | — | (str) The cell range to read from (ie: "A1") or a set of ranges (ie: "A1:B4") |

#### get_single_data_item(_sheet_name, _range)

Return a single value from the Excel document.

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | (str) The name of the worksheet to read from. |
| `_range` | — | (str) The cell range to read from to (ie: "A1") |

#### get_data_by_columns(_sheet_name, _range_address)

Returns a List of column data, each column in a list.

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | (str) The name of the worksheet to read from |
| `_range_address` | — | (str) The range read. ie: "A1:D56" |

#### get_data_with_column_letters(_sheet_name, _range_address)

Returns a Dict of column data, key'd by the Column Letter.

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | (str) The name of the worksheet to read from |
| `_range_address` | — | (str) The range read. ie: "A1:D56" |

#### group_rows(_sheet_name, _row_start, _row_end)

Group one or more rows.

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | — |
| `_row_start` | — | — |
| `_row_end` | — | — |

#### hide_group_details(_sheet_name)

Hide (collapse) all the 'Groups' on the specified worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | — |

#### in_silent_mode()

Context Manager which turns off screen-refresh and auto-calc in the

#### output(_input)

Used to set the output method. Default is None (silent).

| Arg | Type | Description |
|-----|------|-------------|
| `_input` | — | The string to output. |

#### unprotect_all_sheets()

Walk through all the sheets and unprotect them all.

#### write_xl_item(_xl_item, _transpose)

Writes a single XLItem to the worksheet

| Arg | Type | Description |
|-----|------|-------------|
| `_xl_item` | — | (XLItem) The XLItem with a sheet_name, range and value to write. |
| `_transpose` | — | (bool) Transpose the data before writing. Default=False. Set to true if you are passing in a list of items and want them to be written as rows instead of as columns. |

#### calculate()

Recalculate all the formulas in the workbook.

---
