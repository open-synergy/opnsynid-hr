# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    country_id = fields.Many2one(
        string="Nationality",
        comodel_name="res.country",
        related="address_home_id.nationality_id",
        store=True,
    )
