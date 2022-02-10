# -*- coding: utf-8 -*-
# Copyright 2018-2019 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Payslip Integration With Timesheet Computation",
    "version": "8.0.1.0.1",
    "category": "Human Resource",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_payroll",
        "hr_timesheet_computation",
    ],
    "data": [
        "views/hr_payslip_views.xml",
    ],
}
