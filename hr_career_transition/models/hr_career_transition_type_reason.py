# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class HrCareerTransitionTypeReason(models.Model):
    _name = "hr.career_transition_type_reason"
    _description = "Career Transition Type Reason"

    name = fields.Char(string="Reason", required=True)
    description = fields.Text(string="Description")
    active = fields.Boolean(string="Active", default=True)
    type_id = fields.Many2one(
        string="Career Transition Type",
        comodel_name="hr.career_transition_type",
    )
    limit = fields.Integer(
        string="Limit",
        required=True,
        default=0,
    )
