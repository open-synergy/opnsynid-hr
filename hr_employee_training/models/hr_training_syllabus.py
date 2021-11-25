# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class HrTrainingSyllabus(models.Model):
    _name = "hr.training_syllabus"
    _description = "Training Syllabus"

    name = fields.Char(
        string="Training Syllabus",
        required=True,
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
    note = fields.Text(
        string="Note",
    )
