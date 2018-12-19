# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    home_lau3_id = fields.Many2one(
        string="Local Admin. Unit 3",
        comodel_name="res.partner.lau",
        domain=[
            ("level", "=", 3),
        ],
        related="address_home_id.lau3_id",
    )

    @api.multi
    @api.onchange("lau2_id")
    def onchange_home_lau3(self):
        for employee in self:
            if employee.home_lau3_id and \
                    employee.home_lau3_id.parent_id != employee.home_lau2_id:
                employee.home_lau3_id = False
