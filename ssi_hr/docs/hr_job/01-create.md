# Create Job Position

> **Module:** `ssi_hr`\
> **Model:** `hr.job`\
> **Menu:** Human Resource > Configuration > Organization > Job Positions\
> **Actor:** user in group _Job Position_\
> **State:** `—` → `recruit`

## Pre-Condition

- **Data:** Optionally, the department of the job position already exists.
- **Access:** User is in group _Job Position_.

## Flow

1. Open the **Human Resource > Configuration > Organization > Job Positions** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required field:
   - **Job Position** _(required)_: Enter the name of the job position. The name must be
     unique per department in the company.
4. On the **Recruitment** tab, fill in the optional fields as needed:
   - **Department**: Select the department of the job position.
   - **Expected New Employees**: Enter the number of employees to recruit.
5. On the **Job Description** tab, enter the job description. Optional. The description
   is only shown while the status is _Recruitment in Progress_.
6. Click **Save**.

## Post-Condition

- A new job position is created in **Recruitment in Progress** status.
