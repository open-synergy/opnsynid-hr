# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.exceptions import except_orm

from .base import BaseCase


class TestContractViewer(BaseCase):
    def test_contract_viewer_supervisor(self):
        # Condition 1:
        # 1. Employee 2 create a new contract for himself
        # 2. Group Employee 2:
        #       (1) Employee,
        #       (2) Supervisor Operator,
        #       (3) Supervisor Viewer
        # 3. Employee 2 has Department Database Administrator
        # Result:
        # 1. Create successfully
        contract_1 = self.obj_contract.sudo(self.user_2).create(
            {
                "name": "Contract 1",
                "employee_id": self.employee_2.id,
                "wage": 500.00,
            }
        )
        self.assertIsNotNone(contract_1)

        # Condition 2:
        # 1. Employee 2 create a new contract for Employee 5
        # 2. Employee 2 Manager of Department Database Administrator
        # 3. Employee 5 has Department Database Administrator
        # Result:
        # 1. Create Sucessfully
        check_manager_id = self.employee_5.parent_id.id

        self.assertIsNotNone(check_manager_id)
        self.assertEqual(check_manager_id, self.employee_2.id)

        contract_2 = self.obj_contract.sudo(self.user_2).create(
            {
                "name": "Contract 2",
                "employee_id": self.employee_5.id,
                "wage": 500.00,
            }
        )

        self.assertIsNotNone(contract_2)

        # Condition 3:
        # 1. Employee 1 create a new contract for himself
        # 2. Group  Employee 1:
        #       (1) Employee,
        #       (2) Contract Security User Groups
        # 3. Employee 1 has Department Technology Information
        # Result:
        # 1. Create successfully
        contract_3 = self.obj_contract.sudo(self.user_1).create(
            {
                "name": "Contract 3",
                "employee_id": self.employee_1.id,
                "wage": 500.00,
            }
        )
        self.assertIsNotNone(contract_3)

        # Condition 4:
        # 1. Check Visibility data of Contract for Employee 1
        # Result:
        # 1. Employee 1 can only see contract under his management
        #    which is (1)contract_1 and (2)contract_2
        self.assertEqual(contract_1.sudo(self.user_2).name, "Contract 1")
        self.assertEqual(contract_2.sudo(self.user_2).name, "Contract 2")
        with self.assertRaises(except_orm):
            contract_3.sudo(self.user_2).name

    def test_contract_viewer_department(self):
        # Condition 1:
        # 1. Employee 4 create a new contract for himself
        # 2. Group Employee 4:
        #       (1) Employee,
        #       (2) Department Operator,
        #       (3) Department Viewer
        # 3. Employee 4 has Department Human Resource
        # Result:
        # 1. Create successfully
        contract_5 = self.obj_contract.sudo(self.user_4).create(
            {"name": "Contract 5", "employee_id": self.employee_4.id, "wage": 500.00}
        )
        self.assertIsNotNone(contract_5)

        # Condition 2:
        # 1. Employee 4 create a new contract for Employee 7
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

        contract_6 = self.obj_contract.sudo(self.user_4).create(
            {
                "name": "Contract 6",
                "employee_id": self.employee_7.id,
                "wage": 500.00,
            }
        )

        self.assertIsNotNone(contract_6)

        # Condition 3:
        # 1. Employee 8 create a new contract for himself
        # 2. Group Employee 8:
        #       (1) Employee,
        #       (2) Company User
        # 3. Employee 8 has Department Finance and Accounting
        # Result:
        # 1. Create successfully
        contract_7 = self.obj_contract.sudo(self.user_8).create(
            {"name": "Contract 7", "employee_id": self.employee_8.id, "wage": 500.00}
        )
        self.assertIsNotNone(contract_7)

        # Condition 4:
        # 1. Check Visibility data of Contract for Employee 4
        # Result:
        # 1. Employee 4 can only see contract under his department
        #    which is (1)contract_5 and (2)contract_6
        self.assertEqual(contract_5.sudo(self.user_4).name, "Contract 5")
        self.assertEqual(contract_6.sudo(self.user_4).name, "Contract 6")
        with self.assertRaises(except_orm):
            contract_7.sudo(self.user_4).name

    def test_contract_viewer_company(self):
        # Condition 1:
        # 1. Employee 8 create a new contract for himself
        # 2. Group Employee 8:
        #       (1) Employee,
        #       (2) Company User
        # 3. Employee 8 has Department Finance and Accounting
        # 4. Employee 8 has Main Company
        # Result:
        # 1. Create successfully
        contract_8 = self.obj_contract.sudo(self.user_8).create(
            {"name": "Contract 8", "employee_id": self.employee_8.id, "wage": 500.00}
        )
        self.assertIsNotNone(contract_8)

        # Condition 2:
        # 1. Employee 8 create a new contract for Employee 9
        # 2. Employee 8 has Department Finance and Accounting
        # 3. Employee 9 has Department Payroll Service
        # 4. Department Finance and Accounting is a parent of Payroll Service
        # 5. Group Employee 8:
        #       (1) Employee,
        #       (2) Company User
        # 6. Employee 8 has Main Company
        # Result:
        # 1. Create successfully
        contract_9 = self.obj_contract.sudo(self.user_8).create(
            {
                "name": "Contract 9",
                "employee_id": self.employee_6.id,
                "wage": 500.00,
            }
        )
        self.assertIsNotNone(contract_9)

        # Condition 3:
        # 1. Employee 11 create a new contract for himself
        # 2. Group Employee 11:
        #       (1) Employee,
        #       (2) Company User
        # 3. Employee 11 has Training and Development
        # 4. Employee 11 has Kawula Odoo Indonesia Company
        # Result:
        # 1. Create successfully
        contract_10 = self.obj_contract.create(
            {
                "name": "Contract 10",
                "employee_id": self.employee_11.id,
                "wage": 500.00,
            }
        )

        self.assertIsNotNone(contract_10)

        # Condition 4:
        # 1. Check Visibility data of Contract for Employee 8
        # Result:
        # 1. Employee 4 can only see contract under his company
        #    which is (1)contract_8 and (2)contract_9
        self.assertEqual(contract_8.sudo(self.user_8).name, "Contract 8")
        self.assertEqual(contract_9.sudo(self.user_8).name, "Contract 9")
        with self.assertRaises(except_orm):
            contract_10.sudo(self.user_8).name
