# supportive_device

Honeybee-PH-HVAC-Equipment: Aux. Energy Supportive Devices.

**Source**: `honeybee_phhvac/supportive_device.py`

---

## PhSupportiveDevice

No description available.

**Inherits from**: `_base._PhHVACBase`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `device_type` | `int` | — |
| `quantity` | `int` | — |
| `in_conditioned_space` | `bool` | — |
| `norm_energy_demand_W` | `float` | — |
| `annual_period_operation_khrs` | `float` | — |
| `ihg_utilization_factor` | `float` | — |

### Methods

#### base_attrs_from_dict(_input_dict)

| Arg | Type | Description |
|-----|------|-------------|
| `_input_dict` | `Dict[str` | — |

**Returns**: `PhSupportiveDevice`

#### check_dict_type(_input_dict)

Check that the input dict type is correct for the Supportive Device being constructed.

| Arg | Type | Description |
|-----|------|-------------|
| `_input_dict` | `Dict[str` | — |

**Returns**: `None`

#### move(moving_vec3D)

Move the device's elements along a vector.

| Arg | Type | Description |
|-----|------|-------------|
| `moving_vec3D` | — | — |

#### rotate(axis_vec3D, angle_degrees, origin_pt3D)

Rotate the device's elements by a certain angle around an axis_vec3D and origin_pt3D.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_vec3D` | — | — |
| `angle_degrees` | — | — |
| `origin_pt3D` | — | — |

#### rotate_xy(angle_degrees, origin_pt3D)

Rotate the device's elements counterclockwise in the XY plane by a certain angle.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degrees` | — | — |
| `origin_pt3D` | — | — |

#### reflect(normal_vec3D, origin_pt3D)

Reflected the device's elements across a plane with the input normal vector and origin_pt3D.

| Arg | Type | Description |
|-----|------|-------------|
| `normal_vec3D` | — | — |
| `origin_pt3D` | — | — |

#### scale(scale_factor, origin_pt3D)

Scale the device's elements by a factor from an origin_pt3D point.

| Arg | Type | Description |
|-----|------|-------------|
| `scale_factor` | — | — |
| `origin_pt3D` | — | — |

---
