# phi

PHI Certification Settings Class.

**Source**: `honeybee_ph/phi.py`

---

## EnumProperty

Descriptor for creating and managing the PHI-Cert Enum items.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `attribute_name` | — | — |
| `phpp_version` | — | — |
| `enum` | `_create_enum_class` | — |

---

## PHPPSettings10

Settings for PHPP v10

**Inherits from**: `_PHPPSettingsBase`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `building_use_type` | `EnumProperty` | — |
| `ihg_type` | `EnumProperty` | — |
| `certification_class` | `EnumProperty` | — |
| `certification_type` | `EnumProperty` | — |
| `primary_energy_type` | `EnumProperty` | — |
| `retrofit_type` | `EnumProperty` | — |
| `tfa_override` | `Optional[unknown]` | — |

---

## PHPPSettings9

Settings for PHPP v9

**Inherits from**: `_PHPPSettingsBase`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `building_category_type` | `EnumProperty` | — |
| `building_use_type` | `EnumProperty` | — |
| `ihg_type` | `EnumProperty` | — |
| `occupancy_type` | `EnumProperty` | — |
| `certification_type` | `EnumProperty` | — |
| `certification_class` | `EnumProperty` | — |
| `primary_energy_type` | `EnumProperty` | — |
| `enerphit_type` | `EnumProperty` | — |
| `retrofit_type` | `EnumProperty` | — |
| `tfa_override` | `Optional[unknown]` | — |

---

## PhiCertification

PHI PHPP Certification object with Attributes that vary by version (9 | 10)

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `phpp_version` | — | — |
| `attributes` | `PHPPSettings10` | — |

### Methods

#### move(moving_vec3D)

Move the Phius Certification Object along a vector.

| Arg | Type | Description |
|-----|------|-------------|
| `moving_vec3D` | `Vector3D` | — |

**Returns**: `PhiCertification`

#### rotate(axis_vec3D, angle_degrees, origin_pt3D)

Rotate the Phius Certification Object by a certain angle around an axis and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_vec3D` | `Vector3D` | — |
| `angle_degrees` | `float` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `PhiCertification`

#### rotate_xy(angle_degrees, origin_pt3D)

Rotate the Phius Certification Object counterclockwise in the XY plane by a certain angle.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degrees` | `float` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `PhiCertification`

#### reflect(plane)

Reflected the Phius Certification Object across a plane.

| Arg | Type | Description |
|-----|------|-------------|
| `plane` | `Plane` | — |

**Returns**: `PhiCertification`

#### scale(scale_factor, origin_pt3D)

Scale the Phius Certification Object by a factor from an origin point.

| Arg | Type | Description |
|-----|------|-------------|
| `scale_factor` | `float` | — |
| `origin_pt3D` | `Point3D | None` | — |

**Returns**: `PhiCertification`

---
