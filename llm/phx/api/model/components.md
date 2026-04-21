# components

PHX Component (Face, Aperture) Classes

**Source**: `PHX/components.py`

---

## PhxComponentBase

Base class with auto-incrementing ID counter for all PHX building components.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `id_num` | — | — |

---

## PhxComponentOpaque

An opaque building-envelope surface (wall, roof, or floor).

**Inherits from**: `PhxComponentBase`

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `u_value` | — | Whole-assembly U-value (W/m2K) from the assigned opaque construction. |
| `polygon_ids` | — | Return a Set of all the Polygon-id numbers found in the Component's Polygon group. |
| `unique_key` | — | Returns a unique text key,. Useful for sorting / grouping / merging components. |
| `is_shade` | — | True if this component is an opaque shading element (no interior zone attachment). |
| `is_above_grade_wall` | — | True if this component is a wall exposed to exterior air (above grade). |
| `is_below_grade_wall` | — | True if this component is a wall exposed to ground (below grade). |
| `is_above_grade_floor` | — | True if this component is a floor exposed to exterior air (e.g. cantilever). |
| `is_below_grade_floor` | — | True if this component is a floor exposed to ground (slab-on-grade or basement). |
| `is_roof` | — | True if this component is a roof or ceiling surface. |
| `aperture_ids` | — | Return a Set of all the Aperture-id numbers found in the Component's Aperture group. |
| `aperture_elements` | — | Return a list of all the Aperture Elements found in the Component's Aperture group. |

### Methods

#### add_polygons(_input)

Adds a new Polygon or Polygons to the Component's collection.

| Arg | Type | Description |
|-----|------|-------------|
| `_input` | — | The polygon or polygons to add to the component's collection. |

#### add_aperture(_aperture)

Add a new child PhxComponentAperture to the Component.

| Arg | Type | Description |
|-----|------|-------------|
| `_aperture` | — | (PhxComponentAperture): The new PhxComponentAperture to add as a child. |

#### get_host_polygon_by_child_id_num(_id_num)

Return a single Polygon from the collection if it has the specified ID as a 'child'.

| Arg | Type | Description |
|-----|------|-------------|
| `_id_num` | — | (int) The Polygon id-number to search the Component's collection for. |

#### get_aperture_polygon_by_id_num(_id_num)

Return a single Polygon from the collection if it has the specified ID as a 'child'.

| Arg | Type | Description |
|-----|------|-------------|
| `_id_num` | — | (int) The Polygon id-number to search the Component's collection for. |

#### get_aperture_element_by_polygon_id_num(_id_num)

Return a single Aperture Element from the collection if it has the specified ID.

| Arg | Type | Description |
|-----|------|-------------|
| `_id_num` | — | (int) The Polygon id-number to search the Component's collection for. |

#### set_assembly_type(_phx_construction)

Set the Assembly Type for the Component.

| Arg | Type | Description |
|-----|------|-------------|
| `_phx_construction` | — | The Construction to set as the Assembly Type. |

#### get_total_gross_component_area()

Return the total Gross wall area of the Component (ignoring any nested apertures).

#### get_total_aperture_area()

Return the total Gross aperture area of the Component.

#### get_total_net_component_area()

Return the total net area of the Component (gross - apertures).

---

## PhxApertureShadingDimensions

PHPP old-style shading dimensions for an aperture element.

**Inherits from**: `PhxComponentBase`

---

## PhxApertureElement

A single sash or glazing unit within an aperture component.

**Inherits from**: `PhxComponentBase`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `shading_dimensions` | `PhxApertureShadingDimensions` | PHPP-style horizon, reveal, and overhang dimensions. Default: new PhxApertureShadingDimensions(). |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `area` | — | Return the area of the element's polygon. |
| `width` | — | Width of the element's polygon, or perimeter/4 as fallback for non-rectangular shapes. |
| `height` | — | Height of the element's polygon, or perimeter/4 as fallback for non-rectangular shapes. |
| `frame_area` | — | Return the area of the frame in the Aperture Element. |
| `frame_factor` | — | Return the % of the Aperture Element which is frame (as opposed to glazing). |
| `glazing_area` | — | Return the area of the glazing in the Aperture Element. |
| `glazing_factor` | — | Return the % of the Aperture Element which is glazing (as opposed to frame). |

### Methods

#### is_equivalent(other)

Return True if the two elements are equivalent.

| Arg | Type | Description |
|-----|------|-------------|
| `other` | — | — |

#### polygons_are_equivalent(other)

Return True if the two elements have equivalent polygons.

| Arg | Type | Description |
|-----|------|-------------|
| `other` | — | — |

#### scale(_scale_factor)

Scale the element's polygon by the specified factor.

| Arg | Type | Description |
|-----|------|-------------|
| `_scale_factor` | — | — |

---

## PhxComponentAperture

A transparent building-envelope component (window or door) with one or more sash elements.

**Inherits from**: `PhxComponentBase`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `host` | — | The parent opaque component this aperture is installed in. |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `install_depth` | — | Return the installation depth of the Aperture. |
| `average_shading_d_reveal` | — | The average shading 'reveal' distance of the Aperture's Elements from the glass. |
| `default_monthly_shading_correction_factor` | — | Return the default monthly shading correction factor. |
| `shade_type_id_num` | — | Return the ID-Number of the Component Construction's Shade-Type, or -1 if None. |
| `window_type_id_num` | — | ID number of the assigned window construction type. |
| `polygons` | — | Collected polygons from all child elements that have geometry assigned. |
| `polygon_ids` | — | Return a Set of all the Polygon-id numbers found in the Component's Polygon group. |
| `polygon_ids_sorted` | — | Return a Tuple of all the Polygon-id numbers found in the Component's Polygon group, sorted. |
| `unique_key` | — | Returns a unique text key,. Useful for sorting / grouping / merging components. |

### Methods

#### add_elements(_elements)

Add one or more new 'Elements' (Sashes) to the Aperture

| Arg | Type | Description |
|-----|------|-------------|
| `_elements` | — | — |

#### add_element(_element)

Add a new 'Element' (Sash) to the Aperture

| Arg | Type | Description |
|-----|------|-------------|
| `_element` | — | — |

#### set_window_type(_window_type)

Set the Component's Window Type.

| Arg | Type | Description |
|-----|------|-------------|
| `_window_type` | — | — |

#### get_total_aperture_area()

Return the total Window Area of the Component.

#### scale(_scale_factor)

Scale the Component's size by the given factor.

| Arg | Type | Description |
|-----|------|-------------|
| `_scale_factor` | — | — |

---

## PhxComponentThermalBridge

A linear thermal bridge element in the building envelope.

**Inherits from**: `PhxComponentBase`

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `identifier` | — | — |
| `quantity` | — | — |
| `group_type` | — | — |
| `group_number` | — | Integer group number from the thermal bridge type, or 15 (default) if unset. |
| `display_name` | — | — |
| `psi_value` | — | — |
| `fRsi_value` | — | — |
| `length` | — | — |
| `unique_key` | — | Returns a unique text key,. Useful for sorting / grouping / merging components. |

---
