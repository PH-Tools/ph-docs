# unit_type

Class to manage numeric values with a unit-type (ie: 0.5 IN).

**Source**: `ph_units/unit_type.py`

---

## Unit

A numeric value with a unit-type.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `value` | `float` | — |
| `unit` | `str` | — |

### Methods

#### as_a(unit)

Return a new Unit with the value converted to the specified unit-type.

| Arg | Type | Description |
|-----|------|-------------|
| `unit` | `str` | — |

**Returns**: `Unit`

#### inverse()

Return a new Unit with the inverse value.

**Returns**: `Unit`

---
