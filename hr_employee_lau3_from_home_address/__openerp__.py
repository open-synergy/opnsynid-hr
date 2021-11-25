# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Employee LAU Level 3 Information From Home Address",
    "version": "8.0.1.1.0",
    "category": "Human Resource",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_employee_lau_from_home_address",
        "base_location_lau_level3",
    ],
    "data": [
        "views/hr_employee_views.xml",
    ],
}
