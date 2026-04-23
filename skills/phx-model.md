---
name: phx-model
description: "Navigate, understand, modify, and test PHX (Passive House Exchange) model classes. Use when working with PHX model entities such as: PhxProject, PhxVariant, PhxBuilding, PhxZone, PhxSpace, PhxComponentOpaque, PhxComponentAperture, PhxConstructionOpaque, PhxConstructionWindow, PhxMaterial, PhxMechanicalSystemCollection, or any PHX model class. Also trigger when discussing building model elements like walls, floors, roofs, windows, thermal bridges, assemblies, constructions, HVAC devices, ventilation, spaces, zones, or certification data in the context of PHX or Passive House modeling. Useful across the PHX repo, GUI packages (Rhino/Grasshopper), and any codebase that creates or consumes PHX models."
---

# PHX Model Navigation

PHX models are in-memory-only intermediate representations of Passive House building data. They are created from source formats (HBJSON, WUFI XML) and consumed by exporters (WUFI XML, PHPP, PPP, METr JSON).

## Load the Reference Doc

At the start of a PHX model task, fetch the canonical model reference. This contains the full object graph, module map, design patterns, Honeybee↔PHX mapping, and testing patterns:

```
WebFetch https://docs.passivehousetools.com/llm/phx/reference/phx-model-reference.md
```

This is the single source of truth — it consolidates the model hierarchy, honeybee mapping, and testing patterns into one document.

**Related docs** (fetch if the task involves these areas):
- WUFI XML schema/fields: `https://docs.passivehousetools.com/llm/phx/reference/wufi-xml-schema.md`
- PHX architecture overview: `https://docs.passivehousetools.com/llm/phx/dev/architecture.md`
- Exporter/importer patterns: `https://docs.passivehousetools.com/llm/phx/dev/exporter-patterns.md`
- PHPP field mapping: `https://docs.passivehousetools.com/llm/phx/reference/phpp-field-mapping.md`

**If the fetch fails** (offline, URL unreachable), the quick lookup table and key patterns below are sufficient for most tasks. For discovery, try `https://docs.passivehousetools.com/llm-instructions.md`.

## Workflow Decision Tree

Determine the task type, then follow the appropriate workflow:

**Understanding model structure?** Fetch the reference doc above and read the Object Graph section.

**Mapping Honeybee concepts to PHX?** Fetch the reference doc above and read the Honeybee to PHX Concept Mapping section.

**Writing or modifying tests?** Fetch the reference doc above and read the Testing Patterns section.

**Adding or modifying a model class?** Follow the "Modifying Model Classes" checklist below.

**Tracing data through the model?** Follow the "Navigation" guide below.

## Navigation

To find where a concept lives in the PHX model, use the hierarchy: **Project → Variant → Building → Zone → Space** (for room-level data) or **Project → Variant → Building → Components** (for surfaces/geometry).

### Quick Lookup

| You want to find... | Navigate to... |
|---------------------|----------------|
| Wall/floor/roof surfaces | `PhxBuilding._components` (list of `PhxComponentOpaque`) |
| Windows in a wall | `PhxComponentOpaque.apertures` (list of `PhxComponentAperture`) |
| Construction/U-value | `PhxComponentOpaque.assembly` → `PhxConstructionOpaque` |
| Material layers | `PhxConstructionOpaque.layers` → `PhxLayer` → `PhxMaterial` |
| Window properties | `PhxComponentAperture.window_type` → `PhxConstructionWindow` |
| Room ventilation rates | `PhxSpace.ventilation` → `PhxProgramVentilation.load` → `PhxLoadVentilation` |
| Occupancy schedule | `PhxSpace.occupancy` → `PhxProgramOccupancy.schedule` |
| Thermal bridges | `PhxZone.thermal_bridges` (dict of `PhxComponentThermalBridge`) |
| HVAC devices | `PhxVariant.mech_collections` → `PhxMechanicalSystemCollection.devices` |
| Hot water piping | `PhxMechanicalSystemCollection` → `PhxPipeTrunk` / `PhxPipeBranch` |
| Electrical equipment | `PhxZone.elec_equipment_collection` → `PhxElectricDeviceCollection` |
| Climate/location | `PhxVariant.site` → `PhxSite` |
| Certification data | `PhxVariant.phius_cert` or `PhxVariant.phi_cert` |
| All assembly types | `PhxProject.assembly_types` (dict by identifier) |
| All window types | `PhxProject.window_types` (dict by identifier) |

### Traversal Example
```python
# Get all window U-values in a project
for variant in project.variants:
    for component in variant.building.all_components:
        if hasattr(component, 'apertures'):
            for aperture in component.apertures:
                print(aperture.window_type.u_value_glazing)

# Get total ventilation airflow for a zone
for zone in variant.building.zones:
    for space in zone.spaces:
        if space.has_ventilation_airflow:
            print(space.ventilation.load.flow_supply)
```

## Modifying Model Classes

Follow this checklist when adding or changing model classes:

1. **Location**: Place in appropriate module under `PHX/model/` (see module map in the reference doc)
2. **Pattern**: Use `@dataclass` with `ClassVar[int] _count = 0` for auto-incrementing `id_num`. Exception: `PhxComponentBase` subclasses use plain `__init__`
3. **Identity**: Include both `identifier: str` (UUID) and `id_num: int` (counter-based) if the class will be referenced by other objects
4. **Merging**: Implement `__add__` if instances may need consolidation (surfaces, spaces, devices)
5. **Grouping**: Add `unique_key` property if instances should be groupable by construction/type
6. **Counter reset**: Add `ClassName._count = 0` to `_reset_phx_class_counters()` in `tests/conftest.py`
7. **Module reload**: Add `importlib.reload(module)` to `_reload_phx_classes()` in `tests/conftest.py` if needed for reference-case tests
8. **Enums**: Place in `model/enums/` in the appropriate file (or create new one)
9. **Collections**: Use dict-keyed for lookup access, list for ordered iteration
10. **Tests**: Mirror source structure in `tests/test_model/`; use `reset_class_counters` fixture

## Key Patterns to Preserve

- **Program = Load + Schedule**: Never store loads and schedules separately at the space level. Always compose as `PhxProgram*`
- **Library references**: Constructions/windows live in project-level dicts; components reference them by identifier, not by embedding
- **`_count` incrementing**: Always in `__post_init__` (dataclass) or `__init__` (component classes). Never skip this
- **PascalCase in xml_schemas/xml_writables**: Intentional — matches WUFI XML/C# naming. Do not rename to snake_case
