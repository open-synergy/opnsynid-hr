# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class HrEmployee(models.Model):
    # Extends hr.employee to sync personal information from the home
    # address partner.
    #
    # Provides related fields that mirror personal data (nationality,
    # gender, birth date, place of birth, blood type, religion,
    # ethnicity, etc.) from the employee's linked home address
    # (res.partner), keeping both records in sync.

    _inherit = "hr.employee"

    country_id = fields.Many2one(
        comodel_name="res.country",
        related="address_home_id.nationality_id",
        readonly=False,
        store=True,
        compute_sudo=True,
    )
    gender = fields.Selection(
        related="address_home_id.gender",
        readonly=False,
        store=True,
        compute_sudo=True,
    )
    birthday = fields.Date(
        related="address_home_id.birthdate_date",
        readonly=False,
        store=True,
        compute_sudo=True,
    )
    place_of_birth = fields.Char(
        related="address_home_id.birth_city",
        readonly=False,
        store=True,
        compute_sudo=True,
    )
    country_of_birth = fields.Many2one(
        comodel_name="res.country",
        related="address_home_id.birth_country_id",
        readonly=False,
        store=True,
        compute_sudo=True,
    )
    birth_state_id = fields.Many2one(
        string="Birth state",
        comodel_name="res.country.state",
        related="address_home_id.birth_state_id",
        readonly=False,
        store=True,
        compute_sudo=True,
    )
    blood_type = fields.Selection(
        string="Blood Type (ABO)",
        related="address_home_id.blood_type",
        readonly=False,
        store=True,
        compute_sudo=True,
    )
    blood_type_rhesus = fields.Selection(
        string="Blood Type (Rh)",
        related="address_home_id.blood_type_rhesus",
        readonly=False,
        store=True,
        compute_sudo=True,
    )
    religion_id = fields.Many2one(
        string="Religion",
        comodel_name="res_partner_religion",
        related="address_home_id.religion_id",
        readonly=False,
        store=True,
        compute_sudo=True,
    )
    ethnicity_id = fields.Many2one(
        string="Ethnicity",
        comodel_name="res_partner_ethnicity",
        related="address_home_id.ethnicity_id",
        readonly=False,
        store=True,
        compute_sudo=True,
    )
    marital = fields.Selection(
        string="Marital Status",
        related="address_home_id.marital",
        readonly=False,
        store=True,
        compute_sudo=True,
    )
    spouse_complete_name = fields.Char(
        string="Spouse Complete Name",
        related="address_home_id.spouse_complete_name",
        readonly=False,
        store=True,
        compute_sudo=True,
    )
    spouse_birthdate = fields.Date(
        string="Spouse Birthdate",
        related="address_home_id.spouse_birthdate",
        readonly=False,
        store=True,
        compute_sudo=True,
    )
    children_ids = fields.Many2many(
        string="Children",
        comodel_name="res.partner",
        related="address_home_id.children_ids",
        readonly=True,
        compute_sudo=True,
        help="Children of this employee, taken from the children of the "
        "home address contact.",
    )

    def action_add_child(self):
        """Open the wizard used to add a child to this employee.

        :return: an ``ir.actions.act_window`` dict opening the wizard
        """
        for record in self.sudo():
            result = record._add_child()
        return result

    def _add_child(self):
        """Build the window action opening the Add Child wizard.

        :return: an ``ir.actions.act_window`` dict, target new
        """
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Add Child",
            "res_model": "add_employee_child",
            "view_mode": "form",
            "target": "new",
            "context": {"default_employee_id": self.id},
        }
