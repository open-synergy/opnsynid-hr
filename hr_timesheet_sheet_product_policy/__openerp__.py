# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Timesheet Tracking Product Policy",
    "version": "8.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_timesheet_sheet",
        "hr_timesheet_product_policy",
    ],
    "auto_install": True,
    "data": [
        "views/hr_timesheet_sheet_sheet_views.xml",
    ],
}
