# Deactivate Department

> **Module:** `ssi_hr`\
> **Model:** `hr.department`\
> **Menu:** Human Resource > Configuration > Organization > Departments\
> **Actor:** user in group _Department_\
> **Active:** `true` → `false`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The department is currently active.
- **Access:** User is in group _Department_.

## Flow

1. Open the **Human Resource > Configuration > Organization > Departments** menu.
2. Find and open the record to deactivate.
3. Click the **Action** menu, then click **Archive**.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- The department is archived and no longer appears in the default Departments list.
- Employees and documents that already use this department can still be viewed.
