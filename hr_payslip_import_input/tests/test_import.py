# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase
from openerp.modules.module import get_module_resource
import time
from openerp.exceptions import Warning as UserError


class TestImport(TransactionCase):

    def get_file(self, filename):
        """Retrieve file from test data, encode it as base64 """
        path = get_module_resource('hr_payslip_import_input',
                                   'tests', 'data', filename)
        test_data = open(path).read()
        return test_data.encode('base64')

    def setUp(self, *args, **kwargs):
        super(TestImport, self).setUp(*args, **kwargs)
        # Objects
        self.obj_hr_employee = self.env['hr.employee']
        self.obj_payslip = self.env['hr.payslip']
        self.obj_contract = self.env['hr.contract']
        self.obj_struct = self.env['hr.payroll.structure']
        self.obj_payslip_run = self.env['hr.payslip.run']
        self.obj_payslip_emp = self.env['hr.payslip.employees']
        self.wiz = self.env['hr.payslip_import_input']

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
        self.employee_1 = self._create_employee_1()
        self.employee_2 = self._create_employee_2()
        self.struct = self._create_structure()
        self.contract_1 = self._create_contract_1()
        self.contract_2 = self._create_contract_2()

    def _create_employee_1(self):
        vals = {
            'name': 'Alan',
            'country_id': self.country.id,
            'department_id': self.department.id,
            'birthday': '1967-01-01',
            'gender': 'male'
        }

        employee = self.obj_hr_employee.create(vals)
        employee.identification_id = '001'
        return employee

    def _create_employee_2(self):
        vals = {
            'name': 'Robert',
            'identification_id': '002',
            'country_id': self.country.id,
            'department_id': self.department.id,
            'birthday': '1982-01-01',
            'gender': 'male'
        }

        employee = self.obj_hr_employee.create(vals)
        employee.identification_id = '002'
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

    def _create_contract_1(self):
        vals = {
            'name': 'Contract 1',
            'date_start': time.strftime('%Y-%m') + '-1',
            'date_end': time.strftime('%Y') + '-12-31',
            'wage': 7500000.0,
            'type_id': self.type.id,
            'employee_id': self.employee_1.id,
            'struct_id': self.struct.id,
            'working_hours': self.resource.id
        }

        contract = self.obj_contract.create(vals)
        return contract

    def _create_contract_2(self):
        vals = {
            'name': 'Contract 2',
            'date_start': time.strftime('%Y-%m') + '-1',
            'date_end': time.strftime('%Y') + '-12-31',
            'wage': 7500000.0,
            'type_id': self.type.id,
            'employee_id': self.employee_2.id,
            'struct_id': self.struct.id,
            'working_hours': self.resource.id
        }

        contract = self.obj_contract.create(vals)
        return contract

    def test_import_data(self):
        # Generate Payslip
        vals = {
            'name': 'Test Payslip',
            'date_end': time.strftime('%Y-%m-%d'),
            'date_start': time.strftime('%Y-%m-%d')
        }
        payslip_run = self.obj_payslip_run.create(vals)
        data_wzd = {
            'employee_ids': [(
                6, 0, [self.employee_1.id, self.employee_2.id]
            )]
        }
        payslip_emp = self.obj_payslip_emp.with_context(
            active_id=payslip_run.id
        ).create(data_wzd)
        payslip_emp.compute_sheet()

        # Check Generate Payslip
        self.assertNotEqual(len(payslip_run.slip_ids), 0)

        # Check Input
        z = 0
        for payslip in payslip_run.slip_ids:
            if payslip.input_line_ids:
                for input_line in payslip.input_line_ids:
                    z += 1

        self.assertEqual(z, 4)

        # Check Error 1
        wiz = self.wiz.with_context(
            active_id=[payslip_run.id]).create(
            {'data': self.get_file('import_error_1.xlsx'),
             'name': 'import_error_1.xlsx',
             'delimeter': '',
             }
        )

        msg_error_1 = ("Not a valid file!")
        with self.assertRaises(UserError) as error:
            wiz.import_data()

        self.assertEqual(error.exception.message, msg_error_1)

        # Check Error 2
        wiz = self.wiz.with_context(
            active_id=[payslip_run.id]).create(
            {'data': self.get_file('import_error_2.csv'),
             'name': 'import_error_2.csv',
             }
        )

        msg_error_2 = ("Not employee or code or amount keys found")
        with self.assertRaises(UserError) as error:
            wiz.import_data()

        self.assertEqual(error.exception.message, msg_error_2)

        # Import Data
        wiz = self.wiz.with_context(
            active_id=[payslip_run.id]).create(
            {'data': self.get_file('test_import.csv'),
             'name': 'test_import.csv',
             'delimeter': ',',
             }
        )
        wiz.import_data()

        # Check Import Data
        self.assertEqual(payslip_run.imported_files.name, "test_import.csv")

        # Check Process Input
        x = 0
        for inputs in payslip_run.process_inputs:
            if inputs.input_id:
                x += 1

        self.assertEqual(x, 4)

        # Check Error Duplicate Data
        wiz = self.wiz.with_context(
            active_id=[payslip_run.id]).create(
            {'data': self.get_file('test_import.csv'),
             'name': 'test_import.csv',
             'delimeter': ',',
             }
        )
        msg_error_3 = ("Cannot import with the same file")
        with self.assertRaises(UserError) as error:
            wiz.import_data()

        self.assertEqual(error.exception.message, msg_error_3)
