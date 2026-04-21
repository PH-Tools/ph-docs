# utilization_patterns

Collections for organizing PH space schedules as utilization patterns.

**Source**: `PHX/utilization_patterns.py`

---

## UtilizationPatternCollection_Ventilation

Collection of ventilation utilization patterns for PH spaces.

### Methods

#### add_new_util_pattern(_util_pattern)

Add a new ventilation.PhxScheduleVentilation to the Collection.

| Arg | Type | Description |
|-----|------|-------------|
| `_util_pattern` | — | The ventilation.PhxScheduleVentilation pattern to add to the collection. |

#### key_is_in_collection(_id)

Check if the id is in the collection.

| Arg | Type | Description |
|-----|------|-------------|
| `_id` | — | — |

#### get_pattern_by_id_num(_id_num)

Return a ventilation.PhxScheduleVentilation from the collection found by an id-num

| Arg | Type | Description |
|-----|------|-------------|
| `_id_num` | — | The id-number of the Schedule to find. |

#### items()

#### keys()

#### values()

---

## UtilizationPatternCollection_Occupancy

Collection of occupancy utilization patterns for PH spaces.

### Methods

#### add_new_util_pattern(_util_pattern)

Add a new occupancy.PhxScheduleOccupancy to the Collection.

| Arg | Type | Description |
|-----|------|-------------|
| `_util_pattern` | — | The occupancy.PhxScheduleOccupancy pattern to add to the collection. |

#### key_is_in_collection(_id)

Check if the id is in the collection.

| Arg | Type | Description |
|-----|------|-------------|
| `_id` | — | — |

#### get_pattern_by_id_num(_id_num)

Return a occupancy.PhxScheduleOccupancy from the collection found by an id-num

| Arg | Type | Description |
|-----|------|-------------|
| `_id_num` | — | The id-number of the Schedule to find. |

#### items()

#### keys()

#### values()

---

## UtilizationPatternCollection_Lighting

Collection of lighting utilization patterns for PH spaces.

### Methods

#### add_new_util_pattern(_util_pattern)

Add a new lighting.PhxScheduleLighting to the Collection.

| Arg | Type | Description |
|-----|------|-------------|
| `_util_pattern` | — | The lighting.PhxScheduleLighting pattern to add to the collection. |

#### key_is_in_collection(_id)

Check if the id is in the collection.

| Arg | Type | Description |
|-----|------|-------------|
| `_id` | — | — |

#### get_pattern_by_id_num(_id_num)

Return a lighting.PhxScheduleLighting from the collection found by an id-num

| Arg | Type | Description |
|-----|------|-------------|
| `_id_num` | — | The id-number of the Schedule to find. |

#### items()

#### keys()

#### values()

---
