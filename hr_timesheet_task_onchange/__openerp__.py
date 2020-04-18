# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "New API for Timesheet Analytic Line Onchange - Task",
    "version": "8.0.1.1.0",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "auto_install": True,
    "depends": [
        "timesheet_task",
        "project_task_analytic_account",
        "hr_timesheet_onchange",
    ],
    "data": [
        "views/project_task_views.xml",
    ],
}
