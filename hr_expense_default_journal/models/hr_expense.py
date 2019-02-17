# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api


class HrExpenseExpense(models.Model):
    _inherit = "hr.expense.expense"

    @api.onchange(
        "employee_id"
    )
    def onchange_journal_id(self):
        self.journal_id = False
        if self.employee_id:
            self.journal_id = self.employee_id.expense_journal_id
