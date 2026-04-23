# _base

Base class for Honeybee-PH Objects with some generic methods and attributes.

**Source**: `honeybee_ph/_base.py`

---

## _Base

Base class for all Honeybee-PH model objects.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `user_data` | `Dict` | Arbitrary user-supplied metadata dictionary. |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `identifier` | `str` | The globally unique identifier string for this object. |
| `display_name` | `str` | User-facing name for this object, without character restrictions. |
| `identifier_short` | `str` | The first segment of the identifier (before the first hyphen). |

### Methods

#### set_base_attrs_from_source(_source)

Copy identifier, user_data, and display_name from another _Base instance.

| Arg | Type | Description |
|-----|------|-------------|
| `_source` | `_Base` | The source object to copy base attributes from. |

**Returns**: `_Base`

---
