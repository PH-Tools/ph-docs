# CO2_measures

HB-Model Phius REVIVE CO2-Reduction-Measure and Measure-Collection Classes.

**Source**: `honeybee_revive/CO2_measures.py`

---

## CO2ReductionMeasure

No description available.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `name` | — | — |
| `year` | — | — |
| `cost` | — | — |
| `kg_CO2` | — | — |
| `country_name` | — | — |
| `labor_fraction` | — | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `unique_id` | `str` | — |
| `measure_type` | `str` | — |

---

## CO2ReductionMeasureCollection

No description available.

### Methods

#### add_measure(measure)

| Arg | Type | Description |
|-----|------|-------------|
| `measure` | `CO2ReductionMeasure` | — |

**Returns**: `None`

#### measures()

**Returns**: `list[CO2ReductionMeasure]`

#### keys()

**Returns**: `list[str]`

#### values()

**Returns**: `list[CO2ReductionMeasure]`

---
