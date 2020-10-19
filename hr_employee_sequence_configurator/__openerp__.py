# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Employee Sequence Configurator",
    "version": "8.0.1.0.0",
    "category": "Human Resource",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_employee_employment_status",
        "base_sequence_configurator",
    ],
    "data": [
        "data/ir_sequence_data.xml",
        "data/base_sequence_configurator_data.xml",
        "views/hr_employment_status_views.xml",
        "views/hr_employee_views.xml",
    ],
    "images": [
        "static/description/banner.png",
    ],
}
