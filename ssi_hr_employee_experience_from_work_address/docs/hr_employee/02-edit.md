# Edit Employee

> **Module:** `ssi_hr_employee_experience_from_work_address`\
> **Extends:** ssi_hr — model `hr.employee`, aksi `02-edit`

## Additional Pre-Condition

- **Record:** The employee has a **Home Address**. The three experience lists below are
  stored on the **Home Address** contact, so they cannot be filled in while it is empty.

## Additional Fields

When this module is installed, the employee form gains an **Experiences** tab. It is
visible when the record is opened, and its lists become editable after the **Edit**
button is clicked (Flow step 3 of the base work instruction). The tab contains three
lists, each stored on the **Home Address** contact of the employee:

- **Academics**: Academic history of the employee. Add a line to fill in the
  **Institution**, **Diploma**, **Education Level**, **Field of Study**, **Start Date**,
  and **End Date**. Optional.
- **Certifications**: Certifications held by the employee. Add a line to fill in the
  **Certification**, **# Certificate**, **Issued By**, **Start Date**, and **End Date**.
  Optional.
- **Professional Experiences**: Work history of the employee. Add a line to fill in the
  **Job Position**, **Job Level**, **Employer**, **Start Date**, and **End Date**.
  Optional.

## Additional Post-Condition

- The lines added, changed, or removed in the **Experiences** tab are saved on the
  **Home Address** contact of the employee, not on the employee record itself.
