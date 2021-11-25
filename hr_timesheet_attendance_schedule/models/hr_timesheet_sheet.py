# -*- coding: utf-8 -*-
# Copyright 2018-2019 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import datetime

from openerp import api, fields, models
from pytz import timezone


class HrTimesheetSheet(models.Model):
    _inherit = "hr_timesheet_sheet.sheet"

    attendance_schedule_ids = fields.One2many(
        string="Attendance Schedule",
        comodel_name="hr.timesheet_attendance_schedule",
        inverse_name="sheet_id",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    working_schedule_id = fields.Many2one(
        string="Working Schedule",
        comodel_name="resource.calendar",
    )

    @api.multi
    def action_create_attendance_schedule(self):
        for sheet in self:
            sheet._create_attendance_schedule()

    @api.multi
    def _get_working_schedule(self):
        self.ensure_one()

        working_schedule = False

        contract = self.contract_ids.sorted(lambda r: r.date_start, reverse=True)[0]

        if self.working_schedule_id:
            working_schedule = self.working_schedule_id
        elif contract.working_hours:
            working_schedule = contract.working_hours

        return working_schedule

    @api.multi
    def _create_attendance_schedule(self):
        self.ensure_one()
        obj_schedule = self.env["hr.timesheet_attendance_schedule"]
        tz = self.employee_id.user_id.tz or self.env.user.tz

        # TODO: Refactoring
        dt_start = datetime.strptime(self.date_from + " 00:00:00", "%Y-%m-%d %H:%M:%S")
        dt_end = datetime.strptime(self.date_to + " 23:59:00", "%Y-%m-%d %H:%M:%S")

        duration = abs((dt_end - dt_start).days) + 1
        dt_stop = (
            timezone(tz)
            .localize(dt_end)
            .astimezone(timezone("UTC"))
            .replace(tzinfo=None)
        )

        if not self.contract_ids:
            return True

        working_schedule = self._get_working_schedule()

        if not working_schedule:
            return True

        schedules = working_schedule._schedule_days(days=duration, day_date=dt_start)

        if len(schedules) == 0:
            return True

        for schedule in schedules[0]:
            str_start = fields.Datetime.to_string(schedule[0])
            str_end = fields.Datetime.to_string(schedule[1])
            if schedule[0] > dt_stop:
                break

            if self._check_existing_schedule(str_start, str_end):
                data = {
                    "sheet_id": self.id,
                    "date_start": str_start,
                    "date_end": str_end,
                }
                obj_schedule.create(data)

    @api.multi
    def _check_existing_schedule(self, dt_start, dt_end):
        self.ensure_one()
        result = True
        obj_schedule = self.env["hr.timesheet_attendance_schedule"]
        criteria = [
            ("sheet_id", "=", self.id),
            ("date_start", "=", dt_start),
            ("date_end", "=", dt_end),
        ]
        schedule_count = obj_schedule.search_count(criteria)
        if schedule_count > 0:
            result = False
        return result

    @api.multi
    def action_rearrange_attendance_schedule(self):
        waction = self.env.ref(
            "hr_timesheet_attendance_schedule."
            "hr_timesheet_attendance_schedule_rearrange_action"
        ).read()[0]
        waction["domain"] = [
            ("sheet_id", "in", self.ids),
            ("sheet_id.state", "=", "draft"),
        ]
        return waction
