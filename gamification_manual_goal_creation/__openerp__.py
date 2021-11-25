# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Manually Create Gamification Goal",
    "version": "8.0.1.0.0",
    "category": "Human Resources",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "gamification",
    ],
    "data": [
        "wizards/manual_goal_creation.xml",
        "views/gamification_challange_views.xml",
    ],
}
