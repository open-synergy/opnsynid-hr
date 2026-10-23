# Deactivate Employee

> **Module:** `ssi_hr`\
> **Model:** `hr.employee`\
> **Menu:** Human Resource > Employees\
> **Actor:** user in group _Employee_\
> **Active:** `true` → `false`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The employee is currently active.
- **Access:** User is in group _Employee_.

## Flow

1. Open the **Human Resource > Employees** menu.
2. Find and open the record to deactivate.
3. Click the **Action** menu, then click **Archive**.
4. Click **OK** on the confirmation dialog.
5. In the **Register Departure** dialog that appears, fill in the departure data:
   - **Departure Reason**: Select the reason, for example _Fired_, _Resigned_, or
     _Retired_.
   - **Additional Information**: Enter any additional information. Optional.
   - **Archive Private Address**: Keep it checked to archive the private address of the
     employee as well.
   - **Departure Date** _(required)_: Enter the last working date of the employee.
6. Click **Save**. Click **Only Employee** instead to archive the employee without
   registering the departure data.

## Post-Condition

- The employee is archived and no longer appears in the default Employees list.
- The departure reason, additional information, and departure date are stored on the
  employee when the departure was registered with **Save**.
- Documents that already use this employee can still be viewed.
