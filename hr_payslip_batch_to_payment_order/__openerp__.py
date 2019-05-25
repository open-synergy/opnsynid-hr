# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Payslip Batch To Payment Order",
    "version": "8.0.1.0.1",
    "category": "Human Resource",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr_payroll_account",
        "account_payment",
    ],
    "data": [
        "wizards/create_payment_order_from_payslip_batch.xml",
        "views/hr_payslip_run_views.xml",
    ],
}
