# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "HR Payslip Compute Sheet",
    "version": "8.0.1.0.0",
    "summary": "Adds wizard to compute sheet",
    "category": "Human Resources",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": ["hr_payroll"],
    "data": [
        "wizards/hr_compute_sheet_views.xml",
        "views/hr_payslip_views.xml",
        "data/ir_values_data.xml",
    ],
}
