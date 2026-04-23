# space

PH 'Space' and Related Sub-object Classes (FloorSegments, etc).

**Source**: `honeybee_ph/space.py`

---

## SpaceFloorSegment

A single floor area polygon within a PH Space.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `geometry` | `Optional[LBFace3D]` | The planar 3D geometry of this segment. None if not yet assigned. |
| `weighting_factor` | `float` | Multiplier for iCFA/TFA area calculation. Default: 1.0 (no reduction). |
| `net_area_factor` | `float` | Multiplier for net usable area calculation. Default: 1.0 (full area counts). |
| `reference_point` | `Optional[Point3D]` | Point used for spatial containment testing (is this segment inside an HB-Room?). Usually the face centroid, but adjusted for non-convex shapes (L, U). |

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
| `moving_vec3D` | `Vector3D` | The direction and distance to move. |

**Returns**: `SpaceFloorSegment`

#### rotate(axis_vec3D, angle_degrees, origin_pt3D)

Rotate the SpaceFloorSegment by a certain angle around an axis and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_vec3D` | `Vector3D` | The axis of rotation. |
| `angle_degrees` | `float` | The rotation angle in degrees. |
| `origin_pt3D` | `Point3D` | The origin around which to rotate. |

**Returns**: `SpaceFloorSegment`

#### rotate_xy(angle_degrees, origin_pt3D)

Rotate the SpaceFloorSegment counterclockwise in the XY plane.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degrees` | `float` | The rotation angle in degrees. |
| `origin_pt3D` | `Point3D` | The origin around which to rotate. |

**Returns**: `SpaceFloorSegment`

#### reflect(normal_vec3D, origin_pt3D)

Reflect the SpaceFloorSegment across a plane.

| Arg | Type | Description |
|-----|------|-------------|
| `normal_vec3D` | `Vector3D` | The normal vector for the reflection plane. Must be normalized. |
| `origin_pt3D` | `Point3D` | The origin of the reflection plane. |

**Returns**: `SpaceFloorSegment`

#### scale(scale_factor, origin_pt3D)

Scale the SpaceFloorSegment by a factor from an origin point.

| Arg | Type | Description |
|-----|------|-------------|
| `scale_factor` | `float` | The scaling factor. |
| `origin_pt3D` | `Optional[Point3D]` | The origin from which to scale. If None, scales from the World origin (0, 0, 0). |

**Returns**: `SpaceFloorSegment`

---

## SpaceFloor

A collection of SpaceFloorSegments representing one floor level.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `geometry` | `Optional[LBFace3D]` | The merged 3D face for this floor level. None if not yet assigned. |

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
| `moving_vec3D` | `Vector3D` | The direction and distance to move. |

**Returns**: `SpaceFloor`

#### rotate(axis_vec3D, angle_degrees, origin_pt3D)

Rotate the SpaceFloor by a certain angle around an axis and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_vec3D` | `Vector3D` | The axis of rotation. |
| `angle_degrees` | `float` | The rotation angle in degrees. |
| `origin_pt3D` | `Point3D` | The origin around which to rotate. |

**Returns**: `SpaceFloor`

#### rotate_xy(angle_degrees, origin_pt3D)

Rotate the SpaceFloor counterclockwise in the XY plane.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degrees` | `float` | The rotation angle in degrees. |
| `origin_pt3D` | `Point3D` | The origin around which to rotate. |

**Returns**: `SpaceFloor`

#### reflect(normal_vec3D, origin_pt3D)

Reflect the SpaceFloor across a plane.

| Arg | Type | Description |
|-----|------|-------------|
| `normal_vec3D` | `Vector3D` | The normal vector for the reflection plane. Must be normalized. |
| `origin_pt3D` | `Point3D` | The origin of the reflection plane. |

**Returns**: `SpaceFloor`

#### scale(scale_factor, origin_pt3D)

Scale the SpaceFloor by a factor from an origin point.

| Arg | Type | Description |
|-----|------|-------------|
| `scale_factor` | `float` | The scaling factor. |
| `origin_pt3D` | `Optional[Point3D]` | The origin from which to scale. If None, scales from the World origin (0, 0, 0). |

