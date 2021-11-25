# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    job_grade_id = fields.Many2one(
        string="Job Grade",
        comodel_name="hr.job_grade",
        required=False,
        related="current_contract_id.job_grade_id",
        store=True,
        readonly=True,
    )
