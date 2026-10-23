# Edit Employee

> **Module:** `ssi_hr_employee_language_from_work_address`\
> **Extends:** ssi_hr — model `hr.employee`, aksi `02-edit`

## Additional Pre-Condition

- **Record:** The employee has a **Home Address**. The languages below are stored on the
  **Home Address** contact, so they cannot be filled in while it is empty.

## Additional Fields

When this module is installed, the employee form gains a **Languages** tab. It is
visible when the record is opened, and its list becomes editable after the **Edit**
button is clicked (Flow step 3 of the base work instruction). The tab contains one list,
stored on the **Home Address** contact of the employee. Each line has these fields:

- **Language** _(required)_: Language spoken by the employee.
- **Reading** _(required)_: Reading proficiency rating.
- **Writing** _(required)_: Writing proficiency rating.
- **Speaking** _(required)_: Speaking proficiency rating.
- **Listening** _(required)_: Listening proficiency rating.

## Additional Post-Condition

- The lines added, changed, or removed in the **Languages** tab are saved on the **Home
  Address** contact of the employee, not on the employee record itself.
