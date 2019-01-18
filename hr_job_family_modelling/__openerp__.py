# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Job Family Modelling",
    "summary": "Grading system that divides jobs into coherent groups "
               "based on shared characteristics",
    "version": "8.0.1.2.0",
    "category": "Human Resources",
    "website": "https://opensynergy-indonesia.com/",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr",
    ],
    "data": [
        "security/ir.model.access.csv",
        "menu.xml",
        "views/hr_job_grade_category_views.xml",
        "views/hr_job_grade_views.xml",
        "views/hr_job_family_grade_views.xml",
        "views/hr_job_family_views.xml",
        "views/hr_job_family_level_views.xml",
        "views/hr_job_views.xml",
        "views/hr_employee_views.xml",
    ],
}
