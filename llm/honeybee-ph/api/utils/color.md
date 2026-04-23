# color

Basic A-RGB Color class.

**Source**: `honeybee_ph_utils/color.py`

---

## PhColor

An ARGB color with integer channel values in the range 0-255.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `a` | `int` | Alpha channel (0 = fully transparent, 255 = fully opaque). |
| `r` | `int` | Red channel. |
| `g` | `int` | Green channel. |
| `b` | `int` | Blue channel. |

### Methods

#### *classmethod* from_argb(a, r, g, b)

Create a PhColor from explicit alpha, red, green, and blue values.

| Arg | Type | Description |
|-----|------|-------------|
| `a` | `int` | Alpha channel value (clamped to 0-255). |
| `r` | `int` | Red channel value (clamped to 0-255). |
| `g` | `int` | Green channel value (clamped to 0-255). |
| `b` | `int` | Blue channel value (clamped to 0-255). |

**Returns**: `PhColor`

#### *classmethod* from_rgb(r, g, b)

Create a fully opaque PhColor from red, green, and blue values.

| Arg | Type | Description |
|-----|------|-------------|
| `r` | `int` | Red channel value (clamped to 0-255). |
| `g` | `int` | Green channel value (clamped to 0-255). |
| `b` | `int` | Blue channel value (clamped to 0-255). |

**Returns**: `PhColor`

#### *classmethod* from_system_color(color)

Create a PhColor from a .NET System.Drawing.Color.

| Arg | Type | Description |
|-----|------|-------------|
| `color` | `Drawing.Color` | The .NET color to convert. |

**Returns**: `PhColor`

---
