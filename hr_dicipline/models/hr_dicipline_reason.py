# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import fields, models


class HrDiciplineReason(models.Model):
    _name = "hr.dicipline_reason"
    _description = "Dicipline Reason"

    name = fields.Char(
        string="Dicipline Reason",
        required=True,
    )
    dicipline_type_id = fields.Many2one(
        string="Dicipline Type",
        comodel_name="hr.dicipline_type",
        required=True,
    )
    code = fields.Char(
        string="Code",
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
    note = fields.Text(string="Note")
