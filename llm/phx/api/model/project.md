# project

PHX Project Classes

**Source**: `PHX/project.py`

---

## WufiPlugin

WUFI-Passive plugin configuration for a variant.

---

## PhxVariant

A single design variant within a PHX project.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `mech_systems` | — | Return the Default Mechanical System Collection for the variant. |
| `mech_collections` | — | Return the list of Mechanical System Collections for the variant. |
| `default_mech_collection` | — | Return the Default Mechanical System Collection for the variant. |
| `graphics3D` | — | Collects all of the geometry (Polygons, Vertices) in the Project. |
| `phi_certification_major_version` | — | Return the PHI Certification Version Number. |
| `zones` | — | Return a list of all the PHX Zones in the variant.building |

### Methods

#### get_total_gross_wall_area()

Returns the total wall area of the variant.building

#### get_total_net_wall_area()

Returns the total net wall area of the variant.building

#### get_total_wall_aperture_area()

Returns the total window area of the variant.building

#### get_total_gross_roof_area()

Returns the total wall area of the variant.building

#### get_total_net_roof_area()

Returns the total net wall area of the variant.building

#### get_total_roof_aperture_area()

Returns the total window area of the variant.building

#### get_total_gross_envelope_area()

Returns the total gross envelope area of the variant.building

#### add_mechanical_collection(_mech_collection)

Add a new mechanical collection to the variant.

| Arg | Type | Description |
|-----|------|-------------|
| `_mech_collection` | — | — |

#### clear_mechanical_collections()

Clear all mechanical collections from the variant.

#### get_mech_device_by_key(_key)

Return a Tuple of a mech-collection and a mechanical device based on the specified device key, or None if not found.

| Arg | Type | Description |
|-----|------|-------------|
| `_key` | — | — |

#### device_in_collections(_key)

See if the variant's mechanical device collections already includes the specified key.

| Arg | Type | Description |
|-----|------|-------------|
| `_key` | — | — |

#### supportive_device_in_collections(_key)

Return a supportive device based on the specified device key, or None if not found.

| Arg | Type | Description |
|-----|------|-------------|
| `_key` | — | — |

#### renewable_device_in_collections(_key)

Return a renewable device based on the specified device key, or None if not found.

| Arg | Type | Description |
|-----|------|-------------|
| `_key` | — | — |

#### get_mech_device_by_id(_id_num)

Returns a Mechanical Device from the collections which has a matching id-num.

| Arg | Type | Description |
|-----|------|-------------|
| `_id_num` | — | — |

---

## ProjectData_Agent

Contact information for a project stakeholder (customer, owner, designer, etc.).

---

## PhxProjectDate

Timestamp for a PHX project, defaulting to the current date and time.

---

## PhxProjectData

Project-level metadata including stakeholder contacts and dates.

---

## PhxProject

Top-level PHX project container.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `assembly_type_id_numbers` | — | — |
| `window_type_id_numbers` | — | — |
| `shade_type_id_numbers` | — | — |

### Methods

#### add_new_variant(_variant)

Adds a new PHX Variant to the Project.

| Arg | Type | Description |
|-----|------|-------------|
| `_variant` | — | — |

#### add_assembly_type(_assembly_type, _key)

Adds a new PhxConstructionOpaque to the Project's collection

| Arg | Type | Description |
|-----|------|-------------|
| `_assembly_type` | — | — |
| `_key` | — | — |

#### add_new_window_type(_window_type, _key)

Adds a new PhxConstructionWindow to the Project's collection

| Arg | Type | Description |
|-----|------|-------------|
| `_window_type` | — | — |
| `_key` | — | — |

#### get_window_type(_key)

Returns the PhxConstructionWindow with the specified key

| Arg | Type | Description |
|-----|------|-------------|
| `_key` | — | — |

#### get_window_types_by_name(_name)

Returns a list of PhxConstructionWindow with the specified name.

| Arg | Type | Description |
|-----|------|-------------|
| `_name` | — | — |

#### add_new_shade_type(_shade_type, _key)

Adds a new PhxWindowShade to the Project's collection

| Arg | Type | Description |
|-----|------|-------------|
| `_shade_type` | — | — |
| `_key` | — | — |

#### vent_sched_in_project_collection(_key)

See if the project Ventilation schedule collection already includes the specified key.

| Arg | Type | Description |
|-----|------|-------------|
| `_key` | — | — |

#### occupancy_sched_in_project_collection(_key)

See if the project Occupancy schedule collection already includes the specified key.

| Arg | Type | Description |
|-----|------|-------------|
| `_key` | — | — |

#### lighting_sched_in_project_collection(_key)

See if the project Lighting schedule collection already includes the specified key.

| Arg | Type | Description |
|-----|------|-------------|
| `_key` | — | — |

#### add_vent_sched_to_collection(vent_sched)

Add a new Ventilation schedule to the project's collection.

| Arg | Type | Description |
|-----|------|-------------|
| `vent_sched` | — | — |

#### add_occupancy_sched_to_collection(vent_sched)

Add a new Occupancy schedule to the project's collection.

| Arg | Type | Description |
|-----|------|-------------|
| `vent_sched` | — | — |

#### add_lighting_sched_to_collection(lighting_sched)

Add a new Occupancy schedule to the project's collection.

| Arg | Type | Description |
|-----|------|-------------|
| `lighting_sched` | — | — |

#### get_total_gross_wall_area()

Get the total gross wall area for all variants in the project (ignoring any apertures).

#### get_total_net_wall_area()

Get the total net wall area for all variants in the project (ignoring any apertures).

#### get_total_gross_roof_area()

Get the total gross roof area for all variants in the project.

#### get_total_net_roof_area()

Get the total net roof area for all variants in the project.

#### get_total_wall_aperture_area()

Get the total window area for all variants in the project.

#### get_total_roof_aperture_area()

Get the total roof aperture area for all variants in the project.

---
