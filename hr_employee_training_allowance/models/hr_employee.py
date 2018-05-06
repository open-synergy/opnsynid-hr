# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    allowance_pricelist_id = fields.Many2one(
        string="Training Allowance Pricelist",
        comodel_name="product.pricelist",
        company_dependent=True,
    )
