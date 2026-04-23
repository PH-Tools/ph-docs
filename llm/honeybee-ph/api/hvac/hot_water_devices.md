# hot_water_devices

Honeybee-PH-HVAC: Hot Water Devices.

**Source**: `honeybee_phhvac/hot_water_devices.py`

---

## UnknownPhHvacHotWaterHeaterTypeError

No description available.

**Inherits from**: `Exception`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `msg` | `format` | — |

---

## PhHvacHotWaterTankType

Enumeration of hot water storage tank types.

**Inherits from**: `enumerables.CustomEnum`

### Values

| Value | Meaning |
|-------|---------|
| `"0-No storage tank"` | — |
| `"1-DHW and heating"` | — |
| `"2-DHW only"` | — |

---

## PhHvacHotWaterTank

A Passive House hot water storage tank.

**Inherits from**: `_base._PhHVACBase`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | User-facing name for the tank. |
| `quantity` | `int` | Number of identical tanks. |
| `in_conditioned_space` | `bool` | True if the tank is inside conditioned space. |
| `solar_connection` | `bool` | True if the tank has a solar thermal connection. |
| `solar_losses` | `float` | Solar thermal losses (W). |
| `storage_loss_rate` | `float` | Storage heat loss rate (W/K). |
| `storage_capacity` | `float` | Tank volume in liters. |
| `standby_losses` | `float` | Standby heat losses (W/K). |
| `standby_fraction` | `float` | Fraction of standby losses contributing to heating. |
| `room_temp` | `float` | Ambient room temperature surrounding the tank (deg-C). |
| `water_temp` | `float` | Hot water storage temperature (deg-C). |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `tank_type` | `str` | The active tank type value string. |

---

## PhHvacHotWaterHeater

Base class for all PH hot water heater devices.

**Inherits from**: `_base._PhHVACBase`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `percent_coverage` | `float` | Fraction of hot water demand covered by this heater (0.0-1.0). |
| `in_conditioned_space` | `bool` | True if the heater is located inside conditioned space. |

---

## PhHvacHotWaterHeaterElectric

An electric resistance hot water heater.

**Inherits from**: `PhHvacHotWaterHeater`

---

## PhHvacHotWaterHeaterBoiler

A fossil-fuel (gas/oil) boiler hot water heater.

**Inherits from**: `PhHvacHotWaterHeater`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `fuel` | `int` | Fuel type identifier (1=Gas, 2=Oil). |
| `condensing` | `bool` | True if the boiler is a condensing type. |
| `effic_at_30_perc_load` | `float` | Efficiency at 30-percent part-load. |
| `effic_at_nominal_load` | `float` | Efficiency at nominal (full) load. |
| `avg_return_temp_at_30_perc_load` | `int` | Average return temperature at 30-percent load (deg-C). |
| `avg_boiler_temp_at_70_55` | `int` | Average boiler temperature at 70/55 supply/return (deg-C). |
| `avg_boiler_temp_at_55_45` | `int` | Average boiler temperature at 55/45 supply/return (deg-C). |
| `avg_boiler_temp_at_35_28` | `int` | Average boiler temperature at 35/28 supply/return (deg-C). |

---

## PhHvacHotWaterHeaterBoilerWood

A wood-fuel (pellet/log) boiler hot water heater.

**Inherits from**: `PhHvacHotWaterHeater`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `fuel` | `int` | Fuel type identifier (1=Pellet, 2=Log). |
| `effic_in_basic_cycle` | `float` | Efficiency during the basic heating cycle. |
| `effic_in_const_operation` | `float` | Efficiency during constant operation. |
| `avg_frac_heat_released` | `float` | Average fraction of heat released to the space. |
| `on_off_temp_diff` | `int` | Temperature differential for on/off cycling (deg-C). |

---

## PhHvacHotWaterHeaterDistrict

A district heating hot water heater connection.

**Inherits from**: `PhHvacHotWaterHeater`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `energy_carrier` | `int` | Energy carrier type identifier. |
| `solar_fraction` | `int` | Fraction of energy supplied by solar thermal. |
| `util_fact_heat_transfer` | `int` | Utilization factor for heat transfer. |

---

## PhHvacHotWaterHeaterHeatPump_Monthly

A heat pump hot water heater using monthly COP values at two test points.

**Inherits from**: `PhHvacHotWaterHeater`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `COP_1` | `float` | Coefficient of performance at test condition 1. |
| `ambient_temp_1` | — | Ambient temperature for test condition 1 (deg-C). |
| `COP_2` | `float` | Coefficient of performance at test condition 2. |
| `ambient_temp_2` | `float` | Ambient temperature for test condition 2 (deg-C). |

---

## PhHvacHotWaterHeaterHeatPump_Annual

A heat pump hot water heater using a single annual COP value.

**Inherits from**: `PhHvacHotWaterHeater`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `annual_COP` | `(float | None)` | Annual coefficient of performance. |
| `total_system_perf_ratio` | `(float | None)` | Total system performance ratio. |

---

## PhHvacHotWaterHeaterHeatPump_Inside

A heat pump hot water heater located inside conditioned space, rated by annual energy factor.

**Inherits from**: `PhHvacHotWaterHeater`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `annual_COP` | `(float | None)` | Annual coefficient of performance. |
| `total_system_perf_ratio` | `(float | None)` | Total system performance ratio. |
| `annual_energy_factor` | `(float | None)` | Annual energy factor (UEF or EF). |

---

## PhHvacHotWaterHeaterBuilder

Factory class for constructing PhHvacHotWaterHeater objects from dictionaries.

---
