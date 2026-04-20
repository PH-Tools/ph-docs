# ducting

Honeybee-PH-HVAC-Equipment: Ducts.

**Source**: `honeybee_phhvac/ducting.py`

---

## PhDuctSegment

A single duct segment (linear) with geometry and a attributes.

**Inherits from**: `_base._PhHVACBase`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `geometry` | — | — |
| `insulation_thickness` | — | — |
| `insulation_conductivity` | — | — |
| `insulation_reflective` | — | — |
| `diameter` | — | — |
| `height` | — | — |
| `width` | — | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `length` | `float` | Return the length of the duct segment in model-units. |
| `shape_type` | `int` | — |
| `is_round_duct` | `bool` | — |
| `shape_type_description` | `str` | Return a string description of the shape of the duct segment. |

### Methods

#### *classmethod* default()

Return a default Duct segment with a length of 1.0

**Returns**: `PhDuctSegment`

#### move(moving_vec3D)

Move the duct segment along a vector.

| Arg | Type | Description |
|-----|------|-------------|
| `moving_vec3D` | `Point3D` | — |

**Returns**: `PhDuctSegment`

#### rotate(axis_vec3D, angle_degrees, origin_pt3D)

Rotate the duct segment by a certain angle around an axis and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_vec3D` | `Point3D` | — |
| `angle_degrees` | `float` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `PhDuctSegment`

#### rotate_xy(angle_degrees, origin_pt3D)

Rotate the duct segment counterclockwise in the XY plane by a certain angle.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degrees` | `float` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `PhDuctSegment`

#### reflect(normal_vec3D, origin_pt3D)

Reflected the duct segment across a plane with the input normal vector and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `normal_vec3D` | `Point3D` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `PhDuctSegment`

#### scale(scale_factor, origin_pt3D)

Scale the duct segment by a factor from an origin point.

| Arg | Type | Description |
|-----|------|-------------|
| `scale_factor` | `float` | — |
| `origin_pt3D` | `Optional[Point3D]` | — |

**Returns**: `PhDuctSegment`

---

## PhDuctElement

A Duct Element made up of one or more individual Duct Segments.

**Inherits from**: `_base._PhHVACBase`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | — | — |
| `duct_type` | — | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `segments` | `List[PhDuctSegment]` | Return a list of all the PhDuctSegments that make up the PhDuctElement. |
| `length` | `float` | Return the total duct length of all the PhDuctSegments in model-units. |
| `is_round_duct` | `bool` | — |
| `shape_type` | `Optional[int]` | — |
| `shape_type_description` | `Optional[str]` | — |

### Methods

#### *classmethod* default_supply_duct(*args, **kwargs)

Returns a default PhDuctElement with a single segment and a length of 1.0

| Arg | Type | Description |
|-----|------|-------------|
| `*args` | `*Any` | — |
| `**kwargs` | `**Any` | — |

**Returns**: `PhDuctElement`

#### *classmethod* default_exhaust_duct(*args, **kwargs)

Returns a default PhDuctElement with a single segment and a length of 1.0

| Arg | Type | Description |
|-----|------|-------------|
| `*args` | `*Any` | — |
| `**kwargs` | `**Any` | — |

**Returns**: `PhDuctElement`

#### add_segment(_segment)

Add a new PhDuctSegment to the Duct Element.

| Arg | Type | Description |
|-----|------|-------------|
| `_segment` | `PhDuctSegment` | — |

**Returns**: `None`

#### clear_segments()

Clear all the segments from the duct element.

**Returns**: `None`

#### move(moving_vec3D)

Move the duct element's segment along a vector.

| Arg | Type | Description |
|-----|------|-------------|
| `moving_vec3D` | — | — |

#### rotate(axis_vec3D, angle_degrees, origin_pt3D)

Rotate the duct element's segment by a certain angle around an axis and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_vec3D` | — | — |
| `angle_degrees` | — | — |
| `origin_pt3D` | — | — |

#### rotate_xy(angle_degrees, origin_pt3D)

Rotate the duct element's segment counterclockwise in the XY plane by a certain angle.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degrees` | — | — |
| `origin_pt3D` | — | — |

#### reflect(normal_vec3D, origin_pt3D)

Reflected the duct element's segment across a plane with the input normal vector and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `normal_vec3D` | — | — |
| `origin_pt3D` | — | — |

#### scale(scale_factor, origin_pt3D)

Scale the duct element's segments by a factor from an origin point.

| Arg | Type | Description |
|-----|------|-------------|
| `scale_factor` | `float` | — |
| `origin_pt3D` | `Optional[Point3D]` | — |

**Returns**: `PhDuctElement`

---
