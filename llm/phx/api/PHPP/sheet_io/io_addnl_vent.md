# io_addnl_vent

Controller Class for the PHPP "Additional Vent" worksheet.

**Source**: `PHX/io_addnl_vent.py`

---

## Spaces

No description available.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |

### Methods

#### find_section_header_row(_row_start, _row_end)

Return the row number of the 'Rooms' section header.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_start` | — | — |
| `_row_end` | — | — |

#### find_section_first_entry_row()

Return the row number of the very first user-input entry row in the 'Rooms' section.

#### find_section_shape()

#### find_section_last_entry_row(_start_row, _read_length)

| Arg | Type | Description |
|-----|------|-------------|
| `_start_row` | — | — |
| `_read_length` | — | — |

---

## VentilatorDeviceUsage

Convenience class for organizing and cleaning the data.

### Methods

#### *classmethod* from_phpp_data_row(row)

Create a new instance from a row of data from PHPP.

| Arg | Type | Description |
|-----|------|-------------|
| `row` | — | — |

---

## VentUnits

No description available.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `section_header_row` | — | Return the row number of the 'Area input' section header. |
| `section_first_entry_row` | — | Return the row number of the very first user-input entry row in the 'Area input' section. |
| `section_last_entry_row` | — | Return the row number of the last user-input entry row in the 'Area input' section. |

### Methods

#### find_section_header_row(_row_start, _row_end)

Return the row number of the 'Vent-Units' section header.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_start` | — | — |
| `_row_end` | — | — |

#### find_section_first_entry_row()

Return the row number of the very first user-input entry row in the 'Vent Unit' section.

#### find_section_last_entry_row(_rows)

Return the row number of the very last user-input entry row in the 'Vent Unit' section.

| Arg | Type | Description |
|-----|------|-------------|
| `_rows` | — | — |

#### find_section_shape()

#### get_vent_unit_num_by_phpp_id(_phpp_id)

Return the phpp-number of the Ventilation unit from the Additional Ventilation worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_phpp_id` | — | (str): The phpp style id name (ie: "01ud-MyVentUnit") of the ventilation unit to find. |

#### get_ventilation_units()

Return a tuple of VentilatorDeviceUsage objects from the PHPP worksheet.

---

## VentDucts

No description available.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |

### Methods

#### find_section_header_row(_row_start, _row_end)

Return the row number of the 'Rooms' section header.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_start` | — | — |
| `_row_end` | — | — |

#### find_section_first_entry_row()

Return the row number of the very first user-input entry row in the 'Ducts' section.

#### find_section_last_entry_row(_rows)

Return the row number of the very last user-input entry row in the 'Ducts' section.

| Arg | Type | Description |
|-----|------|-------------|
| `_rows` | — | — |

#### find_section_shape()

---

## AddnlVent

IO Controller for the PHPP Additional Vent worksheet.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |
| `spaces` | `Spaces` | — |
| `vent_units` | `VentUnits` | — |
| `vent_ducts` | `VentDucts` | — |

### Methods

#### write_spaces(_spaces)

| Arg | Type | Description |
|-----|------|-------------|
| `_spaces` | — | — |

#### write_vent_units(_vent_units)

| Arg | Type | Description |
|-----|------|-------------|
| `_vent_units` | — | — |

#### write_vent_ducts(_vent_ducts)

| Arg | Type | Description |
|-----|------|-------------|
| `_vent_ducts` | — | — |

#### activate_variants(variants_worksheet_name, vent_unit_range)

Link the Vent unit to the Variants worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `variants_worksheet_name` | — | — |
| `vent_unit_range` | — | — |

#### get_ventilation_units()

Return a list of Ventilation Units found in the Worksheet.

#### read_space_data()

Return all of the Space data from the worksheet.

---
