# io_cooling_units

Controller Class for the PHPP "Cooling Units" worksheet.

**Source**: `PHX/io_cooling_units.py`

---

## CoolingUnitData

Convenience class for organizing and cleaning the data.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `device_type_name` | — | — |

### Methods

#### *classmethod* from_PHPP_data(_data, _seer_unit)

Clean up the data coming in from PHPP

| Arg | Type | Description |
|-----|------|-------------|
| `_data` | — | — |
| `_seer_unit` | — | — |

---

## SupplyAir

Reads supply-air cooling unit data from the PHPP 'Cooling Units' worksheet.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |

### Methods

#### get_phpp_data()

---

## RecirculationAir

Reads recirculation-air cooling unit data from the PHPP 'Cooling Units' worksheet.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |

### Methods

#### get_phpp_data()

---

## Dehumidification

Reads dehumidification cooling unit data from the PHPP 'Cooling Units' worksheet.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |

### Methods

#### get_phpp_data()

---

## Panel

Reads panel cooling unit data from the PHPP 'Cooling Units' worksheet.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |

### Methods

#### get_phpp_data()

---

## CoolingUnits

IO Controller for the PHPP Cooling Units worksheet.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |
| `supply_air` | `SupplyAir` | — |
| `recirculation_air` | `RecirculationAir` | — |
| `dehumidification` | `Dehumidification` | — |
| `panel` | `Panel` | — |

### Methods

#### get_cooling_system_data()

---
