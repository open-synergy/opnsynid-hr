# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class HrDiciplineType(models.Model):
    _inherit = "hr.dicipline_type"

    journal_id = fields.Many2one(
        string="Journal",
        comodel_name="account.journal",
        company_dependent=True,
        domain=[
            ("type", "=", "general"),
        ],
    )
    receivable_account_id = fields.Many2one(
        string="Receivable Account",
        comodel_name="account.account",
        company_dependent=True,
        domain=[
            ("type", "in", ["other", "receivable", "payable"]),
            ("reconcile", "=", True),
        ],
    )
    income_account_id = fields.Many2one(
        string="Income Account",
        comodel_name="account.account",
        company_dependent=True,
        domain=[
            ("type", "in", ["other", "receivable", "payable"]),
            ("reconcile", "=", True),
        ],
    )
