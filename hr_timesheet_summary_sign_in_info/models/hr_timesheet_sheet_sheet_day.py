# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models, api
import pytz
from datetime import datetime
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT

class HrTimesheetSheetSheetDay(models.Model):
    _inherit = "hr_timesheet_sheet.sheet.day"

    @api.multi
    def _convert_datetime_utc(self, employee, dt):
        self.ensure_one()
        user = self.env.user
        convert_dt = datetime.strptime(dt, DEFAULT_SERVER_DATETIME_FORMAT)

        if employee.user_id.tz:
            tz = pytz.timezone(employee.user_id.tz)
        else:
            return False

        convert_tz = tz.localize(convert_dt)
        convert_utc = convert_tz.astimezone(pytz.utc)
        format_utc = datetime.strftime(convert_utc, DEFAULT_SERVER_DATE_FORMAT)

        return format_utc

    @api.multi
    def _compute_summary_info(self):
        obj_hr_attendance = self.env['hr.attendance']
        for sheet_day in self:
            employee = sheet_day.sheet_id.employee_id
            utc_date_1 = sheet_day._convert_datetime_utc(
                dt=sheet_day.name + ' 00:00:00',
                employee=employee
            )
            utc_date_2 = sheet_day._convert_datetime_utc(
                dt=sheet_day.name + ' 23:59:59',
                employee=employee
            )

            if utc_date_1 and utc_date_2:
                criteria_first_sign_in = [
                    ('sheet_id', '=', sheet_day.sheet_id.id),
                    ('action', '=', 'sign_in'),
                    ('name', '>=', utc_date_1),
                    ('name', '<=', utc_date_2),
                ]
                list_sign_in =\
                    obj_hr_attendance.search(criteria_first_sign_in, order='name asc')
                if list_sign_in:
                    first_sign_in = list_sign_in[0].id
                else:
                    first_sign_in = False

                criteria_last_sign_out = [
                    ('sheet_id', '=', sheet_day.sheet_id.id),
                    ('action', '=', 'sign_out'),
                    ('name', '>=', utc_date_1),
                    ('name', '<=', utc_date_2),
                ]
                list_sign_out =\
                    obj_hr_attendance.search(criteria_last_sign_out, order='name asc')
                if list_sign_out:
                    last_sign_out = list_sign_out[-1].id
                else:
                    last_sign_out = False
            else:
                first_sign_in = False
                last_sign_out = False
            sheet_day.first_sign_in = first_sign_in
            sheet_day.last_sign_out = last_sign_out

    first_sign_in = fields.Many2one(
        string="First Sign In",
        comodel_name="hr.attendance",
        compute="_compute_summary_info"
    )

    last_sign_out = fields.Many2one(
        string="Last Sign Out",
        comodel_name="hr.attendance",
        compute="_compute_summary_info"
    )