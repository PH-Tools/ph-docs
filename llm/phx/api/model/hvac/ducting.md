# ducting

PHX ventilation duct distribution objects.

**Source**: `PHX/ducting.py`

---

## PhxDuctSegment

An individual duct segment with geometry, cross-section, and insulation properties.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `length` | — | Segment length derived from the line geometry (m). |
| `diameter_mm` | — | Return the diameter in MM. |
| `height_mm` | — | Return the height in MM. |
| `width_mm` | — | Return the width in MM. |
| `insulation_thickness_mm` | — | Return the insulation-thickness in MM. |

---

## PhxDuctElement

A duct run composed of one or more PhxDuctSegment objects.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `quantity` | — | Always 1 for a single duct element. |
| `segments` | — | All duct segments in this element. |
| `length_m` | — | Total duct length across all segments (m). |
| `diameter_mm` | — | Length-weighted average diameter across all segments (mm). |
| `height_mm` | — | Length-weighted average height for rectangular ducts (mm). 0.0 if round. |
| `width_mm` | — | Length-weighted average width for rectangular ducts (mm). 0.0 if round. |
| `insulation_thickness_mm` | — | Length-weighted average insulation thickness (mm). |
| `insulation_conductivity_wmk` | — | Length-weighted average insulation conductivity (W/mK). |
| `duct_shape` | — | Return 1 for round duct, 2 for rectangular duct. |
| `is_reflective` | — | True if any segment has reflective insulation facing. |
| `assigned_vent_unit_ids` | — | List of ventilation unit IDs this duct element is assigned to. |

### Methods

#### add_segment(_s)

Add a duct segment to this element.

| Arg | Type | Description |
|-----|------|-------------|
| `_s` | — | The duct segment to add. |

---
