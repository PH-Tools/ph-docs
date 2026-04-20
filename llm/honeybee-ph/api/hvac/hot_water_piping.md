# hot_water_piping

Honeybee-PH-HVAC: Hot Water Piping.

**Source**: `honeybee_phhvac/hot_water_piping.py`

---

## PhHvacPipeMaterial

Enumeration of allowable pipe material types.

**Inherits from**: `enumerables.CustomEnum`

### Values

| Value | Meaning |
|-------|---------|
| `"1-COPPER_M"` | Copper type M. |
| `"2-COPPER_L"` | Copper type L (default). |
| `"3-COPPER_K"` | Copper type K. |
| `"4-CPVC_CTS_SDR"` | CPVC CTS SDR. |
| `"5-CPVC_SCH_40"` | CPVC Schedule 40. |
| `"6-PEX"` | PEX tubing. |
| `"7-PE"` | Polyethylene tubing. |
| `"8-PEX_CTS_SDR"` | PEX CTS SDR. |

---

## PhHvacPipeSegment

A single pipe segment (linear) with geometry and a diameter.

**Inherits from**: `_base._PhHVACBase`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `geometry` | — | The 3D line segment geometry of the pipe. |
| `diameter_mm` | — | The pipe diameter in millimeters. |
| `insulation_thickness_mm` | — | The insulation thickness in millimeters. |
| `insulation_conductivity` | — | The insulation thermal conductivity (W/m-K). |
| `insulation_reflective` | — | True if the insulation has a reflective surface. |
| `insulation_quality` | — | Reserved for future use. |
| `daily_period` | — | Hours per day the pipe is in use. |
| `water_temp_c` | — | The water temperature in degrees Celsius. |
| `material` | `PhHvacPipeMaterial` | The pipe material type. |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `length` | `float` | Return the length of the pipe segment in model-units. |
| `diameter_m` | `float` | Return the diameter of the pipe segment in meters. |
| `insulation_thickness_m` | `float` | Return the insulation thickness of the pipe segment in meters. |

### Methods

#### move(moving_vec3D)

Move the pipe's geometry along a vector.

| Arg | Type | Description |
|-----|------|-------------|
| `moving_vec3D` | `Vector3D` | A vector with the direction and distance to move. |

**Returns**: `PhHvacPipeSegment`

#### rotate(axis_3D, angle_degrees, origin_pt3D)

Rotate the pipe's geometry by a certain angle around an axis and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_3D` | `Vector3D` | A vector representing the axis of rotation. |
| `angle_degrees` | `float` | An angle for rotation in degrees. |
| `origin_pt3D` | `Point3D` | The origin around which the object will be rotated. |

**Returns**: `PhHvacPipeSegment`

#### rotate_xy(angle_degrees, origin_pt3D)

Rotate the pipe's geometry counterclockwise in the XY plane by a certain angle.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degrees` | `float` | An angle in degrees. |
| `origin_pt3D` | `Point3D` | The origin around which the object will be rotated. |

**Returns**: `PhHvacPipeSegment`

#### reflect(normal_vec3D, origin_pt3D)

Reflect the pipe's geometry across a plane with the input normal vector and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `normal_vec3D` | `Vector3D` | The normal vector for the reflection plane. THIS VECTOR MUST BE NORMALIZED. |
| `origin_pt3D` | `Point3D` | The origin from which to reflect. |

**Returns**: `PhHvacPipeSegment`

#### scale(scale_factor, origin_pt3D)

Scale the pipe's geometry by a factor from an origin point.

| Arg | Type | Description |
|-----|------|-------------|
| `scale_factor` | `float` | How much the line segment should be scaled. |
| `origin_pt3D` | `Union[None` | The origin from which to scale. If None, it will be scaled from the World origin (0, 0, 0). |

**Returns**: `PhHvacPipeSegment`

---

## PhHvacPipeElement

A Pipe Element (Fixture) made up of one or more individual Pipe Segments.

**Inherits from**: `_base._PhHVACBase`

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `segments` | `List[PhHvacPipeSegment]` | Return a list of all the Pipe-Segments in the Pipe-Element. |
| `length` | `float` | Return the total length of the pipe element in model-units. |
| `diameter_mm` | `float` | Return the length-weighted average diameter of all the pipe segments |
| `water_temp_c` | `float` | Return the length-weighted average water temperature of all the pipe segments |
| `daily_period` | `float` | Return the length-weighted average daily period of all the pipe segments |
| `segment_names` | `List[str]` | Return a list of the names of all the PipeSegments in the PipeElement. |
| `material_name` | `str` | Return the material name of the pipe element. |

