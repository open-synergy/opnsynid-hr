# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class HrExpense(models.Model):
    _inherit = "hr.expense.expense"

    account_id = fields.Many2one(
        string="Account",
        comodel_name="account.account"
    )

    @api.multi
    def action_move_create(self):
        """Reconcile supplier invoice payables with the created move lines."""
        res = super(HrExpense, self).action_move_create()
        for expense in self:
            for line in expense.account_move_id.line_id:
                if not expense.account_id:
                    continue

                partner = expense.employee_id.address_home_id.commercial_partner_id
                acc_payable = partner.property_account_payable
                if line.account_id == acc_payable:
                    line.write({"account_id": expense.account_id.id})
        return res

    @api.model
    def _get_partner_account(self):
        address_home_id =\
            self.employee_id.address_home_id
        if address_home_id:
            commercial_partner_id =\
                address_home_id.commercial_partner_id
            if commercial_partner_id:
                account_id =\
                    commercial_partner_id.property_account_payable
                if account_id:
                    return account_id.id
        return False

    @api.multi
    @api.onchange(
        'journal_id',
        'employee_id'
    )
    def onchange_journal_id(self):
        value = False
        if self.journal_id:
            account_id =\
                self.journal_id.default_credit_account_id
            if account_id:
                value = account_id.id
            else:
                value = self._get_partner_account()
        else:
            value = self._get_partner_account()
        self.account_id = value
