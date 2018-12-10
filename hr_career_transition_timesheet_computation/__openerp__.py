# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Career Transition - Timesheet Computation Integration",
    "version": "8.0.1.0.0",
    "category": "Human Resource",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "auto_install": True,
    "depends": [
        "hr_career_transition",
        "hr_timesheet_computation",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/hr_career_transition_type_views.xml",
        "views/hr_career_transition_views.xml",
    ],
}
