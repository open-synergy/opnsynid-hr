# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Human Resource - Payslip Type",
    "version": "8.0.1.0.0",
    "category": "Human Resource",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_payroll"
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/hr_payslip_type_data.xml",
        "views/hr_payslip_type_views.xml",
        "views/hr_payslip_views.xml",
        "views/hr_payslip_run_views.xml"
    ],
}
