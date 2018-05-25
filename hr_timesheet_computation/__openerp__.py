# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Timesheet Computation",
    "version": "8.0.1.0.0",
    "category": "Human Resource",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_attendance_configuration_page",
        "base_ir_filters_active",
        "hr_timesheet_contract",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/ir_filters_data.xml",
        "data/ir_actions_server_data.xml",
        "data/base_action_rule_data.xml",
        "views/hr_contract_views.xml",
        "views/hr_timesheet_sheet_views.xml",
        "views/hr_timesheet_computation_item_views.xml",
    ],
}
