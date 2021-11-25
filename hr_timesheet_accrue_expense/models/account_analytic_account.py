# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class AccountAnalyticAccount(models.Model):
    _name = "account.analytic.account"
    _inherit = "account.analytic.account"

    accrue_expense_journal_id = fields.Many2one(
        string="Accrue Expense Journal",
        comodel_name="account.journal",
        domain=[
            ("type", "=", "general"),
        ],
    )
    accrue_expense_account_id = fields.Many2one(
        string="Accrue Expense Account",
        comodel_name="account.account",
        domain=[
            ("type", "=", "other"),
        ],
    )
    accrue_expense_ok = fields.Boolean(
        string="Can Create Accrue Expense",
        default=False,
    )
