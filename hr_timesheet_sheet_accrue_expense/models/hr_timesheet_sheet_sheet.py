# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models


class HrTimesheetSheetSheet(models.Model):
    _name = "hr_timesheet_sheet.sheet"
    _inherit = "hr_timesheet_sheet.sheet"

    @api.multi
    def _generate_accrue_expense_move(self):
        self.ensure_one()
        obj_detail = self.env["hr.analytic.timesheet"]
        criteria = [
            ("sheet_id", "=", self.id),
            ("accrue_expense_move_id", "=", False),
            ("accrue_expense_ok", "=", True),
        ]
        details = obj_detail.search(criteria)
        details.action_create_accrue_expense_move()

    @api.multi
    def action_generate_accrue_expense_move(self):
        for document in self:
            document._generate_accrue_expense_move()

    @api.multi
    def _remove_accrue_expense_move(self):
        self.ensure_one()
        obj_detail = self.env["hr.analytic.timesheet"]
        criteria = [
            ("sheet_id", "=", self.id),
            ("accrue_expense_move_id", "!=", False),
        ]
        details = obj_detail.search(criteria)
        details.action_unlink_accrue_expense_move()

    @api.multi
    def action_remove_accrue_expense_move(self):
        for document in self:
            document._remove_accrue_expense_move()
