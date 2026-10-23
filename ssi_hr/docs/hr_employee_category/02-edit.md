# Edit Employee Tag

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
2. Click the row of the tag to edit. The row becomes editable.
3. Change **Tag Name**.
4. Click the **Save** button of the list.

## Post-Condition

- The record is updated with the new value.
