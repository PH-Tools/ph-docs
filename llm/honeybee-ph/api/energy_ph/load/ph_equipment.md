# ph_equipment

HB-PH Electric Equipment and Appliances.

**Source**: `honeybee_energy_ph/ph_equipment.py`

---

## PhEquipment

Base class for PH appliances with common energy and scheduling attributes.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `host` | — | — |
| `equipment_type` | — | Class name used for serialization dispatch. |
| `display_name` | `str` | — |
| `comment` | `str` | Optional user comment. |
| `reference_quantity` | `int` | Reference quantity type (2 = zone occupants). |
| `quantity` | `int` | Number of this appliance installed. |
| `in_conditioned_space` | `bool` | Whether the appliance is inside the thermal envelope. Default: True. |
| `reference_energy_norm` | `int` | Energy normalization period (2 = year). |
| `energy_demand` | `float` | Annual energy demand (kWh). |
| `energy_demand_per_use` | `float` | Energy per use cycle (kWh/use). |
| `combined_energy_factor` | `float` | Combined energy factor (CEF). |
| `ihg_utilization_factor` | `float` | Fraction of energy that becomes internal heat gain inside the envelope (0.0-1.0). Default: 1.0. |

### Methods

#### apply_default_attr_values(_defaults)

Sets all the object attributes to default values, as specified in a "defaults" dict.

| Arg | Type | Description |
|-----|------|-------------|
| `_defaults` | `dict[str` | — |

**Returns**: `None`

#### base_attrs_from_dict(_obj, _input_dict)

Set the base object attributes from a dictionary

| Arg | Type | Description |
|-----|------|-------------|
| `_obj` | `PhEquipment` | The PH Equipment to set the attributes of. |
| `_input_dict` | `dict[str` | The dictionary to get the attribute values from. |

**Returns**: `None`

#### merge(other, weighting_1, weighting_2)

"Merge together two pieces of PhEquipment.

| Arg | Type | Description |
|-----|------|-------------|
| `other` | `PhEquipment` | the PhEquipment to merge with. |
| `weighting_1` | `float` | Optional weighting factor to apply to the 'self' equipment values. |
| `weighting_2` | `float` | Optional weighting factor to apply to the 'other' equipment values. |

**Returns**: `PhEquipment`

#### annual_energy_kWh(*args, **kwargs)

Returns the annual energy use (kWh) of the equipment.

| Arg | Type | Description |
|-----|------|-------------|
| `*args` | `*Any` | — |
| `**kwargs` | `*Any` | — |

**Returns**: `float`

#### annual_avg_wattage(_schedule, *args, **kwargs)

Returns the annual average wattage of the equipment.

| Arg | Type | Description |
|-----|------|-------------|
| `_schedule` | `ScheduleRuleset | None` | — |
| `*args` | `*Any` | — |
| `**kwargs` | `**Any` | — |

**Returns**: `float`

#### *classmethod* phius_default()

Return the default instance of the object.

**Returns**: `'PhEquipment'`

#### *classmethod* phi_default()

Return the default instance of the object.

**Returns**: `'PhEquipment'`

---

## PhDishwasher

PH kitchen dishwasher appliance.

**Inherits from**: `PhEquipment`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `ihg_utilization_factor` | `float` | — |
| `capacity_type` | `int` | Capacity classification. Default: 1. |
| `capacity` | `int` | Place-setting capacity. Default: 12. |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `water_connection` | — | — |

### Methods

#### annual_energy_kWh(*args, **kwargs)

| Arg | Type | Description |
|-----|------|-------------|
| `*args` | `*Any` | — |
| `**kwargs` | `**Any` | — |

**Returns**: `float`

---

## PhClothesWasher

PH laundry clothes washer appliance.

**Inherits from**: `PhEquipment`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `ihg_utilization_factor` | `float` | — |
| `capacity` | `float` | Washer capacity (cu ft). Default: 0.1274. |
| `modified_energy_factor` | `float` | Modified energy factor. Default: 2.7. |
| `utilization_factor` | `int` | Utilization factor. Default: 1. |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `water_connection` | — | — |

### Methods

#### annual_energy_kWh(*args, **kwargs)

| Arg | Type | Description |
|-----|------|-------------|
| `*args` | `*Any` | — |
| `**kwargs` | `**Any` | — |

**Returns**: `float`

---

## PhClothesDryer

PH laundry clothes dryer appliance.

