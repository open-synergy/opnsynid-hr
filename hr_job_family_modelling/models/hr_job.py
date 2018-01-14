# -*- coding: utf-8 -*-
# Copyright 2018-2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api


class HrJob(models.Model):
    _inherit = "hr.job"

    @api.multi
    @api.depends(
        "job_family_level_id"
    )
    def _compute_job_grade(self):
        for job in self:
            result = False
            if job.job_family_level_id:
                result = job.job_family_level_id.job_grade_ids.ids
            job.allowed_job_grade_ids = result

    job_family_level_id = fields.Many2one(
        string="Job Family Level",
        comodel_name="hr.job_family_level",
    )
    allowed_job_grade_ids = fields.Many2many(
        string="Job Grades",
        comodel_name="hr.job_grade",
        compute="_compute_job_grade",
        store=False,
    )
    job_grade_ids = fields.Many2many(
        string="Job Grades",
        comodel_name="hr.job_grade",
        relation="rel_job_2_grade",
        column1="job_id",
        column2="job_grade_id",
    )

    @api.multi
    def onchange_job_family_level_id(self, job_family_level_id):
        value = self._get_value_before_onchange_job_family_level_id()
        domain = self._get_domain_before_onchange_job_family_level_id()

        if job_family_level_id:
            obj_job_family_level = self.env["hr.job_family_level"]
            job_family_level = obj_job_family_level.browse(
                [job_family_level_id])[0]
            value = self._get_value_after_onchange_job_family_level_id(
                job_family_level
            )
            domain = self._get_domain_after_onchange_job_family_level_id(
                job_family_level
            )
        return {"value": value, "domain": domain}

    @api.multi
    def _get_value_before_onchange_job_family_level_id(self):
        return {
            "job_grade_ids": [],
        }

    @api.multi
    def _get_domain_before_onchange_job_family_level_id(self):
        return {}

    @api.multi
    def _get_value_after_onchange_job_family_level_id(self, job_family_level):
        return {
            "job_grade_ids": [],
        }

    @api.multi
    def _get_domain_after_onchange_job_family_level_id(self, job_family_level):
        return {}
