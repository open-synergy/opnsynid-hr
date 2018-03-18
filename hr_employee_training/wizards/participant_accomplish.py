# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, api, fields


class AccomplishParticipant(models.TransientModel):
    _name = "hr.accomplish_participant"
    _description = "Accomplish Participant"

    @api.model
    def _default_training_id(self):
        return self.env.context.get("active_id", False)

    @api.model
    def _default_detail_ids(self):
        training_id = self.env.context.get("active_id", False)
        obj_participant = self.env["hr.training_partisipant"]
        criteria = [
            ("training_id", "=", training_id),
            ("state", "=", "draft")
        ]
        participants = obj_participant.search(criteria)
        result = []
        for participant in participants:
            data = {
                "participant_id": participant.id,
                "employee_id": participant.partisipant_id.id,
            }
            result.append((0, 0, data))
        return result

    training_id = fields.Many2one(
        string="Training",
        comodel_name="hr.training",
        required=True,
        default=lambda self: self._default_training_id(),
    )

    detail_ids = fields.One2many(
        string="Participants",
        comodel_name="hr.accomplish_participant_detail",
        inverse_name="wizard_id",
        default=lambda self: self._default_detail_ids(),
    )

    @api.multi
    def action_confirm(self):
        for wiz in self:
            wiz._confirm_accomplishment()

    @api.multi
    def _confirm_accomplishment(self):
        self.ensure_one()
        for detail in self.detail_ids:
            detail._confirm_accomplishment()


class AccomplishParticipantDetail(models.TransientModel):
    _name = "hr.accomplish_participant_detail"
    _description = "Detail Accomplish Participant"

    wizard_id = fields.Many2one(
        string="Wizard",
        comodel_name="hr.accomplish_participant",
    )
    participant_id = fields.Many2one(
        string="Participant",
        comodel_name="hr.training_partisipant",
    )
    employee_id = fields.Many2one(
        string="Employee",
        comodel_name="hr.employee",
        related="participant_id.partisipant_id",
        store=False,
    )

    @api.multi
    def _confirm_accomplishment(self):
        self.ensure_one()
        self.participant_id.button_accomplish()
