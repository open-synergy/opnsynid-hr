# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class HrTrainingAttendance(models.Model):
    _name = "hr.training_attendance"
    _description = "Training Attendance"

    session_id = fields.Many2one(
        string="Session",
        comodel_name="hr.training_session",
        ondelete="cascade",
    )
    partisipant_id = fields.Many2one(
        string="Partisipant",
        comodel_name="hr.training_partisipant",
        ondelete="cascade",
    )
    employee_id = fields.Many2one(
        string="Employee",
        comodel_name="hr.employee",
        related="partisipant_id.partisipant_id",
        store=True,
    )
    training_id = fields.Many2one(
        string="Training",
        comodel_name="hr.training",
        related="session_id.training_id",
        store=True,
    )
    date_start = fields.Datetime(
        string="Date Start",
        related="session_id.date_start",
        store=True,
    )
    date_end = fields.Datetime(
        string="Date End",
        related="session_id.date_end",
        store=True,
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

    @api.multi
    def button_present(self):
        for attendance in self:
            attendance.write(attendance._prepare_present_data())

    @api.multi
    def button_absence(self):
        for attendance in self:
            attendance.write(attendance._prepare_absence_data())

    @api.multi
    def _prepare_present_data(self):
        self.ensure_one()
        result = {
            "state": "present",
        }
        return result

    @api.multi
    def _prepare_absence_data(self):
        self.ensure_one()
        result = {
            "state": "absence",
        }
        return result
