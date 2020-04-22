# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Timesheet Auto Input",
    "version": "8.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "auto_install": True,
    "depends": [
        "hr_timesheet_sheet_product_policy",
        "timesheet_task",
    ],
    "data": [
        "wizards/wizard_timesheet_auto_input.xml",
        "views/hr_timesheet_sheet_view.xml",
    ],
}
