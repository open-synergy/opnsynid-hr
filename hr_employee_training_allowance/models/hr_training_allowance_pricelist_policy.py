# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class HrTrainingAllowancePricelistPolicy(models.Model):
    _name = "hr.training_allowance_pricelist_policy"
    _description = "Training Allowance Pricelist Policy"
    _order = "sequence"

    type_id = fields.Many2one(
        string="Participant Type",
        comodel_name="hr.training_participant_type",
        required=True,
        ondelete="cascade",
    )
    sequence = fields.Integer(
        string="Sequence",
        required=True,
        default=5,
    )
    policy_field_id = fields.Many2one(
        string="Allowance Pricelist Policy",
        comodel_name="hr.training_allowance_pricelist_policy_field",
        required=True,
    )
