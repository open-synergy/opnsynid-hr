# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    ethnicity_id = fields.Many2one(
        string="Ethnicity",
        comodel_name="partner.ethnicity",
        related="address_home_id.ethnicity_id",
        store=True,
    )
