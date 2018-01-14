# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class HrTrainingSession(models.Model):
    _name = "hr.training_session"
    _description = "Training Session"

    training_id = fields.Many2one(
        string="Training",
        comodel_name="hr.training",
        ondelete="cascade",
    )
    date_start = fields.Datetime(
        string="Date Start",
    )
    date_end = fields.Datetime(
        string="Date End",
    )
    trainer_ids = fields.Many2many(
        string="Trainer",
        comodel_name="res.partner",
        relation="rel_session_2_trainer",
        column1="session_id",
        columns2="partner_id",
    )
    observer_ids = fields.Many2many(
        string="Observer",
        comodel_name="res.partner",
        relation="rel_session_2_observer",
        column1="training_id",
        columns2="partner_id",
    )
    attendance_ids = fields.One2many(
        string="Attendance",
        comodel_name="hr.training_attendance",
        inverse_name="session_id",
    )
    state = fields.Selection(
        string="State",
        selection=[
            ("draft", "Draft"),
            ("start", "Started"),
            ("finish", "Finished"),
            ("cancel", "Cancelled"),
        ],
        required=True,
        default="draft",
    )

    @api.multi
    def button_restart(self):
        for training in self:
            training.write(self._prepare_restart_data())

    @api.multi
    def button_start(self):
        for session in self:
            session.write(session._prepare_start_data())

    @api.multi
    def button_finish(self):
        for session in self:
            session.write(session._prepare_finish_data())

    @api.multi
    def button_cancel(self):
        for session in self:
            session.write(session._prepare_cancel_data())

    @api.multi
    def button_generate_attendance(self):
        for session in self:
            session._delete_attendance()
            session._create_attendance()

    @api.multi
    def _prepare_start_data(self):
        self.ensure_one()
        result = {
            "state": "start",
        }
        return result

    @api.multi
    def _prepare_finish_data(self):
        self.ensure_one()
        result = {
            "state": "finish",
        }
        return result

    @api.multi
    def _prepare_cancel_data(self):
        self.ensure_one()
        result = {
            "state": "cancel",
        }
        return result

    @api.model
    def _prepare_restart_data(self):
        result = {
            "state": "draft",
        }
        return result

    @api.multi
    def _create_attendance(self):
        self.ensure_one()
        obj_attendance = self.env["hr.training_attendance"]
        for participant in self.training_id.partisipant_ids:
            obj_attendance.create(self._prepare_attendance_data(participant))

    @api.multi
    def _prepare_attendance_data(self, participant):
        self.ensure_one()
        result = {
            "session_id": self.id,
            "partisipant_id": participant.id,
        }
        return result

    @api.multi
    def _delete_attendance(self):
        self.ensure_one()
        self.attendance_ids.unlink()
