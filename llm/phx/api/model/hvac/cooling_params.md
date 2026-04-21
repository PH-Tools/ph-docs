# cooling_params

PHX cooling parameter classes for heat pump cooling modes.

**Source**: `PHX/cooling_params.py`

---

## PhxCoolingVentilationParams

Parameters for cooling via the ventilation supply air (cooling coil in AHU).

**Inherits from**: `_base.PhxMechanicalDeviceParams`

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `total_system_perf_ratio` | — | Reciprocal of annual COP (kW-input / kW-cooling). |

---

## PhxCoolingRecirculationParams

Parameters for cooling via recirculated air (fan coil, mini-split, etc.).

**Inherits from**: `_base.PhxMechanicalDeviceParams`

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `total_system_perf_ratio` | — | Reciprocal of annual COP (kW-input / kW-cooling). |

---

## PhxCoolingDehumidificationParams

Parameters for active dehumidification cooling.

**Inherits from**: `_base.PhxMechanicalDeviceParams`

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `total_system_perf_ratio` | — | Reciprocal of annual COP (kW-input / kW-cooling). |

---

## PhxCoolingPanelParams

Parameters for radiant cooling panel distribution.

**Inherits from**: `_base.PhxMechanicalDeviceParams`

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `total_system_perf_ratio` | — | Reciprocal of annual COP (kW-input / kW-cooling). |

---

## PhxCoolingParams

Collection of cooling parameters across all four distribution strategies.

---
