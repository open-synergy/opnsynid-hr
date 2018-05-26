# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class HrHolidays(models.Model):
    _inherit = "hr.holidays"

    @api.multi
    @api.depends(
        "employee_id", "date_from", "date_to")
    def _compute_sheet(self):
        obj_sheet = self.env["hr_timesheet_sheet.sheet"]
        for holiday in self:
            if holiday.type == "add":
                holiday.sheet_id = False
                continue
            criteria = [
                ("employee_id", "=", holiday.employee_id.id),
                ("date_from", "<=", holiday.date_from),
                ("date_to", ">=", holiday.date_from),
            ]
            sheets = obj_sheet.search(criteria, limit=1)
            holiday.sheet_id = sheets[0].id if len(sheets) > 0 else False

    sheet_id = fields.Many2one(
        string="Timesheet",
        comodel_name="hr_timesheet_sheet.sheet",
        compute="_compute_sheet",
        store=True,
    )
