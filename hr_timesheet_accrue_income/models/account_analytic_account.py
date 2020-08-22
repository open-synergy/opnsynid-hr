# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class AccountAnalyticAccount(models.Model):
    _name = "account.analytic.account"
    _inherit = "account.analytic.account"

    accrue_income_journal_id = fields.Many2one(
        string="Accrue Income Journal",
        comodel_name="account.journal",
        domain=[
            ("type", "=", "general"),
        ],
    )
    accrue_income_account_id = fields.Many2one(
        string="Accrue Income Account",
        comodel_name="account.account",
        domain=[
            ("type", "=", "other"),
        ],
    )
    income_account_id = fields.Many2one(
        string="Income Account",
        comodel_name="account.account",
        domain=[
            ("type", "=", "other"),
        ],
    )
    accrue_income_ok = fields.Boolean(
        string="Can Create Accrue Income",
        default=False,
    )
    prepaid_price_unit = fields.Float(
        string="Prepaid Price Unit",
    )
