# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Recruitment Request",
    "version": "8.0.1.0.0",
    "category": "Human Resource",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_recruitment",
        "base_sequence_configurator",
        "base_workflow_policy",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/ir_sequence_data.xml",
        "data/base_workflow_policy_data.xml",
        "data/base_sequence_configurator_data.xml",
        "views/hr_applicant_views.xml",
        "views/hr_recruitment_request_views.xml",
    ],
}
