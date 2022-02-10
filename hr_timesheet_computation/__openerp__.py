# -*- coding: utf-8 -*-
# Copyright 2018-2019 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Timesheet Computation",
    "version": "8.0.1.3.0",
    "category": "Human Resource",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
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
        "reports/hr_timesheet_computation_analysis.xml",
        "views/hr_contract_views.xml",
        "views/hr_timesheet_sheet_views.xml",
        "views/hr_timesheet_computation_item_views.xml",
    ],
}
