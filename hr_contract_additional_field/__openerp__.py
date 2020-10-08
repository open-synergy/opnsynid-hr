# -*- coding: utf-8 -*-
# Copyright 2018-2019 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Additional Field for Employee Contract",
    "version": "8.0.1.4.0",
    "category": "Human Resource",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "auto_install": True,
    "depends": [
        "hr_contract",
        "hr_employee_employment_status",
    ],
    "data": [
        "views/hr_contract_views.xml",
        "views/hr_contract_type_views.xml",
    ],
    "images": [
        "static/description/banner.png",
    ],
}
