# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Generate Accrue Expense Based On Timesheet Details",
    "version": "8.0.2.0.2",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_timesheet_bypass_check",
        "hr_timesheet_onchange",
    ],
    "data": [
        "views/hr_employee_views.xml",
        "views/account_analytic_account_views.xml",
        "views/hr_analytic_timesheet_views.xml",
    ],
}
