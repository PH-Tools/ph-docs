# io_u_values

Controller Class for the PHPP "U-Values" worksheet.

**Source**: `PHX/io_u_values.py`

---

## NoEmptyConstructorError

Raised when no empty constructor slots remain in the PHPP 'U-Values' worksheet.

**Inherits from**: `Exception`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `msg` | `str` | — |

---

## ExistingAssemblyData

Stores name, U-value, R-value, and exposure data for an existing PHPP assembly.

---

## UValues

IO Controller for the PHPP "U-Values" worksheet.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |
| `cache` | `Dict` | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `all_constructor_start_rows` | — | Return a list of all of the PHPP Constructor starting rows |
| `used_constructor_start_rows` | — | Return the PHPP Constructors that have any data in them, one at a time. |

### Methods

#### get_start_rows(_row_start, _row_end)

Reads through the U-Values worksheet and finds each of the constructor 'start' (title) rows.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_start` | — | (int) default=1 |
| `_row_end` | — | (int) default=1730 |

#### get_constructor_phpp_id_by_name(_name, _row_start, _row_end, _use_cache)

Returns the full PHPP-style value for the constructor with a specified name.

| Arg | Type | Description |
|-----|------|-------------|
| `_name` | — | — |
| `_row_start` | — | — |
| `_row_end` | — | — |
| `_use_cache` | — | — |

#### get_used_constructor_names()

Return a list of the used construction names.

#### get_constructor_r_si_type(_row_num)

Return "Wall", "Roof" or "Floor" depending on the constructor type.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_num` | — | — |

#### get_constructor_r_se_type(_row_num)

Return "Ground", "Outdoor air" or "Ventilated" depending on the constructor type.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_num` | — | — |

#### get_constructor_name(_row_num)

Return the name of the constructor at the specified row.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_num` | — | — |

#### get_first_empty_constructor_start_row()

Return the first empty constructor's row number.

#### get_constructor_u_value(_row_num)

Return the U-Value of the constructor at the specified row.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_num` | — | — |

#### get_constructor_r_value(_row_num)

Return the U-Value of the constructor at the specified row.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_num` | — | — |

#### write_single_PHX_construction(_phx_construction, _start_row)

Write a single PHX Construction to the PHPP worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_phx_construction` | — | — |
| `_start_row` | — | — |

#### write_single_constructor_block(_construction, _start_row)

Write a single Construction with all the layers to the PHPP worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_construction` | — | — |
| `_start_row` | — | — |

#### write_constructor_blocks(_const_blocks)

Write a list of ConstructorBlocks to the U-Values worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_const_blocks` | — | — |

#### add_new_phx_construction(_phx_construction)

Add a new PHX Construction to the PHPP worksheet in the first empty slot found.

| Arg | Type | Description |
|-----|------|-------------|
| `_phx_construction` | — | — |

#### clear_single_constructor_data(_row_num, _clear_name)

Clears the existing data from a single constructor block.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_num` | — | — |
| `_clear_name` | — | — |

#### clear_all_constructor_data(_clear_name)

Remove all of the existing input data from all of the constructors in the PHPP.

| Arg | Type | Description |
|-----|------|-------------|
| `_clear_name` | — | — |

#### activate_variants(_assembly_phpp_ids)

Connect all the links to make the 'Variants' page drive the input values.

| Arg | Type | Description |
|-----|------|-------------|
| `_assembly_phpp_ids` | — | — |

#### get_all_envelope_assemblies()

---
