# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Timesheet Computation Integration With Overtime",
    "version": "8.0.1.2.0",
    "category": "Human Resource",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_timesheet_computation",
        "hr_attendance_overtime_request",
    ],
    "data": [
        "data/ir_actions_server_data.xml",
        "views/hr_overtime_config_setting_views.xml",
        "views/hr_timesheet_sheet_views.xml",
        "views/hr_overtime_request_views.xml",
    ],
    "images": [
        "static/description/banner.png",
    ],
}
