# io_elec_non_res

Controller Class for the PHPP "Electricity non-res" worksheet.

**Source**: `PHX/io_elec_non_res.py`

---

## Lighting

No description available.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `section_header_row` | — | Return the row number of the 'Lighting' section header. |
| `section_first_entry_row` | — | Return the row number of the very first user-input entry row in the 'Lighting' section. |
| `section_last_entry_row` | — | Return the row number of the last user-input entry row in the 'Lighting' section. |
| `all_lighting_row_data` | — | Return a generator of all the row_nums and lighting rows in the Lighting worksheet. |
| `used_lighting_row_numbers` | — | Return a generator of all the row_nums that have data in the Lighting section. |

### Methods

#### find_section_header_row(_row_start, _row_end)

Return the row number of the 'Lighting input' section header.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_start` | — | — |
| `_row_end` | — | — |

#### find_section_first_entry_row()

Return the row number of the very first user-input entry row in the 'Lighting input' section.

#### find_section_last_entry_row(_start_row)

Return the row number of the last user-input entry row in the 'Lighting input' section.

| Arg | Type | Description |
|-----|------|-------------|
| `_start_row` | — | — |

#### get_lighting_row_data(_row_num)

Return the lighting row object for the given row number.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_num` | — | — |

#### set_lighting_power_density(_row_num, _power_density, _unit)

Set the lighting power density for the given row number.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_num` | — | — |
| `_power_density` | — | — |
| `_unit` | — | — |

---

## ElecNonRes

IO Controller for the PHPP "Electricity non-res" worksheet.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |
| `lighting` | `Lighting` | — |

---
