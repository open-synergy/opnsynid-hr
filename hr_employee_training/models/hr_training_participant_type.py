# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class HrTrainingParticipantType(models.Model):
    _name = "hr.training_participant_type"
    _description = "Training Participant Type"

    name = fields.Char(
        string="Participant Type",
        required=True,
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
    note = fields.Text(
        string="Note",
    )
