# verification_data

Model class for the Ventilation worksheet various input items.

**Source**: `PHX/verification_data.py`

---

## VerificationInput

Ventilation Worksheet input data item.

### Methods

#### *classmethod* item(shape, input_type, input_data, input_unit, target_unit)

Create a new data-input item.

| Arg | Type | Description |
|-----|------|-------------|
| `shape` | — | — |
| `input_type` | — | — |
| `input_data` | — | — |
| `input_unit` | — | — |
| `target_unit` | — | — |

#### *classmethod* enum(shape, input_type, input_enum_value)

Create a new options-input item.

| Arg | Type | Description |
|-----|------|-------------|
| `shape` | — | — |
| `input_type` | — | — |
| `input_enum_value` | — | — |

#### create_xl_item(_sheet_name, _row_num)

Returns a list of the XL Items to write for this Data item

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | (str) The name of the worksheet to write to. |
| `_row_num` | — | (int) The row number to build the XlItems for |

---
