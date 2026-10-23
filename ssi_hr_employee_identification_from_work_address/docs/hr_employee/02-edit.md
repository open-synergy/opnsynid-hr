# Edit Employee

> **Module:** `ssi_hr_employee_identification_from_work_address`\
> **Extends:** ssi_hr — model `hr.employee`, aksi `02-edit`

## Additional Pre-Condition

- **Record:** The employee has a **Home Address**. The identification numbers below are
  stored on the **Home Address** contact, so they cannot be filled in while it is empty.

## Additional Fields

When this module is installed, the employee form gains an **ID Numbers** tab. It is
visible when the record is opened, and its list becomes editable after the **Edit**
button is clicked (Flow step 3 of the base work instruction). The tab contains one list,
stored on the **Home Address** contact of the employee:

- **ID Numbers**: Identification numbers held by the employee. Add a line to fill in the
  identification number details. Optional.

## Removed / Relaxed

- **Identification No** and **Passport No** are no longer shown on the **Private
  Information** tab. Record the identification and passport numbers in the **ID
  Numbers** tab instead.

## Additional Post-Condition

- The lines added, changed, or removed in the **ID Numbers** tab are saved on the **Home
  Address** contact of the employee, not on the employee record itself.
