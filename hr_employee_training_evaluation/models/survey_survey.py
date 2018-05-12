# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class SurveySurvey(models.Model):
    _inherit = "survey.survey"

    training_pre_ok = fields.Boolean(
        string="Avalaible for Training Pre-Evaluation",
    )

    training_post_ok = fields.Boolean(
        string="Avalaible for Training Post-Evaluation",
    )
