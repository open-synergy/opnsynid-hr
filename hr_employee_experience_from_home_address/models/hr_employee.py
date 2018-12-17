# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    academic_ids = fields.One2many(
        comodel_name="partner.academic",
        related="address_home_id.academic_ids",
        string="Academic experiences",
        help="Academic experiences"
    )
    certification_ids = fields.One2many(
        comodel_name="partner.certification",
        related="address_home_id.certification_ids",
        string="Certifications",
        help="Certifications"
    )
    experience_ids = fields.One2many(
        comodel_name="partner.experience",
        related="address_home_id.experience_ids",
        string="Professional Experiences",
        help="Professional Experiences"
    )
