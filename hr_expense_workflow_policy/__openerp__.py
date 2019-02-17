# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Expense Workflow Policy",
    "version": "8.0.1.0.0",
    "category": "Human Resource",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_expense_journal_configuration_page",
        "base_workflow_policy",
    ],
    "data": [
        "data/base_workflow_policy_data.xml",
        "views/account_journal_views.xml",
        "views/hr_expense_views.xml",
    ],
}
