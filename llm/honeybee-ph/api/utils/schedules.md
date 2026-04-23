# schedules

Utility functions for converting Honeybee schedules into WUFI schedules.

**Source**: `honeybee_ph_utils/schedules.py`

---

## SchedItem

A single period in a WUFI-style four-part ventilation schedule.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `period_speed` | — | Fan speed fraction for this period (0.0-1.0). |
| `period_operating_hours` | — | Hours per day at this speed. |

---

## FourPartSched

A WUFI-style four-part ventilation schedule (high / standard / basic / minimum).

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `high` | — | High-speed period. |
| `standard` | — | Standard-speed period. |
| `basic` | — | Basic-speed period. |
| `minimum` | — | Minimum-speed period. |

---
