# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Employee Project Experience",
    "version": "14.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "LGPL-3",
    "installable": True,
    "application": True,
    "auto_install": True,
    "depends": ["ssi_hr", "ssi_project_assignment"],
    "data": [
        "security/ir.model.access.csv",
        "views/hr_employee_views.xml",
    ],
    "demo": [],
}
