# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class HrTraining(models.Model):
    _inherit = "hr.training"

    allowance_ids = fields.One2many(
        string="Training Allowance",
        comodel_name="hr.training_allowance",
        inverse_name="training_id",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )

    @api.multi
    def button_approve(self):
        _super = super(HrTraining, self)
        _super.button_approve()
        for training in self:  # noqa: B007
            self._generate_participant_allowance()

    @api.multi
    def _generate_participant_allowance(self):
        self.ensure_one()
        for participant in self.partisipant_ids:
            participant.action_generate_allowance()
