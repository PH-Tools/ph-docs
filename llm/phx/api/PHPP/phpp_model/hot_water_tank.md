# hot_water_tank

Model class for a PHPP DHW Tank

**Source**: `PHX/hot_water_tank.py`

---

## TankInput

Model class for a single DHW Tank input.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `input_column` | — | Return the right input column based on the tank-number. |

### Methods

#### create_range(_row_num)

Return the XL Range ("P12",...) for the specific field name.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_num` | — | — |

#### create_xl_items(_sheet_name, _row_num)

Returns a list of the XL Items to write for this DHW Tank

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | (str) The name of the worksheet to write to. |
| `_row_num` | — | (int) The row number to build the XlItems for |

---
