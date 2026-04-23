# phius_mf

Classes for calculating Phius Multifamily Elec. Energy as per Phius Multifamily Calculator (v4.2)

**Source**: `honeybee_energy_ph/phius_mf.py`

---

## PhiusResidentialStory

One residential story in the Phius Multifamily Calculator (v4.2).

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `total_floor_area_ft2` | `calc_story_floor_area_ft2` | Weighted floor area in ft2. |
| `total_number_dwellings` | `calc_num_dwellings` | Count of dwelling units on this story. |
| `total_number_bedrooms` | `calc_story_bedrooms` | Count of bedrooms on this story. |
| `design_occupancy` | `calc_passive_house_occupancy` | PH design occupancy (number of people). |
| `mel` | `misc_electrical` | Annual miscellaneous electrical load (kWh). |
| `lighting_int` | `lighting_interior` | Annual interior lighting load (kWh). |
| `lighting_ext` | `lighting_exterior` | Annual exterior lighting load (kWh). |
| `lighting_garage` | `lighting_garage` | Annual garage lighting load (kWh). |
| `story_number` | — | Zero-padded story number string. |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `story_number` | `str` | Return the story number. |

### Methods

#### calc_story_floor_area_ft2(_hb_rooms, _area_unit)

| Arg | Type | Description |
|-----|------|-------------|
| `_hb_rooms` | `list[Room]` | — |
| `_area_unit` | `str` | — |

**Returns**: `float`

#### calc_story_bedrooms(_hb_rooms)

| Arg | Type | Description |
|-----|------|-------------|
| `_hb_rooms` | `list[Room]` | — |

**Returns**: `int`

#### calc_passive_house_occupancy(_hb_rooms)

| Arg | Type | Description |
|-----|------|-------------|
| `_hb_rooms` | `list[Room]` | — |

**Returns**: `float`

#### calc_num_dwellings(_hb_rooms)

| Arg | Type | Description |
|-----|------|-------------|
| `_hb_rooms` | `list[Room]` | — |

**Returns**: `int`

---

## PhiusNonResProgram

A Phius non-residential program type with lighting and MEL intensities.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `name` | `str` | Program type name. |
| `usage_days_yr` | `int` | Annual usage days. Default: 365. |
| `operating_hours_day` | `float` | Daily operating hours. |
| `lighting_W_per_m2` | `float` | Lighting power density (W/m2). |
| `mel_kWh_m2_yr` | `float` | Annual MEL energy intensity (kWh/m2/yr). |
| `mel_w_m2` | `float` | MEL power density (W/m2). |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `lighting_W_per_ft2` | `float` | Lighting power density converted to W/ft2. |
| `mel_kWh_ft2_yr` | `float` | Annual MEL energy intensity converted to kWh/ft2/yr. |

### Methods

#### to_phius_mf_workbook()

Returns a text block formatted to match the Phius MF Calculator.

**Returns**: `str`

#### *classmethod* from_hb_room(_hb_room)

Returns a new PhiusNonResProgram object with attributes based on an HBE-Room.

| Arg | Type | Description |
|-----|------|-------------|
| `_hb_room` | `Room` | — |

**Returns**: `PhiusNonResProgram`

---

## PhiusNonResProgramCollection

Collection of Phius Non-Res Program Types.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `programs` | `ValuesView[PhiusNonResProgram]` | Returns a ValuesView of the PhiusNonResPrograms in the collection dict. |

### Methods

#### add_program(_program, _key)

Adds a new PhiusNonResProgram to the collection.

| Arg | Type | Description |
|-----|------|-------------|
| `_program` | `PhiusNonResProgram` | — |
| `_key` | `str | None` | — |

**Returns**: `None`

#### to_phius_mf_workbook()

Returns a text block formatted to match the Phius MF Calculator.

**Returns**: `list[str]`

---

## PhiusNonResRoom

A single non-residential space for the Phius MF Calculator.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `multiplier` | `int` | Space multiplier. Default: 1. |
| `occupancy_sensor` | `str` | Occupancy sensor flag ("Y"/"N"). Default: "N". |
| `name` | `str` | Space name. |
| `reference_floor_area_m2` | `float` | Reference floor area (m2). |
| `misc_mel` | `float` | Additional miscellaneous MEL (kWh/yr). |
| `program_type` | `PhiusNonResProgram` | The assigned program type. |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `reference_floor_area_ft2` | `float` | Reference floor area converted to ft2. |
| `mel_kWh_yr` | `float` | Annual MEL energy (kWh) excluding miscellaneous MEL. |
| `mel_w_m2` | `float` | MEL power density from the assigned program type (W/m2). |
| `total_mel_kWh` | `float` | Annual MEL energy (kWh) including miscellaneous MEL. |
| `total_lighting_kWh` | `float` | Annual lighting energy (kWh). |

### Methods

#### to_phius_mf_workbook()

Returns a string representation that matches the Phius MF Calculator.

**Returns**: `str`

#### to_phius_mf_workbook_results()

#### *classmethod* from_ph_space(_ph_space, _area_unit)

Returns a new PhiusNonResSpace with properties based on a PH-Space.

| Arg | Type | Description |
|-----|------|-------------|
| `_ph_space` | `space.Space` | — |
| `_area_unit` | `str` | — |

**Returns**: `PhiusNonResRoom`

---
