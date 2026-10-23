# Stop Recruitment of Job Position

> **Module:** `ssi_hr`\
> **Model:** `hr.job`\
> **Menu:** Human Resource > Configuration > Organization > Job Positions\
> **Actor:** user in group _Job Position_\
> **State:** `recruit` → `open`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Recruitment in Progress**.
- **Access:** User is in group _Job Position_.

## Flow

1. Open the **Human Resource > Configuration > Organization > Job Positions** menu.
2. Find and open the record whose status is **Recruitment in Progress**.
3. Click the **Stop Recruitment** button.

## Post-Condition

- The status changes to **Not Recruiting**.
- **Expected New Employees** and **Hired Employees** are reset to 0.
