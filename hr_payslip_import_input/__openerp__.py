# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Import Other Inputs From Payslip Batches",
    "version": "8.0.1.0.0",
    "summary": "Adds wizard to import other inputs from a CSV file",
    "category": "Human Resources",
    "website": "https://opensynergy-indonesia/",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": False,
    "depends": [
        "hr_payroll",
        "hr_employee_id"
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/hr_payslip_import_input.xml",
        "views/hr_payslip_run_views.xml"
    ],
}
