# space

PH 'Space' and Related Sub-object Classes (FloorSegments, etc).

**Source**: `honeybee_ph/space.py`

---

## SpaceFloorSegment

No description available.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `geometry` | `Optional[LBFace3D]` | — |
| `weighting_factor` | `float` | — |
| `net_area_factor` | `float` | — |
| `reference_point` | `Optional[Point3D]` | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `weighted_floor_area` | `float` | The floor area of the floor segment weighted by any reduction factors (iFCA, TFA) |
| `floor_area` | `float` | The floor area of the floor segment UN-weighted by any reduction factors (iFCA, TFA) |
| `net_floor_area` | `float` | The net area of the floor segment |
| `weighted_net_floor_area` | `float` | The net area of the floor segment weighted by any reduction factors (iFCA, TFA) |

### Methods

#### duplicate_geometry()

**Returns**: `LBFace3D`

#### move(moving_vec3D)

Move the SpaceFloorSegment along a vector.

| Arg | Type | Description |
|-----|------|-------------|
| `moving_vec3D` | `Vector3D` | — |

**Returns**: `SpaceFloorSegment`

#### rotate(axis_vec3D, angle_degrees, origin_pt3D)

Rotate the SpaceFloorSegment by a certain angle around an axis_vec3D and origin_pt3D.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_vec3D` | `Vector3D` | — |
| `angle_degrees` | `float` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `SpaceFloorSegment`

#### rotate_xy(angle_degrees, origin_pt3D)

Rotate the SpaceFloorSegment counterclockwise in the XY plane by a certain angle.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degrees` | `float` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `SpaceFloorSegment`

#### reflect(normal_vec3D, origin_pt3D)

Reflected the SpaceFloorSegment across a plane with the input normal vector and origin_pt3D.

| Arg | Type | Description |
|-----|------|-------------|
| `normal_vec3D` | `Vector3D` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `SpaceFloorSegment`

#### scale(scale_factor, origin_pt3D)

Scale the SpaceFloorSegment by a factor from an origin_pt3D point.

| Arg | Type | Description |
|-----|------|-------------|
| `scale_factor` | `float` | — |
| `origin_pt3D` | `Optional[Point3D]` | — |

**Returns**: `SpaceFloorSegment`

---

## SpaceFloor

No description available.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `geometry` | `Optional[LBFace3D]` | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `reference_points` | — | Returns a list of the Floor's FloorSegment reference points. |
| `weighted_floor_area` | `float` | The total floor area of all floor segments, weighted by any reduction factors (iFCA, TFA) |
| `floor_area` | `float` | The total floor area of all floor segments, UN-weighted by any reduction factors (iFCA, TFA) |
| `net_floor_area` | `float` | The total net floor area of all floor segments |
| `weighted_net_floor_area` | `float` | The total net floor area of all floor segments, weighted by any reduction factors (iFCA, TFA) |
| `floor_segments` | `list[SpaceFloorSegment]` | — |

### Methods

#### add_floor_segment(_floor_seg)

Add a new SpaceFloorSegment to the SpaceFloor.

| Arg | Type | Description |
|-----|------|-------------|
| `_floor_seg` | `SpaceFloorSegment` | The SpaceFloorSegment to add to the SpaceFloor. |

**Returns**: `None`

#### clear_floor_segments()

#### duplicate_geometry()

**Returns**: `LBFace3D`

#### move(moving_vec3D)

Move the SpaceFloor along a vector.

| Arg | Type | Description |
|-----|------|-------------|
| `moving_vec3D` | `Vector3D` | — |

**Returns**: `SpaceFloor`

#### rotate(axis_vec3D, angle_degrees, origin_pt3D)

Rotate the SpaceFloor by a certain angle around an axis_vec3D and origin_pt3D.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_vec3D` | `Vector3D` | — |
| `angle_degrees` | `float` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `SpaceFloor`

#### rotate_xy(angle_degrees, origin_pt3D)

Rotate the SpaceFloor counterclockwise in the XY plane by a certain angle.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degrees` | `float` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `SpaceFloor`

#### reflect(normal_vec3D, origin_pt3D)

Reflected the SpaceFloor across a plane with the input normal vector and origin_pt3D.

| Arg | Type | Description |
|-----|------|-------------|
| `normal_vec3D` | `Vector3D` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `SpaceFloor`

#### scale(scale_factor, origin_pt3D)

Scale the SpaceFloor by a factor from an origin_pt3D point.

| Arg | Type | Description |
|-----|------|-------------|
| `scale_factor` | `float` | — |
| `origin_pt3D` | `Optional[Point3D]` | — |

**Returns**: `SpaceFloor`

---

## SpaceVolume

