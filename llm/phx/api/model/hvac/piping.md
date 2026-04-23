# piping

PHX DHW piping distribution objects.

**Source**: `PHX/piping.py`

---

## PhxRecirculationParameters

Global DHW recirculation piping parameters used by the simplified PHPP method.

---

## PhxPipeSegment

An individual pipe segment with geometry, material, diameter, and insulation properties.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `diameter_mm` | — | Inner pipe diameter converted to millimeters. |
| `diameter_inner_m` | — | Inner pipe diameter (m), alias for diameter_m. |
| `diameter_outer_m` | — | Return the outside diameter including the pipe wall thickness. |
| `diameter_with_insulation_m` | — | Total outer diameter including pipe wall and insulation (m). |
| `length_m` | — | Segment length derived from the line geometry (m). |
| `pipe_heat_loss_coefficient` | — | Return the pipe's heat-loss-coefficient (W/mk) considering the diameter and insulation. |

### Methods

#### reverse_solve_for_insulation_conductivity(target_result, starting_conductivity)

Return an insulation conductivity (W/mk) when given a known heat-loss-coeff (W/MK).

| Arg | Type | Description |
|-----|------|-------------|
| `target_result` | — | — |
| `starting_conductivity` | — | — |

#### *classmethod* from_length(display_name, length_m, pipe_material, pipe_diameter_m)

Create a Pipe Segment from a length value (m).

| Arg | Type | Description |
|-----|------|-------------|
| `display_name` | — | — |
| `length_m` | — | — |
| `pipe_material` | — | — |
| `pipe_diameter_m` | — | — |

---

## PhxPipeElement

A pipe element (run) composed of one or more PhxPipeSegment objects.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `segments` | — | — |
| `length_m` | — | Return the total length of all the Pipe Segments. |
| `weighted_pipe_heat_loss_coefficient` | — | Return a length-weighted total heat loss coefficient (W/mk) |
| `weighted_diameter_mm` | — | Return a length-weighted total diameter (mm) |
| `material` | — | Return the single pipe material shared by all segments. Raises ValueError if mixed. |
| `demand_recirculation` | — | Always False for standard pipe elements (overridden in trunk). |

### Methods

#### add_segment(_s)

Add a pipe segment to this element.

| Arg | Type | Description |
|-----|------|-------------|
| `_s` | — | The pipe segment to add. |

---

## PhxPipeBranch

A DHW pipe branch connecting a trunk to one or more fixture twigs.

### Methods

#### add_fixture(_f)

Append a fixture (twig) pipe element to this branch.

| Arg | Type | Description |
|-----|------|-------------|
| `_f` | — | — |

---

## PhxPipeTrunk

A DHW pipe trunk (riser/main) serving one or more branches.

### Methods

#### add_branch(_b)

Append a branch pipe to this trunk.

| Arg | Type | Description |
|-----|------|-------------|
| `_b` | — | — |

---
