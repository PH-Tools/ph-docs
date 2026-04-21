# certification

PHX Passive House Certification Classes

**Source**: `PHX/certification.py`

---

## PhxSetpoints

Indoor temperature setpoints for heating and cooling seasons.

---

## PhxSummerVentilation

Summer ventilation strategy parameters for overheating prevention.

---

## PhxPhBuildingData

General building-level data used by both PHI and Phius certification paths.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `wind_coefficient_e` | — | Wind pressure coefficient E, used for calculating infiltration due to wind pressure. |

### Methods

#### add_foundation(_input)

Append a foundation element to this building's foundation collection.

| Arg | Type | Description |
|-----|------|-------------|
| `_input` | — | The foundation to add. None values are ignored. |

---

## PhxPhiusCertificationCriteria

Phius certification performance target thresholds.

---

## PhxPhiusCertificationSettings

Phius certification program and building classification settings.

---

## PhxPhiusCertification

Top-level container for all Phius certification data.

---

## PhxPhiCertificationSettings

PHI (Passive House Institute) certification program settings for PHPP 9+.

---

## PhxPhiCertification

Top-level container for PHI (Passive House Institute) certification data.

---
