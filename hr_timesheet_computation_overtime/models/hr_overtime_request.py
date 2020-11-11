# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import models, fields, api
from openerp.exceptions import Warning as UserError
from openerp.tools.translate import _


class HrOvertimeRequest(models.Model):
    _inherit = "hr.overtime_request"

    @api.multi
    def _prepare_criteria_timesheet(self):
        self.ensure_one()
        criteria = [
            ("employee_id", "=", self.employee_id.id),
            ("date_from", "<=", self.date_start),
            ("date_to", ">=", self.date_end),
        ]
        return criteria

    @api.multi
    @api.depends(
        "employee_id", "date_start", "date_end")
    def _compute_sheet(self):
        obj_sheet = self.env["hr_timesheet_sheet.sheet"]
        for overtime in self:
            criteria = overtime._prepare_criteria_timesheet()
            sheets = obj_sheet.search(criteria, limit=1)
            overtime.sheet_id = sheets[0].id if len(sheets) > 0 else False

    sheet_id = fields.Many2one(
        string="Timesheet",
        comodel_name="hr_timesheet_sheet.sheet",
        compute="_compute_sheet",
        store=True,
    )

    @api.multi
    def button_link_to_timesheet(self):
        return self._compute_sheet()

    @api.constrains(
        "sheet_id",
        "state",
        "company_id.overtime_check_timesheet",
    )
    def _check_timesheet(self):
        obj_overtime = self.env[self._name]
        if self.state in ["confirm", "valid"]:
            criteria = [
                ("sheet_id", "=", False),
                ("company_id.overtime_check_timesheet", "<>", False),
            ]
            if obj_overtime.search_count(criteria) > 0:
                raise UserError(_("Timesheet cannot be empty"))
