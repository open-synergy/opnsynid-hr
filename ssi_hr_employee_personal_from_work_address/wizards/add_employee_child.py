# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class AddEmployeeChild(models.TransientModel):
    """Wizard to add a child to an employee's home address partner.

    Collects the child's basic personal data, creates a private
    res.partner for the child, and links it to the home address of
    the employee through res.partner.link_child.
    """

    _name = "add_employee_child"
    _description = "Add Employee Child"

    @api.model
    def _default_employee_id(self):
        """Return the employee this wizard was opened from.

        :return: ``hr.employee`` id, or ``False`` when opened standalone
        """
        if self.env.context.get("active_model") == "hr.employee":
            return self.env.context.get("active_id", False)
        return False

    @api.model
    def _selection_gender(self):
        return self.env["res.partner"]._fields["gender"].selection

    employee_id = fields.Many2one(
        string="Employee",
        comodel_name="hr.employee",
        required=True,
        default=lambda self: self._default_employee_id(),
        help="Employee whose home address partner receives the child.",
    )
    name = fields.Char(
        string="Name",
        required=True,
        help="Full name of the child.",
    )
    birth_city = fields.Char(
        string="Place of Birth",
        help="City where the child was born.",
    )
    birthdate_date = fields.Date(
        string="Birthdate",
        help="Birth date of the child.",
    )
    gender = fields.Selection(
        string="Gender",
        selection="_selection_gender",
        help="Gender of the child.",
    )

    def action_add_child(self):
        """Create the child partner and link it to the employee.

        The wizard dialog is closed afterwards, so the employee form
        reloads and shows the new child.

        :return: an ``ir.actions.act_window_close`` dict
        """
        for record in self.sudo():
            record._add_child()
        return {"type": "ir.actions.act_window_close"}

    def _add_child(self):
        """Create the child partner and link it to the home address.

        Side effect: creates a private ``res.partner`` without a parent
        company contact, then calls ``link_child`` on the home address
        of the employee. The relationship follows the employee gender:
        father for male, mother for female, plain child otherwise.

        :raises UserError: if the employee has no home address
        """
        self.ensure_one()
        parent = self.employee_id.address_home_id
        if not parent:
            error_message = _(
                """
Context: Add employee child
Database ID: %s
Problem: Employee has no home address
Solution: Fill the Home Address of the employee, then add the child again
"""
                % (self.employee_id.id,)
            )
            raise UserError(error_message)
        child = self.env["res.partner"].create(self._prepare_child_values())
        parent.link_child(child, self._get_relationship())

    def _prepare_child_values(self):
        """Build the values used to create the child partner.

        :return: dict of ``res.partner`` create values
        """
        self.ensure_one()
        return {
            "name": self.name,
            "type": "private",
            "is_company": False,
            "birth_city": self.birth_city,
            "birthdate_date": self.birthdate_date,
            "gender": self.gender,
        }

    def _get_relationship(self):
        """Return the relationship of the employee towards the child.

        :return: ``father``, ``mother``, or ``False`` (plain child)
        """
        self.ensure_one()
        return {"male": "father", "female": "mother"}.get(
            self.employee_id.gender, False
        )
