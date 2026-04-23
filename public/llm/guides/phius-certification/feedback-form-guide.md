# Feedback Form Parsing Guide

The Phius Feedback Form is a large Excel workbook (.xlsx) that serves as the single source of truth for the entire certification review process. This guide explains how to read and parse it programmatically.

## Finding the Feedback Form

Location: `{ProjectRoot}/- Feedback Forms/`

The current Feedback Form is the `.xlsx` file at the top level (not in `_Archive/`). Naming pattern:
```
{ProjectNum}_R{Round}_Feedback_V{FormVersion}_{YYYY.MM.DD}.xlsx
```

Example: `2441_R5_Feedback_V5.7_2026.03.11.xlsx`
- Project 2441, currently on Review Round 5, using Form Version 5.7, dated March 11, 2026

## Workbook Structure

### Detecting the Form Version

Cell **B2** always contains the version identifier. Use this to determine which parsing rules to apply:

| B2 Value Pattern | Version | Era |
|-----------------|---------|-----|
| `PHIUS+ FEEDBACK - V4.8` | V4.8 | Older projects (~2021 onward) |
| `Phius Design Feedback - V5.6` | V5.6/V5.7 | Current projects (~2024 onward) |

The version number tells you which supporting worksheets to expect and any minor layout differences (see below).

### Main Review Sheet

The primary sheet name varies by version:

| Version | Multifamily Sheet Name | Single Family Sheet Name |
|---------|----------------------|--------------------------|
| V4.8 | "Feedback - Multifamily (2024)" (may include year) | "Feedback - Single Family" |
| V5.6+ | "Feedback - Multifamily" | "Feedback - Single Family" |

Some workbooks include legacy 2015-era sheets — always skip sheets with "(2015)" in the name unless specifically needed.

### Supporting Worksheets

The supporting worksheets vary by form version. Scan `wb.sheetnames` to see what's available for a given project.

**Common to both V4.8 and V5.6+:**

| Sheet | Purpose |
|-------|---------|
| Thermal Bridges | Annotated details showing potential thermal bridge locations with reviewer/CPHC dialog |
| DHW Pipe Lengths | Domestic hot water piping takeoff data with file references |
| Targets | Phius certification performance targets for the project |
| Geometry | Geometry review notes with annotated detail references |
| Phius 2021 EV | Electric vehicle charging requirements calculator |
| Windows | Window type parameter data |
| UEF to EF | Water heater efficiency conversion equations |
| HP Average COP | Heat pump average COP calculator |

**V5.6+ specific sheets:**

| Sheet | Purpose |
|-------|---------|
| Win Rev | Window dimension and parameter review — compares WUFI entries against documentation |
| ERVs | Energy Recovery Ventilator unit data — MERV ratings, efficiencies, electric efficiency |
| THERM Review | Checklist for 2D thermal bridge calculations |
| HW Storage - No Rating | Hot water storage tank loss calculations |
| Materials | Reference table of material R-values and boundary conditions |
| Heat Pumps | Heat pump performance data |
| Radon Zone Data | County-level radon zone lookup (large dataset) |
| Options(2018_2021) | Dropdown options for the 2018/2021 certification standards |

**V4.8 specific sheets:**

| Sheet | Purpose |
|-------|---------|
| Wall Assignment | Wall type assignment review |
| Site Shading | Site shading geometry review |
| Units | Unit type/count by floor |
| TB | Thermal bridge point/linear calculations |
| HP | Heat pump detailed data |
| Ventilation | Ventilation system review |
| Ducts | Duct takeoff review |
| Ventacity sheets | Product-specific ERV performance data |
| AHRI 1060 Interpolation | AHRI standard interpolation |
| Options | Dropdown options (combined, older format) |

Note: Some V4.8 workbooks have duplicate sheet names with a "(2)" suffix (e.g., "Geometry (2)", "DHW Pipe Lengths (2)"). The "(2)" version is typically the more current one — check dates or content to confirm.

## Main Sheet Column Layout

### Header Area (Rows 1-3)

- **Row 2**: Title ("Phius Design Feedback - V{X}"), plus dates for each review round starting at Column G
- **Row 3**: Column headers — "Certifier Comments" and "Response" alternating from Column G onward

### Column Structure

| Column | Content |
|--------|---------|
| B | **Major Section** headers (e.g., "Localization / Climate", "Building", "Wall Components", "Systems") |
| C | **Sub-section** (e.g., "General", "Assembly", "Surface", "Report: data & results") |
| D | **Item identifier** (e.g., assembly type "RT-01", "WT-04.E", "ST-06", device names) |
| E | **Parameter category** (e.g., "Geometry", "Parameters", "Basic Parameters", "Frame Parameters") |
| F | **Specific field** being reviewed (e.g., "U-glass:", "Framing:", "Heating Demand:", "Floor Slab Area:") |
| G | R1 Certifier Comments |
| H | R1 CPHC Response |
| I | R2 Certifier Comments |
| J | R2 CPHC Response |
| K | R3 Certifier Comments |
| L | R3 CPHC Response |
| M | R4 Certifier Comments |
| N | R4 CPHC Response |
| O | R5 Certifier Comments |
| P | R5 CPHC Response |
| ... | Pattern continues for additional rounds |

