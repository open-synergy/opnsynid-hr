# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Generate Accrue Expense Based On Timesheet Details - Sheet",
    "version": "8.0.2.1.0",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "auto_install": True,
    "depends": [
        "hr_timesheet_accrue_expense",
        "hr_timesheet_sheet_onchange",
        "base_action_rule",
        "base_ir_filters_active",
    ],
    "data": [
        "data/ir_filters_data.xml",
        "data/ir_actions_server_data.xml",
        "data/base_action_rule_data.xml",
        "views/hr_timesheet_sheet_sheet_views.xml",
    ],
}
