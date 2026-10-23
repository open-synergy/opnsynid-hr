# Delete Employee Tag

> **Module:** `ssi_hr`\
> **Model:** `hr.employee.category`\
> **Menu:** Human Resource > Configuration > Employee > Tags\
> **Actor:** user in group _Employee Tags_ (the menu is shown to users in group _Job Position_)\
> **Requires:** `01-create`

## Pre-Condition

- **Access:** User is in group _Job Position_, which shows the **Tags** menu.
- **Access:** User is in group _Employee Tags_, which grants the right to create, edit,
  and delete tags.

## Flow

1. Open the **Human Resource > Configuration > Employee > Tags** menu.
2. Select one or more tags to delete (check the checkbox).
3. Click the **Action** menu, then click **Delete**.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- The selected tags are removed from the Tags list and from the employees that used
  them.
