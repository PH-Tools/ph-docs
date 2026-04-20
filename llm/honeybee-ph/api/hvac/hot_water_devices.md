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

No description available.

**Inherits from**: `enumerables.CustomEnum`

### Values

| Value | Meaning |
|-------|---------|
| `"0-No storage tank"` | — |
| `"1-DHW and heating"` | — |
| `"2-DHW only"` | — |

---

## PhHvacHotWaterTank

No description available.

**Inherits from**: `_base._PhHVACBase`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `quantity` | `int` | — |
| `in_conditioned_space` | `bool` | — |
| `solar_connection` | `bool` | — |
| `solar_losses` | `float` | — |
| `storage_loss_rate` | `float` | — |
| `storage_capacity` | `float` | — |
| `standby_losses` | `float` | — |
| `standby_fraction` | `float` | — |
| `room_temp` | `float` | — |
| `water_temp` | `float` | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `tank_type` | — | — |

---

## PhHvacHotWaterHeater

Base class for all PH Hot-Water Heaters.

**Inherits from**: `_base._PhHVACBase`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `percent_coverage` | `float` | — |
| `in_conditioned_space` | `bool` | — |

---

## PhHvacHotWaterHeaterElectric

No description available.

**Inherits from**: `PhHvacHotWaterHeater`

---

## PhHvacHotWaterHeaterBoiler

No description available.

**Inherits from**: `PhHvacHotWaterHeater`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `fuel` | `int` | — |
| `condensing` | `bool` | — |
| `effic_at_30_perc_load` | `float` | — |
| `effic_at_nominal_load` | `float` | — |
| `avg_return_temp_at_30_perc_load` | `int` | — |
| `avg_boiler_temp_at_70_55` | `int` | — |
| `avg_boiler_temp_at_55_45` | `int` | — |
| `avg_boiler_temp_at_35_28` | `int` | — |

---

## PhHvacHotWaterHeaterBoilerWood

No description available.

**Inherits from**: `PhHvacHotWaterHeater`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `fuel` | `int` | — |
| `effic_in_basic_cycle` | `float` | — |
| `effic_in_const_operation` | `float` | — |
| `avg_frac_heat_released` | `float` | — |
| `on_off_temp_diff` | `int` | — |

---

## PhHvacHotWaterHeaterDistrict

No description available.

**Inherits from**: `PhHvacHotWaterHeater`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `energy_carrier` | `int` | — |
| `solar_fraction` | `int` | — |
| `util_fact_heat_transfer` | `int` | — |

---

## PhHvacHotWaterHeaterHeatPump_Monthly

No description available.

**Inherits from**: `PhHvacHotWaterHeater`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `COP_1` | `float` | — |
| `ambient_temp_1` | — | — |
| `COP_2` | `float` | — |
| `ambient_temp_2` | `float` | — |

---

## PhHvacHotWaterHeaterHeatPump_Annual

No description available.

**Inherits from**: `PhHvacHotWaterHeater`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `annual_COP` | `(float | None)` | — |
| `total_system_perf_ratio` | `(float | None)` | — |

---

## PhHvacHotWaterHeaterHeatPump_Inside

No description available.

**Inherits from**: `PhHvacHotWaterHeater`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `annual_COP` | `(float | None)` | — |
| `total_system_perf_ratio` | `(float | None)` | — |
| `annual_energy_factor` | `(float | None)` | — |

---

## PhHvacHotWaterHeaterBuilder

Constructor class for Hot-Water-Heater objects

---
