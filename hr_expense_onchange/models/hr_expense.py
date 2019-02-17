# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api


class HrExpenseExpense(models.Model):
    _inherit = "hr.expense.expense"

    @api.onchange(
        "employee_id"
    )
    def onchange_company_id(self):
        self.company_id = False
        if self.employee_id:
            self.company_id = self.employee_id.company_id

    @api.onchange(
        "employee_id"
    )
    def onchange_department_id(self):
        self.department_id = False
        if self.employee_id:
            self.department_id = self.employee_id.department_id

    @api.onchange(
        "company_id",
        "journal_id",
    )
    def onchange_currency(self):
        self.currency_id = self.company_id.currency_id
        if self.journal_id:
            if self.journal_id.currency:
                self.currency_id = self.journal_id.currency
