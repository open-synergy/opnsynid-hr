# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    id_numbers = fields.One2many(
        comodel_name="res.partner.id_number",
        related="address_home_id.id_numbers",
        string="Identification Numbers",
        help="Identification Numbers",
        readonly=False,
    )
