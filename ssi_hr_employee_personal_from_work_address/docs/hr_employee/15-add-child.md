# Add Child — Employee

> **Module:** `ssi_hr_employee_personal_from_work_address`\
> **Model:** `hr.employee`\
> **Menu:** Human Resource > Employees\
> **Actor:** user in group _Employee_

## Pre-Condition

- **Record:** The employee has a **Home Address** on the **Private Information** tab.
  The **Add Child** button is hidden while **Home Address** is empty.
- **Access:** User is in group _Employee_.

## Flow

1. Open the **Human Resource > Employees** menu.
2. Open the employee record to add a child to.
3. Click the **Private Information** tab.
4. Click the **Add Child** button (`action_add_child`). The **Add Child** wizard
   appears.
5. Fill in the wizard:
   - **Name** _(required)_: Full name of the child.
   - **Place of Birth**: City where the child was born. Optional.
   - **Birthdate**: Birth date of the child. Optional.
   - **Gender**: Gender of the child. Optional.
6. Click the **Add Child** button in the wizard footer.

## Post-Condition

- The wizard closes and the employee form reloads.
- The child is listed in the **Children** list on the **Private Information** tab, with
  its name, place of birth, birthdate, and gender.
- A new private contact is created for the child. It has no parent company contact, so
  no commercial data of any company is copied onto it.
- The child is linked to the **Home Address** contact of the employee. When the employee
  is **Male**, the **Home Address** contact becomes the child's father; when the
  employee is **Female**, it becomes the child's mother; for any other gender the child
  is only listed under the **Children** of the **Home Address** contact.
- If the employee has no **Home Address**, the wizard refuses to continue with an error
  dialog and nothing is created.
