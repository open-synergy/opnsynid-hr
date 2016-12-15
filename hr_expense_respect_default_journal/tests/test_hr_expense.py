# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp.tests.common import TransactionCase


class HrExpenseCase(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(HrExpenseCase, self).setUp(*args, **kwargs)

        self.journal = self.env[
            "account.journal"].search([
                ("type", "=", "purchase"),
                ("currency", "=", False),
            ], limit=1)
        self.employee = self.env.ref(
            "hr.employee_fp")
        self.obj_expense = self.env["hr.expense.expense"]

    def test_onchange(self):
        expense1 = self.obj_expense.create({
            "name": "Test",
            "employee_id": self.employee.id
        })
        self.assertEqual(
            expense1.journal_id.id,
            False)
        expense2 = self.obj_expense.with_context(
            {"default_journal_id": self.journal.id}).create({
                "name": "Test",
                "employee_id": self.employee.id
            })
        self.assertEqual(
            expense2.journal_id.id,
            self.journal.id)
