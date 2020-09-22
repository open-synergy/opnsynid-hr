# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import models, fields


class HrAwardReason(models.Model):
    _name = "hr.award_reason"
    _description = "Award Reason"

    name = fields.Char(
        string="Award Reason",
        required=True,
    )
    award_type_id = fields.Many2one(
        string="Award Type",
        comodel_name="hr.award_type",
        required=True,
    )
    code = fields.Char(
        string="Code",
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
    note = fields.Text(
        string="Note"
    )