### Methods

#### add_segment(_segment)

Add a new Pipe Segment to the Pipe Element.

| Arg | Type | Description |
|-----|------|-------------|
| `_segment` | `PhHvacPipeSegment` | The pipe segment to add. |

**Returns**: `None`

#### clear_segments()

Clear all the segments from the pipe element.

**Returns**: `None`

#### move(moving_vec3D)

Move the pipe's segments along a vector.

| Arg | Type | Description |
|-----|------|-------------|
| `moving_vec3D` | `Vector3D` | A vector with the direction and distance to move. |

**Returns**: `PhHvacPipeElement`

#### rotate(axis_3D, angle_degrees, origin_pt3D)

Rotate the pipe's segments by a certain angle around an axis and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_3D` | `Vector3D` | A vector representing the axis of rotation. |
| `angle_degrees` | `float` | An angle for rotation in degrees. |
| `origin_pt3D` | `Point3D` | The origin around which the object will be rotated. |

**Returns**: `PhHvacPipeElement`

#### rotate_xy(angle_degrees, origin_pt3D)

Rotate the pipe's segments counterclockwise in the XY plane by a certain angle.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degrees` | `float` | An angle in degrees. |
| `origin_pt3D` | `Point3D` | The origin around which the object will be rotated. |

**Returns**: `PhHvacPipeElement`

#### reflect(normal_vec3D, origin_pt3D)

Reflect the pipe's segments across a plane with the input normal vector and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `normal_vec3D` | `Vector3D` | The normal vector for the reflection plane. THIS VECTOR MUST BE NORMALIZED. |
| `origin_pt3D` | `Point3D` | The origin from which to reflect. |

**Returns**: `PhHvacPipeElement`

#### scale(factor, origin_pt3D)

Scale the pipe's segments by a factor from an origin point.

| Arg | Type | Description |
|-----|------|-------------|
| `factor` | `float` | How much the segments should be scaled. |
| `origin_pt3D` | `Optional[Point3D]` | The origin from which to scale. If None, it will be scaled from the World origin (0, 0, 0). |

**Returns**: `PhHvacPipeElement`

---

## PhHvacPipeBranch

A 'Branch' Pipe which has geometry, and serves one or more 'Fixture' (Twig) pipe elements.

**Inherits from**: `_base._PhHVACBase`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `pipe_element` | `PhHvacPipeElement` | The pipe element representing the branch geometry. |
| `fixtures` | `(List[PhHvacPipeElement])` | The fixture (twig) pipe elements connected to this branch. |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `material_name` | `str` | Return the material name of the pipe element. |
| `diameter_mm` | `float` | Return the length-weighted diameter (MM) of the pipe element. |
| `twigs` | — | Alias for the 'fixtures' to better match Phius terminology. |
| `segments` | — | Return a list of all the Pipe-Segments in the Branch. |
| `length` | `float` | Return the total length of the branch itself in model-units. |
| `water_temp_c` | `float` | Return the length-weighted average water temperature of all the pipe segments. |
| `daily_period` | `float` | Return the length-weighted average daily period of all the pipe segments. |
| `num_fixtures` | `int` | Return the number of fixtures connected to the branch. |
| `total_length` | `float` | Return the total length of the branch PLUS all fixture pipes in model-units. |
| `total_home_run_fixture_length` | `float` | Return the total length (in model-units) of all fixture pipes as measured from end to end. |

### Methods

#### add_fixture(_fixture)

Add a new fixture (twig) pipe element to the branch.

| Arg | Type | Description |
|-----|------|-------------|
| `_fixture` | `PhHvacPipeElement` | The fixture pipe element to add. |

**Returns**: `None`

#### move(moving_vec3D)

Move the pipe's elements along a vector.

| Arg | Type | Description |
|-----|------|-------------|
| `moving_vec3D` | `Vector3D` | A vector with the direction and distance to move. |

**Returns**: `PhHvacPipeBranch`

#### rotate(axis_3D, angle_degrees, origin_pt3D)

Rotate the pipe's elements by a certain angle around an axis and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_3D` | `Vector3D` | A vector representing the axis of rotation. |
| `angle_degrees` | `float` | An angle for rotation in degrees. |
| `origin_pt3D` | `Point3D` | The origin around which the object will be rotated. |

**Returns**: `PhHvacPipeBranch`

