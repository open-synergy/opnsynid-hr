# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Mass Generate Timesheet",
    "version": "8.0.1.0.1",
    "category": "Human Resources",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_timesheet_sheet",
    ],
    "data": ["wizards/hr_timesheet_mass_generate.xml"],
    "images": [
        "static/description/banner.png",
    ],
}
