# ventilation_data

Model class for the Ventilation worksheet various input items.

**Source**: `PHX/ventilation_data.py`

---

## VentilationInputItem

Ventilation Worksheet input item.

### Methods

#### create_xl_item(_sheet_name, _row_num)

Returns a list of the XL Items to write for this Surface Entry

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | (str) The name of the worksheet to write to. |
| `_row_num` | — | (int) The row number to build the XlItems for |

#### *classmethod* vent_type(shape, input_data)

| Arg | Type | Description |
|-----|------|-------------|
| `shape` | — | — |
| `input_data` | — | — |

#### *classmethod* multi_unit_on(shape, input_data)

| Arg | Type | Description |
|-----|------|-------------|
| `shape` | — | — |
| `input_data` | — | — |

#### *classmethod* wind_coeff_e(shape, input_data)

| Arg | Type | Description |
|-----|------|-------------|
| `shape` | — | — |
| `input_data` | — | — |

#### *classmethod* wind_coeff_f(shape, input_data)

| Arg | Type | Description |
|-----|------|-------------|
| `shape` | — | — |
| `input_data` | — | — |

#### *classmethod* airtightness_n50(shape, input_data)

| Arg | Type | Description |
|-----|------|-------------|
| `shape` | — | — |
| `input_data` | — | — |

#### *classmethod* airtightness_Vn50(shape, input_data)

| Arg | Type | Description |
|-----|------|-------------|
| `shape` | — | — |
| `input_data` | — | — |

---
