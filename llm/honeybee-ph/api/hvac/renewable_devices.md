# renewable_devices

Honeybee-PH-HVAC-Equipment: Renewable Energy Devices.

**Source**: `honeybee_phhvac/renewable_devices.py`

---

## UnknownPhRenewableEnergyTypeError

Raised when an unrecognized renewable energy device type is encountered.

**Inherits from**: `Exception`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `msg` | `format` | Formatted error message describing the unknown type and valid options. |

---

## PhRenewableEnergyDevice

Base class for all HBPH Renewable Energy Systems (PV, etc).

**Inherits from**: `_base._PhHVACBase`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `device_typename` | — | Class name string identifying the device type for serialization. |
| `percent_coverage` | `float` | Fraction of energy demand covered by this device (0.0-1.0). |

### Methods

#### base_attrs_from_dict(_input_dict)

| Arg | Type | Description |
|-----|------|-------------|
| `_input_dict` | `PhRenewableEnergyDevice` | — |

**Returns**: `PhRenewableEnergyDevice`

#### check_dict_type(_input_dict)

Check that the input dict type is correct for the Heating System being constructed.

| Arg | Type | Description |
|-----|------|-------------|
| `_input_dict` | `dict` | The dictionary to validate. |

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

## PhPhotovoltaicDevice

Photovoltaic (PV) renewable energy device.

**Inherits from**: `PhRenewableEnergyDevice`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `photovoltaic_renewable_energy` | `float` | Annual PV renewable energy production (kWh/yr). |
| `array_size` | `float` | Total PV array area (m2). |
| `utilization_factor` | `float` | Fraction of generated energy that is utilized (0.0-1.0). |

---

## PhRenewableEnergyDeviceBuilder

Constructor class for PH-Renewable-Energy-System objects.

---
