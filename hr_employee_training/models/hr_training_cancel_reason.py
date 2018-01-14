# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class HrTrainingCancelReason(models.Model):
    _name = "hr.training_cancel_reason"
    _description = "Training Cancel Reason"

    name = fields.Char(
        string="Training Cancel Reason",
        required=True,
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
    note = fields.Text(
        string="Note",
    )
