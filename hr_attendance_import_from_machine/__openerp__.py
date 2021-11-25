# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Import Attendance Data From Machine",
    "version": "8.0.1.5.1",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_attendance",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/hr_attendance_machine_views.xml",
        "wizards/hr_attendance_import.xml",
    ],
}
