# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestSsiHr(YamlTransactionCase):
    """Cover the employee initials generation of ``hr.employee``."""

    def test_ssi_hr(self):
        """Run the employee initials scenarios from the YAML file."""
        self.run_yaml_scenario("test_data_ssi_hr.yaml")
