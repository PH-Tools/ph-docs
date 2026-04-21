# _base

PHX Passive House Mechanical Equipment base classes.

**Source**: `PHX/_base.py`

---

## PhxUsageProfile

Flags indicating which building loads a mechanical device serves and its percent coverage.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `space_heating` | — | True if the device used to provide space heating. |
| `dhw_heating` | — | True if the device used to provide domestic hot water heating. |
| `cooling` | — | True if the device used to provide cooling. |
| `ventilation` | — | True if the device used to provide ventilation. |
| `humidification` | — | True if the device used to provide humidification. |
| `dehumidification` | — | True if the device used to provide dehumidification. |

---

## PhxMechanicalDeviceParams

Base parameter set shared by all PHX mechanical devices.

### Methods

#### *staticmethod* safe_add(attr_1, attr_2)

Add two optional numeric values, returning None only if both are falsy.

| Arg | Type | Description |
|-----|------|-------------|
| `attr_1` | — | — |
| `attr_2` | — | — |

---

## PhxMechanicalDevice

Base class for all PHX mechanical devices (heaters, tanks, ventilators, heat pumps, etc.).

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `identifier` | — | — |
| `quantity` | — | — |

### Methods

#### *classmethod* from_kwargs(**kwargs)

Allow for the create of base object from arbitrary kwarg input.

| Arg | Type | Description |
|-----|------|-------------|
| `**kwargs` | — | — |

---
