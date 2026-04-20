# io_PER

Controller Class for the PHPP PER Worksheet.

**Source**: `PHX/io_PER.py`

---

## BaseBlock

Base class for all PER Data Blocks (Heating, Cooling, etc..)

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `host` | — | — |
| `xl` | — | — |
| `shape` | — | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `block_start_row` | — | Return the row number for the first row of the data block. |
| `block_end_row` | — | Return the row number for the last row of the data block. |
| `phpp_data` | — | Return all the Block PHPP Data as a Dict of Lists of values. |
| `reference_area_address` | — | Return the range address for the Data type's Reference Area (TFA/ Footprint). |
| `reference_area` | — | Return the Data type's Reference Area (TFA/ Footprint). |
| `block_header_row` | — | Return the Row number where the block 'Heading' is found. |
| `worksheet_name` | — | Return the Name of the PER worksheet. |
| `locator_column` | — | Return the column letter for the 'locator' column. |
| `column_final_energy` | — | Return the column letter for the 'Final' (Site) Energy Demand. |
| `column_pe_energy` | — | Return the column letter for the 'Primary' (Source) Energy Demand. |
| `column_co2_emissions` | — | Return the column letter for the 'CO2 Emissions'. |

### Methods

#### find_block_header_row()

Locate the row number for the block heading

#### find_block_start_row()

Locate the row number for the first row of the data block.

#### find_block_end_row()

Locate the row number for the last row of the data block.

#### get_data()

Return all the Block's data from Excel

#### get_final_energy_by_fuel_type()

Return the Block's Final (Site) Energy as a dict of Unit values.

#### get_primary_energy_by_fuel_type()

Return the Block's Primary (Source)) Energy as a dict of values.

---

## Heating

Heating Data Block.

**Inherits from**: `BaseBlock`

---

## Cooling

Cooling Energy

**Inherits from**: `BaseBlock`

---

## DHW

Hot-Water Energy

**Inherits from**: `BaseBlock`

---

## HouseholdElectric

Household Electric (Lighting, Appliances, etc)

**Inherits from**: `BaseBlock`

---

## AdditionalGas

Gas for cooking, dryers

**Inherits from**: `BaseBlock`

---

## EnergyGeneration

Solar, Wind Energy Generation

**Inherits from**: `BaseBlock`

---

## HeatingDeviceUsage

Convenience class for organizing and cleaning the data.

### Methods

#### *classmethod* from_phpp_data_row(row)

Create a new instance from a row of data from PHPP.

| Arg | Type | Description |
|-----|------|-------------|
| `row` | — | — |

---

## PER

IO Controller for the PHPP 'PER' worksheet.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |
| `heating` | `Heating` | — |
| `cooling` | `Cooling` | — |
| `dhw` | `DHW` | — |
| `household_electric` | `HouseholdElectric` | — |
| `additional_gas` | `AdditionalGas` | — |
| `energy_generation` | `EnergyGeneration` | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `heading_row` | — | — |
| `heating_device_data` | — | Return a list of HeatingDeviceUsage objects. |

### Methods

#### get_final_kWh_m2_by_use_type()

Return a Dict of all the Site (Final) Energy [kWh/m2] by use-type.

#### get_final_kWh_by_fuel_type()

Return a Dict of all the Site (Final) Energy [kWh | kBtu] by use and fuel-type.

#### get_primary_kWh_m2_by_use_type()

Return a Dict of all the Source (Primary) Energy [kWh/m2] by use-type.

#### get_primary_kWh_by_fuel_type()

Return a Dict of all the Primary (Source) Energy [kWh | kBtu] by use and fuel type

#### get_heating_device_type_data()

Return a Tuple of HeatingDeviceUsage objects from the PER worksheet.

---
