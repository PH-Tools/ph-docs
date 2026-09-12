# boundarycondition

Extra Boundary Condition objects for Passive House models.

**Source**: `honeybee_energy_ph/boundarycondition.py`

---

## PhAdditionalZone

Boundary condition for surfaces exposed to attached PH zones.

**Inherits from**: `OtherSideTemperature`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `identifier` | — | Unique text identifier. |
| `zone_id_num` | `int` | Numeric ID for the adjacent zone. |
| `zone_name` | — | Name of the adjacent zone. |
| `zone_type` | — | Classification of the adjacent zone. |
| `temperature_reduction_factor` | — | The heating-demand factor, and the fallback for the four optional factors below. Default: 1.0. |
| `heating_load_reduction_factor` | — | Heating-load factor, or None to use the heating-demand factor. Default: None. |
| `cooling_demand_reduction_factor` | — | Cooling-demand factor, or None to use the heating-demand factor. Default: None. |
| `cooling_load_reduction_factor` | — | Cooling-load factor, or None to use the heating-demand factor. Default: None. |
| `passive_cooling_reduction_factor` | — | Passive-cooling factor, or None to use the heating-demand factor. Default: None. |
| `adjacent_zone_temperature_c` | — | Temperature of the adjacent zone (deg. C). Carried for exporters which derive the factors from it rather than taking them directly. Default: None. |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `heating_demand_factor` | `float` | The resolved heating-demand temperature reduction factor. |
| `heating_load_factor` | `float` | The resolved heating-load temperature reduction factor. |
| `cooling_demand_factor` | `float` | The resolved cooling-demand temperature reduction factor. |
| `cooling_load_factor` | `float` | The resolved cooling-load temperature reduction factor. |
| `passive_cooling_factor` | `float` | The resolved passive-cooling temperature reduction factor. |

---
