# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiHrEmployee(HttpSavepointCase):
    """Tour tests for the ``hr.employee`` work instructions.

    Uses ``HttpSavepointCase`` rather than plain ``HttpCase``: in 14.0
    ``TransactionCase`` only assigns ``self.env`` inside instance
    ``setUp()``, so ``cls.env`` is not available in ``setUpClass()``.
    """

    @classmethod
    def setUpClass(cls):
        """Seed an employee that has a home address for the tour.

        Pre-Condition of ``docs/hr_employee/02-edit.md``: the employee
        has a Home Address. The group is granted to ``admin``
        explicitly, and the employee is owned by the ``admin`` user so
        it is visible to the tour session.
        """
        super().setUpClass()
        cls.env.ref("ssi_hr.hr_employee_group").sudo().write(
            {"users": [(4, cls.env.ref("base.user_admin").id)]}
        )
        partner = cls.env["res.partner"].create({"name": "TOUR-EXPERIENCE-PARTNER-UI"})
        cls.employee_experience = cls.env["hr.employee"].create(
            {
                "name": "TOUR-EXPERIENCE-EMPLOYEE-UI",
                "address_home_id": partner.id,
            }
        )

    def test_hr_employee_edit_tour(self):
        """Run the Experiences tab tour.

        IK: docs/hr_employee/02-edit.md
        """
        self.start_tour(
            "/web",
            "ssi_hr_employee_experience_from_work_address_hr_employee_edit",
            login="admin",
        )
