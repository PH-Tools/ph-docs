# water

PHX domestic hot water (DHW) storage tank device classes.

**Source**: `PHX/water.py`

---

## PhxHotWaterDevice

Base class for all PHX DHW devices. Automatically sets dhw_heating usage on init.

**Inherits from**: `_base.PhxMechanicalDevice`

---

## PhxHotWaterTankParams

Performance and geometry parameters for a DHW storage tank.

**Inherits from**: `_base.PhxMechanicalDeviceParams`

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `tank_type` | — | — |
| `input_option` | — | — |
| `in_conditioned_space` | — | — |
| `solar_connection` | — | — |
| `solar_losses` | — | — |
| `storage_loss_rate` | — | — |
| `storage_capacity` | — | — |
| `standby_losses` | — | — |
| `standby_fraction` | — | — |
| `room_temp` | — | — |
| `water_temp` | — | — |

---

## PhxHotWaterTank

A DHW storage tank with standby and solar loss parameters.

**Inherits from**: `PhxHotWaterDevice`

---
