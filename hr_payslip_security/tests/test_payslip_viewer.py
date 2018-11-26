# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from .base import BaseCase
from openerp.exceptions import except_orm


class TestPayslipViewer(BaseCase):
    def test_payslip_viewer_supervisor(self):
        # Condition 1:
        # 1. Employee 2 create a new payslip for himself
        # 2. Group Employee 2:
        #       (1) Employee,
        #       (2) Supervisor Operator,
        #       (3) Supervisor Viewer
        # 3. Employee 2 has Department Database Administrator
        # Result:
        # 1. Create successfully
        payslip_1 = self.obj_payslip.sudo(self.user_2).create({
            "name": "Payslip 1",
            "employee_id": self.employee_2.id,
            "date_from": self.date_from,
            "date_to": self.date_to
        })
        self.assertIsNotNone(payslip_1)

        # Condition 2:
        # 1. Employee 2 create a new payslip for Employee 5
        # 2. Employee 2 Manager of Department Database Administrator
        # 3. Employee 5 has Department Database Administrator
        # Result:
        # 1. Create Sucessfully
        check_manager_id = self.employee_5.parent_id.id

        self.assertIsNotNone(check_manager_id)
        self.assertEqual(check_manager_id, self.employee_2.id)

        payslip_2 = self.obj_payslip.sudo(self.user_2).create({
            "name": "Payslip 2",
            "employee_id": self.employee_5.id,
            "date_from": self.date_from,
            "date_to": self.date_to
        })

        self.assertIsNotNone(payslip_2)

        # Condition 3:
        # 1. Employee 1 create a new payslip for himself
        # 2. Group  Employee 1:
        #       (1) Employee,
        #       (2) Payslip Security User Groups
        # 3. Employee 1 has Department Technology Information
        # Result:
        # 1. Create successfully
        payslip_3 = self.obj_payslip.sudo(self.user_1).create({
            "name": "Payslip 3",
            "employee_id": self.employee_1.id,
            "date_from": self.date_from,
            "date_to": self.date_to
        })
        self.assertIsNotNone(payslip_3)

        # Condition 4:
        # 1. Check Visibility data of Payslip for Employee 1
        # Result:
        # 1. Employee 1 can only see payslip under his management
        #    which is (1)payslip_1 and (2)payslip_2
        self.assertEqual(
            payslip_1.sudo(self.user_2).name,
            "Payslip 1")
        self.assertEqual(
            payslip_2.sudo(self.user_2).name,
            "Payslip 2")
        with self.assertRaises(except_orm):
            payslip_3.sudo(self.user_2).name

    def test_payslip_viewer_department(self):
        # Condition 1:
        # 1. Employee 4 create a new payslip for himself
        # 2. Group Employee 4:
        #       (1) Employee,
        #       (2) Department Operator,
        #       (3) Department Viewer
        # 3. Employee 4 has Department Human Resource
        # Result:
        # 1. Create successfully
        payslip_5 = self.obj_payslip.sudo(self.user_4).create({
            "name": "Payslip 5",
            "employee_id": self.employee_4.id,
            "date_from": self.date_from,
            "date_to": self.date_to
        })
        self.assertIsNotNone(payslip_5)

        # Condition 2:
        # 1. Employee 4 create a new payslip for Employee 7
        # 2. Employee 4 has Department Human Resource
        # 3. Employee 7 has Department Compensation and Evaluations
        # 4. Department Human Resource is a parent of
        #    Compensation and Evaluations
        # 5. Employee 4 is manager of department Compensation and Evaluations
        # 6. Group Employee 4:
        #       (1) Employee,
        #       (2) Department User
        # Result:
        # 1. Create Sucessfully
        self.dept_CAE.manager_id = self.employee_4.id
        check_manager_id = self.dept_CAE.manager_id.id

        self.assertIsNotNone(check_manager_id)
        self.assertEqual(check_manager_id, self.employee_4.id)

        payslip_6 = self.obj_payslip.sudo(self.user_4).create({
            "name": "Payslip 6",
            "employee_id": self.employee_7.id,
            "date_from": self.date_from,
            "date_to": self.date_to
        })

        self.assertIsNotNone(payslip_6)

        # Condition 3:
        # 1. Employee 8 create a new payslip for himself
        # 2. Group Employee 8:
        #       (1) Employee,
        #       (2) Company User
        # 3. Employee 8 has Department Finance and Accounting
        # Result:
        # 1. Create successfully
        payslip_7 = self.obj_payslip.sudo(self.user_8).create({
            "name": "Payslip 7",
            "employee_id": self.employee_8.id,
            "date_from": self.date_from,
            "date_to": self.date_to
        })
        self.assertIsNotNone(payslip_7)

        # Condition 4:
        # 1. Check Visibility data of Payslip for Employee 4
        # Result:
        # 1. Employee 4 can only see payslip under his department
        #    which is (1)payslip_5 and (2)payslip_6
        self.assertEqual(
            payslip_5.sudo(self.user_4).name,
            "Payslip 5")
        self.assertEqual(
            payslip_6.sudo(self.user_4).name,
            "Payslip 6")
        with self.assertRaises(except_orm):
            payslip_7.sudo(self.user_4).name

    def test_payslip_viewer_company(self):
        # Condition 1:
        # 1. Employee 8 create a new payslip for himself
        # 2. Group Employee 8:
        #       (1) Employee,
        #       (2) Company User
        # 3. Employee 8 has Department Finance and Accounting
        # 4. Employee 8 has Main Company
        # Result:
        # 1. Create successfully
        payslip_8 = self.obj_payslip.sudo(self.user_8).create({
            "name": "Payslip 8",
            "employee_id": self.employee_8.id,
            "date_from": self.date_from,
            "date_to": self.date_to
        })
        self.assertIsNotNone(payslip_8)

        # Condition 2:
        # 1. Employee 8 create a new payslip for Employee 9
        # 2. Employee 8 has Department Finance and Accounting
        # 3. Employee 9 has Department Payroll Service
        # 4. Department Finance and Accounting is a parent of Payroll Service
        # 5. Group Employee 8:
        #       (1) Employee,
        #       (2) Company User
        # 6. Employee 8 has Main Company
        # Result:
        # 1. Create successfully
        payslip_9 = self.obj_payslip.sudo(self.user_8).create({
            "name": "Payslip 9",
            "employee_id": self.employee_6.id,
            "date_from": self.date_from,
            "date_to": self.date_to
        })
        self.assertIsNotNone(payslip_9)

        # Condition 3:
        # 1. Employee 11 create a new payslip for himself
        # 2. Group Employee 11:
        #       (1) Employee,
        #       (2) Company User
        # 3. Employee 11 has Training and Development
        # 4. Employee 11 has Kawula Odoo Indonesia Company
        # Result:
        # 1. Create successfully
        payslip_10 = self.obj_payslip.create({
            "name": "Payslip 10",
            "employee_id": self.employee_11.id,
            "date_from": self.date_from,
            "date_to": self.date_to
        })

        self.assertIsNotNone(payslip_10)

        # Condition 4:
        # 1. Check Visibility data of Payslip for Employee 8
        # Result:
        # 1. Employee 4 can only see payslip under his company
        #    which is (1)payslip_8 and (2)payslip_9
        self.assertEqual(
            payslip_8.sudo(self.user_8).name,
            "Payslip 8")
        self.assertEqual(
            payslip_9.sudo(self.user_8).name,
            "Payslip 9")
        with self.assertRaises(except_orm):
            payslip_10.sudo(self.user_8).name
