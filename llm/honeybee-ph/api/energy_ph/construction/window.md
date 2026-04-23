# window

HBPH Window Objects

**Source**: `honeybee_energy_ph/window.py`

---

## PhWindowFrameElement

One side of a PH window frame (top, right, bottom, or left).

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `width` | `float` | Frame element width (m). Default: 0.1. |
| `u_factor` | `float` | Frame U-value (W/m2K). Default: 1.0. |
| `psi_glazing` | `float` | Glazing-edge psi-value (W/mK). Default: 0.04. |
| `psi_install` | `float` | Installation psi-value (W/mK). Default: 0.04. |
| `chi_value` | `float` | Point thermal bridge chi-value (W/K). Default: 0.0. |

---

## PhWindowFrame

A complete PH window frame with four side elements.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `top` | `PhWindowFrameElement` | Top frame element. |
| `right` | `PhWindowFrameElement` | Right frame element. |
| `bottom` | `PhWindowFrameElement` | Bottom frame element. |
| `left` | `PhWindowFrameElement` | Left frame element. |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `elements` | `List[PhWindowFrameElement]` | Return all four frame elements in clockwise order from top (t, r, b, l). |

---

## PhWindowGlazing

PH-style glazing properties for a window unit.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `u_factor` | `float` | Center-of-glass U-value (W/m2K). Default: 1.0. |
| `g_value` | `float` | Solar heat gain coefficient (SHGC). Default: 0.4. |

---
