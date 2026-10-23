# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestSsiHrEmployeeProjectExperience(YamlTransactionCase):
    """Cover the project experience SQL view model."""

    def test_ssi_hr_employee_project_experience(self):
        """Run the SQL view accessibility scenario."""
        self.run_yaml_scenario("test_data_ssi_hr_employee_project_experience.yaml")
