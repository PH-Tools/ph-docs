# _base

HBPH Base class for all Constructions

**Source**: `honeybee_energy_ph/_base.py`

---

## _Base

Base class for all honeybee_energy_ph construction objects.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `id_num` | `int` | Numeric ID for serialization ordering. |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `identifier` | — | Get the text string for unique construction identifier. |
| `display_name` | — | Get or set a string for the object name without any character restrictions. |
| `user_data` | `dict` | Get an optional dictionary for additional meta data for this object. |

### Methods

#### set_base_attrs_from_dict(_input_dict)

Set all the Base attribute values from an input dict.

| Arg | Type | Description |
|-----|------|-------------|
| `_input_dict` | `dict[str` | — |

**Returns**: `None`

#### set_base_attrs_from_obj(other)

Sets the base attributes based on another object. Used during __copy__.

| Arg | Type | Description |
|-----|------|-------------|
| `other` | `_Base` | — |

**Returns**: `None`

---
