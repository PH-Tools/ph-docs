# building

PHX Building Classes

**Source**: `PHX/building.py`

---

## PhxZone

A single thermal zone within a PHX building model.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `thermal_bridges` | — | Return all of the PhxComponentThermalBridge objects in the PhxZone. |
| `ventilated_spaces` | — | Return a list of all the spaces in the PhxZone which have some amount of ventilation airflow. |
| `ventilated_spaces_grouped_by_erv` | — | Return a dictionary of spaces grouped by their ERV ID. |

### Methods

#### add_thermal_bridge(_thermal_bridge)

Add a new PhxComponentThermalBridge to the PhxZone.

| Arg | Type | Description |
|-----|------|-------------|
| `_thermal_bridge` | — | — |

#### add_thermal_bridges(_thermal_bridges)

Add a new PhxComponentThermalBridge (or list of Bridges) to the PhxZone.

| Arg | Type | Description |
|-----|------|-------------|
| `_thermal_bridges` | — | — |

#### clear_thermal_bridges()

Clear all of the PhxComponentThermalBridge objects from the PhxZone.

#### merge_thermal_bridges()

Merge together all the Thermal Bridges in the Zone if they have the same 'unique_key' attribute.

---

## PhxBuilding

The building-level container within a PHX project variant.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `weighted_net_floor_area` | — | Returns the total weighted net floor area of all zones in the PhxBuilding. |
| `tfa_override` | — | Return the total floor area override of the PhxBuilding. |
| `net_volume` | — | Returns the total net-volume of all the zones in the PhxBuilding. |
| `all_components` | — | Return a list of all the Opaque and Aperture Components in the Building. |
| `aperture_components` | — | Returns a sorted list (by display name) of all the aperture components in the building. |
| `aperture_elements` | — | Returns a sorted list (by display name) of all the aperture elements in the building. |
| `aperture_elements_by_orientation` | — | Return all of the Aperture Elements, grouped by their cardinal orientation. |
| `aperture_components_horizontal` | — | Return all aperture components in the building (currently unfiltered). |
| `wall_aperture_components` | — | Returns a sorted list (by display name) of all the wall aperture (window) components in the building. |
| `roof_aperture_components` | — | Returns a sorted list (by display name) of all the roof aperture (skylight) components in the building. |
| `opaque_components` | — | Returns a sorted list (by display name) of all the opaque non-shade components in the building. |
| `roof_components` | — | Returns a sorted list (by display name) of all the roof components in the building. |
| `above_grade_wall_components` | — | Returns a sorted list (by display name) of all the above grade wall components in the building. |
| `shading_components` | — | Returns a list of all the opaque shade components in the building. |
| `polygon_ids` | — | Return a Set of all the Polygon IDs of all Polygons from all the Components in the building. |
| `polygons` | — | Returns a list of all the Polygons of all the Components in the building. |
| `all_spaces` | — | Return a list of all the Spaces in the Building. |

### Methods

#### add_components(_components)

Add new PHX Components to the PhxBuilding.

| Arg | Type | Description |
|-----|------|-------------|
| `_components` | — | — |

#### add_component(_component)

Add a new PHX Components to the PhxBuilding.

| Arg | Type | Description |
|-----|------|-------------|
| `_component` | — | — |

#### add_zones(_zones)

Add a new PhxZone to the PhxBuilding.

| Arg | Type | Description |
|-----|------|-------------|
| `_zones` | — | — |

#### add_zone(_zone)

Add a new PhxZone to the PhxBuilding.

| Arg | Type | Description |
|-----|------|-------------|
| `_zone` | — | — |

#### merge_opaque_components_by_assembly()

Merge together all the Opaque-Components in the Building if they gave the same Attributes.

#### merge_aperture_components_by_assembly()

Merge together all the Aperture-Components in the Building if they have the same Attributes.

#### merge_thermal_bridges()

Merge together all the Thermal Bridges in each of the Building's Zones if they have the same Attributes.

#### get_total_gross_wall_area()

Returns the total wall area of all the opaque components in the building.

#### get_total_net_wall_area()

Returns the total net wall area of all the opaque components in the building.

#### get_total_gross_roof_area()

Returns the total roof area of all the opaque components in the building.

#### get_total_net_roof_area()

Returns the total net roof area of all the opaque components in the building.

#### get_total_wall_aperture_area()

Returns the total window area of all the opaque components in the building.

#### get_total_roof_aperture_area()

Returns the total skylight area of all the opaque components in the building.

#### get_total_gross_envelope_area()

Returns the total gross envelope area of all the opaque components in the building.

#### scale_all_wall_aperture_components(_scale_factor)

Scale all the wall-aperture component's polygons by a given factor.

| Arg | Type | Description |
|-----|------|-------------|
| `_scale_factor` | — | — |

#### scale_all_roof_aperture_components(_scale_factor)

Scale all the roof-aperture component's polygons by a given factor.

| Arg | Type | Description |
|-----|------|-------------|
| `_scale_factor` | — | — |

---
