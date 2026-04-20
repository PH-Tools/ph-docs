# supportive_device

Honeybee-PH-HVAC-Equipment: Aux. Energy Supportive Devices.

**Source**: `honeybee_phhvac/supportive_device.py`

---

## PhSupportiveDevice

Auxiliary energy supportive device for Passive House HVAC systems.

**Inherits from**: `_base._PhHVACBase`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | Human-readable name for the device. |
| `device_type` | `int` | Numeric code identifying the device type. |
| `quantity` | `int` | Number of identical devices. |
| `in_conditioned_space` | `bool` | Whether the device is located inside the thermal envelope. |
| `norm_energy_demand_W` | `float` | Normalized energy demand in Watts. |
| `annual_period_operation_khrs` | `float` | Annual operating period in thousands of hours. |
| `ihg_utilization_factor` | `float` | Fraction of energy that becomes internal heat gain inside the envelope (0.0-1.0). |

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
| `_input_dict` | `Dict[str` | The dictionary to validate. |

**Returns**: `None`

#### move(moving_vec3D)

Move the device's elements along a vector.

| Arg | Type | Description |
|-----|------|-------------|
| `moving_vec3D` | — | A Vector3D with the direction and distance to move the ray. |

#### rotate(axis_vec3D, angle_degrees, origin_pt3D)

Rotate the device's elements by a certain angle around an axis and origin point.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_vec3D` | — | A Vector3D representing the axis of rotation. |
| `angle_degrees` | — | An angle for rotation in degrees. |
| `origin_pt3D` | — | A Point3D for the origin around which the object will be rotated. |

#### rotate_xy(angle_degrees, origin_pt3D)

Rotate the device's elements counterclockwise in the XY plane by a certain angle.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degrees` | — | An angle in degrees. |
| `origin_pt3D` | — | A Point3D for the origin around which the object will be rotated. |

#### reflect(normal_vec3D, origin_pt3D)

Reflect the device's elements across a plane with the input normal vector and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `normal_vec3D` | — | A normalized Vector3D representing the normal vector for the plane across which the element will be reflected. |
| `origin_pt3D` | — | A Point3D representing the origin from which to reflect. |

#### scale(scale_factor, origin_pt3D)

Scale the device's elements by a factor from an origin point.

| Arg | Type | Description |
|-----|------|-------------|
| `scale_factor` | — | A number representing how much the element should be scaled. |
| `origin_pt3D` | — | A Point3D representing the origin from which to scale. If None, it will be scaled from the World origin (0, 0, 0). |

---
