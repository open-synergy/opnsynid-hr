# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models


class HrExpenseExpense(models.Model):
    _inherit = "hr.expense.expense"

    @api.onchange("employee_id")
    def onchange_journal_id(self):
        self.journal_id = False
        default_journal_id = self.env.context.get("default_journal_id", False)
        if default_journal_id:
            self.journal_id = default_journal_id
        elif self.employee_id:
            self.journal_id = self.employee_id.expense_journal_id
