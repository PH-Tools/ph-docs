# xml_schemas

Conversion Schemas for how to write PH/HB objects to WUFI XML

**Source**: `PHX/xml_schemas.py`

---

## DistributionHeating

No description available.

---

## TempDistributionCooling

Temporary wrapper class for WUFI format Cooling Distribution data.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `ventilation_params` | `sum_params` | — |
| `recirculation_params` | `sum_params` | — |
| `dehumidification_params` | `sum_params` | — |
| `panel_params` | `sum_params` | — |

### Methods

#### sum_params(_cooling_params)

Returns a single HVAC Cooling Params, made from a list of input devices, or None if no devices input.

| Arg | Type | Description |
|-----|------|-------------|
| `_cooling_params` | — | — |

---
