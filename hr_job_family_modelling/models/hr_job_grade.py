# -*- coding: utf-8 -*-
# Copyright 2016-2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class HrJobGrade(models.Model):
    _name = "hr.job_grade"
    _description = "Job Grade"

    name = fields.Char(
        string="Job Grade",
        required=True,
        translate=True,
    )
    category_id = fields.Many2one(
        string="Job Grade Category",
        comodel_name="hr.job_grade_category",
        required=False,
    )
    sequence = fields.Integer(
        string="Sequence",
        required=True,
        default=5,
    )
    code = fields.Char(
        string="Code",
        required=True,
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
    note = fields.Text(
        string="Note",
    )
