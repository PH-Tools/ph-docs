# phius_certification

Valid 'types' for PHIUS Certification Settings.

**Source**: `PHX/phius_certification.py`

---

## PhiusCertificationBuildingCategoryType

Building category for Phius certification.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `RESIDENTIAL_BUILDING` | `1` | Residential building category. |
| `NONRESIDENTIAL_BUILDING` | `2` | Non-residential building category. |

---

## PhiusCertificationBuildingUseType

Building use type for Phius certification.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `RESIDENTIAL` | `1` | Residential use. |
| `OFFICE` | `4` | Office building use. |
| `SCHOOL` | `5` | School building use. |
| `OTHER` | `6` | Other building use type. |
| `UNDEFINED` | `7` | Use type not yet defined. |

---

## PhiusCertificationBuildingStatus

Current construction status of the building for Phius certification.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `IN_PLANNING` | `1` | Building is in the design/planning phase. |
| `UNDER_CONSTRUCTION` | `2` | Building is currently under construction. |
| `COMPLETE` | `3` | Building construction is complete. |

---

## PhiusCertificationBuildingType

Building construction type for Phius certification.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `NEW_CONSTRUCTION` | `1` | New construction project. |
| `RETROFIT` | `2` | Retrofit of an existing building. |
| `MIXED` | `3` | Mixed new construction and retrofit. |

---

## PhiusCertificationProgram

Phius certification program version.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `DEFAULT` | `1` | Default certification program. |
| `PHIUS_2015` | `2` | Phius+ 2015 standard. |
| `PHIUS_2018` | `3` | Phius 2018 standard. |
| `ITALIAN` | `4` | Italian Passive House standard. |
| `PHIUS_2018_CORE` | `5` | Phius CORE 2018 (envelope-only) standard. |
| `PHIUS_2018_ZERO` | `6` | Phius ZERO 2018 (net-zero) standard. |
| `PHIUS_2021_CORE` | `7` | Phius CORE 2021 (envelope-only) standard. |
| `PHIUS_2021_ZERO` | `8` | Phius ZERO 2021 (net-zero) standard. |

---