**Inherits from**: `PhEquipment`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `ihg_utilization_factor` | `float` | — |
| `gas_consumption` | `int` | Gas consumption rate. Default: 0. |
| `gas_efficiency_factor` | `float` | Gas efficiency factor. Default: 2.67. |
| `field_utilization_factor_type` | `int` | Utilization factor type. Default: 1. |
| `field_utilization_factor` | `float` | Field utilization factor. Default: 1.18. |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `dryer_type` | — | — |

### Methods

#### annual_energy_kWh(*args, **kwargs)

Returns the annual energy use (kWh) of the equipment.

| Arg | Type | Description |
|-----|------|-------------|
| `*args` | `*Any` | — |
| `**kwargs` | `**Any` | — |

**Returns**: `float`

---

## PhRefrigerator

PH kitchen refrigerator (standalone, no freezer).

**Inherits from**: `PhEquipment`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |

### Methods

#### annual_energy_kWh(*args, **kwargs)

| Arg | Type | Description |
|-----|------|-------------|
| `*args` | `*Any` | — |
| `**kwargs` | `**Any` | — |

**Returns**: `float`

---

## PhFreezer

PH kitchen standalone freezer.

**Inherits from**: `PhEquipment`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |

### Methods

#### annual_energy_kWh(*args, **kwargs)

| Arg | Type | Description |
|-----|------|-------------|
| `*args` | `*Any` | — |
| `**kwargs` | `**Any` | — |

**Returns**: `float`

---

## PhFridgeFreezer

PH kitchen combination refrigerator/freezer.

**Inherits from**: `PhEquipment`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |

### Methods

#### annual_energy_kWh(*args, **kwargs)

| Arg | Type | Description |
|-----|------|-------------|
| `*args` | `*Any` | — |
| `**kwargs` | `**Any` | — |

**Returns**: `float`

---

## PhCooktop

PH kitchen cooktop/range appliance.

**Inherits from**: `PhEquipment`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `ihg_utilization_factor` | `float` | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `cooktop_type` | — | — |

### Methods

#### annual_energy_kWh(*args, **kwargs)

Return annual energy consumption [kWh] for a single dwelling.

| Arg | Type | Description |
|-----|------|-------------|
| `*args` | `*Any` | — |
| `**kwargs` | `**Any` | — |

**Returns**: `float`

---

## PhPhiusMEL

Phius miscellaneous electrical loads (MELs) per RESNET.

**Inherits from**: `PhEquipment`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |

### Methods

#### annual_energy_kWh(*args, **kwargs)

Return annual energy consumption [kWh] for a single dwelling.

| Arg | Type | Description |
|-----|------|-------------|
| `*args` | `*Any` | — |
| `**kwargs` | `**Any` | — |

**Returns**: `float`

---

## PhPhiusLightingInterior

Phius interior lighting load per RESNET.

**Inherits from**: `PhEquipment`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `frac_high_efficiency` | `int` | Fraction of high-efficiency fixtures. Default: 1. |

### Methods

#### annual_energy_kWh(*args, **kwargs)

Return the annual energy consumption [kWh] for a single dwelling.

| Arg | Type | Description |
|-----|------|-------------|
| `*args` | `*Any` | — |
| `**kwargs` | `**Any` | — |

**Returns**: `float`

---

## PhPhiusLightingExterior

Phius exterior lighting load per RESNET.

**Inherits from**: `PhEquipment`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `frac_high_efficiency` | `int` | Fraction of high-efficiency fixtures. Default: 1. |
| `in_conditioned_space` | `bool` | — |

### Methods

#### annual_energy_kWh(*args, **kwargs)

Return the annual energy consumption [kWh] for a single dwelling.

| Arg | Type | Description |
|-----|------|-------------|
| `*args` | `*Any` | — |
| `**kwargs` | `**Any` | — |

**Returns**: `float`

---

## PhPhiusLightingGarage

Phius garage lighting load per RESNET.

**Inherits from**: `PhEquipment`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `frac_high_efficiency` | `int` | Fraction of high-efficiency fixtures. Default: 1. |
| `in_conditioned_space` | `bool` | — |

### Methods

#### annual_energy_kWh(*args, **kwargs)

Return the annual energy consumption [kWh] for a single dwelling.

| Arg | Type | Description |
|-----|------|-------------|
| `*args` | `*Any` | — |
| `**kwargs` | `**Any` | — |

**Returns**: `float`

---

## PhCustomAnnualElectric

