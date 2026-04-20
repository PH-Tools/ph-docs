# fuels

HB-Model Phius REVIVE Fuel types and Fuel-Collection Classes.

**Source**: `honeybee_revive/fuels.py`

---

## Fuel

No description available.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `purchase_price_per_kwh` | — | — |
| `sale_price_per_kwh` | — | — |
| `annual_base_price` | — | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `unique_id` | `str` | — |
| `fuel_type` | `str` | — |

---

## FuelCollection

No description available.

### Methods

#### add_fuel(fuel)

| Arg | Type | Description |
|-----|------|-------------|
| `fuel` | `Fuel` | — |

**Returns**: `None`

#### get_fuel(fuel_type)

| Arg | Type | Description |
|-----|------|-------------|
| `fuel_type` | `str` | — |

**Returns**: `Fuel`

#### fuels()

**Returns**: `list[Fuel]`

#### keys()

**Returns**: `list[str]`

#### values()

**Returns**: `list[Fuel]`

#### *classmethod* with_default_fuels()

**Returns**: `FuelCollection`

---
