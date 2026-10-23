# Start Recruitment of Job Position

> **Module:** `ssi_hr`\
> **Model:** `hr.job`\
> **Menu:** Human Resource > Configuration > Organization > Job Positions\
> **Actor:** user in group _Job Position_\
> **State:** `open` → `recruit`\
> **Requires:** `05-stop-recruitment`

## Pre-Condition

- **Record:** Status is **Not Recruiting**.
- **Access:** User is in group _Job Position_.

## Flow

1. Open the **Human Resource > Configuration > Organization > Job Positions** menu.
2. Find and open the record whose status is **Not Recruiting**.
3. Click the **Start Recruitment** button.

## Post-Condition

- The status changes to **Recruitment in Progress**.
- **Expected New Employees** is set to 1 when it was 0; otherwise it keeps its value.
