# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Attendance Overtime Request",
    "version": "8.0.1.0.1",
    "category": "Human Resources",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_attendance",
    ],
    "data": [
        "menu.xml",
        "security/ir.model.access.csv",
        "data/ir_sequence_data.xml",
        "views/hr_overtime_request_views.xml",
        "views/hr_overtime_config_setting_views.xml",
    ],
}
