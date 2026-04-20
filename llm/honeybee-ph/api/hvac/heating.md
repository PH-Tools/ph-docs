# heating

Honeybee-PH-HVAC-Equipment: Heating Devices.

**Source**: `honeybee_phhvac/heating.py`

---

## UnknownPhHeatingTypeError

Raised when an unrecognized PH heating system type is encountered.

**Inherits from**: `Exception`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `msg` | `format` | Human-readable error message describing the invalid type. |

---

## PhHeatingSystem

Base class for all PH-Heating Systems (elec, boiler, etc...).

**Inherits from**: `_base._PhHVACBase`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `heating_type` | — | The class name of the heating system type. |
| `percent_coverage` | `float` | Fraction of total heating load covered by this system (0.0-1.0). |

### Methods

#### base_attrs_from_dict(_input_dict)

| Arg | Type | Description |
|-----|------|-------------|
| `_input_dict` | `PhHeatingSystem` | — |

**Returns**: `PhHeatingSystem`

#### check_dict_type(_input_dict)

Check that the input dict type is correct for the Heating System being constructed.

| Arg | Type | Description |
|-----|------|-------------|
| `_input_dict` | `dict` | Serialized heating system dictionary with a 'heating_type' key. |

**Returns**: `None`

#### move(moving_vec3D)

Move the System's elements along a vector.

| Arg | Type | Description |
|-----|------|-------------|
| `moving_vec3D` | — | A Vector3D with the direction and distance to move the ray. |

#### rotate(axis_vec3D, angle_degree, origin_pt3D)

Rotate the System's elements by a certain angle around an axis and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_vec3D` | — | A Vector3D axis representing the axis of rotation. |
| `angle_degree` | — | An angle for rotation in degrees. |
| `origin_pt3D` | — | A Point3D for the origin around which the object will be rotated. |

#### rotate_xy(angle_degree, origin_pt3D)

Rotate the System's elements counterclockwise in the XY plane by a certain angle.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degree` | — | An angle in degrees. |
| `origin_pt3D` | — | A Point3D for the origin around which the object will be rotated. |

#### reflect(normal_vec3D, origin_pt3D)

Reflect the System's elements across a plane with the input normal vector and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `normal_vec3D` | — | A Vector3D representing the normal vector for the plane across which the line segment will be reflected. THIS VECTOR MUST BE NORMALIZED. |
| `origin_pt3D` | — | A Point3D representing the origin from which to reflect. |

#### scale(scale_factor, origin)

Scale the System's elements by a factor from an origin point.

| Arg | Type | Description |
|-----|------|-------------|
| `scale_factor` | — | A number representing how much the line segment should be scaled. |
| `origin` | — | A Point3D representing the origin from which to scale. If None, it will be scaled from the World origin (0, 0, 0). |

---

## PhHeatingDirectElectric

Heating via direct-electric (resistance heating).

**Inherits from**: `PhHeatingSystem`

---

## PhHeatingFossilBoiler

Heating via boiler using fossil-fuel (gas, oil).

**Inherits from**: `PhHeatingSystem`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `fuel` | — | Fuel type constant from the fuels module. |
| `condensing` | `bool` | True if the boiler is a condensing type. |
| `in_conditioned_space` | `bool` | True if the boiler is located within conditioned space. |
| `effic_at_30_percent_load` | `float` | Boiler efficiency at 30 percent part-load. |
| `effic_at_nominal_load` | `float` | Boiler efficiency at nominal (full) load. |
| `avg_rtrn_temp_at_30_percent_load` | `int` | Average return temperature at 30 percent load (deg C). |
| `avg_temp_at_70C_55C` | `int` | Average boiler temperature at 70C/55C flow/return (deg C). |
| `avg_temp_at_55C_45C` | `int` | Average boiler temperature at 55C/45C flow/return (deg C). |
| `avg_temp_at_32C_28C` | `int` | Average boiler temperature at 32C/28C flow/return (deg C). |

---

## PhHeatingWoodBoiler

Heating via boiler using wood (log, pellet).

**Inherits from**: `PhHeatingSystem`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `fuel` | — | Fuel type constant from the fuels module. |
| `in_conditioned_space` | `bool` | True if the boiler is located within conditioned space. |
| `effic_in_basic_cycle` | `float` | Efficiency during the basic heating cycle. |
| `effic_in_const_operation` | `float` | Efficiency during constant operation. |
| `avg_frac_heat_output` | `float` | Average fraction of rated heat output. |
| `temp_diff_on_off` | `int` | Temperature difference between on and off cycles (deg C). |
| `rated_capacity` | `int` | Rated heating capacity in kW. |
| `demand_basic_cycle` | `int` | Energy demand per basic cycle in kWh. |
| `power_stationary_run` | `int` | Electrical power during stationary run in W. |
| `power_standard_run` | `Optional[float]` | Electrical power during standard run in W. |
| `no_transport_pellets` | `Optional[bool]` | True if no pellet transport mechanism is used. |
| `only_control` | `Optional[bool]` | True if only control power is consumed. |
| `area_mech_room` | `Optional[float]` | Mechanical room area in m2. |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `useful_heat_output` | `float` | Useful heat output (90 percent of rated capacity) in kWh. |
| `avg_power_output` | `float` | Average power output (50 percent of rated capacity) in kW. |

---

## PhHeatingDistrict

Heating via district-heat.

**Inherits from**: `PhHeatingSystem`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `fuel` | — | District energy carrier constant from the fuels module. |
| `util_factor_of_heat_transfer_station` | `float` | Utilization factor of the heat transfer station. |

---

## PhHeatingSystemBuilder

Constructor class for PH-HeatingSystems.

---
