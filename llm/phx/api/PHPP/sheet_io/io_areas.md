# io_areas

Controller Class for the PHPP "Areas" worksheet.

**Source**: `PHX/io_areas.py`

---

## AreasInputLocation

Generic input item for Areas worksheet items.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `sheet_name` | — | — |
| `search_col` | — | — |
| `search_item` | — | — |
| `input_row_offset` | — | — |

### Methods

#### find_input_row(_row_start, _row_end)

Return the row number where the search-item is found input.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_start` | — | — |
| `_row_end` | — | — |

---

## Surfaces

Reads and writes surface data to the PHPP 'Areas' worksheet.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |
| `surface_cache` | `Dict` | — |
| `group_type_exposures` | — | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `section_header_row` | — | Return the row number of the 'Area input' section header. |
| `section_first_entry_row` | — | Return the row number of the very first user-input entry row in the 'Area input' section. |
| `section_last_entry_row` | — | Return the row number of the last user-input entry row in the 'Area input' section. |
| `all_surface_rows` | — | Return a generator of all the row_nums and surface rows in the Areas worksheet. |

### Methods

#### find_section_header_row(_row_start, _row_end)

Return the row number of the 'Area input' section header.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_start` | — | — |
| `_row_end` | — | — |

#### find_section_first_entry_row()

Return the row number of the very first user-input entry row in the 'Area input' section.

#### find_section_last_entry_row(_start_row)

Return the row number of the last user-input entry row in the 'Area input' section.

| Arg | Type | Description |
|-----|------|-------------|
| `_start_row` | — | — |

#### get_surface_phpp_id_by_name(_name, _use_cache)

Return the PHPP-Style id ("1-NorthRoofSurface", ...) when given the surface name.

| Arg | Type | Description |
|-----|------|-------------|
| `_name` | — | — |
| `_use_cache` | — | — |

#### get_all_construction_names()

Return a set of all the construction names used in the Areas worksheet.

---

## ThermalBridges

Reads and writes thermal bridge data to the PHPP 'Areas' worksheet.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `section_header_row` | — | — |
| `section_first_entry_row` | — | — |

### Methods

#### find_section_header_row(_row_start, _row_end)

Return the row number of the 'Thermal Bridge input' section header.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_start` | — | — |
| `_row_end` | — | — |

#### find_section_first_entry_row()

Return the row number of the very first user-input entry row in the 'Thermal Bridge input' section.

---

## Areas

IO Controller for the PHPP Areas worksheet.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |
| `group_type_exposures` | `get_group_type_exposures` | — |
| `surfaces` | `Surfaces` | — |
| `thermal_bridges` | `ThermalBridges` | — |

### Methods

#### write_thermal_bridges(_tbs)

Write all of the the thermal bridge data to the PHPP Areas worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_tbs` | — | — |

#### write_surfaces(_surfaces)

Write all of the the surface data to the PHPP Areas worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_surfaces` | — | — |

#### write_item(_phpp_model_obj)

Write the VerificationInputItem item out to the PHPP Areas Worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_phpp_model_obj` | — | — |

#### write_custom_group_summaries(_groups)

Write temp zone letters and descriptions for custom groups in the summary section.

| Arg | Type | Description |
|-----|------|-------------|
| `_groups` | — | — |

#### get_group_type_exposures()

Return the group type exposures dictionary from the PHPP Areas worksheet.

#### get_total_net_wall_area()

Return the total net (apertures punched) wall area from the PHPP Areas worksheet.

#### get_total_net_roof_area()

Return the total net (apertures punched) Roof area from the PHPP Areas worksheet.

#### get_total_vertical_window_area()

Return the total window area from the PHPP Areas worksheet.

#### get_total_horizontal_window_area()

Return the total skylight area from the PHPP Areas worksheet.

#### set_surface_row_construction(_row_num, _phpp_constriction_id)

Set the construction-id for the surface row in the PHPP Areas worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_num` | — | — |
| `_phpp_constriction_id` | — | — |

#### set_surface_row_solar_absorptivity(_row_num, _absorptivity)

Set the solar absorptivity for the surface row in the PHPP Areas worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_num` | — | — |
| `_absorptivity` | — | — |

#### set_surface_row_emissivity(_row_num, _emissivity)

Set the emissivity for the surface row in the PHPP Areas worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_num` | — | — |
| `_emissivity` | — | — |

---
