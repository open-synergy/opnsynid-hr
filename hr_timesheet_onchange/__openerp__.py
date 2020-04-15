# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "New API for Timesheet Analytic Line Onchange",
    "version": "8.0.1.1.0",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "auto_install": True,
    "depends": [
        "hr_timesheet",
        "account_analytic_line_onchange",
    ],
    "data": [
        "views/hr_analytic_timesheet_views.xml",
    ],
}
