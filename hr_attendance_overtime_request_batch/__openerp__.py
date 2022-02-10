# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Overtime Request Batches",
    "version": "8.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_attendance_overtime_request",
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/ir_rule_data.xml",
        "data/ir_sequence_data.xml",
        "wizards/hr_overtime_request_by_employee.xml",
        "views/hr_overtime_request_batch_views.xml",
        "views/hr_overtime_request_views.xml",
        "views/hr_overtime_config_setting_views.xml",
    ],
}
