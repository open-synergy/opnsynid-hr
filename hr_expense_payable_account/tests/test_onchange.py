# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from .base import BaseCase


class HrExpensePayableAccount(BaseCase):
    # Check value account_id
    # Condition :
    # journal_id == True
    # default_credit_account == True
    # home_address == True
    # property_account_payable == True
    def test_onchange_journal_id_1(self):
        with self.env.do_in_onchange():
            new = self.obj_hr_expense.new()

            new.journal_id = self.journal_1.id
            new.employee_id = self.employee_1.id

            new.onchange_journal_id()

            self.assertEqual(
                self.journal_1.default_credit_account_id.id,
                new.account_id.id)

    # Check value account_id
    # Condition :
    # journal_id == True
    # default_credit_account == False
    # home_address == True
    # property_account_payable == True
    def test_onchange_journal_id_2(self):
        with self.env.do_in_onchange():
            new = self.obj_hr_expense.new()

            new.journal_id = self.journal_2.id
            new.employee_id = self.employee_1.id

            property_account_payable =\
                new._get_partner_account()

            new.onchange_journal_id()

            self.assertEqual(
                property_account_payable,
                new.account_id.id)

    # Check value account_id
    # Condition :
    # journal_id == True
    # default_credit_account == False
    # home_address == False
    # property_account_payable == False
    def test_onchange_journal_id_3(self):
        with self.env.do_in_onchange():
            new = self.obj_hr_expense.new()

            new.journal_id = self.journal_2.id
            new.employee_id = self.employee_2.id

            new.onchange_journal_id()

            self.assertEqual(
                False,
                new.account_id.id)

    # Check value account_id
    # Condition :
    # journal_id == False
    # default_credit_account == False
    # home_address == True
    # property_account_payable == True
    def test_onchange_journal_id_4(self):
        with self.env.do_in_onchange():
            new = self.obj_hr_expense.new()

            new.journal_id = False
            new.employee_id = self.employee_1.id

            property_account_payable =\
                new._get_partner_account()

            new.onchange_journal_id()

            self.assertEqual(
                property_account_payable,
                new.account_id.id)
