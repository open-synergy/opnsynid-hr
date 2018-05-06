# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Employee Training - Allowance Integration "
            "with Job Family Modelling",
    "version": "8.0.1.0.0",
    "category": "Human Resource",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_employee_training_allowance",
        "product",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/hr_training_allowance_pricelist_policy_field_data.xml",
        "views/hr_job_family_views.xml",
        "views/hr_job_family_grade_views.xml",
        "views/hr_job_grade_views.xml",
        "views/hr_job_grade_category_views.xml",
    ],
}
