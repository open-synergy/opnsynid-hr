# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Employee Join and Termination Date",
    "version": "8.0.1.2.0",
    "category": "Human Resource",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr",
    ],
    "external_dependencies": {
        "python": [
            "pandas",
            "numpy",
        ],
    },
    "data": [
        "data/ir_cron.xml",
        "views/hr_employee_views.xml",
    ],
}
