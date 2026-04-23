# hvac

Valid 'types' for Mech Equipment Options.

**Source**: `PHX/hvac.py`

---

## PhxFuelType

Fuel type for combustion-based heating equipment.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `NATURAL_GAS` | `1` | Natural gas fuel. |
| `OIL` | `2` | Fuel oil. |
| `WOOD_LOG` | `3` | Wood log fuel. |
| `WOOD_PELLET` | `4` | Wood pellet fuel. |

---

## SystemType

Classification of mechanical system types in the energy model.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `ANY` | `0` | Matches any system type (wildcard). |
| `VENTILATION` | `1` | Mechanical ventilation system (HRV/ERV). |
| `ELECTRIC` | `2` | Direct electric heating system. |
| `BOILER` | `3` | Combustion boiler system. |
| `DISTRICT_HEAT` | `4` | District heating connection. |
| `HEAT_PUMP` | `5` | Heat pump system. |
| `USER_DEFINED` | `7` | User-specified custom system. |
| `WATER_STORAGE` | `8` | Hot water storage tank system. |
| `PHOTOVOLTAIC` | `10` | Photovoltaic solar panel system. |

---

## DeviceType

Classification of individual HVAC device types.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `VENTILATION` | `1` | Ventilation unit (HRV/ERV). |
| `ELECTRIC` | `2` | Direct electric heating device. |
| `BOILER` | `3` | Combustion boiler device. |
| `DISTRICT_HEAT` | `4` | District heating device. |
| `HEAT_PUMP` | `5` | Heat pump device. |
| `WATER_STORAGE` | `8` | Hot water storage tank. |
| `PHOTOVOLTAIC` | `10` | Photovoltaic panel array. |

---

## HeatPumpType

Heat pump performance data entry method.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `COMBINED` | `2` | Combined heating and cooling heat pump. |
| `ANNUAL` | `3` | Annual average COP performance data. |
| `RATED_MONTHLY` | `4` | Monthly rated COP performance data. |
| `HOT_WATER` | `5` | Dedicated domestic hot water heat pump. |

---

## CoolingType

Classification of active cooling delivery methods.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `NONE` | `0` | No active cooling. |
| `VENTILATION` | `1` | Cooling via the ventilation supply air. |
| `RECIRCULATION` | `2` | Cooling via recirculated air. |
| `DEHUMIDIFICATION` | `3` | Cooling via dehumidification. |
| `PANEL` | `4` | Cooling via radiant panels. |

---

## PhxHotWaterPipingCalcMethod

Calculation method for hot water distribution piping losses.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `SIMPLIFIED_INDIVIDUAL_PIPES` | `1` | Simplified method specifying individual pipe runs. |
| `SIMPLIFIED_HOT_WATER_CALCULATOR` | `2` | Simplified method using the hot water calculator. |
| `HOT_WATER_PIPING_UNIT_METHOD` | `3` | Detailed method based on per-unit piping lengths. |
| `HOT_WATER_PIPING_FLOOR_METHOD` | `4` | Detailed method based on per-floor piping lengths. |

---

## PhxHotWaterPipingMaterial

Material type for hot water distribution piping.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `COPPER_M` | `1` | Copper pipe, Type M (thin wall). |
| `COPPER_L` | `2` | Copper pipe, Type L (medium wall). |
| `COPPER_K` | `3` | Copper pipe, Type K (thick wall). |
| `CPVC_CTS_SDR` | `4` | CPVC pipe, CTS SDR rating. |
| `CPVC_SCH_40` | `5` | CPVC pipe, Schedule 40. |
| `PEX` | `6` | Cross-linked polyethylene (PEX) pipe. |
| `PE` | `7` | Polyethylene (PE) pipe. |
| `PEX_CTS_SDR` | `8` | PEX pipe, CTS SDR rating. |

---

## PhxHotWaterPipingInchDiameterType

Nominal pipe diameter in inches for hot water piping.

**Inherits from**: `Enum`

---

## PhxHotWaterInputOptions

Input method for hot water storage tank loss specification.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `SPEC_TOTAL_LOSSES` | `1` | Specify total storage losses directly. |
| `SPEC_STANDBY_LOSSES` | `2` | Specify standby losses from the tank data sheet. |
| `TOTAL_LOSSES` | `3` | Use calculated total losses. |

---

## PhxHotWaterTankType

Hot water storage tank usage classification.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `NONE` | `0` | No storage tank. |
| `DHW_AND_HEATING` | `1` | Tank serves both domestic hot water and space heating. |
| `DHW_ONLY` | `2` | Tank serves domestic hot water only. |

---

## PhxHotWaterSelectionUnitsOrFloors

Selection basis for hot water piping calculation scope.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `PH_CASE` | `1` | Use the PH case default (number of dwelling units). |
| `USER_DETERMINED` | `2` | User specifies the number of units or floors. |

---

## PhxExhaustVentType

Type of dedicated exhaust ventilation device.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `DRYER` | `1` | Clothes dryer exhaust. |
| `KITCHEN_HOOD` | `2` | Kitchen range hood exhaust. |
| `USER_DEFINED` | `3` | User-specified exhaust device. |

---

## PhxVentDuctType

Ventilation duct direction classification.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `SUPPLY` | `1` | Supply air duct (outdoor air to rooms). |
| `EXHAUST` | `2` | Exhaust air duct (rooms to outdoors). |

---

## PhxSupportiveDeviceType

Type of supportive (auxiliary) mechanical device.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `HEAT_CIRCULATING_PUMP` | `4` | Circulation pump for the heating loop. |
| `DHW_CIRCULATING_PUMP` | `6` | Recirculation pump for the DHW loop. |
| `DHW_STORAGE_LOAD_PUMP` | `7` | Pump loading the DHW storage tank. |
| `OTHER` | `10` | Other auxiliary device. |

---

## PhxSummerBypassMode

Summer bypass mode for the heat recovery ventilator.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `NONE` | `1` | No summer bypass. |
| `TEMP_CONTROLLED` | `2` | Bypass activated by temperature differential. |
| `ENTHALPY_CONTROLLED` | `3` | Bypass activated by enthalpy differential. |
| `ALWAYS` | `4` | Bypass always active in summer. |

---

## PhxNighttimeVentilationControl

Control strategy for nighttime ventilation cooling.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `TEMPERATURE_CONTROLLED` | `1` | Nighttime ventilation activated by temperature. |
| `HUMIDITY_CONTROLLED` | `2` | Nighttime ventilation activated by humidity. |

---
