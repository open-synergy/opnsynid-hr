# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class HrTrainingPartisipant(models.Model):
    _name = "hr.training_partisipant"
    _description = "Training Partisipant"

    partisipant_id = fields.Many2one(
        string="Partisipant",
        comodel_name="hr.employee",
        required=True,
    )
    training_id = fields.Many2one(
        string="Training",
        comodel_name="hr.training",
        ondelete="cascade",
    )
    job_id = fields.Many2one(
        string="Job",
        comodel_name="hr.job",
    )
    state = fields.Selection(
        string="State",
        selection=[
            ("absence", "Absence"),
            ("present", "Present"),
        ],
        required=True,
        default="absence",
    )

    @api.onchange(
        "partisipant_id",
    )
    def onchange_job_id(self):
        self.job_id = False
        if self.partisipant_id:
            self.job_id = self.partisipant_id.job_id
