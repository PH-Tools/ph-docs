# collection

PHX Mechanical Collection Classes.

**Source**: `PHX/collection.py`

---

## NoDeviceFoundError

No description available.

**Inherits from**: `Exception`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `msg` | — | — |

---

## NoSupportiveDeviceUnitFoundError

No description available.

**Inherits from**: `Exception`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `msg` | — | — |

---

## NoRenewableDeviceUnitFoundError

No description available.

**Inherits from**: `Exception`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `msg` | — | — |

---

## PhxZoneCoverage

Percentage of the building load-type covered by the subsystem.

---

## PhxRenewableDeviceCollection

A Collection of PHX Renewable Energy Devices.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `devices` | — | — |
| `pv_devices` | — | Return a List of all the Photovoltaic devices |

### Methods

#### clear_all_devices()

Reset the collection to an empty dictionary.

#### device_in_collection(_device_key)

Return True if a PHX Renewable Device with the matching key is in the collection.

| Arg | Type | Description |
|-----|------|-------------|
| `_device_key` | — | — |

#### get_device_by_key(_key)

Returns the PHX Renewable Device with the matching key, or None if not found.

| Arg | Type | Description |
|-----|------|-------------|
| `_key` | — | The key to search the collection for. |

#### get_device_by_id(_id_num)

Returns a PHX Renewable Device from the collection which has a matching id-num.

| Arg | Type | Description |
|-----|------|-------------|
| `_id_num` | — | The Renewable Device id-number to search for. |

#### add_new_device(_key, _d)

Adds a new PHX Supportive Device to the collection.

| Arg | Type | Description |
|-----|------|-------------|
| `_key` | — | The key to use when storing the new device |
| `_d` | — | — |

#### group_devices_by_identifier(_devices)

| Arg | Type | Description |
|-----|------|-------------|
| `_devices` | — | — |

#### merge_group_of_devices(_groups)

Merge a group of Dict of device-groups together into a single device.

| Arg | Type | Description |
|-----|------|-------------|
| `_groups` | — | — |

#### merge_all_devices()

Merge all the devices in the collection together by identifier.

---

## PhxSupportiveDeviceCollection

A Collection of PHX Supportive Devices.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `devices` | — | — |
| `heat_circulating_pumps` | — | Return a List of all the Kitchen Hood devices |
| `dhw_circulating_pumps` | — | Return a List of all the Kitchen Hood devices |
| `dhw_storage_pumps` | — | Return a List of all the Kitchen Hood devices |
| `other_devices` | — | Return a List of all the Kitchen Hood devices |

### Methods

#### clear_all_devices()

Reset the collection to an empty dictionary.

#### device_in_collection(_device_key)

Return True if a PHX Supportive Device with the matching key is in the collection.

| Arg | Type | Description |
|-----|------|-------------|
| `_device_key` | — | — |

#### get_device_by_key(_key)

Returns the PHX Supportive Device with the matching key, or None if not found.

| Arg | Type | Description |
|-----|------|-------------|
| `_key` | — | The key to search the collection for. |

#### get_device_by_id(_id_num)

Returns a PHX Supportive Device from the collection which has a matching id-num.

| Arg | Type | Description |
|-----|------|-------------|
| `_id_num` | — | The Supportive Device id-number to search for. |

#### add_new_device(_key, _d)

Adds a new PHX Supportive Device to the collection.

| Arg | Type | Description |
|-----|------|-------------|
| `_key` | — | The key to use when storing the new device |
| `_d` | — | — |

#### group_devices_by_identifier(_devices)

| Arg | Type | Description |
|-----|------|-------------|
| `_devices` | — | — |

#### merge_group_of_devices(_groups)

Merge a group of Dict of device-groups together into a single device.

| Arg | Type | Description |
|-----|------|-------------|
| `_groups` | — | — |

#### merge_all_devices()

Merge all the devices in the collection together by identifier.

---

## PhxExhaustVentilatorCollection

A Collection of PHX Exhaust Ventilation Devices.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `devices` | — | — |
| `kitchen_hood_devices` | — | Return a List of all the Kitchen Hood devices |
| `dryer_devices` | — | Return a List of all the Dryer devices |
| `user_determined_devices` | — | Return a List of all the User-Determined devices |

### Methods

#### clear_all_devices()

Reset the collection to an empty dictionary.

#### device_in_collection(_device_key)

