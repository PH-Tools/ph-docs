# piping

PHX Water Piping Distribution Objects.

**Source**: `PHX/piping.py`

---

## PhxRecirculationParameters

No description available.

---

## PhxPipeSegment

An individual Pipe Segment.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `diameter_mm` | — | — |
| `diameter_inner_m` | — | — |
| `diameter_outer_m` | — | Return the outside diameter including the pipe wall thickness. |
| `diameter_with_insulation_m` | — | — |
| `length_m` | — | — |
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

A Pipe Element / Run made of one or more PhxPipeSegments.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `segments` | — | — |
| `length_m` | — | Return the total length of all the Pipe Segments. |
| `weighted_pipe_heat_loss_coefficient` | — | Return a length-weighted total heat loss coefficient (W/mk) |
| `weighted_diameter_mm` | — | Return a length-weighted total diameter (mm) |
| `material` | — | — |
| `demand_recirculation` | — | — |

### Methods

#### add_segment(_s)

| Arg | Type | Description |
|-----|------|-------------|
| `_s` | — | — |

---

## PhxPipeBranch

A Pipe Branch made of one or more Fixture-pipes (PhxPipeElement).

### Methods

#### add_fixture(_f)

| Arg | Type | Description |
|-----|------|-------------|
| `_f` | — | — |

---

## PhxPipeTrunk

A Pipe Trunk made of one or more Pipe Branches (PhxPipeBranch).

### Methods

#### add_branch(_b)

| Arg | Type | Description |
|-----|------|-------------|
| `_b` | — | — |

---
