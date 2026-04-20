# phius

Phius Certification Data Class

**Source**: `honeybee_ph/phius.py`

---

## PhiusBuildingCertificationProgram

Phius building certification program type enumeration.

**Inherits from**: `enumerables.CustomEnum`

### Values

| Value | Meaning |
|-------|---------|
| `"1-Default"` | Default (unspecified) certification program. |
| `"2-PHIUS 2015"` | — |
| `"3-PHIUS 2018"` | — |
| `"4-Italian"` | Italian certification standard. |
| `"5-PHIUS 2018 CORE"` | — |
| `"6-PHIUS 2018 ZERO"` | — |
| `"7-PHIUS 2021 CORE"` | — |
| `"8-PHIUS 2021 ZERO"` | — |

---

## PhiusBuildingCategoryType

Phius building category type enumeration.

**Inherits from**: `enumerables.CustomEnum`

### Values

| Value | Meaning |
|-------|---------|
| `"1-RESIDENTIAL BUILDING"` | — |
| `"2-NON-RESIDENTIAL BUILDING"` | — |

---

## PhiusBuildingUseType

Phius building use type enumeration.

**Inherits from**: `enumerables.CustomEnum`

### Values

| Value | Meaning |
|-------|---------|
| `"1-RESIDENTIAL"` | Residential use. |
| `""` | — |
| `""` | — |
| `"4-OFFICE/ADMINISTRATIVE BUILDING"` | — |
| `"5-SCHOOL"` | School use. |
| `"6-OTHER"` | Other use type. |
| `"7-UNDEFINED/UNFINISHED"` | Undefined or unfinished use type. |

---

## PhiusBuildingStatus

Phius building status enumeration.

**Inherits from**: `enumerables.CustomEnum`

### Values

| Value | Meaning |
|-------|---------|
| `"1-IN_PLANNING"` | Building is in the planning phase. |
| `"2-UNDER_CONSTRUCTION"` | Building is under construction. |
| `"3-COMPLETE"` | Building is complete. |

---

## PhiusBuildingType

Phius building type enumeration.

**Inherits from**: `enumerables.CustomEnum`

### Values

| Value | Meaning |
|-------|---------|
| `"1-NEW_CONSTRUCTION"` | New construction project. |
| `"2-RETROFIT"` | Retrofit of an existing building. |
| `"3-MIXED"` | Mixed new construction and retrofit. |

---

## PhiusCertification

Phius certification configuration and performance targets for a building.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `localization_selection_type` | `int` | Localization selection type identifier. |
| `PHIUS2021_heating_demand` | `float` | PHIUS 2021 heating demand target (kBtu/ft2/yr). |
| `PHIUS2021_cooling_demand` | `float` | PHIUS 2021 cooling demand target (kBtu/ft2/yr). |
| `PHIUS2021_heating_load` | `float` | PHIUS 2021 heating load target (Btu/h/ft2). |
| `PHIUS2021_cooling_load` | `float` | PHIUS 2021 cooling load target (Btu/h/ft2). |
| `int_gains_evap_per_person` | `int` | Evaporative internal gains per person (W/person). |
| `int_gains_flush_heat_loss` | `bool` | Whether to account for flush heat loss. |
| `int_gains_num_toilets` | `int` | Number of toilets in the building. |
| `int_gains_toilet_room_util_pat` | `Optional[unknown]` | Toilet room utilization pattern name. |
| `int_gains_use_school_defaults` | `bool` | Whether to use school default internal gains. |
| `int_gains_dhw_marginal_perf_ratio` | `Optional[unknown]` | DHW marginal performance ratio. |
| `icfa_override` | `float | None` | Manual override for interior conditioned floor area. |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `certification_program` | `PhiusBuildingCertificationProgram` | The Phius certification program for this building. |
| `building_category_type` | `PhiusBuildingCategoryType` | The Phius building category type (residential or non-residential). |
| `building_use_type` | `PhiusBuildingUseType` | The Phius building use type (residential, school, office, etc.). |
| `building_status` | `PhiusBuildingStatus` | The Phius building status (planning, construction, or complete). |
| `building_type` | `PhiusBuildingType` | The Phius building type (new construction, retrofit, or mixed). |

### Methods

#### move(moving_vec3D)

Move the Phius Certification Object along a vector.

| Arg | Type | Description |
|-----|------|-------------|
| `moving_vec3D` | `Vector3D` | A Vector3D with the direction and distance to move the ray. |

**Returns**: `PhiusCertification`

#### rotate(axis_vec3D, angle_degrees, origin_pt3D)

Rotate the Phius Certification Object by a certain angle around an axis and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_vec3D` | `Vector3D` | A Vector3D axis representing the axis of rotation. |
| `angle_degrees` | `float` | An angle for rotation in degrees. |
| `origin_pt3D` | `Point3D` | A Point3D for the origin around which the object will be rotated. |

**Returns**: `PhiusCertification`

#### rotate_xy(angle_degrees, origin_pt3D)

Rotate the Phius Certification Object counterclockwise in the XY plane by a certain angle.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degrees` | `float` | An angle in degrees. |
| `origin_pt3D` | `Point3D` | A Point3D for the origin around which the object will be rotated. |

**Returns**: `PhiusCertification`

#### reflect(plane)

Reflect the Phius Certification Object across a plane.

| Arg | Type | Description |
|-----|------|-------------|
| `plane` | `Plane` | A Plane representing the plane across which to reflect. |

**Returns**: `PhiusCertification`

#### scale(scale_factor, origin_pt3D)

Scale the Phius Certification Object by a factor from an origin point.

| Arg | Type | Description |
|-----|------|-------------|
| `scale_factor` | `float` | A number representing how much the object should be scaled. |
| `origin_pt3D` | `Optional[Point3D]` | A Point3D representing the origin from which to scale. If None, it will be scaled from the World origin (0, 0, 0). |

**Returns**: `PhiusCertification`

---
