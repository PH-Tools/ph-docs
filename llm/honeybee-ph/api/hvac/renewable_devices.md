# renewable_devices

Honeybee-PH-HVAC-Equipment: Renewable Energy Devices.

**Source**: `honeybee_phhvac/renewable_devices.py`

---

## UnknownPhRenewableEnergyTypeError

No description available.

**Inherits from**: `Exception`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `msg` | `format` | — |

---

## PhRenewableEnergyDevice

Base class for all HBPH Renewable Energy Systems (PV, etc).

**Inherits from**: `_base._PhHVACBase`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `device_typename` | — | — |
| `percent_coverage` | `float` | — |

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
| `_input_dict` | `dict` | — |

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

## PhPhotovoltaicDevice

PV System.

**Inherits from**: `PhRenewableEnergyDevice`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `photovoltaic_renewable_energy` | `float` | — |
| `array_size` | `float` | — |
| `utilization_factor` | `float` | — |

---

## PhRenewableEnergyDeviceBuilder

Constructor class for PH-Renewable-Energy-System objects.

---
