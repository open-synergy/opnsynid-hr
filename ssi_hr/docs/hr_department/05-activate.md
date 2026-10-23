# Activate Department

> **Module:** `ssi_hr`\
> **Model:** `hr.department`\
> **Menu:** Human Resource > Configuration > Organization > Departments\
> **Actor:** user in group _Department_\
> **Active:** `false` → `true`\
> **Requires:** `04-deactivate`

## Pre-Condition

- **Record:** The department is currently archived.
- **Access:** User is in group _Department_.

## Flow

1. Open the **Human Resource > Configuration > Organization > Departments** menu.
2. Enable the **Archived** filter in the search bar.
3. Find and open the record to reactivate.
4. Click the **Action** menu, then click **Unarchive**.

## Post-Condition

- The department is restored and appears again in the default Departments list.
