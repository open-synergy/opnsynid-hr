# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "HR Payroll - Configuration Page",
    "version": "8.0.1.0.0",
    "category": "Hidden",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "auto_install": True,
    "depends": [
        "hr_payroll",
    ],
    "data": [
        "views/hr_payroll_config_setting_views.xml",
    ],
}
