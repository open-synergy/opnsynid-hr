# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Career Transition - Promotion",
    "version": "8.0.1.0.0",
    "category": "Human Resource",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_career_transition",
    ],
    "data": [
        "data/ir_sequence_data.xml",
        "data/hr_career_transition_type_data.xml",
        "data/base_sequence_configurator_data.xml",
        "data/base_workflow_policy_data.xml",
        "views/hr_promotion_transition_views.xml",
    ],
}
