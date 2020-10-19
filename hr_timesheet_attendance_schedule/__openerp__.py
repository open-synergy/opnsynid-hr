# -*- coding: utf-8 -*-
# Copyright 2018-2019 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Timesheet Attendance Schedule",
    "version": "8.0.4.0.0",
    "category": "Human Resource",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_timesheet_sheet",
        "hr_attendance_configuration_page",
        "base_sequence_configurator",
        "base_workflow_policy",
        "web_readonly_bypass",
        "base_multiple_approval",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/ir_filters_data.xml",
        "data/ir_actions_server_data.xml",
        "data/base_action_rule_data.xml",
        "data/ir_values_data.xml",
        "data/ir_sequence_data.xml",
        "data/base_sequence_configurator_data.xml",
        "data/base_workflow_policy_data.xml",
        "views/hr_timesheet_sheet_views.xml",
        "views/hr_timesheet_attendance_schedule_views.xml",
        "views/hr_timesheet_attendance_schedule_change_views.xml",
        "views/hr_attendance_config_setting_views.xml",
    ],
    "images": [
        "static/description/banner.png",
    ],
}
