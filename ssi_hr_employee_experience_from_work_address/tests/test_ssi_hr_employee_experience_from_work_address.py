# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestSsiHrEmployeeExperienceFromWorkAddress(YamlTransactionCase):
    """Scenario tests for experience fields on ``hr.employee``."""

    def test_ssi_hr_employee_experience_from_work_address(self):
        """Run the related experience fields scenario.

        Verifies the three experience lists are readable from an
        employee that has a home address.
        """
        self.run_yaml_scenario(
            "test_data_ssi_hr_employee_experience_from_work_address.yaml"
        )
