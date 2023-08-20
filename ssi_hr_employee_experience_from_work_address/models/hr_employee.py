# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    academic_ids = fields.One2many(
        comodel_name="partner.academic",
        related="address_home_id.academic_ids",
        string="Academic experiences",
        help="Academic experiences",
        readonly=False,
    )
    certification_ids = fields.One2many(
        comodel_name="partner.certification",
        related="address_home_id.certification_ids",
        string="Certifications",
        help="Certifications",
        readonly=False,
    )
    experience_ids = fields.One2many(
        comodel_name="partner.experience",
        related="address_home_id.experience_ids",
        string="Professional Experiences",
        help="Professional Experiences",
        readonly=False,
    )
