# _base

PHX Passive House Mechanical Equipment Classes

**Source**: `PHX/_base.py`

---

## PhxUsageProfile

Is the device used to provide...

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

Base class PHX MechanicalEquipment Params

### Methods

#### *staticmethod* safe_add(attr_1, attr_2)

| Arg | Type | Description |
|-----|------|-------------|
| `attr_1` | — | — |
| `attr_2` | — | — |

---

## PhxMechanicalDevice

Base class for PHX Mechanical Devices (heaters, tanks, ventilators, etc...)

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
