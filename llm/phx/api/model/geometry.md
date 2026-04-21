# geometry

PHX Geometry Classes

**Source**: `PHX/geometry.py`

---

## PolygonEdgeError

Raised when a PhxPolygonRectangular edge cannot be constructed due to missing vertices.

**Inherits from**: `Exception`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `msg` | — | — |

---

## PhxVertix2D

A 2D vertex point used for planar geometry operations.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `unique_key` | — | Return a unique key (str) for the Vertex. Used for dicts, welding, etc |

### Methods

#### is_equivalent(other)

Check coordinate equivalence with another vertex, ignoring ID.

| Arg | Type | Description |
|-----|------|-------------|
| `other` | — | The vertex to compare against. |

---

## PhxVertix

A 3D vertex point used as the fundamental geometric primitive in PHX.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `unique_key` | — | Return a unique key (str) for the Vertex. Used for dicts, welding, etc |

### Methods

#### is_equivalent(other)

Check coordinate equivalence with another vertex, ignoring ID.

| Arg | Type | Description |
|-----|------|-------------|
| `other` | — | The vertex to compare against. |

#### distance_to(other)

Return the distance between this vertex and another.

| Arg | Type | Description |
|-----|------|-------------|
| `other` | — | — |

---

## PhxVector

A 3D vector used for normals, directions, and geometric operations.

### Methods

#### *classmethod* from_2_points(_start_pt, _end_pt)

Return a new PhxVector based on a start and end point.

| Arg | Type | Description |
|-----|------|-------------|
| `_start_pt` | — | — |
| `_end_pt` | — | — |

#### scale(_factor)

Scale this vector in-place by a scalar factor.

| Arg | Type | Description |
|-----|------|-------------|
| `_factor` | — | The scalar multiplier. |

#### dot(other)

Get the dot product of this vector with another.

| Arg | Type | Description |
|-----|------|-------------|
| `other` | — | — |

#### rotate_around(_axis, _angle_deg)

Rotate this vector around an axis by an angle in degrees using Rodrigues' rotation formula.

| Arg | Type | Description |
|-----|------|-------------|
| `_axis` | — | The unit axis of rotation. |
| `_angle_deg` | — | The rotation angle in degrees. |

#### unitize()

Convert this vector to a unit vector.

---

## PhxPlane

A 3D plane defined by an origin point, a normal vector, and local X/Y axes.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `normal` | — | The plane's surface normal vector. |

### Methods

#### xyz_to_xy(point)

Get a Point2D in the coordinate system of this plane from a Point3D.

| Arg | Type | Description |
|-----|------|-------------|
| `point` | — | — |

#### xy_to_xyz(point)

Get a Point3D from a Point2D in the coordinate system of this plane.

| Arg | Type | Description |
|-----|------|-------------|
| `point` | — | — |

---

## PhxLineSegment

A 3D line segment defined by two endpoint vertices.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `length` | — | The Euclidean length of the segment. |

### Methods

#### *classmethod* from_length(_length)

Create a PhxLineSegment from a length value along the X-axis.

| Arg | Type | Description |
|-----|------|-------------|
| `_length` | — | — |

---

## PhxPolygon

A 3D polygon surface defined by 3 or more coplanar vertices.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `area` | — | The polygon area, lazily computed from vertices using the shoelace formula. |
| `center` | — | The polygon centroid, lazily computed as the average of all vertex positions. |
| `display_name` | — | The polygon's display name, falling back to its numeric ID if unset. |
| `vertices` | — | The ordered list of vertices defining this polygon's boundary. |
| `vertices_id_numbers` | — | The ID numbers of all vertices in order. |
| `angle_from_horizontal` | — | Return the surface normal's angle (degrees) off horizontal. |
| `is_horizontal` | — | True if the polygon faces up or down (normal within tolerance of vertical). |
| `is_vertical` | — | True if the polygon's normal is perpendicular to the vertical axis. |
| `cardinal_orientation_angle` | — | Calculate polygon normal's horizontal angle off a reference. By default, the |

### Methods

#### add_vertix(_phx_vertix)

Append a vertex to this polygon's boundary.

| Arg | Type | Description |
|-----|------|-------------|
| `_phx_vertix` | — | The vertex to add. |

#### add_child_poly_id(_child_ids)

Register one or more child polygon IDs (e.g., window openings within a wall polygon).

| Arg | Type | Description |
|-----|------|-------------|
| `_child_ids` | — | A single ID or collection of child polygon IDs. |

#### set_vertex(_phx_vertix, index)

Set a vertex at a specific index.

| Arg | Type | Description |
|-----|------|-------------|
| `_phx_vertix` | — | — |
| `index` | — | — |

#### calculate_area()

Calculate the area of the polygon.

#### calculate_center()

Find the center of the polygon.

#### scale(_scale_factor)

Scale the polygon in-place about its centroid by the given factor.

| Arg | Type | Description |
|-----|------|-------------|
| `_scale_factor` | — | The scale multiplier. Default: 1.0. |

#### perimeter_length()

Calculate the total perimeter length of the polygon.

---

## PhxPolygonRectangular

A rectangular polygon with named corner vertices and edge accessors.

**Inherits from**: `PhxPolygon`

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `edge_top` | — | Returns the PhxLineSegment representing the 'Top' side of the Polygon (viewed from outside). |
| `edge_left` | — | Returns the PhxLineSegment representing the 'Left' side of the Polygon (viewed from outside). |
| `edge_bottom` | — | Returns the PhxLineSegment representing the 'Bottom' side of the Polygon (viewed from outside). |
| `edge_right` | — | Returns the PhxLineSegment representing the 'Right' side of the Polygon (viewed from outside). |
| `width` | — | The width of the rectangular polygon (top edge length). |
| `height` | — | The height of the rectangular polygon (left edge length). |
| `vertices` | — | Return a List of the PhxPolygonRectangle Vertices (counter-clockwise from upper-left). |
| `area` | — | Returns the area of the rectangular surface. |

### Methods

#### add_vertix(_phx_vertix)

| Arg | Type | Description |
|-----|------|-------------|
| `_phx_vertix` | — | — |

#### set_vertex(_phx_vertix, index)

Set a vertex at a specific index.

| Arg | Type | Description |
|-----|------|-------------|
| `_phx_vertix` | — | — |
| `index` | — | — |

#### perimeter_length()

Calculate the total perimeter length of the polygon.

---

## PhxGraphics3D

A collection of 3D polygons representing the geometry of a building component.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `vertices` | — | Returns a sorted list with all of the unique vertix objects of all the polygons in the collection. |

### Methods

#### add_polygons(_polygons)

Adds a new Polygon object to the collection

| Arg | Type | Description |
|-----|------|-------------|
| `_polygons` | — | — |

#### get_polygons_by_id(_ids)

Returns a sorted list of polygons in the collection matching the IDs supplied.

| Arg | Type | Description |
|-----|------|-------------|
| `_ids` | — | (Collection[int]): A collection of one or more id_nums to look for. |

---
