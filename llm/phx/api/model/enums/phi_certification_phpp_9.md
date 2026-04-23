# phi_certification_phpp_9

Valid 'types' for PHI Certification Settings (PHPP v9).

**Source**: `PHX/phi_certification_phpp_9.py`

---

## PhiCertBuildingCategoryType

Building category for PHI certification (PHPP v9).

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `RESIDENTIAL_BUILDING` | `1` | Residential building category. |
| `NONRESIDENTIAL_BUILDING` | `2` | Non-residential building category. |

---

## PhiCertBuildingUseType

Building use type for PHI certification (PHPP v9).

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `DWELLING` | `10` | Residential dwelling. |
| `NURSING_HOME` | `11` | Nursing home or assisted living facility. |
| `OTHER_RES` | `12` | Other residential use type. |
| `OFFICE` | `20` | Office building. |
| `SCHOOL` | `21` | School building. |
| `OTHER_NONRES` | `22` | Other non-residential use type. |

---

## PhiCertIHGType

Internal heat gains calculation method for PHI certification (PHPP v9).

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `STANDARD` | `2` | Standard IHG values per PHI protocol. |
| `RES_CUSTOM` | `3` | Custom IHG values for residential buildings. |
| `NONRES_CUSTOM` | `4` | Custom IHG values for non-residential buildings. |

---

## PhiCertOccupancyType

Occupancy calculation method for PHI certification (PHPP v9).

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `STANDARD` | `1` | Standard occupancy based on TFA per PHI protocol. |
| `CUSTOM` | `2` | User-specified occupancy count. |

---

## PhiCertType

PHI certification standard type (PHPP v9).

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `PASSIVE_HOUSE` | `1` | Passive House certification. |
| `ENERPHIT` | `2` | EnerPHit retrofit certification. |
| `LOW_ENERGY_BUILDING` | `3` | PHI Low Energy Building certification. |
| `OTHER` | `4` | Other certification type. |

---

## PhiCertClass

PHI certification class based on renewable energy generation (PHPP v9).

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `CLASSIC` | `1` | Classic Passive House (no renewable energy generation requirement). |
| `PLUS` | `2` | Passive House Plus (moderate renewable energy generation). |
| `PREMIUM` | `3` | Passive House Premium (high renewable energy generation). |

---

## PhiCertificationPEType

Primary energy evaluation method for PHI certification (PHPP v9).

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `PE` | `1` | Primary Energy (non-renewable). |
| `PER` | `2` | Primary Energy Renewable. |

---

## PhiCertEnerPHitType

EnerPHit certification compliance pathway (PHPP v9).

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `BY_COMPONENT` | `1` | Compliance via component-level U-value criteria. |
| `BY_DEMAND` | `2` | Compliance via whole-building energy demand criteria. |

---

## PhiCertRetrofitType

Building retrofit status for PHI certification (PHPP v9).

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `NEW_BUILDING` | `1` | New construction project. |
| `RETROFIT` | `2` | Complete retrofit project. |
| `STEP_BY_STEP_RETROFIT` | `3` | Phased step-by-step retrofit project. |

---
