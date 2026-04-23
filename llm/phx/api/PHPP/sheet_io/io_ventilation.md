# io_ventilation

Controller Class for the PHPP "Ventilation" worksheet.

**Source**: `PHX/io_ventilation.py`

---

## VentilationInputLocation

Generic input item for Ventilation worksheet items.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `sheet_name` | — | — |
| `search_col` | — | — |
| `search_item` | — | — |

### Methods

#### find_input_row(_row_start, _row_end)

Return the row number where the search-item is found input.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_start` | — | — |
| `_row_end` | — | — |

---

## Ventilation

IO Controller for the PHPP Ventilation worksheet.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |
| `io_vent_type` | `VentilationInputLocation` | — |
| `io_wind_coeff_e` | `VentilationInputLocation` | — |
| `io_wind_coeff_f` | `VentilationInputLocation` | — |
| `io_air_change_rate` | `VentilationInputLocation` | — |
| `io_net_volume` | `VentilationInputLocation` | — |
| `io_multi_vent_worksheet_on` | `VentilationInputLocation` | — |

### Methods

#### write_ventilation_type(_phpp_model_obj)

| Arg | Type | Description |
|-----|------|-------------|
| `_phpp_model_obj` | — | — |

#### write_wind_coeff_e(_phpp_model_obj)

| Arg | Type | Description |
|-----|------|-------------|
| `_phpp_model_obj` | — | — |

#### write_wind_coeff_f(_phpp_model_obj)

| Arg | Type | Description |
|-----|------|-------------|
| `_phpp_model_obj` | — | — |

#### write_airtightness_n50(_phpp_model_obj)

| Arg | Type | Description |
|-----|------|-------------|
| `_phpp_model_obj` | — | — |

#### write_Vn50_volume(_phpp_model_obj)

| Arg | Type | Description |
|-----|------|-------------|
| `_phpp_model_obj` | — | — |

#### write_multi_vent_worksheet_on(_phpp_model_obj)

| Arg | Type | Description |
|-----|------|-------------|
| `_phpp_model_obj` | — | — |

#### activate_variants()

Link Ventilation Type and Airtightness to the Variants worksheet.

---
