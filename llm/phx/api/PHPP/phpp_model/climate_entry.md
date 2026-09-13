# climate_entry

Data-entry constructor for the Climate Worksheet.

**Source**: `PHX/climate_entry.py`

---

## ClimateSettings

The active climate data selections.

### Methods

#### create_selector_xl_items(_sheet_name, _country_code, _region_code, _dataset_name)

Return a list of the XL items to write to the worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | — |
| `_country_code` | — | — |
| `_region_code` | — | — |
| `_dataset_name` | — | — |

#### create_elevation_xl_item(_sheet_name)

Return the site-elevation override item.

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | — |

#### create_xl_items(_sheet_name, _start_row)

Return selector and elevation items for the active climate.

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | — |
| `_start_row` | — | — |

---

## ClimateDataBlock

A single Climate / Weather-Station entry block.

### Methods

#### create_xl_items(_sheet_name, _start_row)

Return a list of the XL items to write to the worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | — |
| `_start_row` | — | — |

---
