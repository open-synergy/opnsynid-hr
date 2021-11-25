# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class HrEmployee(models.Model):
    _name = "hr.employee"
    _inherit = "hr.employee"

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
