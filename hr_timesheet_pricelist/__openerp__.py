# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Timesheet Activities Pricelist",
    "version": "8.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "auto_install": True,
    "depends": [
        "hr_timesheet",
        "account_analytic_line_pricelist",
        "hr_timesheet_product_policy",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/product_pricelist_type_data.xml",
        "views/hr_analytic_timesheet_views.xml",
        "views/account_analytic_account_views.xml",
    ],
}
