# _base

HBE-PH Appliance (Elec Equip.) Base Class

**Source**: `honeybee_energy_ph/_base.py`

---

## _Base

Base class for any HB-Energy-PH appliance / electric equipment object.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `user_data` | `Dict` | Optional metadata dictionary. |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `identifier` | `str` | Unique identifier string (UUID). |
| `display_name` | — | Get or set a string for the object name without any character restrictions. |
| `identifier_short` | `str` | First segment of the UUID (for display). |

---
