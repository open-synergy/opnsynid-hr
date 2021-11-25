# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models


class HrTimesheetSheet(models.Model):
    _name = "hr_timesheet_sheet.sheet"
    _inherit = "hr_timesheet_sheet.sheet"

    @api.model
    def check_employee_attendance_state(self, sheet_id):
        _super = super(HrTimesheetSheet, self)
        obj_ts = self.env["hr_timesheet_sheet.sheet"]
        ts = obj_ts.browse([sheet_id])[0]
        if ts.company_id.check_timesheet_equal_attendance:
            result = _super.check_employee_attendance_state(sheet_id)
        else:
            result = True
        return result
