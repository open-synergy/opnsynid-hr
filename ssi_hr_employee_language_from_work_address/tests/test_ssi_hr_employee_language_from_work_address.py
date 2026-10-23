# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestSsiHrEmployeeLanguageFromWorkAddress(YamlTransactionCase):
    """Scenario tests for the employee language related field."""

    def test_ssi_hr_employee_language_from_work_address(self):
        """Run the related field accessibility scenario.

        The ``language_ids`` field must be readable on an employee that
        has a home address.
        """
        self.run_yaml_scenario(
            "test_data_ssi_hr_employee_language_from_work_address.yaml"
        )
