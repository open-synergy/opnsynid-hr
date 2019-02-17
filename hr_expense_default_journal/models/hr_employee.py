# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    expense_journal_id = fields.Many2one(
        string="Expense Journal",
        comodel_name="account.journal",
        company_dependent=True,
    )
