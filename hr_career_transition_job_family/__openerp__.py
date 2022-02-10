# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Career Transition - Job Family Integration",
    "version": "8.0.1.0.0",
    "category": "Human Resource",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "auto_install": True,
    "depends": [
        "hr_career_transition",
        "hr_employee_job_family_from_contract",
    ],
    "data": [
        "views/hr_career_transition_type_views.xml",
        "views/hr_career_transition_views.xml",
    ],
}
