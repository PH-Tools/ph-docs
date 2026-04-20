# heat_pumps

Honeybee-PH-HVAC-Equipment: Heat-Pump Devices.

**Source**: `honeybee_phhvac/heat_pumps.py`

---

## UnknownPhHeatPumpTypeError

Error raised when an unrecognized heat-pump type name is encountered.

**Inherits from**: `Exception`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `msg` | `format` | Formatted error message including the received type and valid options. |

---

## PhHeatPumpSystem

Base class for all HBPH heat-pump systems.

**Inherits from**: `_base._PhHVACBase`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `heat_pump_class_name` | — | The class name of the heat-pump type. |
| `percent_coverage` | `float` | Fractional coverage of the heating load (0.0-1.0). |
| `cooling_params` | `PhHeatPumpCoolingParams` | Cooling parameter collection for this heat pump. |

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
| `_input_dict` | `Dict[str` | The dictionary to validate. |

**Returns**: `None`

#### move(moving_vec3D)

Move the System's elements along a vector.

| Arg | Type | Description |
|-----|------|-------------|
| `moving_vec3D` | — | A Vector3D with the direction and distance to move the ray. |

#### rotate(axis_vec3D, angle_degrees, origin_pt3D)

Rotate the System's elements by a certain angle around an axis and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_vec3D` | — | A Vector3D representing the axis of rotation. |
| `angle_degrees` | — | An angle for rotation in degrees. |
| `origin_pt3D` | — | A Point3D for the origin around which the object will be rotated. |

#### rotate_xy(angle_degrees, origin_pt3D)

Rotate the System's elements counterclockwise in the XY plane by a certain angle.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degrees` | — | An angle in degrees. |
| `origin_pt3D` | — | A Point3D for the origin around which the object will be rotated. |

#### reflect(normal_vec3D, origin_pt3D)

Reflect the System's elements across a plane with the input normal vector and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `normal_vec3D` | — | A normalized Vector3D representing the normal for the plane across which elements will be reflected. |
| `origin_pt3D` | — | A Point3D representing the origin from which to reflect. |

#### scale(scale_factor, origin_pt3D)

Scale the System's elements by a factor from an origin point.

| Arg | Type | Description |
|-----|------|-------------|
| `scale_factor` | — | A number representing how much the elements should be scaled. |
| `origin_pt3D` | — | A Point3D representing the origin from which to scale. If None, it will be scaled from the World origin (0, 0, 0). |

---

## PhHeatPumpCoolingParams_Base

Base class for all HBPH cooling parameters.

**Inherits from**: `_base._PhHVACBase`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `used` | `bool` | Whether this cooling mode is active. |

### Methods

#### base_attrs_from_dict(_input_dict)

| Arg | Type | Description |
|-----|------|-------------|
| `_input_dict` | `PhHeatPumpCoolingParams_Base` | — |

**Returns**: `PhHeatPumpCoolingParams_Base`

---

## PhHeatPumpCoolingParams_Ventilation

Cooling via the fresh-air ventilation system (ERV).

**Inherits from**: `PhHeatPumpCoolingParams_Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `single_speed` | `bool` | Whether the system operates at a single speed only. |
| `min_coil_temp` | `float` | Minimum coil temperature in degrees Celsius. |
| `capacity` | `float` | Cooling capacity in kW. |
| `annual_COP` | `float` | Annual coefficient of performance. |

---

## PhHeatPumpCoolingParams_Recirculation

Cooling via a recirculation system (typical AC).

**Inherits from**: `PhHeatPumpCoolingParams_Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `single_speed` | `bool` | Whether the system operates at a single speed only. |
| `min_coil_temp` | `float` | Minimum coil temperature in degrees Celsius. |
| `flow_rate_m3_hr` | `float` | Airflow rate in cubic meters per hour. |
| `flow_rate_variable` | `bool` | Whether the flow rate is variable. |
| `capacity` | `float` | Cooling capacity in kW. |
| `annual_COP` | `float` | Annual coefficient of performance. |

---

## PhHeatPumpCoolingParams_Dehumidification

Cooling via a dedicated dehumidification system.

**Inherits from**: `PhHeatPumpCoolingParams_Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `useful_heat_loss` | `bool` | Whether heat loss from dehumidification is considered useful. |
| `annual_COP` | `float` | Annual coefficient of performance. |

---

## PhHeatPumpCoolingParams_Panel

Cooling via radiant panels.

**Inherits from**: `PhHeatPumpCoolingParams_Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `annual_COP` | `float` | Annual coefficient of performance. |

---

## PhHeatPumpCoolingParams

A collection of cooling parameters for various types of cooling systems.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `percent_coverage` | `float` | Fractional coverage of the cooling load (0.0-1.0). |
| `ventilation` | `PhHeatPumpCoolingParams_Ventilation` | Ventilation-based cooling parameters. |
| `recirculation` | `PhHeatPumpCoolingParams_Recirculation` | Recirculation-based cooling parameters. |
| `dehumidification` | `PhHeatPumpCoolingParams_Dehumidification` | Dehumidification-based cooling parameters. |
| `panel` | `PhHeatPumpCoolingParams_Panel` | Radiant-panel-based cooling parameters. |

---

## PhHeatPumpAnnual

Electric heat pump with only annual performance values.

**Inherits from**: `PhHeatPumpSystem`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `annual_COP` | `float` | Annual coefficient of performance. |
| `total_system_perf_ratio` | `float` | Total system performance ratio. |

---

## PhHeatPumpRatedMonthly

Electric heat pump with two separate monthly rated performance values.

**Inherits from**: `PhHeatPumpSystem`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `COP_1` | `float` | Coefficient of performance at the first rating point. |
| `ambient_temp_1` | — | Ambient temperature for the first rating point in degrees Celsius. |
| `COP_2` | `float` | Coefficient of performance at the second rating point. |
| `ambient_temp_2` | `float` | Ambient temperature for the second rating point in degrees Celsius. |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `monthly_COPS` | `List[float]` | The two monthly COP rating values. |
| `monthly_temps` | `List[float]` | The two monthly ambient temperature rating values in degrees Celsius. |

---

## PhHeatPumpCombined

Combined heat pump system (not yet implemented).

**Inherits from**: `PhHeatPumpSystem`

---

## PhHeatPumpSystemBuilder

Factory class for constructing the correct PhHeatPumpSystem subclass from a dictionary.

---
