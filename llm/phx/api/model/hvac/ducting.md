# ducting

PHX Ventilation Ducting Distribution Objects.

**Source**: `PHX/ducting.py`

---

## PhxDuctSegment

An individual Duct Segment Segment.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `length` | — | — |
| `diameter_mm` | — | Return the diameter in MM. |
| `height_mm` | — | Return the height in MM. |
| `width_mm` | — | Return the width in MM. |
| `insulation_thickness_mm` | — | Return the insulation-thickness in MM. |

---

## PhxDuctElement

A Duct Element / Run made of one or more PhxDuctSegments.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `quantity` | — | — |
| `segments` | — | — |
| `length_m` | — | — |
| `diameter_mm` | — | — |
| `height_mm` | — | — |
| `width_mm` | — | — |
| `insulation_thickness_mm` | — | — |
| `insulation_conductivity_wmk` | — | — |
| `duct_shape` | — | — |
| `is_reflective` | — | — |
| `assigned_vent_unit_ids` | — | — |

### Methods

#### add_segment(_s)

| Arg | Type | Description |
|-----|------|-------------|
| `_s` | — | — |

---
