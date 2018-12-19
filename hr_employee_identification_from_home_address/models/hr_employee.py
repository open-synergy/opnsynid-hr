# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    identification_ids = fields.One2many(
        comodel_name="res.partner.id_number",
        related="address_home_id.id_numbers",
        string="Identifications",
    )
