# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class HrContract(models.Model):
    _inherit = "hr.contract"

    department_id = fields.Many2one(
        string="Department",
        comodel_name="hr.department",
    )
    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
    )
