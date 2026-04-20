# occupancy

PHX Occupancy (People) Utilization Schedule.

**Source**: `PHX/occupancy.py`

---

## PhxScheduleOccupancy

A PHX Schedule for the Occupancy (People).

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `annual_utilization_factor` | — | Return the annual Utilization Rate (0-1) relative to the entire year (8760 hours) |
| `daily_operating_hours` | — | Return the total Daily Operating Hours (end-hour - start-hour). |
| `annual_operating_hours` | — | Return the total Annual Operating Hours (daily-hours * annual-util-days). |
| `unique_key` | — | Return a key unique to this 'type' (collection of values) of pattern |

### Methods

#### *classmethod* constant_operation()

Return a constant operation (24/7, 365d) schedule.

---
