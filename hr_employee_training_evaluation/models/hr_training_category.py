# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class HrTrainingCategory(models.Model):
    _inherit = "hr.training_category"

    pre_survey_ids = fields.Many2many(
        string="Pre-Evaluation Survey",
        comodel_name="survey.survey",
        relation="rel_training_category_pre_survey",
        column1="category_id",
        column2="survey_id",
    )
    post_survey_ids = fields.Many2many(
        string="Post-Evaluation Survey",
        comodel_name="survey.survey",
        relation="rel_training_category_post_survey",
        column1="category_id",
        column2="survey_id",
    )
