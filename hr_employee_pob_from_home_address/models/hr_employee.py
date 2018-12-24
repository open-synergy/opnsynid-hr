# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    place_of_birth = fields.Char(
        string="Place of Birth",
        related="address_home_id.place_of_birth",
        store=True,
    )
