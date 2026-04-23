# factors

Energy conversion factor (CO2, Source) functions

**Source**: `honeybee_ph_standards/factors.py`

---

## FuelNotAllowedError

Raised when a fuel type is not in the allowed list for a factor collection.

**Inherits from**: `Exception`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `msg` | `format` | Human-readable error message. |

---

## Factor

A site-to-source or site-to-CO2 energy conversion factor.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `fuel_name` | — | Uppercase fuel identifier (e.g. "NATURAL_GAS"). |
| `value` | — | Conversion factor value. |
| `unit` | — | Unit string (e.g. "KWH/KWH" or "G/KWH"). |

---

## FactorCollection

A named collection of energy conversion factors keyed by fuel type.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `name` | — | Collection name (e.g. "Phius 2024 Source Energy"). |
| `factors` | — | The conversion factors in this collection. |

### Methods

#### add_factor(_new_factor)

Add a new factor to the collection. If the factor already exists, update it.

| Arg | Type | Description |
|-----|------|-------------|
| `_new_factor` | `Factor` | — |

**Returns**: `None`

#### get_factor(_fuel_name)

Get a factor by fuel name.

| Arg | Type | Description |
|-----|------|-------------|
| `_fuel_name` | `str` | — |

**Returns**: `Factor`

#### validate_fuel_types(_allowed_fuels)

| Arg | Type | Description |
|-----|------|-------------|
| `_allowed_fuels` | — | — |

---
