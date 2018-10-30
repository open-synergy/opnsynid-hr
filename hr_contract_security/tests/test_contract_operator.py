# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from .base import BaseCase
from openerp.exceptions import except_orm


class TestContractOperator(BaseCase):

    def test_contract_user(self):
        # Condition 1:
        # 1. Employee 1 create a new contract for himself
        # 2. Group Employee 1:
        #       (1) Employee,
        #       (2) Contract Security User Groups
        # 3. Employee 1 has Department Technology Information
        # Result:
        # 1. Create successfully
        contract_1 = self.obj_contract.sudo(self.user_1).create({
            "name": "Contract 1",
            "employee_id": self.employee_1.id,
            "wage": 500.00,
        })
        self.assertIsNotNone(contract_1)

        # Condition 2:
        # 1. Employee 1 create a new contract for Employee 2
        # 2. Employee 2 has Department Database Administrator
        # 3. Department Database Administrator is child of
        #    department Technology Information
        # 4. Group Employee 1:
        #       (1) Employee,
        #       (2) Contract Security User Groups
        # Result:
        # 1. Raise Error
        with self.assertRaises(except_orm):
            self.obj_contract.sudo(self.user_1).create({
                "name": "Contract 2",
                "employee_id": self.employee_2.id,
                "wage": 500.00,
            })

        # Condition 3:
        # 1. Employee 1 create a new contract for Employee 3
        # 2. Employee 3 has a department same as Employee 1
        # 3. Group Employee 1:
        #       (1) Employee,
        #       (2) Contract Security User Groups
        # Result:
        # 1. Raise Error
        with self.assertRaises(except_orm):
            self.obj_contract.sudo(self.user_1).create({
                "name": "Contract 3",
                "employee_id": self.employee_3.id,
                "wage": 500.00,
            })

        # Condition 4:
        # 1. Employee 1 create a new contract for Employee 4
        # 2. Employee 4 has a Human Resources
        # 3. Group Employee 1:
        #       (1) Employee,
        #       (2) Contract Security User Groups
        # Result:
        # 1. Raise Error
        with self.assertRaises(except_orm):
            self.obj_contract.sudo(self.user_1).create({
                "name": "Contract 4",
                "employee_id": self.employee_4.id,
                "wage": 500.00,
            })

    def test_contract_supervisor(self):
        # Condition 1:
        # 1. Employee 2 create a new contract for himself
        # 2. Group Employee 2:
        #       (1) Employee,
        #       (2) Supervisor User
        # 3. Employee 2 has Department Database Administrator
        # Result:
        # 1. Create successfully
        contract_5 = self.obj_contract.sudo(self.user_2).create({
            "name": "Contract 5",
            "employee_id": self.employee_2.id,
            "wage": 500.00,
        })
        self.assertIsNotNone(contract_5)

        # Condition 2:
        # 1. Employee 2 create a new contract for Employee 1
        # 2. Employee 2 has Department Database Administrator
        # 3. Employee 1 has Department Technology Information
        # 4. Department Technology Information
        #   is a parent of Database Administrator
        # 5. Group Employee 2:
        #       (1) Employee,
        #       (2) Supervisor User
        # Result:
        # 1. Raise Error
        with self.assertRaises(except_orm):
            self.obj_contract.sudo(self.user_2).create({
                "name": "Contract 6",
                "employee_id": self.employee_1.id,
                "wage": 500.00,
            })

        # Condition 3:
        # 1. Employee 2 create a new contract for Employee 4
        # 2. Employee 4 has Department Human Resources
        # 3. Group Employee 2:
        #       (1) Employee,
        #       (2) Supervisor User
        # Result:
        # 1. Raise Error
        with self.assertRaises(except_orm):
            self.obj_contract.sudo(self.user_2).create({
                "name": "Contract 7",
                "employee_id": self.employee_4.id,
                "wage": 500.00,
            })

        # Condition 4:
        # 1. Employee 2 create a new contract for Employee 5
        # 2. Employee 2 Manager of Department Database Administrator
        # 3. Employee 5 has Department Database Administrator
        # 4. Group Employee 2:
        #       (1) Employee,
        #       (2) Supervisor User
        # Result:
        # 1. Create Sucessfully
        check_manager_id = self.employee_5.parent_id.id

        self.assertIsNotNone(check_manager_id)
        self.assertEqual(check_manager_id, self.employee_2.id)

        contract_8 = self.obj_contract.sudo(self.user_2).create({
            "name": "Contract 8",
            "employee_id": self.employee_5.id,
            "wage": 500.00,
        })

        self.assertIsNotNone(contract_8)

    def test_contract_department(self):
        # Condition 1:
        # 1. Employee 4 create a new contract for himself
        # 2. Group Employee 4:
        #       (1) Employee,
        #       (2) Department User
        # 3. Employee 4 has Department Human Resource
        # Result:
        # 1. Create successfully
        contract_9 = self.obj_contract.sudo(self.user_4).create({
            "name": "Contract 9",
            "employee_id": self.employee_4.id,
            "wage": 500.00
        })
        self.assertIsNotNone(contract_9)

        # Condition 2:
        # 1. Employee 4 create a new contract for Employee 1
        # 2. Employee 1 has Department Technical Information
        # 3. Employee 6 has Department Recruitment
        # 4. Group Employee 4:
        #       (1) Employee,
        #       (2) Department User
        # Result:
        # 1. Raise Error
        with self.assertRaises(except_orm):
            self.obj_contract.sudo(self.user_4).create({
                "name": "Contract 10",
                "employee_id": self.employee_1.id,
                "wage": 500.00,
            })

        # Condition 3:
        # 1. Employee 4 create a new contract for Employee 1
        # 2. Employee 4 has Department Human Resources
        # 3. Employee 1 has Department Technology Information
        # 4. Group Employee 2:
        #       (1) Employee,
        #       (2) Department User
        # Result:
        # 1. Raise Error
        with self.assertRaises(except_orm):
            self.obj_contract.sudo(self.user_4).create({
                "name": "Contract 11",
                "employee_id": self.employee_1.id,
                "wage": 500.00,
            })

        # Condition 4:
        # 1. Employee 4 create a new contract for Employee 7
        # 2. Employee 4 has Department Human Resource
        # 3. Employee 7 has Department Compensation and Evaluations
        # 4. Department Human Resource
        #    is a parent of Compensation and Evaluations
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

        contract_12 = self.obj_contract.sudo(self.user_4).create({
            "name": "Contract 12",
            "employee_id": self.employee_7.id,
            "wage": 500.00,
        })

        self.assertIsNotNone(contract_12)

    def test_contract_company(self):
        # Condition 1:
        # 1. Employee 8 create a new contract for himself
        # 2. Group Employee 8:
        #       (1) Employee,
        #       (2) Company User
        # 3. Employee 8 has Department Finance and Accounting
        # 4. Employee 8 has Main Company
        # Result:
        # 1. Create successfully
        contract_13 = self.obj_contract.sudo(self.user_8).create({
            "name": "Contract 13",
            "employee_id": self.employee_8.id,
            "wage": 500.00
        })
        self.assertIsNotNone(contract_13)

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
        contract_14 = self.obj_contract.sudo(self.user_8).create({
            "name": "Contract 14",
            "employee_id": self.employee_6.id,
            "wage": 500.00,
        })
        self.assertIsNotNone(contract_14)

        # Condition 3:
        # 1. Employee 8 create a new contract for Employee 10
        # 2. Employee 8 has Department Finance and Accounting
        # 3. Employee 10 has Department Cash Office
        # 4. Group Employee 8:
        #       (1) Employee,
        #       (2) Company User
        # 5. Employee 8 has Main Company
        # 6. Employee 10 has Opensynergy Indonesia Company
        # 7. Opensynergy Indonesia is child of Main Company
        # Result:
        # 1. Raise Error
        check_company_id_user_8 = self.user_8.company_id.id
        check_company_id_user_10 = self.user_10.company_id.id

        self.assertIsNotNone(check_company_id_user_8)
        self.assertIsNotNone(check_company_id_user_10)
        self.assertNotEqual(
            check_company_id_user_8,
            check_company_id_user_10)

        contract_15 = self.obj_contract.sudo(self.user_8).create({
            "name": "Contract 15",
            "employee_id": self.employee_10.id,
            "wage": 500.00,
        })

        self.assertIsNotNone(contract_15)

        # Condition 4:
        # 1. Employee 8 create a new contract for Employee 11
        # 2. Employee 8 has Department Finance and Accounting
        # 3. Employee 11 has Department Training and Development
        # 4. Group Employee 8:
        #       (1) Employee,
        #       (2) Company User
        # 5. Employee 8 has Main Company
        # 6. Employee 11 has Kawula Odoo Indonesia Company
        # Result:
        # 1. Raise Error
        check_company_id_user_8 = self.user_8.company_id.id
        check_company_id_user_11 = self.user_11.company_id.id

        self.assertIsNotNone(check_company_id_user_8)
        self.assertIsNotNone(check_company_id_user_11)
        self.assertNotEqual(
            check_company_id_user_8,
            check_company_id_user_11
        )

        with self.assertRaises(except_orm):
            self.obj_contract.sudo(self.user_8).create({
                "name": "Contract 16",
                "employee_id": self.employee_11.id,
                "wage": 500.00,
            })
