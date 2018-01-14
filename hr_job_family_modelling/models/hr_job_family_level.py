# -*- coding: utf-8 -*-
# Copyright 2016-2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api, _
from odoo.exceptions import Warning as UserError


class HrJobFamilyLevel(models.Model):
    _name = "hr.job_family_level"
    _description = "Job Family Level"

    @api.multi
    @api.depends(
        "job_family_id",
    )
    def _compute_job_grade(self):
        for jfl in self:
            jfl.allowed_job_grade_ids = jfl.job_family_id.job_grade_ids.ids

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

    code = fields.Char(
        string="Code",
        required=True,
    )
    job_family_id = fields.Many2one(
        string="Job Family",
        comodel_name="hr.job_family",
        required=True,
    )
    job_family_grade_id = fields.Many2one(
        string="Job Family Grade",
        comodel_name="hr.job_family_grade",
        required=True,
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
        relation="rel_job_family_level_2_grade",
        column1="job_family_level_id",
        column2="job_grade_id",
        compute="_compute_job_grade_ids",
        store=True,
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
    active = fields.Boolean(
        string="Active",
        default=True,
    )
    note = fields.Text(
        string="Note",
    )

    @api.multi
    def name_get(self):
        result = []
        for jfl in self:
            grade_count = len(jfl.job_grade_ids)
            if grade_count == 0:
                min_grade = "-"
                max_grade = "-"
            else:
                min_grade = jfl.job_grade_ids[0].name
                max_grade = jfl.job_grade_ids[grade_count - 1].name

            name = "%s %s (%s - %s)" % (
                jfl.job_family_grade_id.name,
                jfl.job_family_id.name,
                min_grade,
                max_grade)
            result.append([jfl.id, name])
        return result

    @api.multi
    def onchange_job_family_id(self, job_family_id):
        value = self._get_value_before_onchange_job_family_id()
        domain = self._get_domain_before_onchange_job_family_id()

        if job_family_id:
            obj_job_family = self.env["hr.job_family"]
            job_family = obj_job_family.browse([job_family_id])[0]
            value = self._get_value_after_onchange_job_family_id(
                job_family
            )
            domain = self._get_domain_after_onchange_job_family_id(
                job_family
            )
        return {"value": value, "domain": domain}

    @api.multi
    def _get_value_before_onchange_job_family_id(self):
        return {
            "job_grade_ids": [],
        }

    @api.multi
    def _get_domain_before_onchange_job_family_id(self):
        return {}

    @api.multi
    def _get_value_after_onchange_job_family_id(self, job_family):
        return {
            "job_grade_ids": [],
        }

    @api.multi
    def _get_domain_after_onchange_job_family_id(self, job_family):
        return {}

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
