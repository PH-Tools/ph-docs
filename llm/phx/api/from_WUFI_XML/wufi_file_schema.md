# wufi_file_schema

Pydantic Model for reading in WUFI-XML file format.

**Source**: `PHX/wufi_file_schema.py`

---

## WufiBaseModel

Base class for all WUFI XML schema models.

**Inherits from**: `BaseModel`

### Methods

#### *classmethod* unpack_all_xml_tags(data)

| Arg | Type | Description |
|-----|------|-------------|
| `data` | — | — |

---

## WufiCO2FactorsUserDef

No description available.

### Methods

#### *classmethod* unpack_xml_tag_name(v)

| Arg | Type | Description |
|-----|------|-------------|
| `v` | — | — |

---

## WufiPEFactorsUserDef

No description available.

### Methods

#### *classmethod* unpack_xml_tag_name(v)

| Arg | Type | Description |
|-----|------|-------------|
| `v` | — | — |

---

## WufiMonthlyClimateTemp_Item

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiMonthlyClimateRadiation_Item

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiPH_ClimateLocation

No description available.

**Inherits from**: `WufiBaseModel`

### Methods

#### set_standard_pe_factors(PH_CertificateCriteriaNum)

Set the PE-Factors from the Standards-Library based on the PH_CertificateCriteria.

| Arg | Type | Description |
|-----|------|-------------|
| `PH_CertificateCriteriaNum` | — | — |

#### set_standard_co2_factors(PH_CertificateCriteriaNum)

Set the CO2-Factors from the Standards-Library based on the PH_CertificateCriteria.

| Arg | Type | Description |
|-----|------|-------------|
| `PH_CertificateCriteriaNum` | — | — |

---

## WufiClimateLocation

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiVertix

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiIdentNr

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiPolygon

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiGraphics_3D

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiRoom

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiLoadPerson

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiLoadsLighting

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiExhaustVent

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiHomeDevice

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiIdentNrPolygons

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiComponent

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiThermalBridge

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiZone

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiBuilding

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiTwig

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiBranch

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiTrunc

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiDistributionDHW

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiDistributionCooling

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiSupportiveDevice

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiAssignedVentUnit

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiDuct

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiPHDistribution

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiZoneCoverage

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiPH_Parameters

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiDHW_Parameters

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiHeating_Parameters

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiCooling_Parameters

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiVentilation_Parameters

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiDevice

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiSystem

No description available.

**Inherits from**: `WufiBaseModel`

### Methods

#### *classmethod* unpack_zone_coverage(v)

| Arg | Type | Description |
|-----|------|-------------|
| `v` | — | — |

---

## WufiSystems

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiFoundationInterface

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiInternalGainsAdditionalData

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiPH_Building

No description available.

**Inherits from**: `WufiBaseModel`

### Methods

#### *classmethod* validate_wind_exposure(v)

| Arg | Type | Description |
|-----|------|-------------|
| `v` | — | — |

---

## WufiPassivehouseData

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiPlugin

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiVariant

No description available.

**Inherits from**: `WufiBaseModel`

### Methods

#### *classmethod* unpack_hvac(v)

| Arg | Type | Description |
|-----|------|-------------|
| `v` | — | — |

#### check_source_energy_factors()

Ensure the ClimateLocation's Energy and CO2 conversion factor lists are populated properly.

---

## WufiColor

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiMaterial

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiDivisionV

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiDivisionH

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiMaterialIDNr

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiLayer

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiExchangeMaterial

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiAssembly

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiWindowType

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiSolarProtectionType

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiUtilizationPatternVent

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiUtilizationPattern

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiDateProject

No description available.

**Inherits from**: `WufiBaseModel`

---

## WufiProjectData

No description available.

**Inherits from**: `WufiBaseModel`

---

## WUFIplusProject

No description available.

**Inherits from**: `WufiBaseModel`

### Methods

#### *classmethod* unpack_unit_system(v)

Since the model gets converted to SI units when it is read in,

| Arg | Type | Description |
|-----|------|-------------|
| `v` | — | — |

---
