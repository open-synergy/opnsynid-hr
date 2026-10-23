# Create Department

> **Module:** `ssi_hr`\
> **Model:** `hr.department`\
> **Menu:** Human Resource > Configuration > Organization > Departments\
> **Actor:** user in group _Department_

## Pre-Condition

- **Data:** Optionally, the employee who will become the manager already exists.
- **Access:** User is in group _Department_.

## Flow

1. Open the **Human Resource > Configuration > Organization > Departments** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required field:
   - **Department Name** _(required)_: Enter the name of the department.
4. Fill in the optional fields as needed:
   - **Manager**: Select the employee who manages the department.
   - **Parent Department**: Select the department above this department.
5. Click **Save**.

## Post-Condition

- A new department is created and is listed in **Departments**.