**Returns**: `SpaceFloor`

---

## SpaceVolume

A 3D volume within a PH Space, defined by a floor and ceiling height.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `avg_ceiling_height` | `float` | Average clear ceiling height in meters. Default: 2.5. |
| `floor` | `SpaceFloor` | The floor level for this volume. |
| `geometry` | `List[LBFace3D]` | The enclosing 3D face geometry. |

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
| `moving_vec3D` | `Vector3D` | The direction and distance to move. |

**Returns**: `SpaceVolume`

#### rotate(axis_vec3D, angle_degrees, origin_pt3D)

Rotate the SpaceVolume by a certain angle around an axis and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_vec3D` | `Vector3D` | The axis of rotation. |
| `angle_degrees` | `float` | The rotation angle in degrees. |
| `origin_pt3D` | `Point3D` | The origin around which to rotate. |

**Returns**: `SpaceVolume`

#### rotate_xy(angle_degrees, origin_pt3D)

Rotate the SpaceVolume counterclockwise in the XY plane.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degrees` | `float` | The rotation angle in degrees. |
| `origin_pt3D` | `Point3D` | The origin around which to rotate. |

**Returns**: `SpaceVolume`

#### reflect(normal_vec3D, origin_pt3D)

Reflect the SpaceVolume across a plane.

| Arg | Type | Description |
|-----|------|-------------|
| `normal_vec3D` | `Vector3D` | The normal vector for the reflection plane. Must be normalized. |
| `origin_pt3D` | `Point3D` | The origin of the reflection plane. |

**Returns**: `SpaceVolume`

#### scale(scale_factor, origin_pt3D)

Scale the SpaceVolume by a factor from an origin point.

| Arg | Type | Description |
|-----|------|-------------|
| `scale_factor` | `float` | The scaling factor. |
| `origin_pt3D` | `Optional[Point3D]` | The origin from which to scale. If None, scales from the World origin (0, 0, 0). |

**Returns**: `SpaceVolume`

---

## Space

A Passive House Space representing an occupiable floor area.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `quantity` | `int` | Number of identical spaces (for repetition). Default: 1. |
| `wufi_type` | `int` | WUFI-Passive space type code. Default: 99 (User-Defined). |
| `name` | `str` | User-facing space name. |
| `number` | `str` | Space number or identifier string. |
| `host` | — | The parent Honeybee Room hosting this space. |
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
| `moving_vec3D` | `Vector3D` | The direction and distance to move. |

**Returns**: `Space`

#### rotate(axis_vec3D, angle_degrees, origin_pt3D)

Rotate the Space and its Volumes around an axis and origin.

| Arg | Type | Description |
|-----|------|-------------|
| `axis_vec3D` | `Vector3D` | The axis of rotation. |
| `angle_degrees` | `float` | The rotation angle in degrees. |
| `origin_pt3D` | `Point3D` | The origin around which to rotate. |

**Returns**: `Space`

#### rotate_xy(angle_degrees, origin_pt3D)

Rotate the Space and its Volumes counterclockwise in the XY plane.

| Arg | Type | Description |
|-----|------|-------------|
| `angle_degrees` | `float` | The rotation angle in degrees. |
| `origin_pt3D` | `Point3D` | The origin around which to rotate. |

**Returns**: `Space`

#### reflect(normal_vec3D, origin_pt3D)

Reflect the Space and its Volumes across a plane.

| Arg | Type | Description |
|-----|------|-------------|
| `normal_vec3D` | `Vector3D` | The normal vector for the reflection plane. Must be normalized. |
| `origin_pt3D` | `Point3D` | The origin of the reflection plane. |

**Returns**: `Space`

#### scale(scale_factor, origin_pt3D)

Scale the Space and its Volumes by a factor from an origin point.

| Arg | Type | Description |
|-----|------|-------------|
| `scale_factor` | `float` | The scaling factor. |
| `origin_pt3D` | `Optional[Point3D]` | The origin from which to scale. If None, scales from the World origin (0, 0, 0). |

**Returns**: `Space`

---
