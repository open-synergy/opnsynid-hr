# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase
from datetime import datetime, timedelta


class BaseCase(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(BaseCase, self).setUp()

        self.obj_partner = self.env["res.partner"]
        self.obj_user = self.env["res.users"]
        self.obj_employee = self.env["hr.employee"]
        self.obj_department = self.env["hr.department"]
        self.grp_employee = self.env.ref("base.group_user")
        self.obj_payslip = self.env["hr.payslip"]
        self.obj_company = self.env["res.company"]
        self.main_company = self.env.ref("base.main_company").id
        date_now = datetime.now().date()
        self.date_from = date_now
        self.date_to = date_now + timedelta(days=25)

        # Create Partner Opensynergy Indonesia
        self.opnsynid_partner = self.obj_partner.create({
            "name": "Opensynergy Indonesia",
            "city": "DKI. Jakarta",
            "country_id": self.env.ref("base.id").id,
            "email": "openerp@opensynergy-indonesia.com",
            "is_company": True
        })

        # Create Company Opensynergy Indonesia
        self.opnsynid_company = self.obj_company.create({
            "name": "Opensynergy Indonesia",
            "partner_id": self.opnsynid_partner.id,
            "parent_id": self.main_company,
            "currency_id": self.env.ref("base.IDR").id
        })

        # Create Partner Kawula Odoo Indonesia
        self.koi_partner = self.obj_partner.create({
            "name": "Kawula Odoo Indonesia",
            "city": "DKI. Jakarta",
            "country_id": self.env.ref("base.id").id,
            "email": "openerp@koi.com",
            "is_company": True
        })

        # Create Company Kawula Odoo Indonesia
        self.koi_company = self.obj_company.create({
            "name": "Kawula Odoo Indonesia",
            "partner_id": self.koi_partner.id,
            "currency_id": self.env.ref("base.IDR").id
        })

        # Departement Technology Information
        self.dept_IT = self.obj_department.create({
            "name": "Technology Information",
        })
        # Departement Database Administrator
        self.dept_DB = self.obj_department.create({
            "name": "Database",
            "parent_id": self.dept_IT.id,
        })
        # Departement Software Engineer
        self.dept_SE = self.obj_department.create({
            "name": "Software Engineer",
            "parent_id": self.dept_IT.id
        })

        # Departement Human Resource
        self.dept_HR = self.obj_department.create({
            "name": "Human Resource",
        })
        # Departement Recruitment
        self.dept_RCR = self.obj_department.create({
            "name": "Recruitment",
            "parent_id": self.dept_HR.id
        })
        # Departement Compensation and Evaluations
        self.dept_CAE = self.obj_department.create({
            "name": "Compensation and Evaluations",
            "parent_id": self.dept_HR.id
        })
        # Departement Training and Development
        self.dept_TD = self.obj_department.create({
            "name": "Training and Development",
            "parent_id": self.dept_HR.id
        })

        # Departement Financial and Accounting
        self.dept_FA = self.obj_department.create({
            "name": "Finance and Accounting",
        })
        # Departement Payroll Services
        self.dept_PS = self.obj_department.create({
            "name": "Payroll Services",
            "parent_id": self.dept_FA.id
        })
        # Departement Cash Office
        self.dept_CO = self.obj_department.create({
            "name": "Cash Office",
            "parent_id": self.dept_FA.id
        })

        # Employee 1 With Payslip Security User Groups
        # Department Technology Information
        # User 1 With Main Company
        self.user_1 = self.obj_user.sudo().create({
            "login": "user.1",
            "name": "User 1",
            "password": "a",
            "groups_id": [(6, 0, [
                self.grp_employee.id,
                self.env.ref("hr_payslip_security.group_payslip_user").id]
            )],
            "company_id": self.main_company
        })
        self.employee_1 = self.obj_employee.create({
            "name": "Employee 1",
            "user_id": self.user_1.id,
            "department_id": self.dept_IT.id,
        })

        # Employee 2 With Supervisor Groups
        # Department Database Administrator
        # User 2 With Main Company
        self.user_2 = self.obj_user.sudo().create({
            "login": "user.2",
            "name": "User 2",
            "password": "a",
            "groups_id": [(6, 0, [
                self.grp_employee.id,
                self.env.ref(
                    "hr_payslip_security.group_payslip_supervisor").id,
                self.env.ref(
                    "hr_payslip_security.group_payslip_viewer_supervisor"
                ).id]
            )],
            "company_id": self.main_company
        })
        self.employee_2 = self.obj_employee.create({
            "name": "Employee 2",
            "user_id": self.user_2.id,
            "department_id": self.dept_DB.id,
        })

        # Employee 3 With Employee Groups
        # Department Technology Information
        # User 3 With Main Company
        self.user_3 = self.obj_user.sudo().create({
            "login": "user.3",
            "name": "User 3",
            "password": "a",
            "groups_id": [(6, 0, [
                self.grp_employee.id]
            )],
            "company_id": self.env.ref("base.main_company").id
        })
        self.employee_3 = self.obj_employee.create({
            "name": "Employee 3",
            "user_id": self.user_3.id,
            "department_id": self.dept_IT.id,
        })

        # Employee 4 With Department Groups
        # Department Human Resources
        # User 4 With Main Company
        self.user_4 = self.obj_user.sudo().create({
            "login": "user.4",
            "name": "User 4",
            "password": "a",
            "groups_id": [(6, 0, [
                self.grp_employee.id,
                self.env.ref(
                    "hr_payslip_security.group_payslip_department").id,
                self.env.ref(
                    "hr_payslip_security.group_payslip_viewer_department"
                ).id]
            )],
            "company_id": self.main_company
        })
        self.employee_4 = self.obj_employee.create({
            "name": "Employee 4",
            "user_id": self.user_4.id,
            "department_id": self.dept_HR.id,
        })

        # Employee 5 With Employee Groups
        # Department Database Administrator
        # Assign Employee 2 as Manager of Employee 5
        # User 5 With Main Company
        self.user_5 = self.obj_user.sudo().create({
            "login": "user.5",
            "name": "User 5",
            "password": "a",
            "groups_id": [(6, 0, [
                self.grp_employee.id,
            ]
            )],
            "company_id": self.main_company
        })
        self.employee_5 = self.obj_employee.create({
            "name": "Employee 5",
            "user_id": self.user_5.id,
            "department_id": self.dept_DB.id,
            "parent_id": self.employee_2.id
        })

        # Employee 6 With Employee Groups
        # Department Recruitment
        # User 6 With Main Company
        self.user_6 = self.obj_user.sudo().create({
            "login": "user.6",
            "name": "User 6",
            "password": "a",
            "groups_id": [(6, 0, [
                self.grp_employee.id,
            ]
            )],
            "company_id": self.main_company
        })
        self.employee_6 = self.obj_employee.create({
            "name": "Employee 6",
            "user_id": self.user_6.id,
            "department_id": self.dept_RCR.id,
        })

        # Employee 7 With Employee Groups
        # Department Recruitment
        # User 7 With Main Company
        self.user_7 = self.obj_user.sudo().create({
            "login": "user.7",
            "name": "User 7",
            "password": "a",
            "groups_id": [(6, 0, [
                self.grp_employee.id,
            ]
            )],
            "company_id": self.env.ref("base.main_company").id
        })
        self.employee_7 = self.obj_employee.create({
            "name": "Employee 7",
            "user_id": self.user_7.id,
            "department_id": self.dept_CAE.id,
        })

        # Employee 8 With Company Groups
        # Department Financial and Accounting
        # User 8 With Main Company
        self.user_8 = self.obj_user.sudo().create({
            "login": "user.8",
            "name": "User 8",
            "password": "a",
            "groups_id": [(6, 0, [
                self.grp_employee.id,
                self.env.ref("hr_payslip_security.group_payslip_company").id,
                self.env.ref(
                    "hr_payslip_security.group_payslip_viewer_department"
                ).id]
            )],
            "company_id": self.main_company
        })
        self.employee_8 = self.obj_employee.create({
            "name": "Employee 8",
            "user_id": self.user_8.id,
            "department_id": self.dept_FA.id,
        })

        # Employee 9 With Employee Groups
        # Department Financial and Accounting
        # User 9 With Main Company
        self.user_9 = self.obj_user.sudo().create({
            "login": "user.9",
            "name": "User 9",
            "password": "a",
            "groups_id": [(6, 0, [
                self.grp_employee.id]
            )],
            "company_id": self.main_company
        })
        self.employee_9 = self.obj_employee.create({
            "name": "Employee 8",
            "user_id": self.user_9.id,
            "department_id": self.dept_PS.id,
        })

        # Employee 10 With Employee Groups
        # Department Cash Office
        # User 10 With Opensynergy Indonesia Company
        self.user_10 = self.obj_user.sudo().create({
            "login": "user.10",
            "name": "User 10",
            "password": "a",
            "groups_id": [(6, 0, [
                self.grp_employee.id]
            )],
            "company_id": self.opnsynid_company.id,
            "company_ids": [(6, 0, [
                self.opnsynid_company.id]
            )],
        })
        self.employee_10 = self.obj_employee.create({
            "name": "Employee 10",
            "user_id": self.user_10.id,
            "department_id": self.dept_CO.id,
        })

        # Employee 11 With Employee Groups
        # Department Training and Development
        # User 11 With Kawula Odoo Indonesia Company
        self.user_11 = self.obj_user.sudo().create({
            "login": "user.11",
            "name": "User 11",
            "password": "a",
            "groups_id": [(6, 0, [
                self.grp_employee.id]
            )],
            "company_id": self.koi_company.id,
            "company_ids": [(6, 0, [
                self.koi_company.id]
            )],
        })
        self.employee_11 = self.obj_employee.create({
            "name": "Employee 11",
            "user_id": self.user_11.id,
            "department_id": self.dept_TD.id,
        })
