# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    home_lau1_id = fields.Many2one(
        string="Local Admin. Unit 1",
        comodel_name="res.partner.lau",
        domain=[
            ("level", "=", 1),
        ],
        related="address_home_id.lau1_id",
    )
    home_lau2_id = fields.Many2one(
        string="Local Admin. Unit 2",
        comodel_name="res.partner.lau",
        domain=[
            ("level", "=", 2),
        ],
        related="address_home_id.lau2_id",
    )

    @api.multi
    @api.onchange("home_lau1_id")
    def onchange_home_lau2(self):
        for employee in self:
            if employee.home_lau2_id and \
                    employee.home_lau2_id.parent_id != employee.home_lau1_id:
                employee.home_lau2_id = False
