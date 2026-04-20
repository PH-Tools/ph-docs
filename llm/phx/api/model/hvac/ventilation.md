# ventilation

PHX Mechanical Ventilation Devices

**Source**: `PHX/ventilation.py`

---

## PhxDeviceVentilation

No description available.

**Inherits from**: `_base.PhxMechanicalDevice`

---

## PhxDeviceVentilatorParams

No description available.

**Inherits from**: `_base.PhxMechanicalDeviceParams`

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `sensible_heat_recovery` | — | — |
| `latent_heat_recovery` | — | — |
| `quantity` | — | — |
| `electric_efficiency` | — | — |
| `frost_protection_reqd` | — | — |
| `temperature_below_defrost_used` | — | — |

---

## PhxDeviceVentilator

No description available.

**Inherits from**: `PhxDeviceVentilation`

---

## PhxExhaustVentilatorParams

No description available.

**Inherits from**: `_base.PhxMechanicalDeviceParams`

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `exhaust_type` | — | — |
| `annual_runtime_minutes` | — | — |
| `exhaust_flow_rate_m3h` | — | — |

---

## PhxExhaustVentilatorBase

Base class for all Exhaust Ventilation.

**Inherits from**: `_base.PhxMechanicalDevice`

---

## PhxExhaustVentilatorRangeHood

No description available.

**Inherits from**: `PhxExhaustVentilatorBase`

---

## PhxExhaustVentilatorDryer

No description available.

**Inherits from**: `PhxExhaustVentilatorBase`

---

## PhxExhaustVentilatorUserDefined

No description available.

**Inherits from**: `PhxExhaustVentilatorBase`

---
