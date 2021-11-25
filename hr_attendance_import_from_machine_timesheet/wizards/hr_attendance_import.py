# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, models


class HrAttendanceImport(models.TransientModel):
    _inherit = "hr.attendance_import"

    @api.model
    def _check_attendance_creation(self, employee_id, attendance_date):
        _super = super(HrAttendanceImport, self)
        result = _super._check_attendance_creation(employee_id, attendance_date)
        ts_check_result = self._check_timesheet(employee_id, attendance_date)
        if result and ts_check_result:
            result = True
        else:
            result = False
        return result

    @api.model
    def _check_timesheet(self, employee_id, attendance_date):
        obj_sheet = self.env["hr_timesheet_sheet.sheet"]
        str_date = attendance_date[0:10]
        criteria = [
            ("employee_id", "=", employee_id),
            ("state", "not in", ["draft", "open"]),
            ("date_from", "<=", str_date),
            ("date_to", ">=", str_date),
        ]
        if obj_sheet.search_count(criteria) > 0:
            result = False
        else:
            result = True
        return result
