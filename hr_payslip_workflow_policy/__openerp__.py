# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "HR Payslip - Workflow Policy",
    "version": "8.0.1.0.0",
    "category": "Human Resource",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_payroll_configuration_page",
    ],
    "data": [
        "views/hr_payroll_config_setting_views.xml",
        "views/hr_payslip_views.xml",
        "views/hr_payslip_run_views.xml",
    ],
}
