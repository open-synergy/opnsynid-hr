# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    @api.multi
    @api.depends(
        "job_id"
    )
    def _compute_job_grade(self):
        for employee in self:
            result = False
            if employee.job_id:
                result = employee.job_id.job_grade_ids.ids
            employee.allowed_job_grade_ids = result

    job_grade_id = fields.Many2one(
        string="Job Grade",
        comodel_name="hr.job_grade",
        required=False,
    )
    allowed_job_grade_ids = fields.Many2many(
        string="Job Grades",
        comodel_name="hr.job_grade",
        compute="_compute_job_grade",
        store=False,
    )
    # job_family_grade_id = fields.Many2one(
    #     string="Job Family Grade",
    #     comodel_name="hr.job_family_grade",
    #     required=False,
    # )
