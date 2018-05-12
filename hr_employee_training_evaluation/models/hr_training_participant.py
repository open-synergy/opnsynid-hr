# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class HrTrainingParticipant(models.Model):
    _inherit = "hr.training_partisipant"

    evaluation_ids = fields.One2many(
        string="Evaluations",
        comodel_name="hr.training_participant_evaluation",
        inverse_name="participant_id",
    )
    pre_evaluation_ids = fields.One2many(
        string="Pre-Evaluations",
        comodel_name="hr.training_participant_evaluation",
        inverse_name="participant_id",
        domain=[
            ("pre_post_test", "=", "pre"),
        ],
    )
    post_evaluation_ids = fields.One2many(
        string="Post-Evaluations",
        comodel_name="hr.training_participant_evaluation",
        inverse_name="participant_id",
        domain=[
            ("pre_post_test", "=", "post"),
        ],
    )
