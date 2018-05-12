# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Employee Training - Evaluation",
    "version": "8.0.1.0.0",
    "category": "Human Resource",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_employee_training",
        "survey",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/survey_survey_views.xml",
        "views/hr_training_views.xml",
        "views/hr_training_category_views.xml",
        "views/hr_training_participant_views.xml",
        "views/hr_training_participant_evaluation_views.xml",
    ],
}
