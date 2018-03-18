# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api
from openerp.exceptions import Warning as UserError
from openerp.tools.translate import _


class HrTrainingSession(models.Model):
    _name = "hr.training_session"
    _description = "Training Session"
    _order = "training_id, date_start, id"

    training_id = fields.Many2one(
        string="Training",
        comodel_name="hr.training",
        ondelete="cascade",
    )
    date_start = fields.Datetime(
        string="Date Start",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    date_end = fields.Datetime(
        string="Date End",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    trainer_ids = fields.Many2many(
        string="Trainer",
        comodel_name="res.partner",
        relation="rel_session_2_trainer",
        column1="session_id",
        columns2="partner_id",
        domain=[
            ("is_company", "=", False),
        ],
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    observer_ids = fields.Many2many(
        string="Observer",
        comodel_name="res.partner",
        relation="rel_session_2_observer",
        column1="training_id",
        columns2="partner_id",
        domain=[
            ("is_company", "=", False),
        ],
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    allowed_trainer_ids = fields.Many2many(
        string="Allowed Trainer",
        comodel_name="res.partner",
        relation="rel_session_2_allowed_trainer",
        column1="session_id",
        columns2="partner_id",
        related="training_id.trainer_ids",
        readonly=True,
    )
    allowed_observer_ids = fields.Many2many(
        string="Allowed Observer",
        comodel_name="res.partner",
        relation="rel_session_2_allowed_observer",
        column1="training_id",
        columns2="partner_id",
        readonly=True,
        related="training_id.observer_ids",
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
        readonly=True,
    )
    training_state = fields.Selection(
        string="Training State",
        selection=[
            ("draft", "Draft"),
            ("confirm", "Waiting for Approval"),
            ("approve", "Approved"),
            ("start", "Started"),
            ("finish", "Finished"),
            ("cancel", "Cancelled"),
        ],
        related="training_id.state",
        store=False,
        readonly=True,
    )

    @api.model
    def create(self, values):
        _super = super(HrTrainingSession, self)
        result = _super.create(values)
        result._create_attendance()
        return result

    @api.multi
    def button_restart(self):
        for training in self:
            training.write(self._prepare_restart_data())

    @api.multi
    def button_start(self):
        for session in self:
            session.write(session._prepare_start_data())
            session._create_attendance()

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
            # session._delete_attendance()
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
            criteria = [
                ("session_id", "=", self.id),
                ("partisipant_id", "=", participant.id),
            ]
            participant_count = obj_attendance.search_count(criteria)
            if participant_count == 0:
                obj_attendance.create(
                    self._prepare_attendance_data(participant))

    @api.multi
    def _prepare_attendance_data(self, participant):
        self.ensure_one()
        result = {
            "session_id": self.id,
            "partisipant_id": participant.id,
        }
        return result

    @api.constrains("date_start", "date_end")
    def _check_duration(self):
        strWarning = _("Date end must be greater than date start")
        if self.date_start and self.date_end:
            if self.date_end < self.date_start:
                raise UserError(strWarning)

    @api.constrains("date_start", "date_end")
    def _check_training_limit(self):
        strWarning1 = _("Session's date start out of training duration")
        strWarning2 = _("Session's date end out of training duration")
        if self.training_id.date_start > self.date_start or \
                self.training_id.date_end < self.date_start:
            raise UserError(strWarning1)
        if self.training_id.date_end < self.date_end or \
                self.training_id.date_start > self.date_end:
            raise UserError(strWarning2)
