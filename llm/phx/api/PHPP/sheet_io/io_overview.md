# io_overview

Controller Class for the PHPP 'Overview' Worksheet.

**Source**: `PHX/io_overview.py`

---

## OverviewBasicData

Reads basic project data (dwellings, occupants, name) from the PHPP 'Overview' worksheet.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `host` | — | — |
| `xl` | — | — |
| `shape` | — | — |

### Methods

#### get_num_dwellings()

Return the Total Net Interior Volume (Vn50)

#### get_num_occupants()

Return the number of occupants.

#### get_project_name()

Return the name of the Project / Building

---

## OverviewVentilation

Reads ventilation data (Vn50) from the PHPP 'Overview' worksheet.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `host` | — | — |
| `xl` | — | — |
| `shape` | — | — |

### Methods

#### get_vn50()

Return the Total Net Interior Volume (Vn50)

---

## OverviewBuildingEnvelope

IO Controller for the PHPP 'Overview' worksheet.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `host` | — | — |
| `xl` | — | — |
| `shape` | — | — |

### Methods

#### get_area_envelope()

Return the Total Envelope Area [M2]

#### get_area_tfa()

Return the Total TFA [M2]

---

## Overview

IO Controller for the PHPP 'Overview' worksheet.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |
| `basic_data` | `OverviewBasicData` | — |
| `building_envelope` | `OverviewBuildingEnvelope` | — |
| `ventilation` | `OverviewVentilation` | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `worksheet_name` | — | — |

### Methods

#### get_area_envelope()

Return the Total Envelope Area [M2 | FT2]

#### get_area_tfa()

Return the Total TFA [M2 | FT2]

#### get_net_interior_volume()

Return the Total Net Interior Volume (Vn50) [M3 | FT3]

#### get_number_of_dwellings()

Return the total number of dwellings.

#### get_number_of_occupants()

Return the total number of occupants.

#### get_project_name()

Return the Name of the Project.

---
