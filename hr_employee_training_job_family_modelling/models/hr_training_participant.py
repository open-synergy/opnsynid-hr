# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class HrTrainingParticipant(models.Model):
    _inherit = "hr.training_partisipant"

    job_grade_id = fields.Many2one(
        string="Job Grade",
        comodel_name="hr.job_grade",
    )
    job_family_grade_id = fields.Many2one(
        string="Job Family Grade",
        comodel_name="hr.job_family_grade",
    )

    @api.onchange(
        "partisipant_id",
    )
    def onchange_job_grade_id(self):
        self.job_grade_id = False
        if self.partisipant_id:
            self.job_grade_id = self.partisipant_id.job_grade_id

    @api.onchange(
        "partisipant_id",
    )
    def onchange_job_family_grade_id(self):
        self.job_family_grade_id = False
        if self.partisipant_id:
            self.job_family_grade_id = self.partisipant_id.job_family_grade_id
