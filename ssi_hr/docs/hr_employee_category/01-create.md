# Create Employee Tag

> **Module:** `ssi_hr`\
> **Model:** `hr.employee.category`\
> **Menu:** Human Resource > Configuration > Employee > Tags\
> **Actor:** user in group _Employee Tags_ (the menu is shown to users in group _Job Position_)

## Pre-Condition

- **Access:** User is in group _Job Position_, which shows the **Tags** menu.
- **Access:** User is in group _Employee Tags_, which grants the right to create, edit,
  and delete tags.

## Flow

1. Open the **Human Resource > Configuration > Employee > Tags** menu.
2. Click the **New** button. **(14.0: "Create")** An editable row is added at the bottom
   of the list.
3. Fill in the required field in the new row:
   - **Tag Name** _(required)_: Enter the name of the tag.
4. Click the **Save** button of the list.

## Post-Condition

- A new tag is created and is listed in **Tags**.
- The tag can be selected in the **Tags** field of an employee.