No description available.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `avg_ceiling_height` | `float` | — |
| `floor` | `SpaceFloor` | — |
| `geometry` | `List[LBFace3D]` | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `net_volume` | `float` | The Interior Net Volume (Vn50). |
| `weighted_floor_area` | `float` | The total floor area of all floor segments in the Volume, weighted by any reduction factors (iFCA, TFA) |
| `floor_area` | `float` | The total floor area of all floor segments in the Volume, UN-weighted by any reduction factors (iFCA, TFA) |
| `net_floor_area` | `float` | The total net floor area of all floor segments in the Volume |
| `weighted_net_floor_area` | `float` | The total net floor area of all floor segments in the Volume, weighted by any reduction factors (iFCA, TFA) |
| `reference_points` | — | Returns the Volume's FloorSegment reference points (center). |
| `floor_segment_surfaces` | `List[Optional[LBFace3D]]` | — |
| `floor_segments` | `List[SpaceFloorSegment]` | — |

### Methods

#### clear_volume_geometry()

Delete all the geometry from the SpaceVolume.

**Returns**: `None`

#### move(moving_vec3D)

Move the SpaceVolume along a vector.

| Arg | Type | Description |
|-----|------|-------------|
| `moving_vec3D` | `Vector3D` | — |

**Returns**: `SpaceVolume`

#### rotate(axis_vec3D, angle_degrees, origin_pt3D)

Rotate the SpaceVolume by a certain angle around an axis_vec3D and origin_pt3D.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_vec3D` | `Vector3D` | — |
| `angle_degrees` | `float` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `SpaceVolume`

#### rotate_xy(angle_degrees, origin_pt3D)

Rotate the SpaceVolume counterclockwise in the XY plane by a certain angle.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degrees` | `float` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `SpaceVolume`

#### reflect(normal_vec3D, origin_pt3D)

Reflected the SpaceVolume across a plane with the input normal vector and origin_pt3D.

| Arg | Type | Description |
|-----|------|-------------|
| `normal_vec3D` | `Vector3D` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `SpaceVolume`

#### scale(scale_factor, origin_pt3D)

Scale the SpaceVolume by a factor from an origin_pt3D point.

| Arg | Type | Description |
|-----|------|-------------|
| `scale_factor` | `float` | — |
| `origin_pt3D` | `Optional[Point3D]` | — |

**Returns**: `SpaceVolume`

---

## Space

No description available.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `quantity` | `int` | — |
| `wufi_type` | `int` | — |
| `name` | `str` | — |
| `number` | `str` | — |
| `host` | — | — |
| `properties` | `SpaceProperties` | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `display_name` | `str` | — |
| `full_name` | `str` | — |
| `net_volume` | `float` | The total interior net volume of all Volumes in the Space. |
| `avg_clear_height` | `float` | Returns the average floor-area-weighted height of all the Volumes in the Space |
| `weighted_floor_area` | `float` | The total floor area of all floor segments in the Space, weighted by any reduction factors (iFCA, TFA) |
| `floor_area` | `float` | The total floor area of all floor segments in the Space, UN-weighted by any reduction factors (iFCA, TFA) |
| `net_floor_area` | `float` | The total net floor area of all floor segments in the Space |
| `weighted_net_floor_area` | `float` | The total net floor area of all floor segments in the Space, weighted by any reduction factors (iFCA, TFA) |
| `average_floor_weighting_factor` | `float` | Returns the average weighting factor (TFA/iCFA) for the Space's floor-segments. |
| `average_floor_net_area_factor` | `float` | Returns the average net area factor for the Space's floor-segments. |
| `reference_points` | `list[Point3D]` | Returns a list of the Space's Volume reference Points (center of the floor segments). |
| `volumes` | `List[SpaceVolume]` | — |
| `floor_segment_surfaces` | `List[List[Optional[LBFace3D]]]` | — |
| `floor_segments` | `List[SpaceFloorSegment]` | — |

### Methods

#### add_new_volumes(_new_volumes)

Add a new SpaceVolume or list of SpaceVolumes to the Space.

| Arg | Type | Description |
|-----|------|-------------|
| `_new_volumes` | `Union[SpaceVolume` | A list of the SpaceVolumes to add. |

**Returns**: `None`

#### clear_volumes()

Delete all the Volumes from the Space.

**Returns**: `None`

#### move(moving_vec3D)

Move the Space and its Volumes along a vector.

| Arg | Type | Description |
|-----|------|-------------|
| `moving_vec3D` | `Vector3D` | — |

**Returns**: `Space`

#### rotate(axis_vec3D, angle_degrees, origin_pt3D)

Rotate the Space and its Volumes by a certain angle around an axis_vec3D and origin_pt3D.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_vec3D` | `Vector3D` | — |
| `angle_degrees` | `float` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `Space`

#### rotate_xy(angle_degrees, origin_pt3D)

Rotate the Space and its Volumes counterclockwise in the XY plane by a certain angle.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degrees` | `float` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `Space`

#### reflect(normal_vec3D, origin_pt3D)

Reflected the Space and its Volumes across a plane with the input normal vector and origin_pt3D.

| Arg | Type | Description |
|-----|------|-------------|
| `normal_vec3D` | `Vector3D` | — |
| `origin_pt3D` | `Point3D` | — |

**Returns**: `Space`

#### scale(scale_factor, origin_pt3D)

Scale the Space and its Volumes by a factor from an origin_pt3D point.

| Arg | Type | Description |
|-----|------|-------------|
| `scale_factor` | `float` | — |
| `origin_pt3D` | `Optional[Point3D]` | — |

**Returns**: `Space`

---
