# CO2_measures

HB-Model Phius REVIVE CO2-Reduction-Measure and Measure-Collection Classes.

**Source**: `honeybee_revive/CO2_measures.py`

---

## CO2ReductionMeasure

A single CO2 reduction measure for Phius REVIVE lifecycle cost analysis.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `name` | — | Display name of the measure. Default: "unnamed_CO2_measure". |
| `year` | — | The year (in the analysis timeline) when this measure is applied. Default: 60. |
| `cost` | — | Total installed cost of the measure in USD. Default: 8500.0. |
| `kg_CO2` | — | Embodied carbon of the measure in kg CO2. Default: 0.0. |
| `country_name` | — | Country of origin for emissions factor lookup. Default: "USA". |
| `labor_fraction` | — | Fraction of cost attributable to labor (0.0 to 1.0). Default: 0.4. |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `unique_id` | `str` | Composite identifier derived from name, type, year, cost, and labor fraction. |
| `measure_type` | `str` | The measure classification: 'PERFORMANCE' or 'NON_PERFORMANCE'. |

---

## CO2ReductionMeasureCollection

An ordered collection of CO2ReductionMeasure objects, keyed by unique_id.

### Methods

#### add_measure(measure)

Add a CO2ReductionMeasure to the collection.

| Arg | Type | Description |
|-----|------|-------------|
| `measure` | `CO2ReductionMeasure` | The measure to add. Keyed by its unique_id. |

**Returns**: `None`

#### measures()

Return all measures in the collection as a list.

**Returns**: `list[CO2ReductionMeasure]`

#### keys()

Return all unique_id keys, sorted by unique_id.

**Returns**: `list[str]`

#### values()

Return all measures, sorted by unique_id.

**Returns**: `list[CO2ReductionMeasure]`

---
