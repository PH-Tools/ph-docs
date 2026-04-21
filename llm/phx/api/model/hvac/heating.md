# heating

PHX mechanical heating device classes.

**Source**: `PHX/heating.py`

---

## PhxHeatingDevice

Base class for all PHX heating devices (electric, boiler, district heat).

**Inherits from**: `_base.PhxMechanicalDevice`

---

## PhxHeaterElectricParams

Parameters for an electric resistance heater (no additional fields beyond base).

**Inherits from**: `_base.PhxMechanicalDeviceParams`

---

## PhxHeaterElectric

An electric resistance heater for space heating and/or DHW.

**Inherits from**: `PhxHeatingDevice`

---

## PhxHeaterBoilerFossilParams

Performance parameters for a fossil-fuel boiler (gas, oil, propane).

**Inherits from**: `_base.PhxMechanicalDeviceParams`

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `fuel` | — | — |
| `condensing` | — | — |
| `in_conditioned_space` | — | — |
| `effic_at_30_percent_load` | — | — |
| `effic_at_nominal_load` | — | — |
| `avg_rtrn_temp_at_30_percent_load` | — | — |
| `avg_temp_at_70C_55C` | — | — |
| `avg_temp_at_55C_45C` | — | — |
| `avg_temp_at_32C_28C` | — | — |
| `standby_loss_at_70C` | — | — |
| `rated_capacity` | — | — |

---

## PhxHeaterBoilerWoodParams

Performance parameters for a wood-fired boiler (log, pellet).

**Inherits from**: `_base.PhxMechanicalDeviceParams`

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `fuel` | — | — |

---

## PhxHeaterBoilerFossil

A fossil-fuel boiler (gas, oil, propane) for space heating and/or DHW.

**Inherits from**: `PhxHeatingDevice`

---

## PhxHeaterBoilerWood

A wood-fired boiler (log or pellet) for space heating and/or DHW.

**Inherits from**: `PhxHeatingDevice`

---

## PhxHeaterDistrictHeatParams

Parameters for a district heat connection (no additional fields beyond base).

**Inherits from**: `_base.PhxMechanicalDeviceParams`

---

## PhxHeaterDistrictHeat

A district heat connection for space heating and/or DHW.

**Inherits from**: `PhxHeatingDevice`

---
