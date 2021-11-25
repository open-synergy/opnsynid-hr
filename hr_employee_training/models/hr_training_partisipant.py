# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class HrTrainingPartisipant(models.Model):
    _name = "hr.training_partisipant"
    _description = "Training Partisipant"
    _rec_name = "partisipant_id"

    partisipant_id = fields.Many2one(
        string="Partisipant",
        comodel_name="hr.employee",
        required=True,
    )
    type_id = fields.Many2one(
        string="Type",
        comodel_name="hr.training_participant_type",
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
        copy=False,
    )
    attendance_ids = fields.One2many(
        string="Attendance",
        comodel_name="hr.training_attendance",
        inverse_name="partisipant_id",
    )
    state = fields.Selection(
        string="State",
        selection=[
            ("draft", "Draft"),
            ("accomplish", "Accomplish"),
            ("cancel", "Cancelled"),
        ],
        required=True,
        default="draft",
        copy=False,
    )
    cancel_reason_id = fields.Many2one(
        string="Cancel Reason",
        comodel_name="hr.training_participant_cancel_reason",
        copy=False,
    )
    substitute_by_id = fields.Many2one(
        string="Substitute By",
        comodel_name="hr.training_partisipant",
        copy=False,
        ondelete="set null",
    )
    substitute_from_id = fields.Many2one(
        string="Substitute From",
        comodel_name="hr.training_partisipant",
        copy=False,
        ondelete="cascade",
    )
    additional = fields.Boolean(
        string="Additional Participant",
    )

    _sql_constraints = [
        (
            "participant_unique",
            "unique(training_id, partisipant_id)",
            "Employee must be unique",
        ),
    ]

    @api.onchange(
        "partisipant_id",
    )
    def onchange_job_id(self):
        self.job_id = False
        if self.partisipant_id:
            self.job_id = self.partisipant_id.job_id

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            result.append((record["id"], record.partisipant_id.name))
        return result

    @api.multi
    def button_accomplish(self):
        for participant in self:
            participant.write(participant._prepare_accomplish_data())

    @api.multi
    def button_cancel(self, cancel_reason_id=False):
        for participant in self:
            participant.write(participant._prepare_cancel_data(cancel_reason_id))

    @api.multi
    def button_reset(self):
        for participant in self:
            participant.write(participant._prepare_reset_data())
            participant._delete_substitute()

    @api.multi
    def _prepare_accomplish_data(self):
        self.ensure_one()
        result = {
            "state": "accomplish",
        }
        return result

    @api.multi
    def _prepare_cancel_data(self, cancel_reason_id=False):
        self.ensure_one()
        result = {
            "state": "cancel",
            "cancel_reason_id": cancel_reason_id,
        }
        return result

    @api.multi
    def _prepare_reset_data(self):
        self.ensure_one()
        result = {
            "state": "draft",
            "cancel_reason_id": False,
        }
        return result

    @api.multi
    def _substitute(self, substitute_by_id):
        self.ensure_one()
        substitute_by = self.copy(self._prepare_substitute_data(substitute_by_id))
        self.write({"substitute_by_id": substitute_by.id})

    @api.multi
    def _prepare_substitute_data(self, substitute_by_id):
        self.ensure_one()
        data = {
            "partisipant_id": substitute_by_id.id,
            "job_id": substitute_by_id.job_id.id,
            "additional": True,
            "substitute_from_id": self.id,
        }
        return data

    def _delete_substitute(self):
        self.ensure_one()
        if self.substitute_by_id:
            self.substitute_by_id.unlink()
