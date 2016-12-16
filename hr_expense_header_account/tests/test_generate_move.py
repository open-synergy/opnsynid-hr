# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from .base import BaseCase
from datetime import datetime


class HrExpensePayableAccount(BaseCase):

    def _create_process_expense(self, account=False):
        data = {
            "employee_id": self.employee_1.id,
            "name": "Test Expense",
            "journal_id": self.journal_1.id,
            "account_id": account and account.id or False,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "line_ids": [(0, 0, {
                "name": "Line #1",
                "date_value": datetime.now().strftime("%Y-%m-%d"),
                "unit_amount": 700.00,
                "unit_quantity": 7.0,
            })],
        }
        expense = self.obj_hr_expense.create(data)
        expense.signal_workflow("confirm")
        expense.signal_workflow("validate")
        expense.signal_workflow("done")
        return expense

    def test_generate_move_without_account(self):
        expense = self._create_process_expense()
        check = False
        account = expense.employee_id.address_home_id.\
            commercial_partner_id.property_account_payable
        for line in expense.account_move_id.line_id:
            if line.account_id == account:
                check = True
        self.assertTrue(check)

    def test_generate_move_with_account(self):
        expense = self._create_process_expense(self.account)
        check = False
        account = self.account
        for line in expense.account_move_id.line_id:
            if line.account_id == account:
                check = True
        self.assertTrue(check)
