# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Career Transition",
    "version": "8.0.1.2.0",
    "category": "Human Resource",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_career_administration_configuration_page",
        "hr_contract_additional_field",
        "hr_contract_reference",
        "base_sequence_configurator",
        "base_workflow_policy",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/base_workflow_policy_data.xml",
        "menu.xml",
        "views/hr_career_transition_type_views.xml",
        "views/hr_career_transition_views.xml",
        "views/hr_employee_views.xml",
    ],
}
