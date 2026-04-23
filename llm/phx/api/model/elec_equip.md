# elec_equip

PHX Passive House electrical equipment (appliance) classes for energy demand and IHG calculations.

**Source**: `PHX/elec_equip.py`

---

## PhxElectricalDevice

Base class for all PHX electrical equipment (dishwashers, laundry, lighting, etc.).

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `reference_quantity` | — | The reference quantity used for energy-demand normalization. |
| `reference_energy_norm` | — | The reference energy normalization standard for the device. |
| `quantity` | — | The number of this device in the zone. |

### Methods

#### get_energy_demand()

To allow for subclass custom behavior. Cannot use @property since

#### get_quantity()

To allow for subclass custom behavior. Cannot use @property since

---

## PhxDeviceDishwasher

A kitchen dishwasher appliance.

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
| `water_connection` | — | The DHW connection type for the dishwasher. |
| `capacity_type` | — | The capacity type classification for the dishwasher. |

---

## PhxDeviceClothesWasher

A clothes washing machine appliance.

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
| `water_connection` | — | The DHW connection type for the clothes washer. |

---

## PhxDeviceClothesDryer

A clothes dryer appliance (electric or gas).

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
| `dryer_type` | — | The dryer type classification (e.g., 4 = condensation dryer). |
| `field_utilization_factor_type` | — | The field utilization factor type (e.g., 1 = timer). |

---

## PhxDeviceRefrigerator

A standalone kitchen refrigerator (no freezer compartment).

**Inherits from**: `PhxElectricalDevice`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `device_type` | — | — |

---

## PhxDeviceFreezer

A standalone kitchen freezer.

**Inherits from**: `PhxElectricalDevice`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `device_type` | — | — |

---

## PhxDeviceFridgeFreezer

A combined refrigerator/freezer unit.

**Inherits from**: `PhxElectricalDevice`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `device_type` | — | — |

---

## PhxDeviceCooktop

A kitchen cooktop appliance (electric or gas).

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
| `cooktop_type` | — | The cooktop fuel type (e.g., 1 = electric). |

---

## PhxDeviceMEL

Miscellaneous electrical loads (MEL) per the Phius protocol.

**Inherits from**: `PhxElectricalDevice`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `device_type` | — | — |

---

## PhxDeviceLightingInterior

Interior lighting per the Phius protocol.

**Inherits from**: `PhxElectricalDevice`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `device_type` | — | — |

---

## PhxDeviceLightingExterior

Exterior lighting per the Phius protocol (outside the thermal envelope).

**Inherits from**: `PhxElectricalDevice`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `device_type` | — | — |
| `in_conditioned_space` | `bool` | — |

---

## PhxDeviceLightingGarage

Garage lighting per the Phius protocol (outside the thermal envelope).

**Inherits from**: `PhxElectricalDevice`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `device_type` | — | — |
| `in_conditioned_space` | `bool` | — |

---

## PhxDeviceCustomElec

A user-defined custom electrical device.

**Inherits from**: `PhxElectricalDevice`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `device_type` | — | — |

---

## PhxDeviceCustomLighting

A user-defined custom lighting device.

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

A user-defined custom miscellaneous electrical load (MEL).

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

A hydraulic elevator, modeled as a custom electrical device for energy demand.

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

A geared-traction elevator, modeled as a custom electrical device for energy demand.

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

A gearless-traction elevator, modeled as a custom electrical device for energy demand.

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

A collection of all the PhxElectricalDevices (laundry, lighting, etc.) in a Zone.

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

Return the device matching the given key, or None if not found.

| Arg | Type | Description |
|-----|------|-------------|
| `_key` | — | The lookup key for the device. |

#### add_new_device(_key, _device)

Adds a new PHX Electric-Equipment device to the PhxElectricDeviceCollection.

| Arg | Type | Description |
|-----|------|-------------|
| `_key` | — | The key to use when storing the new electric-equipment |
| `_device` | — | — |

---
