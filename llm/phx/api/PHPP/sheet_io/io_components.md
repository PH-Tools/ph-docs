# io_components

Controller Class for the PHPP 'Components' worksheet.

**Source**: `PHX/io_components.py`

---

## ExistingGlazingTypeData

Stores name, g-value, and U-value for an existing PHPP glazing type.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `key` | — | — |

---

## Glazings

Reads and writes glazing component data in the PHPP 'Components' worksheet.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |
| `cache` | `Dict` | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `section_header_row` | — | Return the row number of the Glazings section header. |
| `section_first_entry_row` | — | Return the row number of the very first user-input entry row in the Glazing input section. |
| `section_last_entry_row` | — | Return the row number of the very last user-input entry row in the Glazing input section. |

### Methods

#### find_section_header_row(_row_start, _row_end)

Return the row number of the Glazings section header.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_start` | — | — |
| `_row_end` | — | — |

#### find_section_first_entry_row()

Return the row number of the very first user-input entry row in the Glazing input section.

#### find_section_last_entry_row(_start_row)

Return the last row of the glazing input section.

| Arg | Type | Description |
|-----|------|-------------|
| `_start_row` | — | — |

#### find_first_empty_row()

Return the first empty row in the glazing input section.

#### get_glazing_phpp_id_by_name(_name, _use_cache)

Return the PHPP Glazing ID for the given name.

| Arg | Type | Description |
|-----|------|-------------|
| `_name` | — | — |
| `_use_cache` | — | — |

#### get_glazing_phpp_id_by_row_num(_row_num)

Return the PHPP Glazing ID ("01ud-MyGlass", etc..) for the given row number.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_num` | — | — |

#### get_all_glazing_types()

Return a set of all glazing types in the Glazing input section.

---

## Frames

Reads and writes frame component data in the PHPP 'Components' worksheet.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |
| `cache` | `Dict` | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `section_header_row` | — | Return the row number of the 'Frames' section header. |
| `section_first_entry_row` | — | Return the row number of the very first user-input entry row in the Frames input section. |
| `section_last_entry_row` | — | Return the row number of the very last user-input entry row in the Frames input section. |

### Methods

#### find_section_header_row(_row_start, _row_end)

| Arg | Type | Description |
|-----|------|-------------|
| `_row_start` | — | — |
| `_row_end` | — | — |

#### find_section_first_entry_row()

Return the row number of the very first user-input entry row in the Frames input section.

#### find_section_last_entry_row(_start_row)

Return the last row of the Frames input section.

| Arg | Type | Description |
|-----|------|-------------|
| `_start_row` | — | — |

#### find_first_empty_row()

Return the first empty row in the frames input section.

#### get_frame_phpp_id_by_name(_name, _row_start, _row_end, _use_cache)

Return the PHPP ID of a Frame component by name.

| Arg | Type | Description |
|-----|------|-------------|
| `_name` | — | — |
| `_row_start` | — | — |
| `_row_end` | — | — |
| `_use_cache` | — | — |

#### get_frame_phpp_id_by_row_num(_row_num)

Return the PHPP Frame ID ("01ud-MyFrame", etc..) for the given row number.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_num` | — | — |

---

## Ventilators

Reads and writes ventilator component data in the PHPP 'Components' worksheet.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `section_header_row` | — | Return the row number of the 'Ventilators' section header. |
| `section_first_entry_row` | — | Return the row number of the very first user-input entry row in the Ventilators input section. |
| `section_last_entry_row` | — | Return the row number of the very last user-input entry row in the Ventilators input section. |

### Methods

#### find_section_last_entry_row(_start_row)

Return the last row of the Ventilators input section.

| Arg | Type | Description |
|-----|------|-------------|
| `_start_row` | — | — |

#### find_section_header_row(_row_start, _row_end)

Return the row number of the 'Ventilators' section header.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_start` | — | — |
| `_row_end` | — | — |

#### find_section_first_entry_row()

Return the first row of the Ventilators input section.

#### find_first_empty_row()

Return the first empty row in the Ventilators input section.

#### get_ventilator_phpp_id_by_name(_name, _row_start, _row_end)

Return the PHPP ID of a Ventilator component by name.

| Arg | Type | Description |
|-----|------|-------------|
| `_name` | — | — |
| `_row_start` | — | — |
| `_row_end` | — | — |

#### get_ventilator_phpp_id_by_row_num(_row_num)

Return the PHPP Ventilator ID ("01ud-MyVentilator", etc..) for the given row number.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_num` | — | — |

---

## Components

IO Controller for PHPP "Components" worksheet.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |
| `glazings` | `Glazings` | — |
| `frames` | `Frames` | — |
| `ventilators` | `Ventilators` | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `first_empty_glazing_row_num` | — | Return the row number of the first empty row in the Glazings section. |
| `first_empty_frame_row_num` | — | Return the row number of the first empty row in the Frames section. |

### Methods

#### write_single_glazing(_row_num, _glazing_row)

Write a single GlazingRow object to the PHPP "Components" worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_num` | — | — |
| `_glazing_row` | — | — |

#### write_glazings(_glazing_rows)

Write a list of GlazingRow objects to the PHPP "Components" worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_glazing_rows` | — | — |

#### write_single_frame(_row_num, _frame_row)

Write a single FrameRow object to the PHPP "Components" worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_num` | — | — |
| `_frame_row` | — | — |

#### write_frames(_frame_row)

Write a list of FrameRow objects to the PHPP "Components" worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_frame_row` | — | — |

#### write_single_ventilator(_row_num, _ventilator_row)

Write a single VentilatorRow object to the PHPP "Components" worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_num` | — | — |
| `_ventilator_row` | — | — |

#### write_ventilators(_ventilator_row)

Write a list of VentilatorRow objects to the PHPP "Components" worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_ventilator_row` | — | — |

---
