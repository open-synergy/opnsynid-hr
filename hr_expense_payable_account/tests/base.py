# -*- coding: utf-8 -*-
# © 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


class BaseCase(TransactionCase):
    def setUp(self):
        super(BaseCase, self).setUp()
        # Data Object
        self.obj_hr_expense = self.env['hr.expense.expense']

        # Data Journal
        self.journal_1 = self.env.ref('account.expenses_journal')
        self.journal_2 = self.create_journal()
        # Data Employee
        self.employee_1 = self.env.ref('hr.employee_mit')
        self.employee_2 = self.create_employee()

    def create_journal(self):
        # Create Journal
        # Condition :
        # default_credit_account_id = False
        # default_debit_account_id = False
        obj_account_journal = self.env['account.journal']
        sequence = self.env.ref('account.sequence_purchase_journal')
        analytic_acc = self.env.ref('account.exp')
        user = self.env.ref('base.user_root')

        val = {
            'name': 'Test Expenses Journal',
            'code': 'TSTJ',
            'type': 'purchase',
            'sequence_id': sequence.id,
            'default_credit_account_id': False,
            'default_debit_account_id': False,
            'analytic_journal_id': analytic_acc.id,
            'user_id': user.id
        }

        journal =\
            obj_account_journal.create(val)
        return journal

    def create_employee(self):
        # Create Journal
        # Condition :
        # address_home_id = False
        obj_hr_employee = self.env['hr.employee']
        department_id = self.env.ref('hr.dep_rd')
        parent_id = self.env.ref('hr.employee_al')
        job_id = self.env.ref('hr.job_developer')
        category_id = self.env.ref('hr.employee_category_4')

        val = {
            'name': 'Test Employee',
            'department_id': department_id.id,
            'parent_id': parent_id.id,
            'job_id': job_id.id,
            'category_ids': [(6, 0, [category_id.id])],
            'address_home_id': False
        }

        employee =\
            obj_hr_employee.create(val)
        return employee
