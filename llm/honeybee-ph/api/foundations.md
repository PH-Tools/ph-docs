# foundations

PH Foundation Objects.

**Source**: `honeybee_ph/foundations.py`

---

## PhFoundationType

No description available.

**Inherits from**: `enumerables.CustomEnum`

### Values

| Value | Meaning |
|-------|---------|
| `"1-HEATED_BASEMENT"` | — |
| `"2-UNHEATED_BASEMENT"` | — |
| `"3-SLAB_ON_GRADE"` | — |
| `"4-VENTED_CRAWLSPACE"` | — |
| `"5-NONE"` | — |

---

## PhSlabEdgeInsulationPosition

No description available.

**Inherits from**: `enumerables.CustomEnum`

### Values

| Value | Meaning |
|-------|---------|
| `"1-UNDEFINED"` | — |
| `"2-HORIZONTAL"` | — |
| `"3-VERTICAL"` | — |

---

## PhFoundation

No description available.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `foundation_type` | `PhFoundationType` | — |

### Methods

#### base_attrs_from_dict(_obj, _input_dict)

Set the base object attributes from a dictionary

| Arg | Type | Description |
|-----|------|-------------|
| `_obj` | `PhFoundation` | The PH Foundation object to set the attributes of. |
| `_input_dict` | `dict` | The dictionary to get the attribute values from. |

**Returns**: `None`

---

## PhHeatedBasement

No description available.

**Inherits from**: `PhFoundation`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `foundation_type` | `PhFoundationType` | — |
| `floor_slab_area_m2` | `float` | — |
| `floor_slab_u_value` | `float` | — |
| `floor_slab_exposed_perimeter_m` | `float` | — |
| `slab_depth_below_grade_m` | `float` | — |
| `basement_wall_u_value` | `float` | — |

---

## PhUnheatedBasement

No description available.

**Inherits from**: `PhFoundation`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `foundation_type` | `PhFoundationType` | — |
| `floor_ceiling_area_m2` | `float` | — |
| `ceiling_u_value` | `float` | — |
| `floor_slab_exposed_perimeter_m` | `float` | — |
| `slab_depth_below_grade_m` | `float` | — |
| `basement_wall_height_above_grade_m` | `float` | — |
| `basement_wall_uValue_below_grade` | `float` | — |
| `basement_wall_uValue_above_grade` | `float` | — |
| `floor_slab_u_value` | `float` | — |
| `basement_volume_m3` | `float` | — |
| `basement_ventilation_ach` | `float` | — |

---

## PhSlabOnGrade

No description available.

**Inherits from**: `PhFoundation`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `foundation_type` | `PhFoundationType` | — |
| `floor_slab_area_m2` | `float` | — |
| `floor_slab_u_value` | `Union[float, None]` | — |
| `floor_slab_exposed_perimeter_m` | `float` | — |
| `perim_insulation_width_or_depth_m` | `float` | — |
| `perim_insulation_thickness_m` | `float` | — |
| `perim_insulation_conductivity` | `float` | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `perim_insulation_position` | — | — |

---

## PhVentedCrawlspace

No description available.

**Inherits from**: `PhFoundation`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `foundation_type` | `PhFoundationType` | — |
| `crawlspace_floor_slab_area_m2` | `float` | — |
| `ceiling_above_crawlspace_u_value` | `float` | — |
| `crawlspace_floor_exposed_perimeter_m` | `float` | — |
| `crawlspace_wall_height_above_grade_m` | `float` | — |
| `crawlspace_floor_u_value` | `float` | — |
| `crawlspace_vent_opening_are_m2` | `float` | — |
| `crawlspace_wall_u_value` | `float` | — |

---

## PhFoundationFactory

Factory class to build any PhFoundation from an input dictionary.

---
