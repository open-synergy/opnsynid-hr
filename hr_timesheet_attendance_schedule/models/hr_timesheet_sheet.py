# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


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

    @api.multi
    def action_create_attendance_schedule(self):
        for sheet in self:
            sheet._create_attendance_schedule()

    @api.multi
    def _create_attendance_schedule(self):
        self.ensure_one()
        obj_schedule = self.env["hr.timesheet_attendance_schedule"]
        dt_start = fields.Datetime.from_string(self.date_from)
        dt_end = fields.Datetime.from_string(self.date_to)
        duration = abs((dt_end - dt_start).days) + 1
        if not self.contract_ids:
            return True

        contract = self.contract_ids.sorted(
            lambda r: r.date_start, reverse=True)[0]

        if not contract.working_hours:
            return True

        schedules = contract.working_hours._schedule_days(
            days=duration,
            day_date=dt_start)

        if len(schedules) == 0:
            return True

        for schedule in schedules[0]:
            str_start = fields.Datetime.to_string(schedule[0])
            str_end = fields.Datetime.to_string(schedule[1])
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
