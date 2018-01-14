# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    job_grade_id = fields.Many2one(
        string="Job Grade",
        comodel_name="hr.job_grade",
        required=False,
    )
    job_family_grade_id = fields.Many2one(
        string="Job Family Grade",
        comodel_name="hr.job_family_grade",
        required=False,
    )
