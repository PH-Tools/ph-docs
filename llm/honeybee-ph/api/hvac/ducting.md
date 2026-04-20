# ducting

Honeybee-PH-HVAC-Equipment: Ducts.

**Source**: `honeybee_phhvac/ducting.py`

---

## PhDuctSegment

A single duct segment (linear) with geometry and attributes.

**Inherits from**: `_base._PhHVACBase`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `geometry` | — | The 3D line segment representing the duct centerline. |
| `insulation_thickness` | — | Insulation thickness in model-units (default 0.0254 m). |
| `insulation_conductivity` | — | Insulation thermal conductivity in W/(m-K) (default 0.04). |
| `insulation_reflective` | — | True if insulation has a reflective facing. |
| `diameter` | — | Duct diameter in model-units (default 0.160 m), used for round ducts. |
| `height` | — | Rectangular duct height in model-units, or None for round. |
| `width` | — | Rectangular duct width in model-units, or None for round. |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `length` | `float` | Return the length of the duct segment in model-units. |
| `shape_type` | `int` | Return the shape type integer (1=round, 2=rectangular). |
| `is_round_duct` | `bool` | Return True if the duct segment is round. |
| `shape_type_description` | `str` | Return a string description of the shape of the duct segment. |

### Methods

#### *classmethod* default()

Return a default PhDuctSegment with a length of 1.0 along the X-axis.

**Returns**: `PhDuctSegment`

#### move(moving_vec3D)

Move the duct segment along a vector.

| Arg | Type | Description |
|-----|------|-------------|
| `moving_vec3D` | `Point3D` | A Vector3D with the direction and distance to move the ray. |

**Returns**: `PhDuctSegment`

#### rotate(axis_vec3D, angle_degrees, origin_pt3D)

Rotate the duct segment by a certain angle around an axis and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_vec3D` | `Point3D` | A Vector3D axis representing the axis of rotation. |
| `angle_degrees` | `float` | An angle for rotation in degrees. |
| `origin_pt3D` | `Point3D` | A Point3D for the origin around which the object will be rotated. |

**Returns**: `PhDuctSegment`

#### rotate_xy(angle_degrees, origin_pt3D)

Rotate the duct segment counterclockwise in the XY plane by a certain angle.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degrees` | `float` | An angle in degrees. |
| `origin_pt3D` | `Point3D` | A Point3D for the origin around which the object will be rotated. |

**Returns**: `PhDuctSegment`

#### reflect(normal_vec3D, origin_pt3D)

Reflect the duct segment across a plane with the input normal vector and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `normal_vec3D` | `Point3D` | A Vector3D representing the normal vector for the plane across which the line segment will be reflected. THIS VECTOR MUST BE NORMALIZED. |
| `origin_pt3D` | `Point3D` | A Point3D representing the origin from which to reflect. |

**Returns**: `PhDuctSegment`

#### scale(scale_factor, origin_pt3D)

Scale the duct segment by a factor from an origin point.

| Arg | Type | Description |
|-----|------|-------------|
| `scale_factor` | `float` | A number representing how much the line segment should be scaled. |
| `origin_pt3D` | `Optional[Point3D]` | A Point3D representing the origin from which to scale. If None, it will be scaled from the World origin (0, 0, 0). |

**Returns**: `PhDuctSegment`

---

## PhDuctElement

A Duct Element made up of one or more individual Duct Segments.

**Inherits from**: `_base._PhHVACBase`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | — | User-facing name for this duct element. |
| `duct_type` | — | Duct type integer (1=supply, 2=exhaust). |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `segments` | `List[PhDuctSegment]` | Return a list of all the PhDuctSegments that make up the PhDuctElement. |
| `length` | `float` | Return the total duct length of all the PhDuctSegments in model-units. |
| `is_round_duct` | `bool` | Return True if the duct element contains round segments. |
| `shape_type` | `Optional[int]` | Return the shape type integer (1=round, 2=rectangular) or None if no segments. |
| `shape_type_description` | `Optional[str]` | Return a string describing the duct dimensions, or None if no segments. |

### Methods

#### *classmethod* default_supply_duct(*args, **kwargs)

Return a default supply PhDuctElement with a single segment and a length of 1.0.

| Arg | Type | Description |
|-----|------|-------------|
| `*args` | `*Any` | — |
| `**kwargs` | `**Any` | — |

**Returns**: `PhDuctElement`

#### *classmethod* default_exhaust_duct(*args, **kwargs)

Return a default exhaust PhDuctElement with a single segment and a length of 1.0.

| Arg | Type | Description |
|-----|------|-------------|
| `*args` | `*Any` | — |
| `**kwargs` | `**Any` | — |

**Returns**: `PhDuctElement`

#### add_segment(_segment)

Add a new PhDuctSegment to the Duct Element.

| Arg | Type | Description |
|-----|------|-------------|
| `_segment` | `PhDuctSegment` | The duct segment to add. Must match the existing shape type (round or rectangular) if segments already exist. |

**Returns**: `None`

#### clear_segments()

Clear all the segments from the duct element.

**Returns**: `None`

#### move(moving_vec3D)

Move the duct element's segments along a vector.

| Arg | Type | Description |
|-----|------|-------------|
| `moving_vec3D` | — | A Vector3D with the direction and distance to move the ray. |

#### rotate(axis_vec3D, angle_degrees, origin_pt3D)

Rotate the duct element's segments by a certain angle around an axis and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_vec3D` | — | A Vector3D axis representing the axis of rotation. |
| `angle_degrees` | — | An angle for rotation in degrees. |
| `origin_pt3D` | — | A Point3D for the origin around which the object will be rotated. |

#### rotate_xy(angle_degrees, origin_pt3D)

Rotate the duct element's segments counterclockwise in the XY plane by a certain angle.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degrees` | — | An angle in degrees. |
| `origin_pt3D` | — | A Point3D for the origin around which the object will be rotated. |

#### reflect(normal_vec3D, origin_pt3D)

Reflect the duct element's segments across a plane with the input normal vector and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `normal_vec3D` | — | A Vector3D representing the normal vector for the plane across which the line segment will be reflected. THIS VECTOR MUST BE NORMALIZED. |
| `origin_pt3D` | — | A Point3D representing the origin from which to reflect. |

#### scale(scale_factor, origin_pt3D)

Scale the duct element's segments by a factor from an origin point.

| Arg | Type | Description |
|-----|------|-------------|
| `scale_factor` | `float` | A number representing how much the line segment should be scaled. |
| `origin_pt3D` | `Optional[Point3D]` | A Point3D representing the origin from which to scale. If None, it will be scaled from the World origin (0, 0, 0). |

**Returns**: `PhDuctElement`

---
