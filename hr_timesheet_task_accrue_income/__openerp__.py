# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Generate Accrue Income Based On Task Timesheet",
    "version": "8.0.1.1.0",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "auto_install": True,
    "depends": [
        "hr_timesheet_task_onchange",
        "hr_timesheet_accrue_income",
    ],
    "data": [
        "views/project_task_views.xml",
    ],
    "images": [
        "static/description/banner.png",
    ],
}