Return True if a PHX Exhaust Ventilator with the matching key is in the collection.

| Arg | Type | Description |
|-----|------|-------------|
| `_device_key` | — | — |

#### get_ventilator_by_key(_key)

Returns the PHX Exhaust Ventilator with the matching key, or None if not found.

| Arg | Type | Description |
|-----|------|-------------|
| `_key` | — | The key to search the collection for. |

#### get_ventilator_by_id(_id_num)

Returns a PHX Exhaust Ventilator from the collection which has a matching id-num.

| Arg | Type | Description |
|-----|------|-------------|
| `_id_num` | — | The Exhaust Ventilator id-number to search for. |

#### add_new_ventilator(_key, _d)

Adds a new PHX Exhaust Ventilator to the collection.

| Arg | Type | Description |
|-----|------|-------------|
| `_key` | — | The key to use when storing the new mechanical device |
| `_d` | — | — |

#### merge_all_devices()

Merge all the devices in the collection together by type.

---

## PhxMechanicalSystemCollection

A Collection of all the mechanical devices (heating, cooling, etc) and distribution in the project

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `devices` | — | Returns a list of the 'devices' in the collection. |
| `ventilation_devices` | — | Returns a list of the 'Ventilation' devices in the collection. |
| `space_heating_devices` | — | Returns a list of the 'Space Heating' devices in the collection. |
| `heat_pump_devices` | — | Returns a list of all the Heat-Pump devices in the collection. |
| `cooling_devices` | — | Returns a list of all the Cooling devices (heat pumps) in the collection. |
| `dhw_heating_devices` | — | Returns a list of only the 'DHW Heating' devices (no tanks) in the collection. |
| `dhw_tank_devices` | — | Returns a list of only the 'DHW Storage Tank' devices (no heaters) in the collection. |
| `dhw_distribution_trunks` | — | — |
| `dhw_distribution_piping` | — | Returns a list of ALL the DHW Piping from ALL Trunks, Branches, Twigs in the collection. |
| `dhw_distribution_piping_segments` | — | Returns a list of ALL the DHW Piping Segments from ALL Trunks, Branches, Twigs in the collection. |
| `dhw_distribution_piping_segments_by_diam` | — | Returns a list of the DHW branch-piping segments, grouped by diameter. |
| `dhw_recirc_piping` | — | Returns a list of all the DHW recirculation-piping in the collection. |
| `dhw_recirc_piping_segments_by_diam` | — | Returns a list of the DHW recirculation-piping segments, grouped by diameter. |
| `dhw_recirc_total_length_m` | — | — |
| `dhw_recirc_weighted_heat_loss_coeff` | — | Return a length-weighted average pipe heat-loss coefficient. |
| `dhw_distribution_total_length_m` | — | — |
| `dhw_distribution_weighted_diameter_mm` | — | Return a length-weighted average diameter for the trunk/branch/twig piping. |
| `vent_ducting` | — | Returns a list of all the Vent. Ducting in the collection. |

### Methods

#### device_in_collection(_device_key)

Return True if the a Mech device with the matching key is already in the collection.

| Arg | Type | Description |
|-----|------|-------------|
| `_device_key` | — | — |

#### get_mech_device_by_key(_key)

Returns the mechanical device with the matching key, or None if not found.

| Arg | Type | Description |
|-----|------|-------------|
| `_key` | — | The key to search the collection for. |

#### get_mech_device_by_id(_id_num)

Returns a Mechanical Device from the collection which has a matching id-num.

| Arg | Type | Description |
|-----|------|-------------|
| `_id_num` | — | The Mechanical Device id-number to search for. |

#### add_new_mech_device(_key, _d)

Adds a new PHX Mechanical device to the collection.

| Arg | Type | Description |
|-----|------|-------------|
| `_key` | — | The key to use when storing the new mechanical device |
| `_d` | — | — |

#### add_distribution_piping(_p)

Add a new DHW Trunc-Pipe to the System.

| Arg | Type | Description |
|-----|------|-------------|
| `_p` | — | — |

#### add_recirc_piping(_p)

Add a new DHW Recirc-Pipe to the System.

| Arg | Type | Description |
|-----|------|-------------|
| `_p` | — | — |

#### add_vent_ducting(_d)

| Arg | Type | Description |
|-----|------|-------------|
| `_d` | — | — |

---
