# geometry

PHX Geometry Classes

**Source**: `PHX/geometry.py`

---

## PolygonEdgeError

No description available.

**Inherits from**: `Exception`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `msg` | — | — |

---

## PhxVertix2D

A 2D vertix.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `unique_key` | — | Return a unique key (str) for the Vertex. Used for dicts, welding, etc |

### Methods

#### is_equivalent(other)

| Arg | Type | Description |
|-----|------|-------------|
| `other` | — | — |

---

## PhxVertix

No description available.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `unique_key` | — | Return a unique key (str) for the Vertex. Used for dicts, welding, etc |

### Methods

#### is_equivalent(other)

| Arg | Type | Description |
|-----|------|-------------|
| `other` | — | — |

#### distance_to(other)

Return the distance between this vertex and another.

| Arg | Type | Description |
|-----|------|-------------|
| `other` | — | — |

---

## PhxVector

No description available.

### Methods

#### *classmethod* from_2_points(_start_pt, _end_pt)

Return a new PhxVector based on a start and end point.

| Arg | Type | Description |
|-----|------|-------------|
| `_start_pt` | — | — |
| `_end_pt` | — | — |

#### scale(_factor)

| Arg | Type | Description |
|-----|------|-------------|
| `_factor` | — | — |

#### dot(other)

Get the dot product of this vector with another.

| Arg | Type | Description |
|-----|------|-------------|
| `other` | — | — |

#### rotate_around(_axis, _angle_deg)

Rotate this vector around an axis by an angle in radians.

| Arg | Type | Description |
|-----|------|-------------|
| `_axis` | — | — |
| `_angle_deg` | — | — |

#### unitize()

Convert this vector to a unit vector.

---

## PhxPlane

No description available.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `normal` | — | — |

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

No description available.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `length` | — | — |

### Methods

#### *classmethod* from_length(_length)

Create a PhxLineSegment from a length value along the X-axis.

| Arg | Type | Description |
|-----|------|-------------|
| `_length` | — | — |

---

## PhxPolygon

A Polygon surface defined by 3 or more vertices.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `area` | — | — |
| `center` | — | — |
| `display_name` | — | — |
| `vertices` | — | — |
| `vertices_id_numbers` | — | — |
| `angle_from_horizontal` | — | Return the surface normal's angle (degrees) off horizontal. |
| `is_horizontal` | — | — |
| `is_vertical` | — | — |
| `cardinal_orientation_angle` | — | Calculate polygon normal's horizontal angle off a reference. By default, the |

### Methods

#### add_vertix(_phx_vertix)

| Arg | Type | Description |
|-----|------|-------------|
| `_phx_vertix` | — | — |

#### add_child_poly_id(_child_ids)

| Arg | Type | Description |
|-----|------|-------------|
| `_child_ids` | — | — |

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

Scale the polygon by the given factor.

| Arg | Type | Description |
|-----|------|-------------|
| `_scale_factor` | — | — |

#### perimeter_length()

Calculate the total perimeter length of the polygon.

---

## PhxPolygonRectangular

A Polygon with additional geometric attributes for rectangular surfaces.

**Inherits from**: `PhxPolygon`

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `edge_top` | — | Returns the PhxLineSegment representing the 'Top' side of the Polygon (viewed from outside). |
| `edge_left` | — | Returns the PhxLineSegment representing the 'Left' side of the Polygon (viewed from outside). |
| `edge_bottom` | — | Returns the PhxLineSegment representing the 'Bottom' side of the Polygon (viewed from outside). |
| `edge_right` | — | Returns the PhxLineSegment representing the 'Right' side of the Polygon (viewed from outside). |
| `width` | — | — |
| `height` | — | — |
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

No description available.

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
