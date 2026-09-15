# electricity_item

Model class for a PHPP Electricity / Equipment row input.

**Source**: `PHX/electricity_item.py`

---

## ElectricityAnnualRowXLWriter

One PHPP 'Other devices' annual row holding every device of one category.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `total_kwh` | — | The category's annual energy, kWh/a. |

### Methods

#### create_xl_items(_shape, _description_column, _row)

Return the description, quantity, IHG flag and annual energy for one annual row.

| Arg | Type | Description |
|-----|------|-------------|
| `_shape` | — | — |
| `_description_column` | — | — |
| `_row` | — | — |

---

## ElectricityItemXLWriter

Model class for a single Electric-Equipment item entry row.

### Methods

#### create_xl_items(_shape)

Returns a list of xl_data.XlItem or raises and Error if equipment type is unrecognized.

| Arg | Type | Description |
|-----|------|-------------|
| `_shape` | — | — |

---

## PHPPReadAddress

Attribute Name / PHPP Address pair.

**Inherits from**: `NamedTuple`

---

## ReaderDataItem

Electric-Equipment data for a single PHPP item.

**Inherits from**: `NamedTuple`

---

## ReaderAddressesGroup

Electric-Equipment data for a single PHPP item.

**Inherits from**: `NamedTuple`

---

## ElectricityItemXLReader

Model class for defining read-locations for Electric-Equipment data in the PHPP.

---
