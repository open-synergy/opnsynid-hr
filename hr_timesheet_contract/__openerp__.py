# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Helper Module To List All Contracts That Relevant to Timesheet",
    "version": "8.0.1.0.0",
    "category": "Hidden",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_timesheet_sheet",
        "hr_contract",
    ],
    "data": [
        "views/hr_timesheet_sheet_views.xml",
    ],
}
