# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api
from pytz import timezone
from datetime import datetime


class HrTimesheetAttendanceSchedule(models.Model):
    _name = "hr.timesheet_attendance_schedule"
    _description = "Timesheet Attendance Schedule"
    _order = "sheet_id, date_start"

    @api.multi
    @api.depends("attendance_ids")
    def _compute_attendance(self):
        obj_attendance = self.env["hr.attendance"]
        for schedule in self:
            criteria = [
                ("schedule_id", "=", schedule.id),
                ("action", "=", "sign_in"),
            ]
            attendances = obj_attendance.search(criteria)
            if len(attendances) > 0:
                attendances = attendances.sorted(key=lambda r: r.name)
                start_attendance_id = attendances[
                    0].id if len(attendances) > 0 else False
            else:
                start_attendance_id = False

            criteria = [
                ("schedule_id", "=", schedule.id),
                ("action", "=", "sign_out"),
            ]
            attendances = obj_attendance.search(criteria)
            if len(attendances) > 0:
                attendances = attendances.sorted(
                    key=lambda r: r.name, reverse=True)
                end_attendance_id = attendances[
                    0].id if len(attendances) > 0 else False
            else:
                end_attendance_id = False

            schedule.start_attendance_id = start_attendance_id
            schedule.end_attendance_id = end_attendance_id

    @api.multi
    @api.depends(
        "start_attendance_id", "end_attendance_id",
    )
    def _compute_state(self):
        for attn in self:
            if attn.start_attendance_id and \
                    attn.end_attendance_id:
                attn.state = "present"
            elif (attn.start_attendance_id and not attn.end_attendance_id) or \
                    (not attn.start_attendance_id and attn.end_attendance_id):
                attn.state = "open"
            elif not attn.start_attendance_id and \
                    not attn.end_attendance_id:
                attn.state = "absence"

    @api.multi
    @api.depends(
        "date_start", "date_end",
        "start_attendance_id", "end_attendance_id",
        "start_attendance_id.name", "end_attendance_id.name",
    )
    def _compute_work_hour(self):
        for attn in self:
            schedule_work_hour = real_work_hour = early_start_hour = \
                late_start_hour = finish_early_hour = finish_late_hour = \
                0.0
            dt_schedule_start = fields.Datetime.from_string(attn.date_start) \
                if attn.date_start else False
            dt_schedule_end = fields.Datetime.from_string(attn.date_end) \
                if attn.date_end else False
            dt_real_start = fields.Datetime.\
                from_string(attn.start_attendance_id.name) if attn.\
                start_attendance_id else False
            dt_real_end = fields.Datetime.\
                from_string(attn.end_attendance_id.name) if attn.\
                end_attendance_id else False

            if dt_schedule_start and dt_schedule_end:
                schedule_work_hour = \
                    (dt_schedule_end - dt_schedule_start).total_seconds() / \
                    3600.0

            if dt_real_start and dt_real_end:
                real_work_hour = \
                    (dt_real_end - dt_real_start).total_seconds() / \
                    3600.0

            if dt_schedule_start and dt_real_start:
                if dt_schedule_start > dt_real_start:
                    early_start_hour = (dt_schedule_start - dt_real_start).\
                        total_seconds() / 3600.0

                if dt_schedule_start < dt_real_start:
                    late_start_hour = (dt_real_start - dt_schedule_start).\
                        total_seconds() / 3600.0

            if dt_schedule_end and dt_real_end:
                if dt_schedule_end > dt_real_end:
                    finish_early_hour = (dt_schedule_end - dt_real_end).\
                        total_seconds() / 3600.0

                if dt_schedule_end < dt_real_end:
                    finish_late_hour = (dt_real_end - dt_schedule_end).\
                        total_seconds() / 3600.0

            attn.schedule_work_hour = schedule_work_hour
            attn.real_work_hour = real_work_hour
            attn.early_start_hour = early_start_hour
            attn.late_start_hour = late_start_hour
            attn.finish_early_hour = finish_early_hour
            attn.finish_late_hour = finish_late_hour

    sheet_id = fields.Many2one(
        string="Timesheet",
        comodel_name="hr_timesheet_sheet.sheet",
        ondelete="cascade",
        required=True,
    )
    employee_id = fields.Many2one(
        string="Employee",
        related="sheet_id.employee_id",
        store=True,
    )
    date_start = fields.Datetime(
        string="Date Start",
        required=False,
    )
    date_end = fields.Datetime(
        string="Date End",
        required=False,
    )
    attendance_ids = fields.One2many(
        string="Attendances",
        comodel_name="hr.attendance",
        inverse_name="schedule_id",
    )
    start_attendance_id = fields.Many2one(
        string="Start Attendance",
        comodel_name="hr.attendance",
        compute="_compute_attendance",
        store=True,
    )
    end_attendance_id = fields.Many2one(
        string="End Attendance",
        comodel_name="hr.attendance",
        compute="_compute_attendance",
        store=True,
    )
    real_date_start = fields.Datetime(
        string="Real Date Start",
        related="start_attendance_id.name",
    )
    real_date_end = fields.Datetime(
        string="Real Date End",
        related="end_attendance_id.name",
    )

    state = fields.Selection(
        string="State",
        selection=[
            ("absence", "Absence"),
            ("open", "Open"),
            ("present", "Present"),
        ],
        default="absence",
        required=True,
        compute="_compute_state",
        store=True,
    )
    schedule_work_hour = fields.Float(
        string="Schedule Work Hour",
        compute="_compute_work_hour",
        store=True,
    )
    real_work_hour = fields.Float(
        string="Real Work Hour",
        compute="_compute_work_hour",
        store=True,
    )
    early_start_hour = fields.Float(
        string="Early Start",
        compute="_compute_work_hour",
        store=True,
    )
    late_start_hour = fields.Float(
        string="Late Start",
        compute="_compute_work_hour",
        store=True,
    )
    finish_early_hour = fields.Float(
        string="Finish Early",
        compute="_compute_work_hour",
        store=True,
    )
    finish_late_hour = fields.Float(
        string="Finish Late",
        compute="_compute_work_hour",
        store=True,
    )

    @api.multi
    def name_get(self):
        result = []

        for schedule in self:
            tz = schedule.employee_id.user_id.tz or self.env.user.tz
            dt_start = datetime.strptime(
                schedule.date_start, "%Y-%m-%d %H:%M:%S")
            dt_start = timezone("UTC").localize(dt_start)
            dt_start = dt_start.astimezone(timezone(tz))
            str_start = dt_start.strftime("%Y-%m-%d %H:%M:%S")

            dt_end = datetime.strptime(
                schedule.date_end, "%Y-%m-%d %H:%M:%S")
            dt_end = timezone("UTC").localize(dt_end)
            dt_end = dt_end.astimezone(timezone(tz))
            str_end = dt_end.strftime("%Y-%m-%d %H:%M:%S")
            name = "%s - %s" % (str_start, str_end)
            result.append([schedule.id, name])
        return result
