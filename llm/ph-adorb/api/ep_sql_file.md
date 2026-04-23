# ep_sql_file

Functions to load and process the source data SQL files.

**Source**: `ph_adorb/ep_sql_file.py`

---

## DataFileSQL

An EnergyPlus simulation results .SQL file reader.

**Inherits from**: `BaseModel`

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `file_name` | — | The name of the file. |

### Methods

#### get_peak_electric_watts()

Get the 'Facility Total Building Electricity Demand Rate' [W] from the SQL File.

#### get_hourly_purchased_electricity_kwh()

Get the hourly purchased electricity values (kWh) from the SQL file.

#### get_total_purchased_electricity_kwh()

Get the total annual purchased electricity (kWh) from the SQL file.

#### get_total_sold_electricity_kwh()

Get the total annual sold/surplus electricity (kWh) from the SQL file.

#### get_total_purchased_gas_kwh()

Return the total purchased gas in KWH.

#### get_total_end_kwh_by_fuel_type()

Return total end-use energy (kWh) grouped by fuel type from the SQL file.

---
