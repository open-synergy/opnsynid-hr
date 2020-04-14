# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api


class HrAnalyticTimesheet(models.Model):
    _name = "hr.analytic.timesheet"
    _inherit = "hr.analytic.timesheet"

    @api.onchange(
        "product_id",
        "journal_id",
        "account_id",
    )
    def onchange_general_account_id(self):
        account = False
        is_sale_line = False
        obj_substitution = self.\
            env["account.analytic_general_account_substitution"]

        if self.journal_id:
            if self.journal_id.type == "sale":
                is_sale_line = True

        if self.product_id and \
                self.account_id:
            criteria = [
                ("analytic_account_id", "=", self.account_id.id),
                ("product_id", "=", self.product_id.id),
            ]
            substitutes = obj_substitution.search(criteria)
            if len(substitutes) > 0:
                substitute = substitutes[0]

                if is_sale_line and \
                        substitute.income_general_account_id:
                    account = substitute.income_general_account_id
                elif not is_sale_line and \
                        substitute.expense_general_account_id:
                    account = substitute.expense_general_account_id

        if not account:
            _super = super(HrAnalyticTimesheet, self)
            _super.onchange_general_account_id()
        else:
            self.general_account_id = account
