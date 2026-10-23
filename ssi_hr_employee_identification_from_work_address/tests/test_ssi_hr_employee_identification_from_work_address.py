# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestSsiHrEmployeeIdentificationFromWorkAddress(YamlTransactionCase):
    """Scenario tests for identification numbers on ``hr.employee``."""

    def test_ssi_hr_employee_identification_from_work_address(self):
        """Run the related identification numbers scenario.

        Verifies the ``id_numbers`` list is readable from an employee
        that has a home address.
        """
        self.run_yaml_scenario(
            "test_data_ssi_hr_employee_identification_from_work_address.yaml"
        )
