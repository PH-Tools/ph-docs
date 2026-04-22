# metr_converter

Schema lookup: finds the appropriate METr JSON schema function for a given PHX object.

**Source**: `PHX/metr_converter.py`

---

## NoMETrSchemaFoundError

Raised when no METr JSON schema is found for a given PHX object.

**Inherits from**: `Exception`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `message` | — | Detailed error describing the missing schema, object type, and module searched. |

---
