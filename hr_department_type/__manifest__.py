# Copyright 2018-2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Human Resource - Department Type",
    "version": "10.0.1.0.0",
    "category": "Human Resource",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr"
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/hr_department_type_views.xml",
        "views/hr_department_views.xml"
    ],
}
