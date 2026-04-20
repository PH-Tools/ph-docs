# phpp_app

Controller for managing the PHPP Connection.

**Source**: `PHX/phpp_app.py`

---

## PHPPConnection

Interface for a PHPP Excel Document.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `version` | `get_phpp_version` | — |
| `easyPh` | `is_easyPh` | — |
| `verification` | `Verification` | — |
| `climate` | `Climate` | — |
| `u_values` | `UValues` | — |
| `components` | `Components` | — |
| `areas` | `Areas` | — |
| `windows` | `Windows` | — |
| `shading` | `Shading` | — |
| `addnl_vent` | `AddnlVent` | — |
| `heating` | `HeatingDemand` | — |
| `heating_load` | `HeatingPeakLoad` | — |
| `cooling` | `CoolingDemand` | — |
| `cooling_load` | `CoolingPeakLoad` | — |
| `ventilation` | `Ventilation` | — |
| `hot_water` | `HotWater` | — |
| `electricity` | `Electricity` | — |
| `variants` | `Variants` | — |
| `per` | `PER` | — |
| `overview` | `Overview` | — |
| `use_non_res` | `UseNonRes` | — |
| `elec_non_res` | `ElecNonRes` | — |
| `ihg_non_res` | `IhgNonRes` | — |
| `cooling_units` | `CoolingUnits` | — |
| `solar_dhw` | `SolarDHW` | — |
| `solar_pv` | `SolarPV` | — |

### Methods

#### get_data_worksheet()

Return the 'Data' worksheet from the active PHPP file, support English, German, Spanish.

#### get_phpp_version(_search_col, _row_start, _row_end)

Find the PHPP Version and Language of the active xl-file.

| Arg | Type | Description |
|-----|------|-------------|
| `_search_col` | — | — |
| `_row_start` | — | — |
| `_row_end` | — | — |

#### is_easyPh()

Return True if the active PHPP file is an 'easyPH' file.

#### phpp_version_equals_phx_phi_cert_version(_phx_variant)

Return True if the PHX PHI Certification Version and the PHPP Version match.

| Arg | Type | Description |
|-----|------|-------------|
| `_phx_variant` | — | — |

#### write_certification_config(phx_project)

| Arg | Type | Description |
|-----|------|-------------|
| `phx_project` | — | — |

#### write_climate_data(phx_project)

Write the variant's weather-station data to the PHPP 'Climate' worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `phx_project` | — | — |

#### write_project_constructions(phx_project)

Write all of the opaque constructions to the PHPP 'U-Values' worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `phx_project` | — | — |

#### write_project_window_components(phx_project)

Write all of the frame and glass constructions from a PhxProject to the PHPP 'Components' worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `phx_project` | — | — |

#### write_project_ventilation_components(phx_project)

Write all of the ventilators from a PhxProject to the PHPP 'Components' worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `phx_project` | — | — |

#### write_project_tfa(phx_project)

| Arg | Type | Description |
|-----|------|-------------|
| `phx_project` | — | — |

#### write_project_opaque_surfaces(phx_project)

Write all of the opaque surfaces from a PhxProject to the PHPP 'Areas' worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `phx_project` | — | — |

#### write_project_thermal_bridges(phx_project)

Write all of the thermal-bridge elements of a PhxProject to the PHPP 'Areas' worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `phx_project` | — | — |

#### write_project_window_surfaces(phx_project)

Write all of the window surfaces from a PhxProject to the PHPP 'Windows' worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `phx_project` | — | — |

#### write_project_window_shading(phx_project)

| Arg | Type | Description |
|-----|------|-------------|
| `phx_project` | — | — |

#### write_project_ventilators(phx_project)

Write all of the used Ventilator Units from a PhxProject to the PHPP 'Additional Vent' worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `phx_project` | — | — |

#### write_project_spaces(phx_project)

Write all of the PH-Spaces from a PhxProject to the PHPP 'Additional Vent' worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `phx_project` | — | — |

#### write_project_ventilation_type(phx_project)

Set the Ventilation-Type to the PHPP 'Ventilation' worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `phx_project` | — | — |

#### write_project_volume(phx_project)

Write the Vn50 and Vv to the PHPP 'Ventilation Worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `phx_project` | — | — |

#### write_project_airtightness(phx_project)

Write the Airtightness data to the PHPP 'Ventilation' worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `phx_project` | — | — |

#### write_project_hot_water(phx_project)

Write the Hot Water data to the PHPP 'DHW+Distribution' worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `phx_project` | — | — |

#### write_project_res_elec_appliances(phx_project)

Write out all of the detailed residential appliances to the "Electricity" Worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `phx_project` | — | — |

#### write_non_res_utilization_profiles(phx_project)

Write out all of the Utilization patterns to the "Use non-res" Worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `phx_project` | — | — |

#### write_non_res_space_lighting(phx_project)

Write out all of the Space Lighting values to the "Electricity non-res" Worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `phx_project` | — | — |

#### write_non_res_IHG(phx_project)

Write out all of the Occupancy patterns to the "IHG non-res" Worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `phx_project` | — | — |

#### activate_variant_assemblies()

Remove all existing U-Value information and link assemblies to the Variants worksheet.

#### activate_variant_windows()

Set the Frame and Glass Components to link to the Variants worksheet for all windows.

#### activate_variant_ventilation()

Set the ACH, Ventilation type to link to the Variants worksheet.

#### activate_variant_additional_vent()

Set the Ventilator, duct length and insulation to link to the Variants worksheet.

#### calculate()

Recalculate all the worksheets in the PHPP file.

---
