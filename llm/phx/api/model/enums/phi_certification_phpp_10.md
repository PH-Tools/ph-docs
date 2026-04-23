# phi_certification_phpp_10

Valid 'types' for PHI Certification Settings (PHPP v10).

**Source**: `PHX/phi_certification_phpp_10.py`

---

## PhiCertBuildingUseType

Building use type for PHI certification (PHPP v10).

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `DWELLING` | `10` | Residential dwelling. |
| `OTHER_RES` | `12` | Other residential use type. |
| `OFFICE` | `20` | Office building. |
| `SCHOOL_HALF_DAY` | `21` | School with half-day operation. |
| `SCHOOL_FULL_DAY` | `22` | School with full-day operation. |
| `OTHER_NONRES` | `23` | Other non-residential use type. |

---

## PhiCertIHGType

Internal heat gains calculation method for PHI certification (PHPP v10).

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `STANDARD` | `2` | Standard IHG values per PHI protocol. |
| `RES_CUSTOM` | `3` | Custom IHG values for residential buildings. |
| `NONRES_CUSTOM` | `4` | Custom IHG values for non-residential buildings. |

---

## PhiCertType

PHI certification standard type (PHPP v10).

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `PASSIVE_HOUSE` | `10` | Passive House certification. |
| `ENERPHIT_BY_COMPONENT` | `21` | EnerPHit certification via component-level criteria. |
| `ENERPHIT_BY_DEMAND` | `22` | EnerPHit certification via energy demand criteria. |
| `LOW_ENERGY_BUILDING` | `30` | PHI Low Energy Building certification. |
| `OTHER` | `44` | Other certification type. |

---

## PhiCertClass

PHI certification class based on renewable energy generation (PHPP v10).

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `CLASSIC` | `10` | Classic Passive House (no renewable energy generation requirement). |
| `PLUS` | `20` | Passive House Plus (moderate renewable energy generation). |
| `PREMIUM` | `30` | Passive House Premium (high renewable energy generation). |
| `CLASSIC_PE` | `11` | Classic Passive House using Primary Energy (non-renewable) evaluation. |

---

## PhiCertificationPEType

Primary energy factor source for PHI certification (PHPP v10).

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `STANDARD` | `1` | Standard primary energy factors per PHI dataset. |
| `PROJECT_SPECIFIC` | `2` | Project-specific primary energy factors. |

---

## PhiCertRetrofitType

Building retrofit status for PHI certification (PHPP v10).

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `NEW_BUILDING` | `1` | New construction project. |
| `RETROFIT` | `2` | Complete retrofit project. |
| `STEP_BY_STEP_RETROFIT` | `3` | Phased step-by-step retrofit project. |

---
