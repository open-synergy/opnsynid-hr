# -*- coding: utf-8 -*-
# © 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api, _
from openerp.exceptions import Warning as UserError


class HrJobFamily(models.Model):
    _name = "hr.job_family"
    _description = "Job Family"

    @api.multi
    @api.depends(
        "min_job_grade_id",
        "max_job_grade_id",
        "max_job_grade_id.sequence",
        "min_job_grade_id.sequence",
    )
    def _compute_job_grade_ids(self):
        obj_jg = self.env["hr.job_grade"]
        job_grade_ids = obj_jg.search([]).ids
        for jf in self:
            result = []
            if jf.min_job_grade_id and jf.max_job_grade_id:
                min_job_grade_id = jf.min_job_grade_id.id
                max_job_grade_id = jf.max_job_grade_id.id
                min_index = job_grade_ids.index(min_job_grade_id)
                max_index = job_grade_ids.index(max_job_grade_id)
                result = job_grade_ids[min_index:max_index + 1]
            jf.job_grade_ids = result

    name = fields.Char(
        string="Job Family",
        required=True,
        translate=True,
    )
    code = fields.Char(
        string="Code",
        required=True,
    )
    min_job_grade_id = fields.Many2one(
        string="Min. Grade",
        comodel_name="hr.job_grade",
        required=True,
    )
    max_job_grade_id = fields.Many2one(
        string="Max. Grade",
        comodel_name="hr.job_grade",
        required=True,
    )
    job_grade_ids = fields.Many2many(
        string="Job Grades",
        comodel_name="hr.job_grade",
        relation="rel_job_family_2_grade",
        column1="job_family_id",
        column2="job_grade_id",
        compute="_compute_job_grade_ids",
        store=True,
        readonly=True,
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
    note = fields.Text(
        string="Note",
    )

    @api.constrains(
        "min_job_grade_id",
        "max_job_grade_id",
    )
    def _check_min_max_grade(self):
        obj_jg = self.env["hr.job_grade"]
        job_grade_ids = obj_jg.search([]).ids
        msg = _("Wrong Max Min Grade")
        for jf in self:
            if jf.min_job_grade_id and jf.max_job_grade_id:
                min_job_grade_id = jf.min_job_grade_id.id
                max_job_grade_id = jf.max_job_grade_id.id
                min_index = job_grade_ids.index(min_job_grade_id)
                max_index = job_grade_ids.index(max_job_grade_id)
                if min_index > max_index:
                    raise UserError(msg)
