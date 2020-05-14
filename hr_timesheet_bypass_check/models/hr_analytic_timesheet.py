# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api, fields


class HrAnalyticTimesheet(models.Model):
    _name = "hr.analytic.timesheet"
    _inherit = "hr.analytic.timesheet"

    @api.multi
    def _check(self):
        return True

    @api.depends(
        "sheet_id.employee_id",
        "sheet_id.date_from",
        "sheet_id.date_to",
        "user_id",
        "date",
    )
    def _compute_sheet(self):
        obj_sheet = self.env["hr_timesheet_sheet.sheet"]
        for document in self:
            criteria = [
                ("date_to", ">=", document.date),
                ("date_from", "<=", document.date),
                ("employee_id.user_id", "=", document.user_id.id),
            ]
            sheets = obj_sheet.search(criteria)
            if len(sheets) > 0:
                document.sheet_id = sheets[0]

    sheet_id = fields.Many2one(
        compute="_compute_sheet",
        store=True,
    )
