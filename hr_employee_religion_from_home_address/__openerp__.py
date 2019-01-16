# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Employee Religion From Home Address",
    "version": "8.0.1.0.0",
    "category": "Human Resource",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_contract",
        "partner_contact_religion",
    ],
    "data": [
        "views/hr_employee_views.xml",
    ],
}
