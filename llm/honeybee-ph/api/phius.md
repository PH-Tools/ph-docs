# phius

Phius Certification Data Class

**Source**: `honeybee_ph/phius.py`

---

## PhiusBuildingCertificationProgram

No description available.

**Inherits from**: `enumerables.CustomEnum`

### Values

| Value | Meaning |
|-------|---------|
| `"1-Default"` | — |
| `"2-PHIUS 2015"` | — |
| `"3-PHIUS 2018"` | — |
| `"4-Italian"` | — |
| `"5-PHIUS 2018 CORE"` | — |
| `"6-PHIUS 2018 ZERO"` | — |
| `"7-PHIUS 2021 CORE"` | — |
| `"8-PHIUS 2021 ZERO"` | — |

---

## PhiusBuildingCategoryType

No description available.

**Inherits from**: `enumerables.CustomEnum`

### Values

| Value | Meaning |
|-------|---------|
| `"1-RESIDENTIAL BUILDING"` | — |
| `"2-NON-RESIDENTIAL BUILDING"` | — |

---

## PhiusBuildingUseType

No description available.

**Inherits from**: `enumerables.CustomEnum`

### Values

| Value | Meaning |
|-------|---------|
| `"1-RESIDENTIAL"` | — |
| `""` | — |
| `""` | — |
| `"4-OFFICE/ADMINISTRATIVE BUILDING"` | — |
| `"5-SCHOOL"` | — |
| `"6-OTHER"` | — |
| `"7-UNDEFINED/UNFINISHED"` | — |

---

## PhiusBuildingStatus

No description available.

**Inherits from**: `enumerables.CustomEnum`

### Values

| Value | Meaning |
|-------|---------|
| `"1-IN_PLANNING"` | — |
| `"2-UNDER_CONSTRUCTION"` | — |
| `"3-COMPLETE"` | — |

---

## PhiusBuildingType

No description available.

**Inherits from**: `enumerables.CustomEnum`

### Values

| Value | Meaning |
|-------|---------|
| `"1-NEW_CONSTRUCTION"` | — |
| `"2-RETROFIT"` | — |
| `"3-MIXED"` | — |

---

## PhiusCertification

No description available.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `localization_selection_type` | `int` | — |
| `PHIUS2021_heating_demand` | `float` | — |
| `PHIUS2021_cooling_demand` | `float` | — |
| `PHIUS2021_heating_load` | `float` | — |
| `PHIUS2021_cooling_load` | `float` | — |
| `int_gains_evap_per_person` | `int` | — |
| `int_gains_flush_heat_loss` | `bool` | — |
| `int_gains_num_toilets` | `int` | — |
| `int_gains_toilet_room_util_pat` | `Optional[unknown]` | — |
| `int_gains_use_school_defaults` | `bool` | — |
| `int_gains_dhw_marginal_perf_ratio` | `Optional[unknown]` | — |
| `icfa_override` | `float | None` | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `certification_program` | `PhiusBuildingCertificationProgram` | — |
| `building_category_type` | `PhiusBuildingCategoryType` | — |
| `building_use_type` | `PhiusBuildingUseType` | — |
| `building_status` | `PhiusBuildingStatus` | — |
| `building_type` | `PhiusBuildingType` | — |

### Methods

#### move(moving_vec3D)

Move the Phius Certification Object along a vector.

| Arg | Type | Description |
|-----|------|-------------|
| `moving_vec3D` | `Vector3D` | — |

**Returns**: `PhiusCertification`

#### rotate(axis_vec3D, angle_degrees, origin_pt3D)

Rotate the Phius Certification Object by a certain angle around an axis and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_vec3D` | `Vector3D` | — |
| `angle_degrees` | `float` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `PhiusCertification`

#### rotate_xy(angle_degrees, origin_pt3D)

Rotate the Phius Certification Object counterclockwise in the XY plane by a certain angle.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degrees` | `float` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `PhiusCertification`

#### reflect(plane)

Reflected the Phius Certification Object across a plane.

| Arg | Type | Description |
|-----|------|-------------|
| `plane` | `Plane` | — |

**Returns**: `PhiusCertification`

#### scale(scale_factor, origin_pt3D)

Scale the Phius Certification Object by a factor from an origin point.

| Arg | Type | Description |
|-----|------|-------------|
| `scale_factor` | `float` | — |
| `origin_pt3D` | `Point3D | None` | — |

**Returns**: `PhiusCertification`

---
