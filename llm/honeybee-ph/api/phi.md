# phi

PHI Certification Settings Class.

**Source**: `honeybee_ph/phi.py`

---

## EnumProperty

Descriptor for creating and managing the PHI-Cert Enum items.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `attribute_name` | — | The name of the attribute this descriptor manages. |
| `phpp_version` | — | The PHPP version number (9 or 10). |
| `enum` | `_create_enum_class` | The dynamically created enum class for validation. |

---

## PHPPSettings10

Settings for PHPP v10.

**Inherits from**: `_PHPPSettingsBase`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `building_use_type` | `EnumProperty` | The building use type classification. |
| `ihg_type` | `EnumProperty` | The internal heat gains calculation type. |
| `certification_class` | `EnumProperty` | The certification class (Classic, Plus, Premium). |
| `certification_type` | `EnumProperty` | The certification type (Passive House, EnerPHit, etc.). |
| `primary_energy_type` | `EnumProperty` | The primary energy evaluation type. |
| `retrofit_type` | `EnumProperty` | The retrofit category (New Building, Retrofit, Staged Retrofit). |
| `tfa_override` | `Optional[unknown]` | Optional override for the treated floor area. |

---

## PHPPSettings9

Settings for PHPP v9.

**Inherits from**: `_PHPPSettingsBase`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `building_category_type` | `EnumProperty` | The building category (Residential or Non-Residential). |
| `building_use_type` | `EnumProperty` | The building use type classification. |
| `ihg_type` | `EnumProperty` | The internal heat gains calculation type. |
| `occupancy_type` | `EnumProperty` | The occupancy type (Standard or User Determined). |
| `certification_type` | `EnumProperty` | The certification type (Passive House, EnerPHit, etc.). |
| `certification_class` | `EnumProperty` | The certification class (Classic, Plus, Premium). |
| `primary_energy_type` | `EnumProperty` | The primary energy evaluation type. |
| `enerphit_type` | `EnumProperty` | The EnerPHit method (Component or Energy Demand). |
| `retrofit_type` | `EnumProperty` | The retrofit category (New Building, Retrofit, Step-by-Step Retrofit). |
| `tfa_override` | `Optional[unknown]` | Optional override for the treated floor area. |

---

## PhiCertification

PHI PHPP Certification object with Attributes that vary by version (9 | 10).

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `phpp_version` | — | The PHPP version number (9 or 10). |
| `attributes` | `PHPPSettings10` | Version-specific certification settings. |

### Methods

#### move(moving_vec3D)

Move the PHI Certification object along a vector.

| Arg | Type | Description |
|-----|------|-------------|
| `moving_vec3D` | `Vector3D` | A Vector3D with the direction and distance to move the object. |

**Returns**: `PhiCertification`

#### rotate(axis_vec3D, angle_degrees, origin_pt3D)

Rotate the PHI Certification object by a certain angle around an axis and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_vec3D` | `Vector3D` | A Vector3D axis representing the axis of rotation. |
| `angle_degrees` | `float` | An angle for rotation in degrees. |
| `origin_pt3D` | `Point3D` | A Point3D for the origin around which the object will be rotated. |

**Returns**: `PhiCertification`

#### rotate_xy(angle_degrees, origin_pt3D)

Rotate the PHI Certification object counterclockwise in the XY plane by a certain angle.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degrees` | `float` | An angle in degrees. |
| `origin_pt3D` | `Point3D` | A Point3D for the origin around which the object will be rotated. |

**Returns**: `PhiCertification`

#### reflect(plane)

Reflect the PHI Certification object across a plane.

| Arg | Type | Description |
|-----|------|-------------|
| `plane` | `Plane` | A Plane representing the plane across which to reflect. |

**Returns**: `PhiCertification`

#### scale(scale_factor, origin_pt3D)

Scale the PHI Certification object by a factor from an origin point.

| Arg | Type | Description |
|-----|------|-------------|
| `scale_factor` | `float` | A number representing how much the object should be scaled. |
| `origin_pt3D` | `Point3D | None` | A Point3D representing the origin from which to scale. If None, it will be scaled from the World origin (0, 0, 0). |

**Returns**: `PhiCertification`

---
