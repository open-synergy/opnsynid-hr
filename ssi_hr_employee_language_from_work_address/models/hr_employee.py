# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    language_ids = fields.One2many(
        comodel_name="partner.language",
        related="address_home_id.language_ids",
        string="Languages",
        help="Languages",
        readonly=False,
        compute_sudo=True,
    )
