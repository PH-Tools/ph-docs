# io_windows

Controller Class for the PHPP Windows worksheet.

**Source**: `PHX/io_windows.py`

---

## Windows

IO Controller Class for PHPP "Windows" worksheet.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `header_row` | — | The row number for the Window entry 'Header'. |
| `first_entry_row` | — | Return the starting row for the window data entry block. |
| `last_entry_row` | — | Return the ending row for the window data entry block. |
| `entry_range_start` | — | — |
| `entry_range_end` | — | — |
| `entry_range` | — | Return the range for the window data entry block. |
| `windows_row_numbers` | — | Return a list of all the window row numbers. |
| `used_window_row_numbers` | — | — |

### Methods

#### find_header_row(_row_start, _read_length)

Return the row number for the Window entry section 'Header'

| Arg | Type | Description |
|-----|------|-------------|
| `_row_start` | — | — |
| `_read_length` | — | — |

#### find_first_entry_row(_start_row, _read_length)

Return the starting row for the window data entry block.

| Arg | Type | Description |
|-----|------|-------------|
| `_start_row` | — | — |
| `_read_length` | — | — |

#### find_last_entry_row(_start_row)

Return the last row of the Window input section.

| Arg | Type | Description |
|-----|------|-------------|
| `_start_row` | — | — |

#### set_single_window_construction_ids(_row_num, _glazing_construction_id, _frame_construction_id)

Set the glazing and frame construction IDs for a single window.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_num` | — | int The row number for the window to set the construction IDs for. |
| `_glazing_construction_id` | — | str The glazing construction ID to set. |
| `_frame_construction_id` | — | str The frame construction ID to set. |

#### write_single_window(_row_num, _window_row)

Write a single WindowRow object to the Windows worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_num` | — | — |
| `_window_row` | — | — |

#### write_windows(_window_rows)

Write a list of WindowRow objects to the Windows worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_window_rows` | — | — |

#### get_all_window_names()

Return a list of all the window names found in the worksheet.

#### get_total_window_area(_tolerance)

Return the total window area from the PHPP Windows worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_tolerance` | — | — |

#### get_total_skylight_area(_tolerance)

Return the total skylight area from the PHPP Windows worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_tolerance` | — | — |

#### get_all_glazing_names()

Return a set of all the construction names used in the Areas worksheet.

#### activate_variants()

Set the frame and glass values to link to the Variants worksheet.

#### scale_window_size(_row_num, _scale_factor)

Scale the size of a single window based on an overall scale-factor.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_num` | — | int The row number of the window to scale. |
| `_scale_factor` | — | float The factor to scale the window by. |

#### row_is_window(_row_num, _tolerance)

Return True if the row is a window, False otherwise.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_num` | — | — |
| `_tolerance` | — | — |

#### row_is_skylight(_row_num, _tolerance)

Return True if the row is a skylight, False otherwise.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_num` | — | — |
| `_tolerance` | — | — |

---
