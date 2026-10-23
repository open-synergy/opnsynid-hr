# Activate Employee

> **Module:** `ssi_hr`\
> **Model:** `hr.employee`\
> **Menu:** Human Resource > Employees\
> **Actor:** user in group _Employee_\
> **Active:** `false` → `true`\
> **Requires:** `04-deactivate`

## Pre-Condition

- **Record:** The employee is currently archived.
- **Access:** User is in group _Employee_.

## Flow

1. Open the **Human Resource > Employees** menu.
2. Enable the **Archived** filter in the search bar.
3. Find and open the record to reactivate.
4. Click the **Action** menu, then click **Unarchive**.

## Post-Condition

- The employee is restored and appears again in the default Employees list.
- The departure reason, additional information, and departure date are cleared.
- The archived private address of the employee is restored as well.
