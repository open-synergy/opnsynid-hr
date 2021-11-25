# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class HrTrainingCategory(models.Model):
    _name = "hr.training_category"
    _description = "Training Category"

    code = fields.Char(
        string="Code",
        required=True,
    )
    name = fields.Char(
        string="Training Category",
        required=True,
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
    note = fields.Text(
        string="Note",
    )
    parent_id = fields.Many2one(
        string="Parent",
        comodel_name="hr.training_category",
    )
    type = fields.Selection(
        string="Type",
        selection=[
            ("view", "View"),
            ("normal", "Normal"),
        ],
        required=True,
        default="normal",
    )
