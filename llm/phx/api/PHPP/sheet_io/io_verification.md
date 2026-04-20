# io_verification

Controller Class for the PHPP Climate worksheet.

**Source**: `PHX/io_verification.py`

---

## VerificationInputLocation

Generic input item for Verification worksheet items.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `sheet_name` | — | — |
| `search_col` | — | — |
| `search_item` | — | — |
| `input_row_offset` | — | — |

### Methods

#### find_input_row(_row_start, _row_end)

Return the row number where the search-item is found input.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_start` | — | — |
| `_row_end` | — | — |

---

## TeamMemberData

A Dataclass to store team-member information when read in from the PHPP.

### Methods

#### *classmethod* from_raw_excel_data(_xl_data)

Create a new TeamMemberData object from raw excel data read in from PHPP

| Arg | Type | Description |
|-----|------|-------------|
| `_xl_data` | — | List[List[str]]: A list of lists containing the data read in from PHPP. |

---

## Verification

No description available.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |

### Methods

#### write_item(_phpp_model_obj)

Write the VerificationInputItem item out to the PHPP Verification Worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_phpp_model_obj` | — | — |

#### read_architect()

Return a TeamMemberData object with the architect info from PHPP.

#### read_energy_consultant()

Return a TeamMemberData object with the consultant info from PHPP.

#### read_building()

Return a TeamMemberData object with the Building address from PHPP.

#### read_site_owner()

Return a TeamMemberData object with the owner info from PHPP.

#### read_mech_engineer()

#### read_ph_certification()

Return a TeamMemberData object with the Certifier info from PHPP.

---
