# foundations

PH Foundation Objects.

**Source**: `honeybee_ph/foundations.py`

---

## PhFoundationType

Classification of foundation types for PH certification.

**Inherits from**: `enumerables.CustomEnum`

### Values

| Value | Meaning |
|-------|---------|
| `"1-HEATED_BASEMENT"` | Fully conditioned basement. |
| `"2-UNHEATED_BASEMENT"` | Unconditioned basement below thermal envelope. |
| `"3-SLAB_ON_GRADE"` | Foundation slab directly on soil. |
| `"4-VENTED_CRAWLSPACE"` | Ventilated crawlspace below floor. |
| `"5-NONE"` | No foundation modeled. |

---

## PhSlabEdgeInsulationPosition

Position of perimeter slab edge insulation.

**Inherits from**: `enumerables.CustomEnum`

### Values

| Value | Meaning |
|-------|---------|
| `"1-UNDEFINED"` | Undefined or not specified. |
| `"2-HORIZONTAL"` | Horizontal insulation extending outward from slab edge. |
| `"3-VERTICAL"` | Vertical insulation extending downward from slab edge. |

---

## PhFoundation

Base class for all PH foundation types.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `foundation_type` | `PhFoundationType` | The foundation classification. Default: "5-NONE". |

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

Heated (conditioned) basement foundation.

**Inherits from**: `PhFoundation`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `foundation_type` | `PhFoundationType` | — |
| `floor_slab_area_m2` | `float` | Floor slab area in square meters. |
| `floor_slab_u_value` | `float` | Floor slab U-value in W/(m2K). Default: 1.0. |
| `floor_slab_exposed_perimeter_m` | `float` | Exposed perimeter length in meters. |
| `slab_depth_below_grade_m` | `float` | Depth of slab below grade in meters. Default: 2.5. |
| `basement_wall_u_value` | `float` | Basement wall U-value in W/(m2K). Default: 1.0. |

---

## PhUnheatedBasement

Unheated (unconditioned) basement foundation.

**Inherits from**: `PhFoundation`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `foundation_type` | `PhFoundationType` | — |
| `floor_ceiling_area_m2` | `float` | Area of ceiling above the basement in m2. |
| `ceiling_u_value` | `float` | Ceiling U-value in W/(m2K). Default: 1.0. |
| `floor_slab_exposed_perimeter_m` | `float` | Exposed perimeter length in meters. |
| `slab_depth_below_grade_m` | `float` | Depth of slab below grade in meters. |
| `basement_wall_height_above_grade_m` | `float` | Wall height above grade in meters. |
| `basement_wall_uValue_below_grade` | `float` | Below-grade wall U-value in W/(m2K). Default: 1.0. |
| `basement_wall_uValue_above_grade` | `float` | Above-grade wall U-value in W/(m2K). Default: 1.0. |
| `floor_slab_u_value` | `float` | Floor slab U-value in W/(m2K). Default: 1.0. |
| `basement_volume_m3` | `float` | Basement air volume in cubic meters. |
| `basement_ventilation_ach` | `float` | Basement ventilation rate in ACH. |

---

## PhSlabOnGrade

Slab-on-grade foundation.

**Inherits from**: `PhFoundation`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `foundation_type` | `PhFoundationType` | — |
| `floor_slab_area_m2` | `float` | Floor slab area in square meters. |
| `floor_slab_u_value` | `Union[float, None]` | Floor slab U-value in W/(m2K). None if not set. |
| `floor_slab_exposed_perimeter_m` | `float` | Exposed perimeter length in meters. |
| `perim_insulation_width_or_depth_m` | `float` | Insulation width or depth in meters. Default: 0.300. |
| `perim_insulation_thickness_m` | `float` | Insulation thickness in meters. Default: 0.050. |
| `perim_insulation_conductivity` | `float` | Insulation thermal conductivity in W/(mK). Default: 0.04. |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `perim_insulation_position` | `PhSlabEdgeInsulationPosition` | The perimeter insulation position (horizontal or vertical). |

---

## PhVentedCrawlspace

Ventilated crawlspace foundation.

**Inherits from**: `PhFoundation`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `foundation_type` | `PhFoundationType` | — |
| `crawlspace_floor_slab_area_m2` | `float` | Crawlspace floor slab area in m2. |
| `ceiling_above_crawlspace_u_value` | `float` | Ceiling U-value above crawlspace in W/(m2K). Default: 1.0. |
| `crawlspace_floor_exposed_perimeter_m` | `float` | Exposed perimeter in meters. Default: 2.5. |
| `crawlspace_wall_height_above_grade_m` | `float` | Crawlspace wall height above grade in meters. |
| `crawlspace_floor_u_value` | `float` | Crawlspace floor U-value in W/(m2K). Default: 1.0. |
| `crawlspace_vent_opening_are_m2` | `float` | Ventilation opening area in m2. |
| `crawlspace_wall_u_value` | `float` | Crawlspace wall U-value in W/(m2K). Default: 1.0. |

---

## PhFoundationFactory

Factory class to build PhFoundation objects from dictionaries.

---
