# lighting

PHX Lighting Utilization Schedule.

**Source**: `PHX/lighting.py`

---

## PhxScheduleLighting

A PHX Schedule for the Lighting.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `annual_utilization_factor` | — | Return the annual Utilization Rate (0-1) relative to the entire year (8760 hours) |
| `daily_operating_hours` | — | Return the total Daily Operating Hours (end-hour - start-hour). |
| `annual_operating_hours` | — | Return the total Annual Operating Hours (daily-hours * annual-util-days). |
| `unique_key` | — | Return a key unique to this 'type' (collection of values) of pattern |
| `full_load_lighting_hours` | — | — |

### Methods

#### *classmethod* from_annual_operating_hours(_annual_operating_hours)

| Arg | Type | Description |
|-----|------|-------------|
| `_annual_operating_hours` | — | — |

---
