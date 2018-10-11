# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Holidays Batches",
    "version": "8.0.1.0.0",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_holidays",
        "hr_holiday_configuration_page"
    ],
    "data": [
        "security/ir_module_category_data.xml",
        "security/res_groups_data.xml",
        "security/ir.model.access.csv",
        "security/ir_rule_data.xml",
        "data/ir_sequence_data.xml",
        "wizards/hr_holiday_by_employee.xml",
        "views/hr_holiday_batch_leave_request.xml",
        "views/hr_holiday_batch_allocation_request.xml",
        "views/hr_holiday_views.xml",
        "views/hr_holiday_config_setting_views.xml",
    ],
}
