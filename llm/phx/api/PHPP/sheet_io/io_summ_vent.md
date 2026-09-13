# io_summ_vent

Controller class for the PHPP 'SummVent' worksheet.

**Source**: `PHX/io_summ_vent.py`

---

## SummVentInputLocation

Location of the summer heat-recovery checkbox group in 'SummVent'.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |

### Methods

#### find_input_row(_row_start, _row_end)

Return the row of the summer heat-recovery header in column Q.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_start` | — | — |
| `_row_end` | — | — |

---

## SummVent

IO controller for the PHPP 'SummVent' worksheet.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |
| `io_hrv_summer_mode` | `SummVentInputLocation` | — |

### Methods

#### write_summer_hrv_mode(_phpp_model_obj)

Write one selected summer heat-recovery mode and clear its three siblings.

| Arg | Type | Description |
|-----|------|-------------|
| `_phpp_model_obj` | — | — |

---
