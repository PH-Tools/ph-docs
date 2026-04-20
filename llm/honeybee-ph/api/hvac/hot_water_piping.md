# hot_water_piping

Honeybee-PH-HVAC: Hot Water Piping.

**Source**: `honeybee_phhvac/hot_water_piping.py`

---

## PhHvacPipeMaterial

No description available.

**Inherits from**: `enumerables.CustomEnum`

### Values

| Value | Meaning |
|-------|---------|
| `"1-COPPER_M"` | — |
| `"2-COPPER_L"` | — |
| `"3-COPPER_K"` | — |
| `"4-CPVC_CTS_SDR"` | — |
| `"5-CPVC_SCH_40"` | — |
| `"6-PEX"` | — |
| `"7-PE"` | — |
| `"8-PEX_CTS_SDR"` | — |

---

## PhHvacPipeSegment

A single pipe segment (linear) with geometry and a diameter

**Inherits from**: `_base._PhHVACBase`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `geometry` | — | — |
| `diameter_mm` | — | — |
| `insulation_thickness_mm` | — | — |
| `insulation_conductivity` | — | — |
| `insulation_reflective` | — | — |
| `insulation_quality` | — | — |
| `daily_period` | — | — |
| `water_temp_c` | — | — |
| `material` | `PhHvacPipeMaterial` | — |

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
| `moving_vec3D` | `Vector3D` | — |

**Returns**: `PhHvacPipeSegment`

#### rotate(axis_3D, angle_degrees, origin_pt3D)

Rotate the pipe's geometry by a certain angle_degrees around an axis_3D and origin_pt3D.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_3D` | `Vector3D` | — |
| `angle_degrees` | `float` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `PhHvacPipeSegment`

#### rotate_xy(angle_degrees, origin_pt3D)

Rotate the pipe's geometry counterclockwise in the XY plane by a certain angle_degrees.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degrees` | `float` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `PhHvacPipeSegment`

#### reflect(normal_vec3D, origin_pt3D)

Reflected the pipe's geometry across a plane with the input normal vector and origin_pt3D.

| Arg | Type | Description |
|-----|------|-------------|
| `normal_vec3D` | `Vector3D` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `PhHvacPipeSegment`

#### scale(scale_factor, origin_pt3D)

Scale the pipe's geometry by a factor from an origin_pt3D point.

| Arg | Type | Description |
|-----|------|-------------|
| `scale_factor` | `float` | — |
| `origin_pt3D` | `Union[None` | — |

**Returns**: `PhHvacPipeSegment`

---

## PhHvacPipeElement

A Pipe Element (Fixture) made up of one or more individual Pipe Segments.

**Inherits from**: `_base._PhHVACBase`

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `segments` | `List[PhHvacPipeSegment]` | Return a list of a;; the Pipe-Segments in the Pipe-Element. |
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
| `_segment` | `PhHvacPipeSegment` | — |

**Returns**: `None`

#### clear_segments()

Clear all the segments from the pipe element.

**Returns**: `None`

#### move(moving_vec3D)

Move the pipe's segments along a vector.

| Arg | Type | Description |
|-----|------|-------------|
| `moving_vec3D` | `Vector3D` | — |

**Returns**: `PhHvacPipeElement`

#### rotate(axis_3D, angle_degrees, origin_pt3D)

Rotate the pipe's segments by a certain angle_degrees around an axis_3D and origin_pt3D.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_3D` | `Vector3D` | — |
| `angle_degrees` | `float` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `PhHvacPipeElement`

#### rotate_xy(angle_degrees, origin_pt3D)

Rotate the pipe's segments counterclockwise in the XY plane by a certain angle_degrees.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degrees` | `float` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `PhHvacPipeElement`

#### reflect(normal_vec3D, origin_pt3D)

Reflected the pipe's segments across a plane with the input normal_vec3D vector and origin_pt3D.

| Arg | Type | Description |
|-----|------|-------------|
| `normal_vec3D` | `Vector3D` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `PhHvacPipeElement`

#### scale(factor, origin_pt3D)

