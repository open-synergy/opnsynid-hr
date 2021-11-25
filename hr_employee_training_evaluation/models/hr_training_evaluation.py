# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class HrTrainingEvaluation(models.Model):
    _name = "hr.training_evaluation"
    _description = "Employee Training Evaluation"
    _order = "sequence, id"

    training_id = fields.Many2one(
        string="Training",
        comodel_name="hr.training",
        required=True,
        ondelete="cascade",
    )
    pre_post_test = fields.Selection(
        string="Pre/Post Evaluation",
        selection=[
            ("pre", "Pre Evaluation"),
            ("post", "Post Evaluation"),
        ],
        required=True,
    )
    survey_id = fields.Many2one(
        string="Survey",
        comodel_name="survey.survey",
        required=True,
        ondelete="restrict",
    )
    sequence = fields.Integer(
        string="Sequence",
        required=True,
        default=5,
    )

    @api.multi
    def _create_participant_evaluation(self, participant):
        self.ensure_one()
        obj_evaluation = self.env["hr.training_participant_evaluation"]

        obj_evaluation.create(self._prepare_participant_evaluation(participant))

    @api.multi
    def _prepare_participant_evaluation(self, participant):
        self.ensure_one()
        return {
            "participant_id": participant.id,
            "training_evaluation_id": self.id,
        }
