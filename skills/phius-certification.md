---
name: phius-certification
description: "Navigate and manage Phius passive building certification project folders, parse Feedback Forms, track review status, and cross-reference documentation. Use this skill whenever the user mentions Phius, WUFI-Passive, passive house certification, feedback forms, review rounds, datasheets, thermal bridges, assembly types, cut-sheets, or any task involving a Phius certification project folder. Also trigger when the user asks about items that are pending, resolved, or need responses in a certification review — even if they don't say 'Phius' explicitly but are clearly working within a Phius project directory structure (numbered folders like '0. WUFI-Passive Energy Model', '1. Drawings & Takeoffs', '2. Datasheets & Specs', etc.)."
---

# Phius Certification Project Navigator

You are helping a Phius CPHC (Certified Passive House Consultant) manage building energy certification projects. The user creates WUFI-Passive energy models and manages the documentation collection process for Phius review. Your job is to help them navigate the project folder, parse the Feedback Form, track what's resolved vs. pending, and cross-reference file paths to actual documentation.

## Load the Reference Docs

At the start of a Phius certification task, fetch the canonical guides. These contain the complete project folder structure map and Feedback Form parsing strategies:

```
WebFetch https://docs.passivehousetools.com/llm/guides/phius-certification/folder-map.md
WebFetch https://docs.passivehousetools.com/llm/guides/phius-certification/feedback-form-guide.md
```

These are the single source of truth — they consolidate the folder hierarchy, Excel parsing rules, and file conventions into two documents.

**If the fetch fails** (offline, URL unreachable), the quick-start sections below are sufficient for basic navigation. For discovery, try `https://docs.passivehousetools.com/llm-instructions.md`.

## Quick Start: Two-Folder Architecture

Each Phius project has **two separate Dropbox folders**:

| Folder | Purpose | Content |
|--------|---------|---------|
| **Working Folder** `~/Dropbox/bldgtyp/<project>/` | CPHC's internal project folder | Rhino, PHPP/WUFI files, admin, backups, scripts |
| **Certification Folder** `~/Dropbox/<project>/` | Phius-shared folder at Dropbox root | Final submissions only: WUFI model, PDFs, datasheets, Feedback Form |

**Important**: You will typically be mounted to the **Certification Folder** during certification work, not the working folder. Paths in the Feedback Form reference the certification folder.

## Quick Start: Feedback Form Basics

The Feedback Form is an Excel workbook (`.xlsx`) located in `- Feedback Forms/` (note the leading dash — sorts to top). File naming: `{ProjectNum}_R{Round}_Feedback_V{FormVersion}_{Date}.xlsx`

### Main Sheet Layout

| Column | Contains |
|--------|----------|
| B | Major section (e.g., "Building", "Wall Components", "Systems") |
| C | Sub-section (e.g., "Assembly", "Parameters") |
| D | Item (assembly type like RT-01, WT-04.E, ST-06) |
| E | Category (e.g., "Geometry", "Basic Parameters") |
| F | Specific field (e.g., "U-glass:", "Framing:") |
| G onward | Alternating Certifier Comments / CPHC Response columns, one pair per review round |

### Interpreting Review Status

- **Resolved**: Certifier's comment starts with "Ok" (most recent round)
- **Pending**: Certifier says "Pending" or asks a question (look for ?, "please confirm", "please provide")
- **No action**: Dash "-" means not applicable or no change
- **Ditto**: Quotation mark `"` means same as the row above — look up to find actual value

## Working with Files

The certification folder contains primarily PDFs (~90%): drawings, cut-sheets, WUFI reports, Flixo thermal calculations, specifications. Also Excel files (~10%): Feedback Form, Phius calculators (MF Calculator, Blinds Calculator, HSPF Deration, etc.), takeoffs, and room data.

### Cross-Referencing File Paths

The Feedback Form references files with Dropbox-relative paths like:
```
.../Dropbox/2441-Arverne East (Building D)_Edwin May/2. Datasheets & Specs/1. HVAC/2. Ventilation/ERV 1-1_1-5.pdf
```

When the user has mounted the certification folder, translate these by:
1. Stripping everything up to and including the project folder name
2. Prepending the workspace mount path (usually `.` for current directory)

Result: `2. Datasheets & Specs/1. HVAC/2. Ventilation/ERV 1-1_1-5.pdf`

### Reading the Feedback Form Programmatically

Use `openpyxl` (install with `pip install openpyxl --break-system-packages` if needed):

```python
import openpyxl
wb = openpyxl.load_workbook(path, data_only=True)

# Find main feedback sheet — skip 2015 legacy sheets
main_sheet = None
for name in wb.sheetnames:
    if 'Feedback' in name and '2015' not in name:
        main_sheet = wb[name]
        break

# Get form version from B2
version_string = str(main_sheet['B2'].value)  # e.g., "Phius Design Feedback - V5.6"

# Row 3 contains header structure ("Certifier Comments", "Response")
# Columns start at G (R1), I (R2), K (R3), etc.
```

## Common Tasks

### 1. Summarize Review Status
Parse the Feedback Form and count: resolved items (Ok), pending items (needs response), no-action items (dashes). Identify which sections have the most open work.

### 2. Find Open Items in a Section
Filter to a specific section (e.g., "Wall Components") and list items where the latest certifier comment isn't "Ok".

### 3. Cross-Reference a File
When the Feedback Form cites a file path, verify it exists in the mounted workspace and optionally read it (PDF skill, or openpyxl for Excel) to confirm the value referenced.

### 4. Navigate Folder Structure
Locate files: "Where's the ERV datasheet for unit 1-3?" → search in `2. Datasheets & Specs/1. HVAC/2. Ventilation/`.

### 5. Work Through Open Items
For each action-needed item:
- Locate the referenced file in the project folder
- Read the PDF/document to verify or extract the value the certifier is asking about
- Draft a response referencing the correct file path
- Help update the Feedback Form response column

## Important Context

- Assembly types follow Phius naming: RT = Roof Type, WT = Wall Type, ST = Slab Type
- Thermal bridge calculations use Flixo (2D) or THERM software — results are in `3. Calculations/`
- WUFI-Passive model files (.mwp) are binary; read WUFI Report PDFs instead (in `0. WUFI-Passive Energy Model/{date} - WUFI Report PDFs/`)
- Form versions include V4.8 (older) and V5.6+ (current). The reference doc covers both.
- Previous rounds are in `_Archive` folders — current files are always at parent level
- File naming often uses YYMMDD format (e.g., `240625_Phius_MF_Calculator.xlsx` = June 25, 2024)

## Related Resources

- **WUFI-Passive XML verification**: Use the `wufi-xml` skill if you need to verify values in the energy model against feedback items
- **PDF extraction**: Use the `pdf` skill to read cut-sheets and draw comparisons to Feedback Form data
- **LLM Setup Guide**: General instructions for using these reference docs with AI tools
