# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    religion_id = fields.Many2one(
        string="Religion",
        comodel_name="partner.religion",
        related="address_home_id.religion_id",
        store=True,
    )
