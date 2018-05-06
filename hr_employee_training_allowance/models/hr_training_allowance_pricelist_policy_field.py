# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class HrTrainingAllowancePricelistPolicyField(models.Model):
    _name = "hr.training_allowance_pricelist_policy_field"
    _description = "Training Allowance Pricelist Policy_field"

    name = fields.Char(
        string="Policy Field",
        required=True,
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
    note = fields.Text(
        string="Note",
    )
    python_code = fields.Text(
        string="Computation",
        required=True,
    )