User-defined annual electric equipment load.

**Inherits from**: `PhEquipment`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |

### Methods

#### annual_energy_kWh(*args, **kwargs)

| Arg | Type | Description |
|-----|------|-------------|
| `*args` | `*Any` | — |
| `**kwargs` | `**Any` | — |

**Returns**: `float`

---

## PhCustomAnnualLighting

User-defined annual lighting load.

**Inherits from**: `PhEquipment`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |

### Methods

#### annual_energy_kWh(*args, **kwargs)

| Arg | Type | Description |
|-----|------|-------------|
| `*args` | `*Any` | — |
| `**kwargs` | `**Any` | — |

**Returns**: `float`

---

## PhCustomAnnualMEL

User-defined annual miscellaneous electric load.

**Inherits from**: `PhEquipment`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |

### Methods

#### annual_energy_kWh(*args, **kwargs)

| Arg | Type | Description |
|-----|------|-------------|
| `*args` | `*Any` | — |
| `**kwargs` | `**Any` | — |

**Returns**: `float`

---

## PhElevatorHydraulic

Hydraulic elevator (up to ~6 stories) per Phius/RESNET.

**Inherits from**: `PhEquipment`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `comment` | `str` | — |
| `quantity` | `int` | — |

### Methods

#### set_energy_demand(_num_dwellings)

Set the annual energy demand (kWh) based on the number of dwelling units

| Arg | Type | Description |
|-----|------|-------------|
| `_num_dwellings` | — | — |

#### annual_energy_kWh(*args, **kwargs)

Returns the annual energy use (kWh) of the equipment.

| Arg | Type | Description |
|-----|------|-------------|
| `*args` | `*Any` | — |
| `**kwargs` | `**Any` | — |

**Returns**: `float`

---

## PhElevatorGearedTraction

Geared traction elevator (7-20 stories) per Phius/RESNET.

**Inherits from**: `PhEquipment`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `comment` | `str` | — |
| `quantity` | `int` | — |

### Methods

#### set_energy_demand(_num_dwellings)

Set the annual energy demand (kWh) based on the number of dwelling units

| Arg | Type | Description |
|-----|------|-------------|
| `_num_dwellings` | — | — |

#### annual_energy_kWh(*args, **kwargs)

Returns the annual energy use (kWh) of the equipment.

| Arg | Type | Description |
|-----|------|-------------|
| `*args` | `*Any` | — |
| `**kwargs` | `**Any` | — |

**Returns**: `float`

---

## PhElevatorGearlessTraction

Gearless traction elevator (21+ stories) per Phius/RESNET.

**Inherits from**: `PhEquipment`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | `str` | — |
| `comment` | `str` | — |
| `quantity` | `int` | — |

### Methods

#### set_energy_demand(_num_dwellings)

Set the annual energy demand (kWh) based on the number of dwelling units

| Arg | Type | Description |
|-----|------|-------------|
| `_num_dwellings` | — | — |

#### annual_energy_kWh(*args, **kwargs)

Returns the annual energy use (kWh) of the equipment.

| Arg | Type | Description |
|-----|------|-------------|
| `*args` | `*Any` | — |
| `**kwargs` | `**Any` | — |

**Returns**: `float`

---

## PhEquipmentBuilder

Constructor class for PH Equipment objects

---

## PhEquipmentCollection

A collection of PH appliances stored on a Honeybee-Room's energy properties.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `host` | `ElectricEquipmentPhProperties | None` | — |

### Methods

#### items()

**Returns**: `ItemsView[str, PhEquipment]`

#### keys()

**Returns**: `KeysView[str]`

#### values()

**Returns**: `ValuesView[PhEquipment]`

#### add_equipment(_new_equipment, _key)

Adds a new piece of Ph-Equipment to the collection.

| Arg | Type | Description |
|-----|------|-------------|
| `_new_equipment` | `PhEquipment` | The new Ph Equipment to add to the set. |
| `_key` | `Any` | Optional key to use for storing the equipment. If None, the equipment's "identifier" will be used as the key. |

**Returns**: `None`

#### remove_all_equipment()

Reset the Collection to an empty set.

**Returns**: `None`

#### total_collection_wattage(_hb_room)

Returns the total annual-average-wattage of the appliances.

| Arg | Type | Description |
|-----|------|-------------|
| `_hb_room` | `room.Room` | The reference Honeybee-Room to get occupancy from. |

**Returns**: `float`

---
