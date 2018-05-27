# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class HrOvertimeRequest(models.Model):
    _inherit = "hr.overtime_request"

    @api.multi
    @api.depends(
        "employee_id", "date_start", "date_end")
    def _compute_sheet(self):
        obj_sheet = self.env["hr_timesheet_sheet.sheet"]
        for overtime in self:
            criteria = [
                ("employee_id", "=", overtime.employee_id.id),
                ("date_from", "<=", overtime.date_start),
                ("date_to", ">=", overtime.date_end),
            ]
            sheets = obj_sheet.search(criteria, limit=1)
            overtime.sheet_id = sheets[0].id if len(sheets) > 0 else False

    sheet_id = fields.Many2one(
        string="Timesheet",
        comodel_name="hr_timesheet_sheet.sheet",
        compute="_compute_sheet",
        store=True,
    )
