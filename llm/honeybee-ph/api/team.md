# team

Project Team-Member Classes.

**Source**: `honeybee_ph/team.py`

---

## ProjectTeamMember

A single member of the project team (client, owner, designer, etc.).

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `name` | — | Full name of the team member. |
| `street` | — | Street address. |
| `city` | — | City name. |
| `post_code` | — | Postal or ZIP code. |
| `telephone` | — | Phone number. |
| `email` | — | Email address. |
| `license_number` | — | Professional license number. |

---

## ProjectTeam

The collection of team members associated with a Passive House project.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `customer` | `ProjectTeamMember` | The customer or client contact. |
| `building` | `ProjectTeamMember` | The building contact. |
| `owner` | `ProjectTeamMember` | The building owner. |
| `designer` | `ProjectTeamMember` | The project designer or architect. |
| `project_date` | `str` | The project date string. Default: "". |
| `owner_is_client` | `bool` | True if the owner is also the client. Default: False. |
| `year_constructed` | `int` | Year the building was constructed. Default: 0. |
| `image` | `Optional[unknown]` | Project image data. Default: None. |

---
