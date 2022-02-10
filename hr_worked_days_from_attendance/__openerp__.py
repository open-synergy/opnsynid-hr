# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Worked Days From Attendance",
    "summary": "Compute worked days from attendance",
    "version": "8.0.1.0.1",
    "category": "Human Resources",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "hr_timesheet_sheet",
        "hr_payroll",
    ],
    "data": [
        "views/hr_payslip_view.xml",
    ],
}
