# fuels

HB-Model Phius REVIVE Fuel types and Fuel-Collection Classes.

**Source**: `honeybee_revive/fuels.py`

---

## Fuel

A fuel type with purchase, sale, and base pricing for REVIVE cost analysis.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `purchase_price_per_kwh` | — | Purchase price per kWh in USD. Default: 0.0. |
| `sale_price_per_kwh` | — | Sale (export) price per kWh in USD. Default: 0.0. |
| `annual_base_price` | — | Fixed annual base price in USD. Default: 0.0. |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `unique_id` | `str` | Composite identifier derived from fuel type and pricing. |
| `fuel_type` | `str` | The fuel classification: 'ELECTRICITY' or 'NATURAL_GAS'. |

---

## FuelCollection

An ordered collection of Fuel objects, keyed by fuel_type.

### Methods

#### add_fuel(fuel)

Add a Fuel to the collection, keyed by its fuel_type.

| Arg | Type | Description |
|-----|------|-------------|
| `fuel` | `Fuel` | The fuel to add. |

**Returns**: `None`

#### get_fuel(fuel_type)

Return a Fuel by its fuel_type key.

| Arg | Type | Description |
|-----|------|-------------|
| `fuel_type` | `str` | The fuel type to look up (e.g. "ELECTRICITY"). |

**Returns**: `Fuel`

#### fuels()

Return all fuels in the collection as a list.

**Returns**: `list[Fuel]`

#### keys()

Return all fuel_type keys, sorted alphabetically.

**Returns**: `list[str]`

#### values()

Return all fuels, sorted by fuel_type.

**Returns**: `list[Fuel]`

#### *classmethod* with_default_fuels()

Create a FuelCollection pre-populated with default electricity and natural gas pricing.

**Returns**: `FuelCollection`

---
