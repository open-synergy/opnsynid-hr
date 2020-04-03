# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api, fields


class HrExpenseExpense(models.Model):
    _name = "hr.expense.expense"
    _inherit = [
        "hr.expense.expense",
        "base.sequence_document",
    ]

    @api.model
    def _default_name(self):
        return "/"

    name = fields.Char(
        default=lambda self: self._default_name(),
        string="# Document",
    )

    @api.model
    def create(self, values):
        _super = super(HrExpenseExpense, self)
        result = _super.create(values)
        sequence = result._create_sequence()
        result.write({
            "name": sequence,
        })
        return result
