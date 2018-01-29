# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Employee Training",
    "version": "8.0.1.1.0",
    "category": "Human Resource",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr",
    ],
    "data": [
        "security/ir.model.access.csv",
        "menu.xml",
        "wizards/select_participant.xml",
        "views/hr_training_category_views.xml",
        "views/hr_training_method_views.xml",
        "views/hr_training_purpose_views.xml",
        "views/hr_training_syllabus_views.xml",
        "views/hr_training_cancel_reason_views.xml",
        "views/hr_training_views.xml",
        "views/hr_training_session_views.xml",
        "views/hr_training_attendance_views.xml",
    ],
}
