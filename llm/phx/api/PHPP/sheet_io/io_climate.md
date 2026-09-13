# io_climate

Controller Class for the PHPP Climate worksheet.

**Source**: `PHX/io_climate.py`

---

## Climate

IO Controller for the PHPP Climate Worksheet.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |

### Methods

#### get_start_rows()

#### write_climate_block(_climate_entry)

| Arg | Type | Description |
|-----|------|-------------|
| `_climate_entry` | — | — |

#### write_active_climate(_active_climate, _country_code, _region_code, _dataset_name)

| Arg | Type | Description |
|-----|------|-------------|
| `_active_climate` | — | — |
| `_country_code` | — | — |
| `_region_code` | — | — |
| `_dataset_name` | — | — |

#### try_library_codes(_active_climate)

Select valid cascading PHPP library codes, or report fallback/unsupported.

| Arg | Type | Description |
|-----|------|-------------|
| `_active_climate` | — | — |

#### write_user_defined_active_climate(_active_climate)

Select the first user-defined block using this shape's localized literals.

| Arg | Type | Description |
|-----|------|-------------|
| `_active_climate` | — | — |

#### read_active_country()

#### read_active_region()

#### read_active_data_set()

#### read_station_elevation()

#### read_site_elevation()

#### read_latitude()

#### read_longitude()

#### read_active_monthly_data()

Return the Monthly Climate data for the currently active set from the 'Climate' worksheet.

---
