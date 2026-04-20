# heating

Honeybee-PH-HVAC-Equipment: Heating Devices.

**Source**: `honeybee_phhvac/heating.py`

---

## UnknownPhHeatingTypeError

No description available.

**Inherits from**: `Exception`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `msg` | `format` | — |

---

## PhHeatingSystem

Base class for all PH-Heating Systems (elec, boiler, etc...)

**Inherits from**: `_base._PhHVACBase`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `heating_type` | — | — |
| `percent_coverage` | `float` | — |

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
| `_input_dict` | `dict` | — |

**Returns**: `None`

#### move(moving_vec3D)

Move the System's elements along a vector.

| Arg | Type | Description |
|-----|------|-------------|
| `moving_vec3D` | — | — |

#### rotate(axis_vec3D, angle_degree, origin_pt3D)

Rotate the System's elements by a certain angle around an axis and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_vec3D` | — | — |
| `angle_degree` | — | — |
| `origin_pt3D` | — | — |

#### rotate_xy(angle_degree, origin_pt3D)

Rotate the System's elements counterclockwise in the XY plane by a certain angle.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degree` | — | — |
| `origin_pt3D` | — | — |

#### reflect(normal_vec3D, origin_pt3D)

Reflected the System's elements across a plane with the input normal vector and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `normal_vec3D` | — | — |
| `origin_pt3D` | — | — |

#### scale(scale_factor, origin)

Scale the System's elements by a factor from an origin point.

| Arg | Type | Description |
|-----|------|-------------|
| `scale_factor` | — | — |
| `origin` | — | — |

---

## PhHeatingDirectElectric

Heating via direct-electric (resistance heating).

**Inherits from**: `PhHeatingSystem`

---

## PhHeatingFossilBoiler

Heating via boiler using fossil-fuel (gas, oil)

**Inherits from**: `PhHeatingSystem`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `fuel` | — | — |
| `condensing` | `bool` | — |
| `in_conditioned_space` | `bool` | — |
| `effic_at_30_percent_load` | `float` | — |
| `effic_at_nominal_load` | `float` | — |
| `avg_rtrn_temp_at_30_percent_load` | `int` | — |
| `avg_temp_at_70C_55C` | `int` | — |
| `avg_temp_at_55C_45C` | `int` | — |
| `avg_temp_at_32C_28C` | `int` | — |

---

## PhHeatingWoodBoiler

Heating via boiler using wood (log, pellet).

**Inherits from**: `PhHeatingSystem`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `fuel` | — | — |
| `in_conditioned_space` | `bool` | — |
| `effic_in_basic_cycle` | `float` | — |
| `effic_in_const_operation` | `float` | — |
| `avg_frac_heat_output` | `float` | — |
| `temp_diff_on_off` | `int` | — |
| `rated_capacity` | `int` | — |
| `demand_basic_cycle` | `int` | — |
| `power_stationary_run` | `int` | — |
| `power_standard_run` | `Optional[float]` | — |
| `no_transport_pellets` | `Optional[bool]` | — |
| `only_control` | `Optional[bool]` | — |
| `area_mech_room` | `Optional[float]` | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `useful_heat_output` | — | — |
| `avg_power_output` | — | — |

---

## PhHeatingDistrict

Heating via district-heat.

**Inherits from**: `PhHeatingSystem`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `fuel` | — | — |
| `util_factor_of_heat_transfer_station` | `float` | — |

---

## PhHeatingSystemBuilder

Constructor class for PH-HeatingSystems

---