Scale the pipe's segments by a factor from an origin_pt3D point.

| Arg | Type | Description |
|-----|------|-------------|
| `factor` | `float` | — |
| `origin_pt3D` | `Optional[Point3D]` | — |

**Returns**: `PhHvacPipeElement`

---

## PhHvacPipeBranch

A 'Branch' Pipe which has geometry, and serves one or more 'Fixture' (Twig) pipe elements.

**Inherits from**: `_base._PhHVACBase`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `pipe_element` | `PhHvacPipeElement` | — |
| `fixtures` | `(List[PhHvacPipeElement])` | — |

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

Add a new HBPH Fixture (twig) PhPipeBranch to the Trunk.

| Arg | Type | Description |
|-----|------|-------------|
| `_fixture` | `PhHvacPipeElement` | — |

**Returns**: `None`

#### move(moving_vec3D)

Move the pipe's elements along a vector.

| Arg | Type | Description |
|-----|------|-------------|
| `moving_vec3D` | `Vector3D` | — |

**Returns**: `PhHvacPipeBranch`

#### rotate(axis_3D, angle_degrees, origin_pt3D)

Rotate the pipe's elements by a certain angle_degrees around an axis_3D and origin_pt3D.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_3D` | `Vector3D` | — |
| `angle_degrees` | `float` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `PhHvacPipeBranch`

#### rotate_xy(angle_degrees, origin_pt3D)

Rotate the pipe's elements counterclockwise in the XY plane by a certain angle_degrees.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degrees` | `float` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `PhHvacPipeBranch`

#### reflect(normal_vec3D, origin_pt3D)

Reflected the pipe's elements across a plane with the input normal_vec3D vector and origin_pt3D.

| Arg | Type | Description |
|-----|------|-------------|
| `normal_vec3D` | `Vector3D` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `PhHvacPipeBranch`

#### scale(factor, origin_pt3D)

Scale the pipe's elements by a factor from an origin_pt3D point.

| Arg | Type | Description |
|-----|------|-------------|
| `factor` | `float` | — |
| `origin_pt3D` | `Optional[Point3D]` | — |

**Returns**: `PhHvacPipeBranch`

---

## PhHvacPipeTrunk

A 'Trunk' Pipe which has geometry, and serves one or more 'Branches'.

**Inherits from**: `_base._PhHVACBase`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `pipe_element` | `PhHvacPipeElement` | — |
| `multiplier` | `int` | — |
| `branches` | `(List[PhHvacPipeBranch])` | — |
| `demand_recirculation` | `bool` | — |

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

Add a new HBPH PhPipeBranch to the Trunk.

| Arg | Type | Description |
|-----|------|-------------|
| `_branch` | `PhHvacPipeBranch` | — |

**Returns**: `None`

#### move(moving_vec3D)

Move the pipe's elements along a vector.

| Arg | Type | Description |
|-----|------|-------------|
| `moving_vec3D` | `Vector3D` | — |

**Returns**: `PhHvacPipeTrunk`

#### rotate(axis_3D, angle_degrees, origin_pt3D)

Rotate the pipe's elements by a certain angle_degrees around an axis_3D and origin_pt3D.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_3D` | `Vector3D` | — |
| `angle_degrees` | `float` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `PhHvacPipeTrunk`

#### rotate_xy(angle_degrees, origin_pt3D)

Rotate the pipe's elements counterclockwise in the XY plane by a certain angle_degrees.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degrees` | `float` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `PhHvacPipeTrunk`

#### reflect(normal_vec3D, origin_pt3D)

Reflected the pipe's elements across a plane with the input normal_vec3D vector and origin_pt3D.

| Arg | Type | Description |
|-----|------|-------------|
| `normal_vec3D` | — | — |
| `origin_pt3D` | — | — |

#### scale(factor, origin_pt3D)

Scale the pipe's elements by a factor from an origin_pt3D point.

| Arg | Type | Description |
|-----|------|-------------|
| `factor` | `float` | — |
| `origin_pt3D` | `Optional[Point3D]` | — |

**Returns**: `PhHvacPipeTrunk`

---
