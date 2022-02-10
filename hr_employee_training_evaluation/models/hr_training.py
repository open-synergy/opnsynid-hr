# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class HrTraining(models.Model):
    _inherit = "hr.training"

    @api.multi
    @api.depends(
        "category_id",
    )
    def _compute_survey(self):
        for training in self:
            if training.category_id:
                training.pre_survey_ids = [
                    (6, 0, training.category_id.pre_survey_ids.ids)
                ]
                training.post_survey_ids = [
                    (6, 0, training.category_id.post_survey_ids.ids)
                ]

    pre_survey_ids = fields.Many2many(
        string="Pre-Evaluation Survey",
        comodel_name="survey.survey",
        compute="_compute_survey",
    )
    post_survey_ids = fields.Many2many(
        string="Post-Evaluation Survey",
        comodel_name="survey.survey",
        compute="_compute_survey",
    )
    evaluation_ids = fields.One2many(
        string="Evaluations",
        comodel_name="hr.training_evaluation",
        inverse_name="training_id",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    pre_evaluation_ids = fields.One2many(
        string="Pre-Evaluations",
        comodel_name="hr.training_evaluation",
        inverse_name="training_id",
        domain=[
            ("pre_post_test", "=", "pre"),
        ],
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    post_evaluation_ids = fields.One2many(
        string="Post-Evaluations",
        comodel_name="hr.training_evaluation",
        inverse_name="training_id",
        domain=[
            ("pre_post_test", "=", "post"),
        ],
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )

    @api.multi
    def action_create_participant_evaluation(self):
        for training in self:
            training._create_participant_evaluation()

    @api.multi
    def _create_participant_evaluation(self):
        self.ensure_one()
        obj_evaluation = self.env["hr.training_participant_evaluation"]
        for participant in self.partisipant_ids:
            for evaluation in self.evaluation_ids:
                criteria = [
                    ("participant_id", "=", participant.id),
                    ("training_evaluation_id", "=", evaluation.id),
                ]
                num = obj_evaluation.search_count(criteria)
                if num == 0:
                    evaluation._create_participant_evaluation(participant)
