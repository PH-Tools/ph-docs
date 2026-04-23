# areas_surface

Model class for a PHPP Areas / Surface-Entry row

**Source**: `PHX/areas_surface.py`

---

## SurfaceRow

A single Areas/Surface entry row.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `phpp_group_number_format` | — | Return the correct PHPP 'Group Format' depending on the PHPP version. |
| `phpp_group_number_int` | — | Return the raw PHPP group number as an integer, based on face type and exposure. |
| `phpp_group_number` | — | Return the PHPP group number as a version-formatted string (e.g. '12-' for v10, '12' for v9). |

### Methods

#### create_xl_items(_sheet_name, _row_num)

Returns a list of the XL Items to write for this Surface Entry

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | (str) The name of the worksheet to write to. |
| `_row_num` | — | (int) The row number to build the XlItems for |

---

## ExistingSurfaceRow

The data from an existing PHPP Surface Entry row.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `is_empty` | — | — |
| `name` | — | — |
| `face_group_type_phpp_string` | — | Return the face's Group-Type string from the row-data. |
| `face_group_type_phpp_number` | — | Return the face's Group-Type number as an int from the Group-Type string. |
| `face_exposure_phpp_letter` | — | Return the face's exposure-type letter ("A", "B", etc..) based on the group_type_phpp_number |
| `face_type` | — | Return the face type enum (WALL, FLOOR, etc..) based on the group_type_phpp_number. |
| `face_exposure` | — | Return the exposure type enum (EXTERIOR, GROUND, SURFACE) based on the face_exposure_phpp_letter |
| `face_construction_phpp_id` | — | Return the face's construction PHPP-ID (ie: "01ud-MyConst") from the row-data. |
| `face_construction_phpp_name` | — | Return the face's construction PHPP-Name (ie: "MyConst") from the row-data. |

---
