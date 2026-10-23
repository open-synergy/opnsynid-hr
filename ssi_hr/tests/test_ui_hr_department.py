# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# HttpSavepointCase, not HttpCase: HttpCase has no cls.env in 14.0.
from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiHrDepartment(HttpSavepointCase):
    """Tour tests for the ``hr.department`` work instructions."""

    def test_create(self):
        """Run the create tour for ``hr.department``.

        IK: docs/hr_department/01-create.md
        """
        self.start_tour("/web", "ssi_hr_hr_department_create", login="admin")
