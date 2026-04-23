# variant

A Building Variant with all of its relevant data, and related functions.

**Source**: `ph_adorb/variant.py`

---

## PhAdorbVariant

A single variant of a building design with all data needed for ADORB cost calculation.

**Inherits from**: `BaseModel`

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `total_purchased_electricity_kwh` | — | Return the total annual purchased electricity in KWH. |
| `all_carbon_measures` | — | Return a collection of all the Carbon Measures. |
| `performance_measure_collection` | — | Return a collection of only the Performance Carbon Measures. |
| `nonperformance_carbon_measures` | — | Return a collection of only the Non-Performance Carbon Measures. |

---
