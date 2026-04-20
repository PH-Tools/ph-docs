# hot_water_system

Honeybee-PH-HVAC: Hot Water System.

**Source**: `honeybee_phhvac/hot_water_system.py`

---

## PhHotWaterSystem_FromDictError

No description available.

**Inherits from**: `Exception`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `msg` | `format` | — |

---

## PhHotWaterSystem

A Passive House hot water system with tanks, heaters, distribution and recirculation piping.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `identifier` | `str` | Unique identifier for the system. |
| `id_num` | `int` | Numeric identifier for the system. |
| `display_name` | `str` | User-facing display name for the system. |
| `tank_1` | `Optional[hwd.PhHvacHotWaterTank]` | Primary hot water tank. |
| `tank_2` | `Optional[hwd.PhHvacHotWaterTank]` | Secondary hot water tank. |
| `tank_buffer` | `Optional[hwd.PhHvacHotWaterTank]` | Buffer tank. |
| `tank_solar` | `Optional[hwd.PhHvacHotWaterTank]` | Solar tank. |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `total_distribution_pipe_length` | `float` | Returns the total length of all trunk, branch, and fixture piping. |
| `total_home_run_fixture_pipe_length` | `float` | Returns the total length of all fixture piping from end to end. |
| `total_recirc_pipe_length` | `float` | Returns the total length of all recirculation piping. |
| `recirc_temp` | `float` | Return the length weighted average of recirculation piping temperatures |
| `recirc_hours` | `int` | Return the length-weighted average of recirculation piping hours. |
| `number_tap_points` | `int` | Unless set explicitly by the user, will return the number of Branch Pipe Elements. |
| `heaters` | `ValuesView[hwd.PhHvacHotWaterHeater]` | Returns a list of all the heaters on the system. |
| `distribution_piping` | `ValuesView[hwp.PhHvacPipeTrunk]` | Returns a list of all the distribution-piping (Trunks) in the system. |
| `recirc_piping` | `ValuesView[hwp.PhHvacPipeElement]` | Returns a list of all the recirculation-piping objects in the system. |
| `tanks` | `list[hwd.PhHvacHotWaterTank | None]` | Return a list of the system tanks in order (1, 2, buffer, solar). |

### Methods

#### clear_heaters()

Remove all heaters from the system.

#### add_heater(_heater)

Add a new hot-water heater to the system.

| Arg | Type | Description |
|-----|------|-------------|
| `_heater` | `Optional[hwd.PhHvacHotWaterHeater]` | The heater to add. If None, no action is taken. |

**Returns**: `None`

#### add_distribution_piping(_distribution_piping, _key)

Add a new distribution (branch, trunk, fixture) to the system.

| Arg | Type | Description |
|-----|------|-------------|
| `_distribution_piping` | `Union[hwp.PhHvacPipeTrunk` | The piping to add. |
| `_key` | `hwp.PhHvacPipeBranch` | An optional key to use for storing the trunk. |

**Returns**: `None`

#### clear_distribution_piping()

Clear all distribution piping (Trunks) from the system.

#### add_recirc_piping(_recirc_piping, _key)

Add a new recirculation pipe element to the system.

| Arg | Type | Description |
|-----|------|-------------|
| `_recirc_piping` | `hwp.PhHvacPipeElement` | The recirculation pipe element to add. |
| `_key` | `Optional[str]` | An optional key to use for storing the pipe element. |

**Returns**: `None`

#### clear_recirc_piping()

Remove all recirculation piping from the system.

#### apply_properties_from_dict(abridged_data)

| Arg | Type | Description |
|-----|------|-------------|
| `abridged_data` | — | — |

#### move(moving_vec3D)

Move the System's piping along a vector.

| Arg | Type | Description |
|-----|------|-------------|
| `moving_vec3D` | `Point3D` | A vector with the direction and distance to move. |

**Returns**: `PhHotWaterSystem`

#### rotate(axis_vec3D, angle_degrees, origin_pt3D)

Rotate the System's piping by a certain angle around an axis and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_vec3D` | `Point3D` | A vector representing the axis of rotation. |
| `angle_degrees` | `float` | An angle for rotation in degrees. |
| `origin_pt3D` | `Point3D` | The origin around which the object will be rotated. |

**Returns**: `PhHotWaterSystem`

#### rotate_xy(angle_degrees, origin_pt3D)

Rotate the System's piping counterclockwise in the XY plane by a certain angle.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degrees` | `float` | An angle in degrees. |
| `origin_pt3D` | `Point3D` | The origin around which the object will be rotated. |

**Returns**: `PhHotWaterSystem`

#### reflect(normal_vec3D, origin_pt3D)

Reflect the System's piping across a plane with the input normal vector and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `normal_vec3D` | `Vector3D` | The normal vector for the reflection plane. THIS VECTOR MUST BE NORMALIZED. |
| `origin_pt3D` | `Point3D` | The origin from which to reflect. |

**Returns**: `PhHotWaterSystem`

#### scale(scale_factor, origin_pt3D)

Scale the System's piping by a factor from an origin point.

| Arg | Type | Description |
|-----|------|-------------|
| `scale_factor` | `float` | How much the piping should be scaled. |
| `origin_pt3D` | `Optional[Point3D]` | The origin from which to scale. If None, it will be scaled from the World origin (0, 0, 0). |

**Returns**: `PhHotWaterSystem`

---
