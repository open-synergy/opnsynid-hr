# -*- coding: utf-8 -*-
# © 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class HrJobFamilyLevel(models.Model):
    _name = "hr.job.family.level"
    _description = "Job Family Level"

    name = fields.Char(
        string="Job Family Level",
        required=True,
        translate=True,
    )
    code = fields.Char(
        string="Code",
        required=True,
    )
    job_family_id = fields.Many2one(
        string="Job Family",
        comodel_name="hr.job.family",
        required=False,
    )
    job_family_grade_id = fields.Many2one(
        string="Job Family Grade",
        comodel_name="hr.job.family.grade",
        required=False,
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
    note = fields.Text(
        string="Note",
    )
