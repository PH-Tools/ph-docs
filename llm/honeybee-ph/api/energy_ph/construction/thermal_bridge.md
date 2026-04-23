# thermal_bridge

HBPH Thermal Bridge Objects

**Source**: `honeybee_energy_ph/thermal_bridge.py`

---

## PhThermalBridgeType

Classification of thermal bridge geometry types for PH certification.

**Inherits from**: `enumerables.CustomEnum`

### Values

| Value | Meaning |
|-------|---------|
| `""` | — |
| `""` | — |
| `""` | — |
| `""` | — |
| `""` | — |
| `""` | — |
| `""` | — |
| `""` | — |
| `""` | — |
| `""` | — |
| `""` | — |
| `""` | — |
| `""` | — |
| `""` | — |
| `""` | — |
| `"15-Ambient"` | Thermal bridge at ambient boundary. |
| `"16-Perimeter"` | Thermal bridge at perimeter/slab edge. |
| `"17-FS/BC"` | Thermal bridge at floor slab / boundary condition. |

---

## PhThermalBridge

A linear thermal bridge with 3D geometry and PH thermal properties.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `geometry` | — | The 3D line geometry. |
| `display_name` | `str` | — |
| `quantity` | `float` | Number of identical bridges. Default: 1.0. |
| `psi_value` | `float` | Linear thermal transmittance (W/mK). Default: 0.1. |
| `fRsi_value` | `float` | Temperature factor at the interior surface. Default: 0.75. |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `length` | `float` | Total length of the thermal bridge geometry (model units). |
| `group_type` | `PhThermalBridgeType` | The thermal bridge classification type. |

### Methods

#### move(moving_vec3D)

Move the TB-Geometry along a vector.

| Arg | Type | Description |
|-----|------|-------------|
| `moving_vec3D` | `Vector3D` | — |

**Returns**: `PhThermalBridge`

#### rotate(axis_vec3D, angle_degrees, origin_pt3D)

Rotate the TB-Geometry by a certain angle around an axis and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_vec3D` | `Vector3D` | — |
| `angle_degrees` | `float` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `PhThermalBridge`

#### rotate_xy(angle_degrees, origin_pt3D)

Rotate the TB-Geometry counterclockwise in the XY plane by a certain angle.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degrees` | `float` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `PhThermalBridge`

#### reflect(plane)

Reflected the TB-Geometry across a plane.

| Arg | Type | Description |
|-----|------|-------------|
| `plane` | `Plane` | — |

**Returns**: `PhThermalBridge`

#### scale(scale_factor, origin_pt3D)

Scale the TB-Geometry by a factor from an origin point.

| Arg | Type | Description |
|-----|------|-------------|
| `scale_factor` | `float` | — |
| `origin_pt3D` | `Point3D | None` | — |

**Returns**: `PhThermalBridge`

---
