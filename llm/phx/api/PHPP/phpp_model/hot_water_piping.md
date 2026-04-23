# hot_water_piping

Model class for a PHPP DHW Piping Elements.

**Source**: `PHX/hot_water_piping.py`

---

## RecircPipingInput

Model class for a single DHW Recirculation Pipe Element.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `input_column` | — | Return the right input column based on the pipe-group-number. |

### Methods

#### create_xl_items(_sheet_name, _row_num)

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | — |
| `_row_num` | — | — |

---

## BranchPipingInput

Model class for a single DHW Branch Pipe Element.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `input_column` | — | Return the right input column based on the pipe-group-number. |

### Methods

#### create_range(_row_num)

Return the XL Range ("P12",...) for the specific field name.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_num` | — | — |

#### create_xl_items(_sheet_name, _row_num)

Returns a list of Branch Piping Xl-Write items.

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | — |
| `_row_num` | — | — |

---
