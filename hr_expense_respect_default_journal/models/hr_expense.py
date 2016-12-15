# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api


class HrExpense(models.Model):
    _inherit = "hr.expense.expense"

    @api.onchange("currency_id", "company_id")
    def onchange_currency_id(self):
        result = super(HrExpense, self).onchange_currency_id(
            self.currency_id and self.currency_id.id or False,
            self.company_id and self.company_id.id or False)
        journal_id = self.env.context.get("default_journal_id", False)
        if journal_id:
            self.journal_id = self.journal_id
        else:
            self.journal_id = result["value"]["journal_id"]
