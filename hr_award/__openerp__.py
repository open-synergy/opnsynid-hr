# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Employee Award",
    "version": "8.0.2.0.0",
    "category": "Human Resource",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_career_administration_configuration_page",
        "base_sequence_configurator",
        "base_workflow_policy",
        "base_cancel_reason",
        "base_multiple_approval",
    ],
    "data": [
        "security/ir_module_category_data.xml",
        "security/res_groups_data.xml",
        "security/ir.model.access.csv",
        "security/ir_rule_data.xml",
        "data/base_workflow_policy_data.xml",
        "data/ir_sequence_data.xml",
        "data/base_sequence_configurator_data.xml",
        "data/base_cancel_reason_config_data.xml",
        "menu.xml",
        "views/hr_award_type_views.xml",
        "views/hr_award_reason_views.xml",
        "views/hr_award_views.xml",
    ],
    "images": [
        "static/description/banner.png",
    ],
}
