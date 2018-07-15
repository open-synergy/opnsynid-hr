# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Employee Training - Allowance",
    "version": "8.0.1.3.0",
    "category": "Human Resource",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_employee_training",
        "product",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/product_pricelist_type_data.xml",
        "data/hr_training_allowance_pricelist_policy_field_data.xml",
        "views/hr_employee_views.xml",
        "views/hr_department_views.xml",
        "views/hr_job_views.xml",
        "views/hr_training_category_views.xml",
        "views/hr_training_views.xml",
        "views/hr_training_allowance_pricelist_policy_field_views.xml",
        "views/hr_training_participant_type_views.xml",
        "views/hr_training_participant_views.xml",
        "views/product_template_views.xml",
    ],
}
