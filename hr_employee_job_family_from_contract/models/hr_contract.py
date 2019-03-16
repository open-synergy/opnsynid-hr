# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class HrContract(models.Model):
    _inherit = "hr.contract"

    @api.multi
    @api.depends(
        "job_id"
    )
    def _compute_job_grade(self):
        for contract in self:
            result = False
            if contract.job_id:
                result = contract.job_id.job_grade_ids.ids
            contract.allowed_job_grade_ids = result

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

    @api.onchange("job_id")
    def onchange_job_grade_id(self):
        self.job_grade_id = False
