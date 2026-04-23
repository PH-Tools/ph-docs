# ventilation

PHX mechanical ventilation device classes.

**Source**: `PHX/ventilation.py`

---

## PhxDeviceVentilation

Base class for all PHX balanced ventilation devices (HRV/ERV).

**Inherits from**: `_base.PhxMechanicalDevice`

---

## PhxDeviceVentilatorParams

Performance parameters for a balanced ventilation unit (HRV/ERV).

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

A balanced ventilation unit (HRV or ERV) with sensible/latent recovery.

**Inherits from**: `PhxDeviceVentilation`

---

## PhxExhaustVentilatorParams

Performance parameters for a point-exhaust ventilator (range hood, dryer, etc.).

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

A kitchen range-hood exhaust ventilator.

**Inherits from**: `PhxExhaustVentilatorBase`

---

## PhxExhaustVentilatorDryer

A clothes-dryer exhaust ventilator.

**Inherits from**: `PhxExhaustVentilatorBase`

---

## PhxExhaustVentilatorUserDefined

A user-defined point-exhaust ventilator.

**Inherits from**: `PhxExhaustVentilatorBase`

---
