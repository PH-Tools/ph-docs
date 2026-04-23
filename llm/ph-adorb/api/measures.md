# measures

CO2 Reduction Measures and Collection

**Source**: `ph_adorb/measures.py`

---

## CO2MeasureType

Classification of CO2 reduction measures.

**Inherits from**: `str`, `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `PERFORMANCE` | `'PERFORMANCE'` | Measures that improve building energy performance (e.g., insulation upgrades). |
| `NON_PERFORMANCE` | `'NON_PERFORMANCE'` | Measures that reduce carbon without affecting energy use (e.g., low-carbon materials). |

---

## PhAdorbCO2ReductionMeasure

A single CO2 reduction measure with cost and carbon data.

**Inherits from**: `BaseModel`

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `material_fraction` | — | Fraction of cost attributable to materials (1 - labor_fraction). |

---

## PhAdorbCO2MeasureCollection

A dict-backed, iterable collection of CO2 reduction measures.

**Inherits from**: `BaseModel`

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `performance_measures` | — | Return a collection of PERFORMANCE measures. |
| `nonperformance_measures` | — | Return a collection of NON-PERFORMANCE measures. |

### Methods

#### add_measure(factor)

Add a CO2 reduction measure to the collection.

| Arg | Type | Description |
|-----|------|-------------|
| `factor` | — | — |

#### get_measure(key)

Return a measure by name.

| Arg | Type | Description |
|-----|------|-------------|
| `key` | — | — |

#### keys()

Return measure names sorted by year.

#### values()

Return measures sorted by year.

---
