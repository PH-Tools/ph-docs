# io_variants

Controller Class for the PHPP "Variants" worksheet.

**Source**: `PHX/io_variants.py`

---

## VariantAssemblyLayerName

Variants Assembly PHPP ID.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `phpp_id` | — | — |

---

## VariantWindowTypeName

Variants Window Type PHPP ID.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `phpp_id` | — | — |

---

## Variants

IO Controller for the PHPP "Variants" worksheet.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |

### Methods

#### get_results_section_start(_start_row, _read_length)

Return the row number of the results section header.

| Arg | Type | Description |
|-----|------|-------------|
| `_start_row` | — | — |
| `_read_length` | — | — |

#### get_user_input_section_start(_start_row, _read_length)

Return the row number of the user-input section header.

| Arg | Type | Description |
|-----|------|-------------|
| `_start_row` | — | — |
| `_read_length` | — | — |

#### get_assembly_layers_start(_row_start, _rows)

Return the row number of the start of the Building Assembly Layers variant section.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_start` | — | — |
| `_rows` | — | — |

#### get_window_types_start(_row_start, _rows)

Return the row number of the start of the Window Types input section.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_start` | — | — |
| `_rows` | — | — |

#### get_ventilation_start(_row_start, _rows)

Return the row number of the start of the Ventilation input section.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_start` | — | — |
| `_rows` | — | — |

#### get_ventilation_input_item_rows()

Return a dict of the input items and their row-numbers for the ventilation items.

#### write_assembly_layer(_assembly_name, _assembly_num)

Write a new assembly layer to the Variants worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_assembly_name` | — | — |
| `_assembly_num` | — | — |

#### write_window_type(_window_type_name, _window_type_num)

Write a new Window Type name to the Variants worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_window_type_name` | — | — |
| `_window_type_num` | — | — |

#### get_assembly_layer_phpp_ids()

Return a list of the Variants PHPP-ids for all assembly layers.

#### get_window_type_phpp_ids()

#### get_variant_results_data(_num_variants)

Return the data from the Variants worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_num_variants` | — | — |

---
