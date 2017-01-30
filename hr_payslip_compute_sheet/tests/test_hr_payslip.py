# -*- coding: utf-8 -*-
# Copyright 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase
import time
from openerp.exceptions import Warning as UserError


class TestHRPayslip(TransactionCase):
    def setUp(self, *args, **kwargs):
        super(TestHRPayslip, self).setUp(*args, **kwargs)
        # Objects
        self.obj_hr_employee = self.env['hr.employee']
        self.obj_payslip = self.env['hr.payslip']
        self.obj_contract = self.env['hr.contract']
        self.obj_struct = self.env['hr.payroll.structure']
        self.wiz = self.env['hr.compute_sheet']

        # Data
        self.country = self.env.ref(
            'base.id')
        self.department = self.env.ref(
            'hr.dep_rd')
        self.company = self.env.ref('base.main_company')
        self.type =\
            self.env.ref('hr_contract.hr_contract_type_emp')
        self.resource =\
            self.env.ref('resource.timesheet_group1')
        self.rule_1 = self.env.ref(
            'hr_payroll.hr_salary_rule_houserentallowance1')
        self.rule_2 = self.env.ref(
            'hr_payroll.hr_salary_rule_convanceallowance1')
        self.rule_3 = self.env.ref(
            'hr_payroll.hr_salary_rule_professionaltax1')
        self.rule_4 = self.env.ref(
            'hr_payroll.hr_salary_rule_providentfund1')
        self.rule_5 = self.env.ref(
            'hr_payroll.hr_salary_rule_meal_voucher')
        self.rule_6 = self.env.ref(
            'hr_payroll.hr_salary_rule_sales_commission')
        self.employee = self._create_employee()
        self.struct = self._create_structure()
        self.contract = self._create_contract()

    def _create_employee(self):
        vals = {
            'name': 'Alan',
            'country_id': self.country.id,
            'department_id': self.department.id,
            'birthday': '1967-01-01',
            'gender': 'male'
        }

        employee = self.obj_hr_employee.create(vals)
        return employee

    def _create_structure(self):
        vals = {
            'name': 'Test Salary Structure',
            'code': 'TST',
            'company_id': self.company.id,
            'rule_ids': [(6, 0, [
                self.rule_1.id,
                self.rule_2.id,
                self.rule_3.id,
                self.rule_4.id,
                self.rule_5.id,
                self.rule_6.id
            ])]

        }

        struct = self.obj_struct.create(vals)
        return struct

    def _create_contract(self):
        vals = {
            'name': 'Test Contract',
            'date_start': time.strftime('%Y-%m')+'-1',
            'date_end': time.strftime('%Y')+'-12-31',
            'wage': 7500000.0,
            'type_id': self.type.id,
            'employee_id': self.employee.id,
            'struct_id': self.struct.id,
            'working_hours': self.resource.id
        }

        contract = self.obj_contract.create(vals)
        return contract

    def test_compute_sheet(self):
        # Create Payslip
        vals = {
            'employee_id': self.employee.id,
            'contract_id': self.contract.id,
            'struct_id': self.struct.id
        }
        new = self.obj_payslip.create(vals)
        onchange = new.onchange_employee_id(
            date_to=new.date_to,
            date_from=new.date_from,
            employee_id=new.employee_id.id,
            contract_id=new.contract_id.id
        )
        lst_worked_days = []
        lst_inputs = []
        for worked_days in onchange["value"]["worked_days_line_ids"]:
            lst_worked_days.append((0, 0, worked_days))
        for inputs in onchange["value"]["input_line_ids"]:
            lst_inputs.append((0, 0, inputs))
        new.write({
            "worked_days_line_ids": lst_worked_days,
            "input_line_ids": lst_inputs
        })
        check_nod = new.worked_days_line_ids.number_of_days
        check_amount = new.input_line_ids[0].amount

        # Modify Number Of Days
        new.worked_days_line_ids.number_of_days = 30
        # Check Number Of Days
        self.assertNotEqual(
            check_nod,
            new.worked_days_line_ids.number_of_days
        )

        # Modify Amount
        new.input_line_ids[0].amount = 100
        # Check Amount
        self.assertNotEqual(
            check_amount,
            new.input_line_ids[0].amount
        )

        # Create Compute Sheet
        wiz = self.wiz.with_context(active_ids=[new.id])

        wiz.create({
            'reload_workdays': True,
            'reload_input': True
        }).button_compute_sheet()

        # Check Reload Worked Days
        self.assertEqual(
            check_nod,
            new.worked_days_line_ids.number_of_days
        )
        # Check Reload Inputs
        self.assertEqual(
            check_amount,
            new.input_line_ids[0].amount
        )

        # Change State = Done
        new.signal_workflow('hr_verify_sheet')

        self.assertEqual(
            'done',
            new.state
        )

        # Create Compute Sheet
        wiz = self.wiz.with_context(active_ids=[new.id])

        msg = (
            'Payslip No. %s '
            'cannot be computed '
            'because state is done.'
        ) % (new.number,)

        with self.assertRaises(UserError) as error:
            wiz.create({
                'reload_workdays': True,
                'reload_input': True
            }).button_compute_sheet()

        self.assertEqual(error.exception.message, msg)
