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
| `temperature_reduction_factor` | — | Factor applied to the temperature difference across this boundary. Default: 1.0. |

---
