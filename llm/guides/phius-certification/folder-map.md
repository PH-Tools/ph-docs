# Phius Project Folder Map

This is the standard folder structure Phius creates for each certification project. The project root folder is named `{ProjectNum}-{ProjectName}_{ConsultantName}`.

## Top-Level Folders

```
{ProjectRoot}/
├── - Feedback Forms/              ← THE key document lives here (dash prefix sorts it first)
│   ├── {Num}_R{Round}_Feedback_V{Ver}_{Date}.xlsx   ← Current Feedback Form
│   ├── Phius Certification Guidebook v{X}.pdf        ← Phius reference guidebook
│   └── _Archive/                  ← Previous round submissions of the Feedback Form
│
├── 0. WUFI-Passive Energy Model/  ← The energy model and its exports
│   ├── {date}.mwp                 ← Current WUFI-Passive model file (binary, not readable)
│   ├── {date}.mwp.res             ← Model results file
│   ├── {date}_Phius_MF_Calculator.xlsx  ← Phius Multifamily Calculator
│   ├── {date} - WUFI Report PDFs/ ← Current exported report PDFs from the model
│   │   ├── Assemblies and Window Types.pdf
│   │   ├── Climate.pdf
│   │   ├── HVAC.pdf
│   │   ├── Passive House Data.pdf
│   │   ├── Passive House Verification.pdf
│   │   ├── Passive House Site Energy.pdf
│   │   ├── Passive House Source Energy Report.pdf
│   │   ├── Project Data.pdf
│   │   ├── Results.pdf
│   │   ├── REM-Rate Report.pdf
│   │   └── Zones and Components.pdf
│   └── _Archive/                  ← Previous model versions and their report PDFs
│
├── 1. Drawings & Takeoffs/        ← Construction drawings organized by discipline
│   ├── 0. Combined Set/           ← Full combined drawing set PDFs
│   ├── 1. Architectural/          ← Architectural drawings
│   │   ├── Takeoffs/              ← Area/quantity takeoffs from drawings
│   │   ├── Window Sizes/          ← Window dimension takeoffs
│   │   └── iCFA Plans/            ← Interior Conditioned Floor Area plans
│   ├── 2. Electrical/
│   │   └── Electric Vehicle Readiness/
│   ├── 3. Mechanical/
│   │   ├── ERV Zone Plans/        ← Ventilator zone assignment plans
│   │   ├── Mech Vent Flow Rate Plans/
│   │   └── Ventilator Duct Takeoffs/
│   ├── 4. Plumbing/
│   │   └── DHW Takeoffs/          ← Domestic hot water piping takeoffs
│   └── 5. Structural/
│
├── 2. Datasheets & Specs/         ← Product cut-sheets and specifications
│   ├── 1. HVAC/
│   │   ├── 1. Heating & Cooling/  ← Heat pump submittals, unit heater specs, HSPF calculators
│   │   └── 2. Ventilation/        ← ERV/HRV datasheets, fan submittals, AHRI certificates
│   ├── 2. DHW/
│   │   ├── 1. Water Heater/
│   │   ├── 2. Pumps/
│   │   └── 3. Storage Tank/
│   ├── 3. Lighting & Plug Loads/
│   │   ├── 1. Light Fixtures/
│   │   └── 2. Additional Devices/
│   ├── 4. Insulation/
│   │   ├── 0. Assembly Types/     ← Assembly type reference documents
│   │   ├── 1. Rigid/              ← XPS, EPS, Polyiso datasheets
│   │   ├── 2. Cavity/             ← Mineral wool, fiberglass datasheets
│   │   ├── 3. Ducts/
│   │   ├── 4. Plumbing/
│   │   ├── 5. Thermal Breaks/
│   │   └── 6. Spray/              ← Spray foam datasheets
│   ├── 5. Windows & Doors/
│   │   ├── 0. Glazing/            ← Glass performance data (SHGC, U-values)
│   │   ├── 1. Windows/            ← Window frame profiles, U-values
│   │   ├── 2. Glazed Doors/       ← Balcony/terrace door specs
│   │   ├── 3. Opaque Doors/
│   │   ├── 4. Shades/             ← Blind specs and Phius blinds calculator
│   │   └── 5. Storefront/         ← Aluminum storefront system specs
│   ├── 6. Appliances/
│   │   ├── Dishwashers/
│   │   ├── Hoods/
│   │   ├── Laundry/
│   │   ├── Refrigerators/
│   │   └── Stoves/
│   ├── 6. Renewable Systems/      ← (Note: duplicate numbering with Appliances in some templates)
│   │   ├── 1. On-Site PV/
│   │   ├── 2. Directly Owned Off-Site Renewables/
│   │   ├── 3. Community Renewable Energy/
│   │   ├── 4. Virtual Power Purchase Agreements (PPA)/
│   │   └── 5. Renewable Energy Certificates (RECs)/
│   ├── 7. Appliances/             ← (Alternate numbering in some templates)
│   └── 8. WRB and Airtightness/   ← Weather-resistive barrier and air barrier specs
│
├── 3. Calculations/               ← Engineering calculations
│   ├── 1. Miscellaneous/
│   ├── 2. THERM/                  ← THERM 2D thermal bridge models
│   │   └── 1. Detail X_Sheet Y/  ← Named by drawing detail reference
│   ├── 2b. Flixo [2D]/           ← Flixo 2D thermal bridge calculations
│   │   └── {SheetNum}_{DetailNum}_{Description}/
│   │       ├── DTL_{name}.flx     ← Flixo model file
│   │       ├── DTL_{name}.pdf     ← Exported results
│   │       └── Detail.png         ← Screenshot of the construction detail
│   └── 3. WUFI-Hygrothermal/     ← Hygrothermal analysis (moisture risk)
│
├── 4. On-Site Verification/       ← Field verification documentation
│   ├── 0. Phius QA Workbook/
│   ├── 1. Co-requisite Program Certificates/
│   │   ├── 1. EPA Indoor airPLUS/
│   │   ├── 2. Energy Star/
│   │   └── 3. Zero Energy Ready Homes/
│   ├── 2. HERS Building Summary/
│   ├── 3. Air Tightness Test Reports/
│   │   ├── 1. Preliminary (recommended)/
│   │   └── 2. Final (required)/
│   ├── 4. HVAC Testing & Balancing/
│   │   ├── 1. Ventilation/
│   │   └── 2. Heating_Cooling/
│   └── 5. Photos/
│       ├── 0. Infrared/
│       ├── 1. Insulation Inspection/
│       ├── 2. Windows & Doors/
│       ├── 3. HVAC/
│       ├── 4. DHW/
│       ├── 5. Appliances/
│       ├── 6. Renewables/
│       └── 7. General/
│
├── 5. Marketing & Database Photos/
├── 6. LOI from Rater or Verifier/ ← Letter of Intent from the field verifier
├── Helpful Phius Documents/       ← Reference materials from Phius
└── ReadMe.txt                     ← Phius's instructions for using the folder
```

## Key Conventions

- **`_Archive` folders**: Found throughout the project. Always contain superseded/previous versions. Current files are at the parent level.
- **Date prefixes**: Files often use `YYMMDD` format (e.g., `240625_Phius_MF_Calculator.xlsx` = June 25, 2024)
- **WUFI Report PDFs**: Exported as a batch from the WUFI-Passive model. Each submission gets its own dated subfolder.
- **Flixo folders**: Named by drawing reference `{SheetNum}_{DetailNum}_{Description}` matching the architectural detail they calculate.
- **Duplicate numbering**: Some Phius templates have overlapping folder numbers (e.g., two "6." folders under Datasheets). This is a known quirk.