#### rotate_xy(angle_degrees, origin_pt3D)

Rotate the pipe's elements counterclockwise in the XY plane by a certain angle.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degrees` | `float` | An angle in degrees. |
| `origin_pt3D` | `Point3D` | The origin around which the object will be rotated. |

**Returns**: `PhHvacPipeBranch`

#### reflect(normal_vec3D, origin_pt3D)

Reflect the pipe's elements across a plane with the input normal vector and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `normal_vec3D` | `Vector3D` | The normal vector for the reflection plane. THIS VECTOR MUST BE NORMALIZED. |
| `origin_pt3D` | `Point3D` | The origin from which to reflect. |

**Returns**: `PhHvacPipeBranch`

#### scale(factor, origin_pt3D)

Scale the pipe's elements by a factor from an origin point.

| Arg | Type | Description |
|-----|------|-------------|
| `factor` | `float` | How much the elements should be scaled. |
| `origin_pt3D` | `Optional[Point3D]` | The origin from which to scale. If None, it will be scaled from the World origin (0, 0, 0). |

**Returns**: `PhHvacPipeBranch`

---

## PhHvacPipeTrunk

A 'Trunk' Pipe which has geometry, and serves one or more 'Branches'.

**Inherits from**: `_base._PhHVACBase`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `pipe_element` | `PhHvacPipeElement` | The pipe element representing the trunk geometry. |
| `multiplier` | `int` | A multiplier applied to the trunk for identical risers. |
| `branches` | `(List[PhHvacPipeBranch])` | The branch pipes connected to this trunk. |
| `demand_recirculation` | `bool` | True if the trunk uses demand recirculation. |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `material_name` | `str` | Return the material name of the pipe element. |
| `diameter_mm` | `float` | Return the length-weighted diameter (MM) name of the pipe element. |
| `segments` | — | Return a list of all the Pipe-Segments in the Trunk. |
| `length` | `float` | Return the total length of the trunk itself in model-units. |
| `water_temp_c` | `float` | Return the length-weighted average water temperature (deg-C) of all the pipe segments. |
| `daily_period` | `float` | Return the length-weighted average daily period of all the pipe segments. |
| `num_fixtures` | `int` | Return the number of fixtures connected to the trunk. |
| `total_length` | `float` | Return the total length (in model-units) of the trunk PLUS all branches and fixture pipes in model-units. |
| `total_home_run_fixture_length` | `float` | Return the total length (in model-units) of all fixture pipes as measured from end to end. |

### Methods

#### add_branch(_branch)

Add a new branch pipe to the trunk.

| Arg | Type | Description |
|-----|------|-------------|
| `_branch` | `PhHvacPipeBranch` | The branch pipe to add. |

**Returns**: `None`

#### move(moving_vec3D)

Move the pipe's elements along a vector.

| Arg | Type | Description |
|-----|------|-------------|
| `moving_vec3D` | `Vector3D` | A vector with the direction and distance to move. |

**Returns**: `PhHvacPipeTrunk`

#### rotate(axis_3D, angle_degrees, origin_pt3D)

Rotate the pipe's elements by a certain angle around an axis and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_3D` | `Vector3D` | A vector representing the axis of rotation. |
| `angle_degrees` | `float` | An angle for rotation in degrees. |
| `origin_pt3D` | `Point3D` | The origin around which the object will be rotated. |

**Returns**: `PhHvacPipeTrunk`

#### rotate_xy(angle_degrees, origin_pt3D)

Rotate the pipe's elements counterclockwise in the XY plane by a certain angle.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degrees` | `float` | An angle in degrees. |
| `origin_pt3D` | `Point3D` | The origin around which the object will be rotated. |

**Returns**: `PhHvacPipeTrunk`

#### reflect(normal_vec3D, origin_pt3D)

Reflect the pipe's elements across a plane with the input normal vector and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `normal_vec3D` | — | The normal vector for the reflection plane. THIS VECTOR MUST BE NORMALIZED. |
| `origin_pt3D` | — | The origin from which to reflect. |

#### scale(factor, origin_pt3D)

Scale the pipe's elements by a factor from an origin point.

| Arg | Type | Description |
|-----|------|-------------|
| `factor` | `float` | How much the elements should be scaled. |
| `origin_pt3D` | `Optional[Point3D]` | The origin from which to scale. If None, it will be scaled from the World origin (0, 0, 0). |

**Returns**: `PhHvacPipeTrunk`

---
