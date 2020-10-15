# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Timesheet Computation Integration With Holiday",
    "version": "8.0.1.0.1",
    "category": "Human Resource",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_timesheet_computation",
        "hr_holidays",
    ],
    "images": [
        "static/description/banner.png",
    ],
    "data": [
        "views/hr_timesheet_sheet_views.xml",
        "views/hr_holidays_views.xml",
    ],
}
