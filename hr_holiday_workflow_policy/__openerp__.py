# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "HR Holiday - Workflow Policy",
    "version": "8.0.1.0.0",
    "category": "Human Resource",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_holiday_configuration_page",
        "hr_department_notebook",
    ],
    "data": [
        "views/hr_holidays_views.xml",
        "views/hr_department_views.xml",
    ],
}
