# bldg_segment

Building 'Segment' Level Data Attributes

**Source**: `honeybee_ph/bldg_segment.py`

---

## PhVentilationSummerBypassMode

No description available.

**Inherits from**: `enumerables.CustomEnum`

### Values

| Value | Meaning |
|-------|---------|
| `"1-None"` | — |
| `"2-Temperature Controlled"` | — |
| `"3-Enthalpy Controlled"` | — |
| `"4-Always"` | — |

---

## PhWindExposureType

No description available.

**Inherits from**: `enumerables.CustomEnum`

### Values

| Value | Meaning |
|-------|---------|
| `"1-SEVERAL_SIDES_EXPOSED_NO_SCREENING"` | — |
| `"2-SEVERAL_SIDES_EXPOSED_MODERATE_SCREENING"` | — |
| `"3-SEVERAL_SIDES_EXPOSED_HIGH_SCREENING"` | — |
| `"4-ONE_SIDE_EXPOSED_NO_SCREENING"` | — |
| `"5-ONE_SIDE_EXPOSED_MODERATE_SCREENING"` | — |
| `"6-USER_DEFINED"` | — |
| `"7-ONE_SIDE_EXPOSED_HIGH_SCREENING"` | — |

---

## PhSummerVentilationExtractSystemControl

No description available.

**Inherits from**: `enumerables.CustomEnum`

### Values

| Value | Meaning |
|-------|---------|
| `"1-TEMPERATURE_CONTROLLED"` | — |
| `"2-HUMIDITY_CONTROLLED"` | — |

---

## SummerVentilation

No description available.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `ventilation_system_ach` | — | — |
| `summer_bypass_mode` | `PhVentilationSummerBypassMode` | — |
| `daytime_extract_system_ach` | — | — |
| `daytime_extract_system_fan_power_wh_m3` | — | — |
| `daytime_window_ach` | — | — |
| `nighttime_extract_system_ach` | — | — |
| `nighttime_extract_system_fan_power_wh_m3` | — | — |
| `nighttime_extract_system_heat_fraction` | — | — |
| `nighttime_extract_system_control` | `PhSummerVentilationExtractSystemControl` | — |
| `nighttime_window_ach` | — | — |
| `nighttime_minimum_indoor_temp_C` | — | — |

---

## SetPoints

No description available.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `winter` | `float` | — |
| `summer` | `float` | — |

---

## BldgSegment

No description available.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `num_floor_levels` | `int` | — |
| `num_dwelling_units` | `int` | — |
| `site` | `Site` | — |
| `source_energy_factors` | `FactorCollection` | — |
| `co2e_factors` | `FactorCollection` | — |
| `phius_certification` | `PhiusCertification` | — |
| `phi_certification` | `PhiCertification` | — |
| `set_points` | `SetPoints` | — |
| `mech_room_temp` | `float` | — |
| `non_combustible_materials` | `bool` | — |
| `thermal_bridges` | `Dict[str, PhThermalBridge]` | — |
| `wind_exposure_type` | `PhWindExposureType` | — |
| `summer_ventilation` | `SummerVentilation` | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `summer_hrv_bypass_mode` | — | — |

### Methods

#### add_new_thermal_bridge(tb)

| Arg | Type | Description |
|-----|------|-------------|
| `tb` | `PhThermalBridge` | — |

**Returns**: `None`

#### move(moving_vec3D)

Move the BldgSegment along a vector.

| Arg | Type | Description |
|-----|------|-------------|
| `moving_vec3D` | `Vector3D` | — |

**Returns**: `BldgSegment`

#### rotate(axis_vec3D, angle_degrees, origin_pt3D)

Rotate the BldgSegment by a certain angle around an axis_vec3D and origin_pt3D.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_vec3D` | `Vector3D` | — |
| `angle_degrees` | `float` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `BldgSegment`

#### rotate_xy(angle_degrees, origin_pt3D)

Rotate the BldgSegment counterclockwise in the XY plane by a certain angle.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degrees` | `float` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `BldgSegment`

#### reflect(plane)

Reflected the BldgSegment across a plane with the input normal vector and origin_pt3D.

| Arg | Type | Description |
|-----|------|-------------|
| `plane` | `Plane` | — |

**Returns**: `BldgSegment`

#### scale(scale_factor, origin_pt3D)

Scale the BldgSegment a factor from an origin_pt3D point.

| Arg | Type | Description |
|-----|------|-------------|
| `scale_factor` | `float` | — |
| `origin_pt3D` | `Point3D | None` | — |

**Returns**: `BldgSegment`

---
