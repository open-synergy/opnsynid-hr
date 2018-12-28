# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Timesheet Attendance Schedule",
    "version": "8.0.2.0.3",
    "category": "Human Resource",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_timesheet_sheet",
        "hr_attendance_configuration_page",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/ir_filters_data.xml",
        "data/ir_actions_server_data.xml",
        "data/base_action_rule_data.xml",
        "data/ir_values_data.xml",
        "views/hr_timesheet_sheet_views.xml",
        "views/hr_timesheet_attendance_schedule_views.xml",
        "views/hr_attendance_config_setting_views.xml",
    ],
}
