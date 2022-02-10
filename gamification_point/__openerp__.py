# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Gamification Goal's Point",
    "version": "8.0.2.1.0",
    "category": "Human Resources",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "gamification_analysis",
    ],
    "data": [
        "reports/gamification_goal_analysis.xml",
        "views/gamification_challange_views.xml",
        "views/gamification_goal_views.xml",
    ],
}
