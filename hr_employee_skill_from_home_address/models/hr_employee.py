# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    skill_ids = fields.One2many(
        comodel_name="partner.skill",
        related="address_home_id.skill_ids",
        string="Skills",
    )
