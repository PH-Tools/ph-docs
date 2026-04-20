# elec_equip

PHX Passive House Electrical Equipment (Appliances) Classes

**Source**: `PHX/elec_equip.py`

---

## PhxElectricalDevice

Base class for PHX Electrical Equipment (dishwashers, laundry, lighting, etc.)

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `reference_quantity` | — | — |
| `reference_energy_norm` | — | — |
| `quantity` | — | — |

### Methods

#### get_energy_demand()

To allow for subclass custom behavior. Cannot use @property since

#### get_quantity()

To allow for subclass custom behavior. Cannot use @property since

---

## PhxDeviceDishwasher

No description available.

**Inherits from**: `PhxElectricalDevice`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `device_type` | — | — |
| `ihg_utilization_factor` | `float` | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `water_connection` | — | — |
| `capacity_type` | — | — |

---

## PhxDeviceClothesWasher

No description available.

**Inherits from**: `PhxElectricalDevice`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `device_type` | — | — |
| `ihg_utilization_factor` | `float` | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `water_connection` | — | — |

---

## PhxDeviceClothesDryer

No description available.

**Inherits from**: `PhxElectricalDevice`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `device_type` | — | — |
| `ihg_utilization_factor` | `float` | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `dryer_type` | — | — |
| `field_utilization_factor_type` | — | — |

---

## PhxDeviceRefrigerator

No description available.

**Inherits from**: `PhxElectricalDevice`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `device_type` | — | — |

---

## PhxDeviceFreezer

No description available.

**Inherits from**: `PhxElectricalDevice`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `device_type` | — | — |

---

## PhxDeviceFridgeFreezer

No description available.

**Inherits from**: `PhxElectricalDevice`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `device_type` | — | — |

---

## PhxDeviceCooktop

No description available.

**Inherits from**: `PhxElectricalDevice`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `device_type` | — | — |
| `ihg_utilization_factor` | `float` | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `cooktop_type` | — | — |

---

## PhxDeviceMEL

No description available.

**Inherits from**: `PhxElectricalDevice`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `device_type` | — | — |

---

## PhxDeviceLightingInterior

No description available.

**Inherits from**: `PhxElectricalDevice`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `device_type` | — | — |

---

## PhxDeviceLightingExterior

No description available.

**Inherits from**: `PhxElectricalDevice`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `device_type` | — | — |
| `in_conditioned_space` | `bool` | — |

---

## PhxDeviceLightingGarage

No description available.

**Inherits from**: `PhxElectricalDevice`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `device_type` | — | — |
| `in_conditioned_space` | `bool` | — |

---

## PhxDeviceCustomElec

No description available.

**Inherits from**: `PhxElectricalDevice`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `device_type` | — | — |

---

## PhxDeviceCustomLighting

Override so that WUFI output quantity shows up as 1

**Inherits from**: `PhxElectricalDevice`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `device_type` | — | — |

### Methods

#### get_energy_demand()

#### get_quantity()

---

## PhxDeviceCustomMEL

Override so that WUFI output quantity shows up as 1

**Inherits from**: `PhxElectricalDevice`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `device_type` | — | — |

### Methods

#### get_energy_demand()

#### get_quantity()

---

## PhxElevatorHydraulic

No description available.

**Inherits from**: `PhxElectricalDevice`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `device_type` | — | — |

### Methods

#### get_energy_demand()

#### get_quantity()

---

## PhxElevatorGearedTraction

No description available.

**Inherits from**: `PhxElectricalDevice`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `device_type` | — | — |

### Methods

#### get_energy_demand()

#### get_quantity()

---

## PhxElevatorGearlessTraction

No description available.

**Inherits from**: `PhxElectricalDevice`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `device_type` | — | — |

### Methods

#### get_energy_demand()

#### get_quantity()

---

## PhxElectricDeviceCollection

A collection of all the PhxElectricalDevices (laundry, lighting, etc.) in the Zone

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `devices` | — | Returns a list of all the devices in the PhxElectricDeviceCollection, sorted by display_name. |

### Methods

#### device_key_in_collection(_device_key)

Returns True if the key supplied is in the existing device collection.

| Arg | Type | Description |
|-----|------|-------------|
| `_device_key` | — | — |

#### get_equipment_by_key(_key)

| Arg | Type | Description |
|-----|------|-------------|
| `_key` | — | — |

#### add_new_device(_key, _device)

Adds a new PHX Electric-Equipment device to the PhxElectricDeviceCollection.

| Arg | Type | Description |
|-----|------|-------------|
| `_key` | — | The key to use when storing the new electric-equipment |
| `_device` | — | — |

---