**Important**: The exact starting column for review rounds and which round maps to which column pair is consistent within a project but may shift between projects or form versions. Always read Row 3 to confirm the "Certifier Comments" / "Response" pattern and Row 2 for the dates.

### Major Sections (Column B)

The Feedback Form follows the WUFI-Passive model structure:

1. **Project** (Row ~4): Project metadata — submitter, CPHC name/number, verifier, address
2. **Case** (Row ~16): Certification criteria, general case info
3. **Localization / Climate** (Row ~27): Climate data, source energy factors
4. **Building** (Row ~42): Geometry, plan/section dimensions, orientation
5. **PH Case** (Row ~47): Building parameters — occupancy, airtightness, ventilation type, indoor temps
6. **Zone 1** (Row ~77): Volume, iCFA, heat capacity, foundation interface
7. **Visualized Components** (Row ~81): The bulk of the form
   - **Roof Components** (~82): Roof assembly types (RT-xx)
   - **Wall Components** (~105): Wall assembly types (WT-xx)
   - **Opaque Door** (~155): Door assemblies
   - **Floor / Slab Components** (~160): Slab types (ST-xx)
   - **Window Components** (~174): Window types, parameters, solar protection, shading
8. **Not Visualized Components** (~229): Thermal bridges, construction/ambient psi-values
9. **Internal Loads / Occupancy** (~276): Lighting, appliances, plug loads, occupancy
10. **Ventilation / Rooms** (~323): ERV/HRV units, ductwork, room ventilation assignments
11. **Attached Zones** (~429): Unconditioned adjacent spaces
12. **Remaining Elements** (~431): Miscellaneous items
13. **Systems** (~433): HVAC systems, DHW, renewable energy, distribution
14. **SECTION 1: Drawings** (~550): Drawing documentation checklist
15. **SECTION 2: Additional Requirements** (~568): Radon, Appendix K & L

## Parsing Strategy

### Step 1: Identify Version and Active Sheet

```python
import openpyxl
wb = openpyxl.load_workbook(path, data_only=True)

# Find the main feedback sheet — skip legacy 2015 sheets
main_sheet = None
for name in wb.sheetnames:
    if 'Feedback' in name and '2015' not in name:
        main_sheet = wb[name]
        break

# Read the form version from B2
version_string = str(main_sheet['B2'].value)  # e.g. "PHIUS+ FEEDBACK - V4.8" or "Phius Design Feedback - V5.6"
# Extract version number
import re
version_match = re.search(r'V(\d+\.\d+)', version_string)
form_version = float(version_match.group(1)) if version_match else None
# form_version will be 4.8, 5.6, 5.7, etc.
```

### Step 2: Identify Review Round Columns

```python
# Row 3 contains "Certifier Comments" and "Response" headers
# Find all column pairs
round_columns = []
for col in range(7, main_sheet.max_column + 1):  # Start at G
    header = main_sheet.cell(row=3, column=col).value
    if header and 'Certifier' in str(header):
        # This column is certifier, next column is response
        round_columns.append({
            'certifier_col': col,
            'response_col': col + 1,
            'date': main_sheet.cell(row=2, column=col).value
        })
```

### Step 3: Determine the Latest Round

The latest round with content is typically the last pair that has non-empty cells. The most recent certifier column with actual comments represents the current review round.

### Step 4: Parse Row by Row

For each row, build a context path from columns B through F:
```
Section (B) > Sub-section (C) > Item (D) > Category (E) > Field (F)
```

Many of these cells use ditto marks (`"`) to mean "same as above." When you encounter a `"`, look upward in that column to find the actual value. Build a running context as you iterate rows.

### Step 5: Classify Status

For each row that has content in the latest certifier column:

```python
def classify_status(certifier_comment, response_comment):
    if not certifier_comment or certifier_comment.strip() in ['-', '']:
        return 'no_action'

    comment = str(certifier_comment).strip()

    if comment == '"':
        return 'ditto'  # Same as row above

    # Check for resolved
    if comment.lower().startswith('ok'):
        return 'resolved'
    if comment.lower().startswith('n/a'):
        return 'resolved'

    # Check for explicitly pending
    if 'pending' in comment.lower():
        return 'pending'

    # Check for questions / action items
    if '?' in comment or 'please' in comment.lower():
        return 'action_needed'

    # Has content but ambiguous — flag for review
    return 'needs_review'
```

## File Path Cross-References

The Feedback Form contains many Dropbox-relative file paths in both certifier and CPHC response columns. These look like:

```
.../Dropbox/{ProjectFolder}/2. Datasheets & Specs/1. HVAC/2. Ventilation/ERV 1-1_1-5.pdf
```

or sometimes shortened to:

```
See: .../2. Datasheets & Specs/4. Insulation/1. Rigid/...
```

To resolve these to actual files in the mounted workspace:
1. Extract the path portion after the project folder name
2. Search the workspace for matching files
3. Use fuzzy matching if the exact filename doesn't match (files may have been renamed between rounds)

## Tips

- Empty cells and cells containing only `-` can be skipped when summarizing
- The form is often very wide — focus on the latest 1-2 review round column pairs for current status
- Assembly type codes (RT-01, WT-04.E, ST-06) are the primary identifiers for building components
- When the CPHC references a file, the reviewer typically confirms it in the next round with "Ok, per datasheet provided" or similar
- Values in the form (R-values, U-values, efficiencies) are in IP units unless otherwise noted
