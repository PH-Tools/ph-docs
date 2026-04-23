# ventilation

PHX Fresh-Air Ventilation Utilization Schedule.

**Source**: `PHX/ventilation.py`

---

## Vent_OperatingPeriod

A single ventilation operating period with duration and fan speed.

---

## Vent_UtilPeriods

Collection of four ventilation operating periods at descending speed levels.

---

## PhxScheduleVentilation

Fresh-air ventilation utilization schedule with multi-speed operating periods.

### Methods

#### force_max_utilization_hours(_max_hours, _tol)

Clamp total daily operating hours to a maximum by adjusting the high-speed period.

| Arg | Type | Description |
|-----|------|-------------|
| `_max_hours` | — | Maximum allowed total daily hours. Default: 24.0. |
| `_tol` | — | Rounding precision (decimal places). Default: 2. |

---
