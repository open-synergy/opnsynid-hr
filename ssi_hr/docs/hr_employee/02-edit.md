# Edit Employee

> **Module:** `ssi_hr`\
> **Model:** `hr.employee`\
> **Menu:** Human Resource > Employees\
> **Actor:** user in group _Employee_\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The employee is active.
- **Access:** User is in group _Employee_.

## Flow

1. Open the **Human Resource > Employees** menu.
2. Find and open the record to edit.
3. Click the **Edit** button.
4. Change the required fields, for example **Employee's Name**, **Department**, or
   **Manager**. **Initials** follows **Employee's Name** automatically, unless it was
   changed manually before; set **Initials** to change it explicitly.
5. Click **Save**.

## Post-Condition

- The record is updated with the new values.
