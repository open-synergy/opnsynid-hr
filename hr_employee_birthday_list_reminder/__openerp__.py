# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Employee Birthday List Reminder",
    "version": "8.0.1.0.0",
    "category": "Human Resource",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "mail",
        "email_template",
        "hr",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/hr_birthday_list_reminder_views.xml",
    ],
    "external_dependencies": {
        "python": ["pandas"],
    },
}
