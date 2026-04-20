# heat_pumps

Honeybee-PH-HVAC-Equipment: Heat-Pump Devices.

**Source**: `honeybee_phhvac/heat_pumps.py`

---

## UnknownPhHeatPumpTypeError

No description available.

**Inherits from**: `Exception`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `msg` | `format` | — |

---

## PhHeatPumpSystem

Base class for all HBPH-Cooling-Systems.

**Inherits from**: `_base._PhHVACBase`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `heat_pump_class_name` | — | — |
| `percent_coverage` | `float` | — |
| `cooling_params` | `PhHeatPumpCoolingParams` | — |

### Methods

#### base_attrs_from_dict(_input_dict)

| Arg | Type | Description |
|-----|------|-------------|
| `_input_dict` | `PhHeatPumpSystem` | — |

**Returns**: `PhHeatPumpSystem`

#### check_dict_type(_input_dict)

Check that the input dict type is correct for the Heat Pump System being constructed.

| Arg | Type | Description |
|-----|------|-------------|
| `_input_dict` | `Dict[str` | — |

**Returns**: `None`

#### move(moving_vec3D)

Move the System's elements along a vector.

| Arg | Type | Description |
|-----|------|-------------|
| `moving_vec3D` | — | — |

#### rotate(axis_vec3D, angle_degrees, origin_pt3D)

Rotate the System's elements by a certain angle around an axis_vec3D and origin_pt3D.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_vec3D` | — | — |
| `angle_degrees` | — | — |
| `origin_pt3D` | — | — |

#### rotate_xy(angle_degrees, origin_pt3D)

Rotate the System's elements counterclockwise in the XY plane by a certain angle.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degrees` | — | — |
| `origin_pt3D` | — | — |

#### reflect(normal_vec3D, origin_pt3D)

Reflected the System's elements across a plane with the input normal vector and origin_pt3D.

| Arg | Type | Description |
|-----|------|-------------|
| `normal_vec3D` | — | — |
| `origin_pt3D` | — | — |

#### scale(scale_factor, origin_pt3D)

Scale the System's elements by a factor from an origin_pt3D point.

| Arg | Type | Description |
|-----|------|-------------|
| `scale_factor` | — | — |
| `origin_pt3D` | — | — |

---

## PhHeatPumpCoolingParams_Base

Base class for all HBPH-Cooling-Parameters.

**Inherits from**: `_base._PhHVACBase`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `used` | `bool` | — |

### Methods

#### base_attrs_from_dict(_input_dict)

| Arg | Type | Description |
|-----|------|-------------|
| `_input_dict` | `PhHeatPumpCoolingParams_Base` | — |

**Returns**: `PhHeatPumpCoolingParams_Base`

---

## PhHeatPumpCoolingParams_Ventilation

Cooling via the Fresh-Air Ventilation System (ERV).

**Inherits from**: `PhHeatPumpCoolingParams_Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `single_speed` | `bool` | — |
| `min_coil_temp` | `float` | — |
| `capacity` | `float` | — |
| `annual_COP` | `float` | — |

---

## PhHeatPumpCoolingParams_Recirculation

Cooling via a 'recirculation' system (typical AC).

**Inherits from**: `PhHeatPumpCoolingParams_Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `single_speed` | `bool` | — |
| `min_coil_temp` | `float` | — |
| `flow_rate_m3_hr` | `float` | — |
| `flow_rate_variable` | `bool` | — |
| `capacity` | `float` | — |
| `annual_COP` | `float` | — |

---

## PhHeatPumpCoolingParams_Dehumidification

Cooling via dedicated dehumidification system.

**Inherits from**: `PhHeatPumpCoolingParams_Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `useful_heat_loss` | `bool` | — |
| `annual_COP` | `float` | — |

---

## PhHeatPumpCoolingParams_Panel

Cooling via radiant panels.

**Inherits from**: `PhHeatPumpCoolingParams_Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `annual_COP` | `float` | — |

---

## PhHeatPumpCoolingParams

A Collection of Cooling Parameters for various types of systems.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `percent_coverage` | `float` | — |
| `ventilation` | `PhHeatPumpCoolingParams_Ventilation` | — |
| `recirculation` | `PhHeatPumpCoolingParams_Recirculation` | — |
| `dehumidification` | `PhHeatPumpCoolingParams_Dehumidification` | — |
| `panel` | `PhHeatPumpCoolingParams_Panel` | — |

---

## PhHeatPumpAnnual

Electric heat-pump with only Annual performance values.

**Inherits from**: `PhHeatPumpSystem`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `annual_COP` | `float` | — |
| `total_system_perf_ratio` | `float` | — |

---

## PhHeatPumpRatedMonthly

Electric heat-pump with 2 separate monthly performance values.

**Inherits from**: `PhHeatPumpSystem`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `COP_1` | `float` | — |
| `ambient_temp_1` | — | — |
| `COP_2` | `float` | — |
| `ambient_temp_2` | `float` | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `monthly_COPS` | — | — |
| `monthly_temps` | — | — |

---

## PhHeatPumpCombined

No description available.

**Inherits from**: `PhHeatPumpSystem`

---

## PhHeatPumpSystemBuilder

Constructor class for HBPH-CoolingSystems

---
