# fuel

Fuel Types and cost related data.

**Source**: `ph_adorb/fuel.py`

---

## PhAdorbFuelType

Classification of energy fuel types.

**Inherits from**: `str`, `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `ELECTRICITY` | `'Electricity'` | Grid-supplied electricity. |
| `NATURAL_GAS` | `'Natural Gas'` | Piped natural gas. |

---

## PhAdorbFuel

Pricing and usage data for a single fuel type.

**Inherits from**: `BaseModel`

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `name` | — | Return the display name of the fuel type. |

---
