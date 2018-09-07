# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "HR Holiday Code",
    "version": "8.0.1.0.0",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_holidays",
    ],
    "data": [
        "data/hr_holidays_sequence.xml",
        "views/hr_holidays_view.xml",
        "views/hr_holidays_status_view.xml",
        "views/res_company_views.xml"
    ],
    "pre_init_hook": "create_code_equal_to_id",
    "post_init_hook": "assign_old_sequences",
}
