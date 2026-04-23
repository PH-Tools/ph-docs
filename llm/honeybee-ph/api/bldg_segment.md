# bldg_segment

Building 'Segment' Level Data Attributes

**Source**: `honeybee_ph/bldg_segment.py`

---

## PhVentilationSummerBypassMode

Summer bypass control mode for the ventilation system heat exchanger.

**Inherits from**: `enumerables.CustomEnum`

### Values

| Value | Meaning |
|-------|---------|
| `"1-None"` | No bypass. |
| `"2-Temperature Controlled"` | — |
| `"3-Enthalpy Controlled"` | — |
| `"4-Always"` | Bypass always active in summer. |

---

## PhWindExposureType

Wind exposure classification for infiltration calculations.

**Inherits from**: `enumerables.CustomEnum`

### Values

| Value | Meaning |
|-------|---------|
| `"1-SEVERAL_SIDES_EXPOSED_NO_SCREENING"` | Multiple exposed sides, no screening. |
| `"2-SEVERAL_SIDES_EXPOSED_MODERATE_SCREENING"` | Multiple exposed sides, moderate screening. |
| `"3-SEVERAL_SIDES_EXPOSED_HIGH_SCREENING"` | Multiple exposed sides, high screening. |
| `"4-ONE_SIDE_EXPOSED_NO_SCREENING"` | One exposed side, no screening. |
| `"5-ONE_SIDE_EXPOSED_MODERATE_SCREENING"` | One exposed side, moderate screening. |
| `"6-USER_DEFINED"` | User-defined wind exposure coefficient. |
| `"7-ONE_SIDE_EXPOSED_HIGH_SCREENING"` | One exposed side, high screening. |

---

## PhSummerVentilationExtractSystemControl

Control mode for summer nighttime extract ventilation system.

**Inherits from**: `enumerables.CustomEnum`

### Values

| Value | Meaning |
|-------|---------|
| `"1-TEMPERATURE_CONTROLLED"` | Controlled by temperature setpoint. |
| `"2-HUMIDITY_CONTROLLED"` | Controlled by humidity setpoint. |

---

## SummerVentilation

Summer ventilation settings for a building segment.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `ventilation_system_ach` | — | Ventilation system air change rate. |
| `summer_bypass_mode` | `PhVentilationSummerBypassMode` | HRV bypass control mode. Default: "4-Always". |
| `daytime_extract_system_ach` | — | Daytime extract system ACH. |
| `daytime_extract_system_fan_power_wh_m3` | — | Daytime extract fan specific power in Wh/m3. |
| `daytime_window_ach` | — | Daytime window ventilation ACH. |
| `nighttime_extract_system_ach` | — | Nighttime extract system ACH. |
| `nighttime_extract_system_fan_power_wh_m3` | — | Nighttime extract fan specific power in Wh/m3. |
| `nighttime_extract_system_heat_fraction` | — | Nighttime extract heat recovery fraction. |
| `nighttime_extract_system_control` | `PhSummerVentilationExtractSystemControl` | Nighttime extract system control mode. Default: "1-TEMPERATURE_CONTROLLED". |
| `nighttime_window_ach` | — | Nighttime window ventilation ACH. |
| `nighttime_minimum_indoor_temp_C` | — | Minimum indoor temperature for nighttime ventilation in degrees Celsius. |

---

## SetPoints

Heating and cooling temperature setpoints for a building segment.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `winter` | `float` | Winter heating setpoint in degrees Celsius. Default: 20.0. |
| `summer` | `float` | Summer cooling setpoint in degrees Celsius. Default: 25.0. |

---

## BldgSegment

A building segment representing one thermally distinct zone for PH certification.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `num_floor_levels` | `int` | Number of above-grade floor levels. Default: 1. |
| `num_dwelling_units` | `int` | Number of dwelling units. Default: 1. |
| `site` | `Site` | Climate and location data for this segment. |
| `source_energy_factors` | `FactorCollection` | Source energy conversion factors. |
| `co2e_factors` | `FactorCollection` | CO2-equivalent emission factors. |
| `phius_certification` | `PhiusCertification` | Phius certification settings. |
| `phi_certification` | `PhiCertification` | PHI certification settings. |
| `set_points` | `SetPoints` | Heating/cooling temperature setpoints. |
| `mech_room_temp` | `float` | Mechanical room temperature in degrees Celsius. Default: 20.0. |
| `non_combustible_materials` | `bool` | True if non-combustible construction. Default: False. |
| `thermal_bridges` | `Dict[str, PhThermalBridge]` | Thermal bridges keyed by identifier. |
| `wind_exposure_type` | `PhWindExposureType` | Wind exposure classification. |
| `summer_ventilation` | `SummerVentilation` | Summer ventilation parameters. |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `summer_hrv_bypass_mode` | — | — |

### Methods

#### add_new_thermal_bridge(tb)

Add a thermal bridge to this building segment.

| Arg | Type | Description |
|-----|------|-------------|
| `tb` | `PhThermalBridge` | The thermal bridge to add. |

**Returns**: `None`

#### move(moving_vec3D)

Move the BldgSegment along a vector.

| Arg | Type | Description |
|-----|------|-------------|
| `moving_vec3D` | `Vector3D` | The direction and distance to move. |

**Returns**: `BldgSegment`

#### rotate(axis_vec3D, angle_degrees, origin_pt3D)

Rotate the BldgSegment by a certain angle around an axis and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_vec3D` | `Vector3D` | The axis of rotation. |
| `angle_degrees` | `float` | The rotation angle in degrees. |
| `origin_pt3D` | `Point3D` | The origin around which to rotate. |

**Returns**: `BldgSegment`

#### rotate_xy(angle_degrees, origin_pt3D)

Rotate the BldgSegment counterclockwise in the XY plane by a certain angle.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degrees` | `float` | The rotation angle in degrees. |
| `origin_pt3D` | `Point3D` | The origin around which to rotate. |

**Returns**: `BldgSegment`

#### reflect(plane)

Reflect the BldgSegment across a plane.

| Arg | Type | Description |
|-----|------|-------------|
| `plane` | `Plane` | The plane across which to reflect. |

**Returns**: `BldgSegment`

#### scale(scale_factor, origin_pt3D)

Scale the BldgSegment by a factor from an origin point.

| Arg | Type | Description |
|-----|------|-------------|
| `scale_factor` | `float` | The scaling factor. |
| `origin_pt3D` | `Point3D | None` | The origin from which to scale. If None, scales from the World origin (0, 0, 0). |

**Returns**: `BldgSegment`

---
