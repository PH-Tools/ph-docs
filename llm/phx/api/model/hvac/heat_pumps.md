# heat_pumps

PHX heat pump device classes for heating and cooling.

**Source**: `PHX/heat_pumps.py`

---

## PhxHeatPumpDevice

Base class for all PHX heat pump devices (heating and/or cooling).

**Inherits from**: `_base.PhxMechanicalDevice`

---

## PhxHeatPumpAnnualParams

Parameters for a heat pump characterized by a single annual COP.

**Inherits from**: `_base.PhxMechanicalDeviceParams`

---

## PhxHeatPumpMonthlyParams

Parameters for a heat pump characterized by two rated COP/temperature points.

**Inherits from**: `_base.PhxMechanicalDeviceParams`

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `monthly_COPS` | — | — |
| `monthly_temps` | — | — |
| `COP_1` | — | — |
| `COP_2` | — | — |
| `ambient_temp_1` | — | — |
| `ambient_temp_2` | — | — |

---

## PhxHeatPumpHotWaterParams

Parameters for a dedicated DHW heat pump (heat-pump water heater).

**Inherits from**: `_base.PhxMechanicalDeviceParams`

---

## PhxHeatPumpCombinedParams

Parameters for a combined (space heating + DHW) heat pump.

**Inherits from**: `_base.PhxMechanicalDeviceParams`

---

## PhxHeatPumpAnnual

A heat pump characterized by a single annual COP value.

**Inherits from**: `PhxHeatPumpDevice`

---

## PhxHeatPumpMonthly

A heat pump characterized by two rated COP/temperature operating points.

**Inherits from**: `PhxHeatPumpDevice`

---

## PhxHeatPumpCombined

A combined heat pump serving both space heating and DHW.

**Inherits from**: `PhxHeatPumpDevice`

---

## PhxHeatPumpHotWater

A dedicated DHW heat pump (heat-pump water heater).

**Inherits from**: `PhxHeatPumpDevice`

---
