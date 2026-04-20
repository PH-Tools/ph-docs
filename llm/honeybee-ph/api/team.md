# team

Project Team-Member Classes.

**Source**: `honeybee_ph/team.py`

---

## ProjectTeamMember

No description available.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `name` | — | — |
| `street` | — | — |
| `city` | — | — |
| `post_code` | — | — |
| `telephone` | — | — |
| `email` | — | — |
| `license_number` | — | — |

---

## ProjectTeam

No description available.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `customer` | `ProjectTeamMember` | — |
| `building` | `ProjectTeamMember` | — |
| `owner` | `ProjectTeamMember` | — |
| `designer` | `ProjectTeamMember` | — |
| `project_date` | `str` | — |
| `owner_is_client` | `bool` | — |
| `year_constructed` | `int` | — |
| `image` | `Optional[unknown]` | — |

---
