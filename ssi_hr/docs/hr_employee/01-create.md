# Create Employee

> **Module:** `ssi_hr`\
> **Model:** `hr.employee`\
> **Menu:** Human Resource > Employees\
> **Actor:** user in group _Employee_

## Pre-Condition

- **Access:** User is in group _Employee_.

## Flow

1. Open the **Human Resource > Employees** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required field:
   - **Employee's Name** _(required)_: Enter the full name of the employee.
4. Fill in the optional fields as needed:
   - **Job Title**: Enter the job title of the employee.
   - **Tags**: Select one or more employee tags.
   - **Initials**: Automatically filled from **Employee's Name**. Change if needed.
   - **Work Mobile**, **Work Phone**, **Work Email**: Enter the work contact details.
   - **Department**, **Manager**, **Coach**: Select the organization data of the
     employee.
5. Click **Save**.

## Post-Condition

- A new employee record is created.
- **Initials** shows the initials generated from the employee name. Once the initials
  are changed manually, they are no longer overwritten when the name changes.
