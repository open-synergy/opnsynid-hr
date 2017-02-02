# -*- coding: utf-8 -*-
# © 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, api, _


class HrPayslip(models.Model):
    _inherit = "hr.payslip"

    @api.multi
    def button_import_attendance(self):
        for payslip in self:
            payslip._import_attendance()

    @api.multi
    def _import_attendance(self):
        self.ensure_one()
        wd_obj = self.env["hr.payslip.worked_days"]
        day_obj = self.env["hr_timesheet_sheet.sheet.day"]
        date_from = self.date_from
        date_to = self.date_to

        criteria1 = [
            ("payslip_id", "=", self.id),
            ("import_from_attendance", "=", True),
        ]
        wd_obj.search(criteria1).unlink()

        res = {
            "name": _("Total Attendance"),
            "code": "ATTN",
            "number_of_days": 0.0,
            "number_of_hours": 0.0,
            "contract_id": self.contract_id.id,
            "import_from_attendance": True,
            "payslip_id": self.id,
        }

        criteria2 = [
            ("name", ">=", date_from),
            ("name", "<=", date_to),
            ("sheet_id.employee_id", "=", self.employee_id.id),
            ("sheet_id.state", "=", "done"),
        ]

        for day in day_obj.search(criteria2):
            if day.total_attendance >= 0.0:
                res["number_of_days"] += 1
                res["number_of_hours"] += day.total_attendance

        wd_obj.create(res)
