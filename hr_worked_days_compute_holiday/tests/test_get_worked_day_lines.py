# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase


class TestGetWorkedDayLines(TransactionCase):
    def setUp(self, *args, **kwargs):
        super(TestGetWorkedDayLines, self).setUp(*args, **kwargs)
        # Objects
        self.obj_hr_employee = self.env['hr.employee']
        self.obj_res_partner = self.env['res.partner']
        self.obj_payslip = self.env['hr.payslip']
        self.obj_contract = self.env['hr.contract']
        self.obj_struct = self.env['hr.payroll.structure']
        self.obj_holiday = self.env["hr.holidays.public"]
        self.obj_holiday_line = self.env["hr.holidays.public.line"]

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

    def _create_holiday(self):
        holiday = self.obj_holiday.create({
            'year': 2017,
            'country_id': self.country.id
        })
        self.obj_holiday_line.create({
            'name': 'Test Holiday #1',
            'date': '2017-02-10',
            'year_id': holiday.id
        })

        return True

    def _create_employee(self):
        vals_home_addr = {
            'name': 'Home Address Alan',
            'country_id': self.country.id
        }
        addr = self.obj_res_partner.create(
            vals_home_addr)
        vals = {
            'name': 'Alan',
            'department_id': self.department.id,
            'birthday': '1967-01-01',
            'gender': 'male',
            'address_id': addr.id
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

    def _create_contract(self, employee, struct):
        vals = {
            'name': 'Test Contract',
            'date_start': '2017-02-1',
            'date_end': '2017-12-31',
            'wage': 7500000.0,
            'type_id': self.type.id,
            'employee_id': employee.id,
            'struct_id': struct.id,
            'working_hours': self.resource.id
        }

        contract = self.obj_contract.create(vals)
        return contract

    def test_get_worked_day_lines(self):
        # Create Holiday
        self._create_holiday()

        # Create Employee
        employee = self._create_employee()

        # Create Structure
        struct = self._create_structure()

        # Create Contract
        contract = self._create_contract(
            employee=employee,
            struct=struct)

        # Create Payslip
        vals = {
            'employee_id': employee.id,
            'contract_id': contract.id,
            'struct_id': struct.id,
            'date_from': '2017-02-1',
            'date_to': '2017-02-28'
        }
        new = self.obj_payslip.create(vals)
        onchange = new.onchange_employee_id(
            date_to=new.date_to,
            date_from=new.date_from,
            employee_id=new.employee_id.id,
            contract_id=new.contract_id.id
        )
        worked_days_line_ids =\
            onchange["value"]["worked_days_line_ids"][0]
        self.assertEqual(19.0, worked_days_line_ids['number_of_days'])
