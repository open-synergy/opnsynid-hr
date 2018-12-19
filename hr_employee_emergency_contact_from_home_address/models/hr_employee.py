# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    emergency_contact_ids = fields.Many2many(
        string="Emergency Contact",
        comodel_name="res.partner",
        related="address_home_id.emergency_contact_ids",
        readonly=False,
    )
